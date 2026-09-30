# Vértice — cadastro, login e loja

Projeto de estudo feito com Django, com cadastro e autenticação de usuários, painel por perfil e um fluxo simples de loja, carrinho e pedidos.

## Estrutura

O código da aplicação está na pasta [`project/`](./project/). As URLs existentes ficam configuradas em `project/sistema/urls.py`.

## Requisitos

- Python 3.10 ou superior
- Git (opcional)

## Baixar e executar

Clone o repositório e entre na pasta da aplicação:

```bash
git clone https://github.com/Emmanuel8727/project.git
cd project/project
```

Crie e ative um ambiente virtual.

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux ou macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências, prepare o banco local e inicie o servidor:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra <http://127.0.0.1:8000/>.

## E-mail

Em desenvolvimento, o Django usa o backend de console. Para SMTP em um ambiente que não seja de desenvolvimento, configure as variáveis `DJANGO_SECRET_KEY`, `EMAIL_HOST_USER` e `EMAIL_HOST_PASSWORD` no ambiente antes de iniciar a aplicação. Não salve credenciais no código nem envie arquivos `.env` ao repositório.

As configurações atuais são para desenvolvimento. Antes de disponibilizar a aplicação em produção, configure `DEBUG`, `ALLOWED_HOSTS`, uma chave secreta própria e as proteções de produção recomendadas pelo Django.

## Rotas principais

- `/` — página inicial
- `/cadastro/` — cadastro de usuário
- `/login/` — login
- `/painel/` — painel principal
- `/carrinho/loja/` — loja
- `/carrinho/lista_carrinho/` — carrinho
- `/carrinho/checkout/` — finalização do pedido
- `/admin/` — administração do Django

## Observações

- O banco SQLite é criado localmente pelas migrações; o arquivo de banco não é incluído no repositório.
- O projeto é destinado a estudo e desenvolvimento local, não está pronto para produção sem configuração adicional.
