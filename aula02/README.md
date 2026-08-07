# Configuração e Execução do Projeto Django

Este é o guia essencial para configurar e executar a aplicação localmente. O projeto utiliza Django e Django REST Framework para a construção da API.

## 🛠️ Passo a Passo para Configuração

Siga os comandos abaixo no terminal do seu sistema (recomendado uso do PowerShell no Windows) para iniciar o ambiente e a aplicação.

**1. Criar o ambiente virtual (Virtual Environment)**
Cria uma pasta chamada `venv` que isolará as dependências deste projeto das bibliotecas globais do seu computador.

```bash
python -m venv venv

```

**2. Ativar o ambiente virtual**
Ativa o ambiente para garantir que as instalações sejam feitas apenas dentro dele. *(Nota: este comando é para Windows PowerShell. No Linux/Mac seria `source venv/bin/activate`)*.

```powershell
venv\Scripts\Activate.ps1

```

**3. Instalar as dependências**
Instala o Django, o Django REST Framework (para criação de APIs) e o CORS Headers (para permitir que aplicações frontend em domínios diferentes consumam a API).

```bash
pip install django djangorestframework django-cors-headers

```

**4. Iniciar o projeto Django**
Cria a estrutura base do projeto chamado `loja` no diretório atual (o `.` no final indica que ele não deve criar uma subpasta extra).

```bash
django-admin startproject loja .

```

**5. Criar uma aplicação (App)**
Cria um módulo/app dentro do projeto chamado `produtos`. No Django, um projeto é composto por vários "apps" com responsabilidades específicas.

```bash
python manage.py startapp produtos

```

**6. Preparar o banco de dados (Migrations)**
Analisa as alterações feitas na estrutura dos dados (nos seus `models.py`) e cria os arquivos de instrução para o banco de dados.

```bash
python manage.py makemigrations

```

**7. Aplicar as migrações**
Executa os arquivos de migração gerados no passo anterior, criando as tabelas reais no banco de dados.

```bash
python manage.py migrate

```

**8. Criar um superusuário**
Cria uma conta de administrador para acessar o painel administrativo nativo do Django (`/admin`).

```bash
python manage.py createsuperuser

```

**9. Rodar o servidor de desenvolvimento**
Inicia a aplicação localmente. O `0.0.0.0:8000` faz com que o servidor fique acessível não só no `localhost`, mas também através do IP da sua máquina na rede local.

```bash
python manage.py runserver 0.0.0.0:8000

```

---

## 💻 Fluxo de Desenvolvimento da API

Se você está começando a desenvolver novas funcionalidades na aplicação, o fluxo de trabalho com Django REST Framework geralmente segue a ordem abaixo dentro do seu app (ex: `produtos`):

### 1. Models (`models.py`)

Aqui você define a estrutura do seu banco de dados usando classes Python. Cada classe representa uma tabela e seus atributos representam as colunas.
*Exemplo:* Criar uma classe `Produto` com os campos `nome`, `preco` e `quantidade`.

### 2. Serializers (`serializers.py`)

*Arquivo que precisa ser criado manualmente.* O serializer traduz os dados complexos (como as instâncias dos seus Models) em formatos compreensíveis por APIs (como JSON) e vice-versa. Ele também cuida da validação dos dados que chegam.
*Exemplo:* Criar um `ProdutoSerializer` que aponta para o model `Produto`.

### 3. Views (`views.py`)

Aqui fica a lógica de negócios da sua API. Usando o Django REST Framework, você geralmente cria `ViewSets` ou `APIViews` que definem o que acontece quando alguém faz um GET, POST, PUT ou DELETE.
*Exemplo:* Um `ProdutoViewSet` que utiliza o `ProdutoSerializer` para listar ou criar novos produtos.

### 4. Rotas (`urls.py`)

Define os caminhos (endpoints) da sua API. Você liga uma URL específica a uma View criada no passo anterior.
*Exemplo:* Mapear a URL `/api/produtos/` para o seu `ProdutoViewSet`.

> **Dica:** Não se esqueça de adicionar os apps instalados (`rest_framework`, `corsheaders` e o seu app `produtos`) na lista `INSTALLED_APPS` dentro do arquivo `settings.py` do projeto principal!