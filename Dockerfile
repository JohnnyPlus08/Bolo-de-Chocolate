# Usa uma imagem leve oficial do Python
FROM python:3.11-slim

# Define a pasta onde o projeto vai rodar dentro do container
WORKDIR /app

# Copia e instala as dependências do requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para dentro do container
COPY . .

# Expõe a porta que o Flask utiliza
EXPOSE 5000

# Executa o servidor aceitando conexões externas
CMD ["python", "app.py"]
