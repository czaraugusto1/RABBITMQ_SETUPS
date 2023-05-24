FROM python:3

# Instala o RabbitMQ
RUN apt-get update && apt-get install -y rabbitmq-server

# Instala o supervisor
RUN apt-get install -y supervisor

# Configura o supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Configuração do diretório de trabalho
WORKDIR /app
COPY . .

# Instala as dependências do seu aplicativo Python
RUN pip install -r requirements.txt

# Configuração do RabbitMQ
RUN rabbitmq-plugins enable rabbitmq_management
COPY rabbitmq.config /etc/rabbitmq/

# Executa o supervisor
CMD ["/usr/bin/supervisord"]
