# Documentação Técnica Simplificada - Cadastro de Clientes

**Aluno:** Cauã Machado Leite  
**Matrícula:** 01438266  
**Disciplina:** Tópicos Integradores 2  
**Professora:** Pryscilla  

---

**Resumo executivo (1 página):**
O sistema "Cadastro de Clientes" é uma aplicação web simples desenvolvida em Python (usando o framework Flask)
que permite cadastrar e listar clientes em um banco de dados SQLite.
Seu objetivo é demonstrar uma feature mínima funcional e o uso de boas práticas de versionamento com Git e GitHub.

**Arquitetura (fluxo do sistema):**
1. Usuário acessa a rota `/` → a função `index()` consulta o banco SQLite e exibe os clientes cadastrados.
2. Usuário acessa `/add` → a função `add()` exibe um formulário para inserção de novos clientes.
3. Após o envio, o sistema salva o cliente no banco e redireciona o usuário para a listagem principal.

**Tecnologias utilizadas:**
- Python 3.x
- Flask (microframework web)
- SQLite (banco de dados leve embutido)
- HTML + CSS (templates com Jinja2)

**Manual de instalação e execução:**
1. Clonar o repositório GitHub.
2. Criar ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```
3. Instalar dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Executar o servidor:
   ```bash
   python app.py
   ```
5. Acessar o sistema em: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

**Objetivo educacional:**
Avaliar a capacidade do aluno em desenvolver, versionar e documentar um pequeno sistema funcional.
