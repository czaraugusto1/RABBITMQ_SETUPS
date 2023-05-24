import pika

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria a fila
channel.queue_declare(queue='fila_teste')

# Publica uma mensagem na fila
message = 'Olá, RabbitMQ!'
channel.basic_publish(exchange='', routing_key='fila_teste', body=message)
print("Mensagem enviada: %r" % message)

# Fecha a conexão
connection.close()
