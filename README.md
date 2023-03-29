# SpyFruit
Aplicação Web integrada via API com ThingSpeak para monitoramento de temperatura enviado por módulo A6 GSM/GPRS e microcontrolador atmega328p


## Objetivo

Com o objetivo de monitorar a temperatura de forma remota, optou-se pelo uso do sensor DS18B20 em conjunto com o módulo A6 GSM/GPRS para o envio dos dados. Para que os dados sejam visualizados de maneira mais prática, decidiu-se integrar o envio para o ThingSpeak, que é uma plataforma online para armazenamento e visualização de dados em tempo real. Além disso, foi realizada uma conexão via API com uma aplicação web desenvolvida com o Django, onde será apresentado um dashboard de monitoramento do tempo. Para tornar a apresentação dos dados mais amigável, foram utilizadas bibliotecas gráficas como o ChartJs, que permite a criação de gráficos e visualizações interativas. Dessa forma, é possível monitorar a temperatura de forma eficiente e acessível a qualquer momento e em qualquer lugar.

## Requisitos

É necessário ter instalado Python, Django e caso deseje utilizar manter o modelo SGBD, o PostgreSql.

Após a instalação dessas ferramentas, todas as dependências de bibliotecas necessárias devem ser instaladas utilizando o comando dentro da pasta raiz do projeto:

* **pip install -r requirements.txt**

É importante ressaltar que as configurações da API Key e Channel do ThingSpeak, bem como os dados do usuário, senha e nome do banco de dados, devem ser descritos no arquivo .env, que está localizado dentro da pasta principal do SpyFruit.

![database](https://user-images.githubusercontent.com/73910233/228676754-9136da9b-8ebe-46be-bfe8-4e8852752e48.png)

## Criação de superusuários

Para criação de um superusuário, deverá ser feito pelo terminal:

* **python manage.py createsuperuser**

Assim informar nome de usuário, e-mail e senha

## Execução

Utilizar o comando:

* **python manage.py runserver** 

![login](https://user-images.githubusercontent.com/73910233/228676914-d2592415-e13f-4240-a80d-01b40920cbac.png)

![dashboard](https://user-images.githubusercontent.com/73910233/228676933-3eaccc49-1edd-416f-9880-4f0ec5fbf07f.png)

## Observações
Essa versão não está implementada CronJob para atualização dos dados via API, com isso é necessário acessar a rota /save_data para serem transferidos os dados para o banco de dados local.
A rota de login é 127.0.0.1:8000/login
