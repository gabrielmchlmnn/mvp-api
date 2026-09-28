# MVP API

API REST desenvolvida em **Python com FastAPI** para gerenciamento de alunos. A aplicação permite realizar operações de cadastro, consulta, atualização e exclusão de alunos, utilizando **PostgreSQL** como banco de dados.

## Tecnologias utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn
* HTTPX
* Docker
* Docker Compose

## Funcionalidades

* Cadastro de alunos
* Consulta de todos os alunos
* Consulta de aluno por ID
* Atualização de alunos
* Exclusão de alunos
* Validação de e-mail
* Validação de CEP
* Integração com a API pública ViaCEP para consulta de endereços

## Estrutura do projeto

```text
mvp-api/
├── app/
│   ├── models/
│   │   └── student.py
│   ├── routes/
│   │   └── students.py
│   ├── schemas/
│   │   └── student.py
│   ├── database.py
│   └── main.py
├── .dockerignore
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Requisitos

Para executar o projeto localmente sem Docker, é necessário ter instalado:

* Python 3.12 ou superior
* PostgreSQL
* Git

Para execução utilizando containers:

* Docker
* Docker Compose

## Instalação local

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd mvp-api
```

### 2. Crie um ambiente virtual

Windows:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco PostgreSQL chamado `mvp_db`.

Configure a variável de ambiente `DATABASE_URL`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mvp_db
```

As credenciais podem ser alteradas de acordo com a configuração do PostgreSQL utilizado.

### 5. Inicie a API

```bash
uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://localhost:8000
```

A documentação interativa do FastAPI pode ser acessada em:

```text
http://localhost:8000/docs
```

## Execução com Docker

O projeto também possui configuração para execução utilizando Docker Compose.

Na pasta raiz do projeto, execute:

```bash
docker compose up --build
```

Esse comando inicializa:

* API FastAPI
* Banco de dados PostgreSQL

A API estará disponível em:

```text
http://localhost:8000
```

Para interromper os containers:

```bash
docker compose down
```

Para interromper os containers e remover os dados persistidos do PostgreSQL:

```bash
docker compose down -v
```

## Endpoints

| Método | Endpoint                 | Descrição             |
| ------ | ------------------------ | --------------------- |
| GET    | `/students/`             | Lista todos os alunos |
| GET    | `/students/{student_id}` | Consulta um aluno     |
| POST   | `/students/`             | Cadastra um aluno     |
| PUT    | `/students/{student_id}` | Atualiza um aluno     |
| DELETE | `/students/{student_id}` | Exclui um aluno       |

### Exemplo de cadastro

```json
{
  "name": "Gabriel Michelmann",
  "email": "gabriel@example.com",
  "phone": "47999999999",
  "zip_code": "89069040"
}
```

## Integração com ViaCEP

O projeto utiliza a API pública **ViaCEP** para consultar informações de endereço a partir do CEP informado pelo usuário.

A consulta é realizada pela interface e os dados retornados são utilizados para apresentar:

* Logradouro
* Bairro
* Cidade
* Estado

O endereço consultado não é armazenado no banco de dados. O sistema armazena somente o CEP associado ao aluno.

## Banco de dados

A aplicação utiliza PostgreSQL e possui a tabela `students`, contendo os seguintes campos:

| Campo      | Tipo    | Descrição              |
| ---------- | ------- | ---------------------- |
| `id`       | Integer | Identificador do aluno |
| `name`     | String  | Nome do aluno          |
| `email`    | String  | E-mail do aluno        |
| `phone`    | String  | Telefone do aluno      |
| `zip_code` | String  | CEP do aluno           |

## Desenvolvimento

Para verificar alterações no código durante o desenvolvimento, execute a API com:

```bash
uvicorn app.main:app --reload
```

O parâmetro `--reload` faz com que o servidor seja reiniciado automaticamente quando houver alterações nos arquivos do projeto.
