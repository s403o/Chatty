from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# app.host = 'localhost'
app.debug = True

socketio = SocketIO(app, cors_allowed_origins="*") # create server & fix cors errors

@socketio.on('message')
def message(msg):
  print('Message: ', msg)
  send(msg, broadcast=True) # send to everyone
  return None

if __name__ == '__main__':
  socketio.run(app)