import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="tarefa", durable=True)
print(" [*] Aguardando Tarefas!!")


def callback(ch, method, properties, body):
    items = body.decode().split(",")
    items = [int(item) for item in items]
    print(f" [x] Recebi {items}")
    result = sum(items) / len(items)
    print(f" [x] Pronto! {result}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="tarefa", on_message_callback=callback)

channel.start_consuming()
