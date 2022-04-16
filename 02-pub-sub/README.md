# Pub-sub - Atualizando um placar



Imagine que você tem um aplicativo que acompanha o placar de um jogo em tempo
real. Como atualizar o placar para cada cliente, assim que um gol acontece?

Usando a arquitetura de pub-sub, um código de 'publisher' publica mensagens sobre
o que está acontecendo enquanto um código 'subscriber' acompanha essas mudanças.

Podemos implementar essa arquitetura de diversas formas. Nesse exemplo, fazemos
com RabbitMQ

## Rodando

1. Usando [docker](https://docs.docker.com/get-docker/),
rode uma instância de rabbitMQ:

```
docker run -p 5672:5672 rabbitmq
```

2. Abra pelo menos dois terminais ao mesmo tempo - para ver o efeito! - e execute
o código `subscriber.py`

3. Rode então o código `publisher.py`

4. Observe como o código `publisher` envia as mensagens de gol para o RabbitMQ
e como os códigos de `subscriber` leem essas informações.