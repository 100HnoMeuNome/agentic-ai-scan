FROM python:3.11-slim

# Instala ferramentas básicas
RUN apt-get update && apt-get install -y \
    wget \
    git \
    nmap \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Instala Go 1.22+ manualmente
ENV GOLANG_VERSION 1.22.3

RUN wget https://go.dev/dl/go$GOLANG_VERSION.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go$GOLANG_VERSION.linux-amd64.tar.gz && \
    rm go$GOLANG_VERSION.linux-amd64.tar.gz

ENV PATH="/usr/local/go/bin:$PATH"

# Clona e compila o Zgrab2
RUN git clone https://github.com/zmap/zgrab2.git /opt/zgrab2 && \
    cd /opt/zgrab2 && go build

# Copia requirements e instala Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . /app
WORKDIR /app

# Torna o script executável
RUN chmod +x entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]
