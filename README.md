Projeto Conceptus loja virtual
---

O projeto consiste em uma implementação de uma REST-API utilizando o DRF (DjangoRESTFramework), para simular um catalogo simples de produtos, contendo os seguintes campos:

Produto:
 - Nome, Preço, Descrição e Categoria (podendo nao ter categoria)
Categoria:
- Nome

O projeto foi implementado utilizando django 3.1.1 e DjangoRESTFramework 3.12.0, como banco de dados sqlite 3.31.1
e django-filter 2.4.0

A Api implementada é bem simples possuindo apenas dois endpoints:

/produto/ e /categoria/

onde poderao ser utilizados os verbos padrão do REST para interagir com os dados. foi utilizada a interface do DRF para facilitar os testes via navegador, de forma que o usuario pode acessar a url para utilizar filtros e realizar consultas.

Para enriquecer a API, foram adicionados 3 tipos de filtros para os produtos, que devem ser acessados via parametros GET:

- um para busca textual do nome do produto: search
- um para selecionar categoria de produtos (listar produtos de determinada categoria por exemplo)
- um de ordenacao, onde os campos podem ser ordenados

Todos esses filtros podem ser testados e verificados pela interface web do navegador de API do DRF.

Como instalar:
--
Para utilizar o projeto, basta seguir os passos:

1) Criar ambiente virtual

mkdir conceptus
cd conceptus
python3 -m venv env
. env/bin/activate

2) Baixar o codigo do repositorio

git clone https://github.com/rodrixl/conceptu.git
cd conceptu

Instalar pacotes de dependencias

pip install -r requeriments.txt

3) Executar o servidor do django

./manage runserver 0.0.0.0:5000

logar na aplicação (acesso é restrito a usuários logados, conforme especificação)
usar usuario: admin e senha: senha123

http://0.0.0.0:5000/api-auth/login/

4) Acessar o API via urls (possui interface do DRF para tornar amigavel as coisas):

http://0.0.0.0:5000/api/

ou (se desejado) acessar via admin para gerenciar os dados

http://0.0.0.0:5000/admin

Lembrando que, para acessar a api, será necessário está logado em alguma conta. o banco de dados que acompanha o projeto, ja possui um usuario admin com as credenciais:

login: admin
password: senha123

o usuario pode se logar e deslogar pelas urls:

http://0.0.0.0:5000/api_auth/login/
e
http://0.0.0.0:5000/api_auth/logout/

exemplos de chamadas da API:

http://localhost:5000/api/produto/?ordering=-nome
http://localhost:5000/api/produto/?search=heineken
http://localhost:5000/api/produto/?categoria=Mercado

http://localhost:5000/api/categoria/

Att,
Rodrigo.
