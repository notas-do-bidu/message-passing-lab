import pika
from time import sleep


def envia_mensagem(mensagem, exchange):
    """
    Aceita uma mensagem em forma de string
    e envia para o canal padrão do RabbitMQ.
    """

    # Não podemos mandar strings puras para o RabbitMQ. Primeiro elas precisam
    # ser convertidas em bytes. Em python nós podemos fazer isso usando o
    # método 'encode'. Utilizamos do encoding UTF-8 por ser praticamente
    # o padrão para toda forma de comunicação digital atualmente.
    corpo_mensagem = mensagem.encode("utf-8")

    # Primeiro criamos uma conexão
    conexão = pika.BlockingConnection()

    # Então abrimo o canal
    canal = conexão.channel()
    canal.exchange_declare(exchange=exchange, exchange_type="fanout")

    # E então publicamos a mensagem
    canal.basic_publish(exchange=exchange, routing_key="hello", body=corpo_mensagem)

    # Por fim, fechamos a conexão
    conexão.close()


mensagens = [
    "SAO",
    "SAO",
    "SAO",
    "COR",
    "fim",
]

for mensagem in mensagens:
    print("Enviando mensagem de futebol")
    envia_mensagem(mensagem, "futebol")
    sleep(1)
