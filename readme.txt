Dockerfile contendo python build base da aplicação


FROM python:2.7 #conteiner a ser editado
ADD . /todo #cria um diretório na imagem do conteiner python que tem o linux
WORKDIR /todo #seta o diretório criado como o diretório principal de trabalho do conteiner
RUN pip install -r requirements.txt #executa a instalação dos modulos listados no txt pelo pip




docker-compose contendo redis flask e mongo, dois bancos para teste e o servidor 

web: #da build no conteiner web com o python, libera a porta de acesso do servidor (flask) e linka os conteiners de dependência no "links" que são os dois db's 
  build: . #comando que executa o build do dockerfile que esta no diretório
  command: python -u app.py #comando que executa o arquivo da aplicação
  ports: #libera a porta 
    - "5000:5000"
  volumes: #diretório da máquina onde é guardado toda a aplicação
    - .:/todo
  links: #conteiners linkados
    - db
    - redis
db: #especificando a imagem do mongo a ser baixada
  image: mongo:3.0.2
redis: #imagem do redis a ser baixada (quando n tem parâmetro de versão é a mais atual)
  image: redis

app.py contem o back-end da aplicação teste
templates contem front-end da aplicação em jinja2 (padrão flask html)
