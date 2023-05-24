import pika

# Função callback para processar as mensagens recebidas
def callback(ch, method, properties, body):
    print("Mensagem recebida: %r" % body)

# Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Cria a fila
channel.queue_declare(queue='fila_teste')

# Define a função de callback para processar as mensagens
channel.basic_consume(queue='fila_teste', on_message_callback=callback, auto_ack=True)

# Inicia o consumo de mensagens
print('Aguardando mensagens. Pressione CTRL+C para sair.')
channel.start_consuming()
