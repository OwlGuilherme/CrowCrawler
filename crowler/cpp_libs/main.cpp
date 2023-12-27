#define PY_SSIZE_T_CLEAN
#include <python3.12/Python.h>
#include <cstdlib>
#include <ctime>
#include <exception>
#include <iomanip>
#include <iostream>
#include <sqlite3.h>
#include <sstream>
#include <vector>

int criar_tabela() {
  sqlite3 *db;
  int result = sqlite3_open("banco.db", &db);

  if (result != SQLITE_OK) {
    std::cerr << "Erro ao abrir/criar o banco de dados: " << sqlite3_errmsg(db)
              << '\n';
    sqlite3_close(db);
    exit(EXIT_FAILURE);
  }

  const char *sql = "CREATE TABLE IF NOT EXISTS dados (produto TEXT, horario "
                    "TIMESTAMP, precos REAL, site TEXT);";
  result = sqlite3_exec(db, sql, 0, 0, 0);

  if (result != SQLITE_OK) {
    std::cerr << "Erro ao executar consulta ao banco de dados: "
              << sqlite3_errmsg(db) << '\n';
    sqlite3_close(db);
    exit(EXIT_FAILURE);
  }

  sqlite3_close(db);

  return 0;
}

int salvar_dados(const std::string &nome, const std::string &preco_atual,
                  const std::string &site) {

  sqlite3 *db;
  int result = sqlite3_open("banco.db", &db);

  if (result != SQLITE_OK) {
    std::cerr << "Erro ao abrir o banco de dados: " << sqlite3_errmsg(db)
              << '\n';
    sqlite3_close(db);
    exit(EXIT_FAILURE);
  }

  try {
    const char *sql = "INSERT INTO dados VALUES (?, ?, ?, ?)";
    sqlite3_stmt *stmt;

    result = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);

    if (result != SQLITE_OK) {
      std::cerr << "Erro ao preparar a consulta SQL: " << sqlite3_errmsg(db)
                << '\n';
      sqlite3_close(db);
      exit(EXIT_FAILURE);
    }

    sqlite3_bind_text(stmt, 1, nome.c_str(), -1, SQLITE_STATIC);

    std::time_t timestamp = std::time(0);
    sqlite3_bind_int64(stmt, 2, timestamp);

    double preco = std::stod(preco_atual.substr(3));

    sqlite3_bind_text(stmt, 4, site.c_str(), -1, SQLITE_STATIC);

    result = sqlite3_step(stmt);

    if (result != SQLITE_OK) {
      std::cerr << "Erro ao executar consulta SQL: " << sqlite3_errmsg(db)
                << '\n';
      sqlite3_close(db);
      exit(EXIT_FAILURE);
    }

    std::cout << "Dados inseridos com sucesso:  " << nome << ", " << preco_atual
              << ", " << site << '\n';

  } catch (const std::exception &e) {
    std::cerr << "Erro ao inserir dados: " << e.what() << '\n';
  }

  sqlite3_close(db);
  return 0;
}

std::vector<std::tuple<std::string, std::string, double, std::string>>
obter_dados() {
  sqlite3 *db;
  int result = sqlite3_open("banco.db", &db);

  if (result != SQLITE_OK) {
    std::cerr << "Erro ao criar banco de dados: " << sqlite3_errmsg(db) << '\n';
    sqlite3_close(db);
    exit(EXIT_FAILURE);
  }

  const char *sql = "SELECT produto, horario, precos, site, FROM dados";
  sqlite3_stmt *stmt;

  result = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);

  if (result != SQLITE_OK) {
    std::cerr << "Erro ao preparar a consulta SQL: " << sqlite3_errmsg(db)
              << '\n';
    sqlite3_close(db);
    exit(EXIT_FAILURE);
  }

  std::vector<std::tuple<std::string, std::string, double, std::string>> dados;

  while (sqlite3_step(stmt) == SQLITE_ROW) {

    std::string produto =
        reinterpret_cast<const char *>(sqlite3_column_text(stmt, 0));
    std::time_t timestamp = sqlite3_column_int64(stmt, 1);
    double preco = sqlite3_column_double(stmt, 2);
    std::string site =
        reinterpret_cast<const char *>(sqlite3_column_text(stmt, 3));

    std::tm *tm_info = std::localtime(&timestamp);
    std::stringstream ss;
    ss << std::put_time(tm_info, "%Y-%m-%d %H:%M"
                                 "%Y-%m-%d %H:%M");
    std::string horario = ss.str();

    dados.emplace_back(produto, horario, preco, site);
  }

  sqlite3_finalize(stmt);
  sqlite3_close(db);

  return dados;
}

static PyObject *criar_tabela(PyObject  *self, PyObject *args){
  criar_tabela();
  Py_RETURN_NONE;
}

static PyObject *salvar_dados(PyObject *self, PyObject *args){
  const char *nome;
  const char *preco_atual;
  const char *site;

  if (!PyArg_Parse(args, "sss", &nome, &preco_atual, &site)) {
    return nullptr;
  }

  salvar_dados(nome, preco_atual, site);
  Py_RETURN_NONE;
}

static PyObject *obter_dados(PyObject *self, PyObject *args){
  auto dados = obter_dados();

  PyObject *result = PyList_New(dados.size());

  for (std::size_t i = 0; i < dados.size(); ++i) {
    const auto &d = dados[i];

    PyObject *tuple = PyTuple_Pack(4, PyUnicode_DecodeUTF8(std::get<0>(d).c_str(), -1, nullptr),
                                    PyUnicode_DecodeUTF8(std::get<1>(d).c_str(), -1, nullptr),
                                    PyFloat_FromDouble(std::get<2>(d)),
                                    PyUnicode_DecodeUTF8(std::get<3>(d).c_str(), -1, nullptr));

    PyList_SetItem(result, i, tuple);
  }

  return result;

}

static PyMethodDef db_act_methods[] = {
  {"criar_tabela", criar_tabela, METH_NOARGS, "Cria a tabela e o banco de dados."},
  {"salva_dados", salvar_dados, METH_VARARGS, "Salva os dados no banco de dados."},
  {"obter_dados", obter_dados, METH_NOARGS, "Obtem os dados do banco de dados. "},
  {NULL, NULL, 0, NULL}
};

static struct  PyModuleDef db_act_module = {
  PyModuleDef_HEAD_INIT,
  "db_act",
  NULL,
  -1,
  db_act_methods  
};

PyMODINIT_FUNC PyInit_db_act(void){
  return PyModule_Create(&db_act_module);
}