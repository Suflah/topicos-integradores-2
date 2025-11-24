[README.md.md](https://github.com/user-attachments/files/23720931/README.md.md)
# Cadastro de Clientes (corrigido)

Como rodar:
1. Crie e ative um virtualenv (recomendado).
2. `pip install -r requirements.txt`
3. `python app.py`
4. Abra http://127.0.0.1:5000 no navegador.

Observações:
- O banco SQLite (`clients.db`) será criado automaticamente na mesma pasta do `app.py`.
- Em produção, use um servidor WSGI (gunicorn) e configure `app.config['SECRET_KEY']` adequadamente.
