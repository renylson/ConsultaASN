# Projeto Docker: Consulta de ASN por IP/Domínio
 

Este documento fornece instruções para construir e rodar o contêiner Docker para o projeto `app_consulta_asn`.

## Pré-requisitos

Antes de começar, certifique-se de que você tem o Docker instalado em sua máquina. Você pode baixar e instalar o Docker a partir de [docker.com](https://www.docker.com/products/docker-desktop).

## Configuração do Projeto

### 1. Inserir a API Key do [IPinfo](https://ipinfo.io/)


Antes de construir a imagem Docker, você precisa inserir a sua API Key do [IPinfo](https://ipinfo.io/) no arquivo `app.py`. Abra o `app.py` e localize a linha onde a API Key é configurada. Substitua o valor da chave pela sua API Key.

  

```python

# Inserir sua API key no lugar do 'SUA_API_KEY_AQUI'

API_KEY = 'SUA_API_KEY_AQUI'


```

### 2. Construir a Imagem Docker

No diretório do projeto onde o arquivo Dockerfile está localizado, execute o seguinte comando para construir a imagem Docker:

  

```sh

docker build -t app_consulta_asn .

```

### 3. Rodar o Contêiner Docker

Depois de construir a imagem, execute o seguinte comando para rodar o contêiner Docker:


```sh

docker run -d -p 5000:5000  --name app_consulta_asn app_consulta_asn

```

Isso iniciará o contêiner em segundo plano (-d) e mapeará a porta 5000 do contêiner para a porta 5000 da sua máquina local.


### 4. Verificar o Contêiner

Para verificar se o contêiner está rodando corretamente, use o comando:

```sh

docker ps

```

Isso exibirá uma lista dos contêineres em execução, incluindo app_consulta_asn.


### 5. Acessar o Aplicativo

Após o contêiner estar rodando, você pode acessar o aplicativo na seguinte URL:

```sh

http://<seu_ip>:5000

```

### 6. Encerrar o Contêiner

Para parar e remover o contêiner, você pode usar os comandos:

```sh

docker stop app_consulta_asn

docker rm app_consulta_asn

```

## Problemas e Suporte

Se você encontrar algum problema, verifique os logs do contêiner com o comando:

  

```sh

docker logs app_consulta_asn

```

Para suporte adicional, consulte a documentação oficial do Docker ou entre em contato com o mantenedor do projeto.

  

Aproveite ``` app_consulta_asn ```!
  
### Contato:

## [Clique aqui](https://gravatar.com/renylsonm)