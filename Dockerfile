# Usando a imagem oficial do Python 3.10 como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código do projeto para o diretório de trabalho
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expõe a porta que o Django usará
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
