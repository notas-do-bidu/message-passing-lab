import pika
import csv


def envia_tarefa(números):
    """
    Aceita uma mensagem em forma de string
    e envia para o canal padrão do RabbitMQ.
    """

    # Não podemos mandar strings puras para o RabbitMQ. Primeiro elas precisam
    # ser convertidas em bytes. Em python nós podemos fazer isso usando o
    # método 'encode'. Utilizamos do encoding UTF-8 por ser praticamente
    # o padrão para toda forma de comunicação digital atualmente.
    mensagem = ",".join(números)
    corpo_mensagem = mensagem.encode("utf-8")

    # Primeiro criamos uma conexão
    conexão = pika.BlockingConnection()

    # Então abrimo o canal
    canal = conexão.channel()
    canal.queue_declare(queue="tarefa", durable=True)

    # E então publicamos a mensagem
    canal.basic_publish(
        exchange="",
        routing_key="tarefa",
        body=corpo_mensagem,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ),
    )

    # Por fim, fechamos a conexão
    conexão.close()


for record in csv.reader(open("data.csv")):
    envia_tarefa(record)
