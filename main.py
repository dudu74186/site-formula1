import formula as f1
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import threading

#teste flask
app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

numdrive = 55
sessao = str("latest")
dados = f1.getapicardata(numdrive, sessao)

# Função para atualizar a variável em segundo plano
def update_data():
    while True:
        shared_data = f1.percorreapi(dados)
        socketio.emit("update", shared_data)  # Enviar dados ao cliente
thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

if __name__ == '__main__':
    socketio.run(app, debug=False)