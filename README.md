# Invoice Generator - Stark Bank

Este projeto gera automaticamente de 8 a 12 invoices a cada execução, que são de 3 em 3h durante 24h, utilizando a API do Stark Bank com dados fictícios.

## 📦 Requisitos

- Python 3.10+
- Conta e projeto configurado no Stark Bank
- Chave privada no formato `secp256k1` no arquivo `.env`

---

## ⚙️ Instalação

```bash
# 1. Clone o projeto
git clone https://github.com/Rampazo/invoice_generator.git
cd invoice_generator

# 2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv
.\venv\Scripts\activate # Windows
source venv/bin/activate # Linux ou Mac

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure a variável de ambiente
# Crie um arquivo .env com o token esperado:
STARKBANK_ENVIROMENT=sandbox
STARKBANK_PROJECT_ID=seu_project_id
STARKBANK_PRIVATE_KEY=-----BEGIN EC PRIVATE KEY-----SUA_CHAVE_AQUI-----END EC PRIVATE KEY-----

# 5. Execute o script
python main.py
```

---

## 🧑🏻‍💻 Autor

```bash
Gabriel Rampazo
gabriel.rampazo@hotmail.com
```