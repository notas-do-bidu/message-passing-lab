import pika
from collections import defaultdict

connection = pika.BlockingConnection()
channel = connection.channel()

channel.exchange_declare(exchange="futebol", exchange_type="fanout")

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange="futebol", queue=queue_name)

print(" [*] Ouvindo mensagens de futebol!")


gols = defaultdict(int)


def callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    if msg == "fim":
        print(f"Fim de jogo! Placar final: {dict(gols)}")
        return
    print(f"Gol do {msg}!")
    gols[msg] += 1


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)


channel.start_consuming()
