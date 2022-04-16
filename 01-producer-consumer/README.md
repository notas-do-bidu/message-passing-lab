Demo de passagens de mensagens entre um código Go e um código Python usando RabbitMQ

1. Rode um servidor rabbitmq com `docker run -p 5672:5672 rabbitmq`
2. Rode o código usando o comando `go run .` na pasta `receiver-go`
3. Rode o código python executando `python sender.py`