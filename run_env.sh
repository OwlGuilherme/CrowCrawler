#!/bin/bash

# Nome do ambiente virtual
venv_name="scrapper-env"

# Verifica se o ambiente virtual já existe
if [! -d "$venv_name" ]; then
    python -m venv "$venv_name"
fi

# Ativa o ambiente virtual
source "$venv_name/bin/activate"

# Instala as dependências (opcional, dependendo do seu projeto)
# pip install -r requirements.txt