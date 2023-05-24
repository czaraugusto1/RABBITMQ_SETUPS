import pika

# Função para gerar mensagens
def gerar_mensagens():
    # Conexão com o RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Cria a fila
    channel.queue_declare(queue='fila_teste')

    # Gera 10 mensagens para serem consumidas
    for i in range(1, 11):
        mensagem = f"Mensagem {i}"
        # Publica a mensagem na fila
        channel.basic_publish(exchange='', routing_key='fila_teste', body=mensagem)
        print("Mensagem gerada e enviada: %r" % mensagem)

    # Fecha a conexão
    connection.close()

# Chamada da função para gerar mensagens
gerar_mensagens()
