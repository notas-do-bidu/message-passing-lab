"""
Exemplo de código python que envia mensagens para o RabbitMQ.

(Sobre o idioma: https://notasdobidu.com/eca-o-bidu-ta-programando-em-portugues/)
"""
import pika


def envia_mensagem(mensagem):
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

    # E então publicamos a mensagem
    canal.basic_publish(exchange="", routing_key="hello", body=corpo_mensagem)

    # Por fim, fechamos a conexão
    conexão.close()


print("Enviando Hello!")
envia_mensagem("Hello")

print("Enviando 'oi' ")
