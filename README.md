# CrowCrawler

Ferramenta para coleta e análise de dados de e-commerce

> Status: A aplicação está em desenvolvimento, mas já é funcional. ⚠️

## 💻 Pré-requisitos

Antes de começar, verifique os seguintes requisitos:

+ [Python](https://www.python.org/downloads/)
+ [Pip](https://pip.pypa.io/en/stable/installation/)

## 🧰 Linguagens utilizadas
+ ![GitHub top language](https://img.shields.io/github/languages/top/OwlGuilherme/CrowCrawler)

## 🧰 Sobre

+ Esta aplicação tem como objetivo realizar a raspagem de dados de sites de e-commerce e salvar tais dados em um banco de dados portável, no caso, sqlite3.

### Estado funcional da aplicação
+ A presente aplicação encontra-se funcional
Basta, no respetivo arquivo .json, inserir os links dos produtos, do site que deseja raspar, e poderá salvar o nome do produto, seu preço e o momento em que foi salvo o preço do produto.
#### Sites que já funcionam
+ Amazon
+ Centauro
+ Declathon

## ⚙️ Utilização
+ Abra o seu terminal
+ Faça o download do repositório com o comando:
```
git clone https://github.com/OwlGuilherme/CrowCrawler
```
+ Entre na pasta do projeto com o comando:
```
cd CrowCrawler
```
+ Crie um ambiente virtual e ative o ambiente (opcional):
```
python -m venv scrapper-env && source scrapper-env/bin/activate
```
+ Instale as dependências do projeto:
```
pip install -r requirements.txt
```
+ Adicione, nos arquivos .json os links dos produtos, dos respectivos sites que deseja salvar.
Caminho para os arquivos "./crowler/crowler/rules/*.json".
+ Execute a aplicação
```
python main.py
```

## 📮 Contribuindo para o CrowCrawler

Caso queira contribuir com o projeto, ficarei muito grato e, para isso, siga estas etapas:

1. _Fork_ este repositório.
2. Clone o seu repositório _forkado_ com o comando _git clone <link do repositório>_.
3. Faça suas alterações e confirme-as: _git commit -m '<mensagem_commit>'_
4. Envie para o branch original: _git push origin <nome_do_projeto> / <local>_
5. Crie a solicitação de pull.

+ Caso queira me mandar uma mensagem, fique à vontade: 

[E-mail: ](malito:guilhermesantos.adv@protonmail.com)
