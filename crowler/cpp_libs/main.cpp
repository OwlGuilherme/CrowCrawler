#include <cstdlib>
#include <ctime>
#include <exception>
#include <iomanip>
#include <iostream>
#include <sqlite3.h>
#include <sstream>
#include <vector>

void criar_tabela() {
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
}

void salvar_dados(const std::string &nome, const std::string &preco_atual,
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
}

std::vector<std::tuple<std::string, std::string, double, std::string>>
obter_dados() {
  sqlite3 *db;
  int result = sqlite3_open("banco.db", &db);

  if (result != SQLITE_OK) {
    std::err << "Erro ao criar banco de dados: " << sqlite3_errmsg(db) << '\n';
    sqlite3_close(db);
    exit(EXIT_FAILURE);
  }

  const char *sql = "SELECT produto, horario, precos, site, FROM dados";
  sqlite3_stmt *stmt;

  result = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);

  if (result != SQLITE_OK) {
    std::err << "Erro ao preparar a consulta SQL: " << sqlite3_errmsg(db)
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
