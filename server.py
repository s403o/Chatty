from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy

# server
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*") # create server & fix cors errors

# db 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:docker@localhost:5432/chat"
db = SQLAlchemy(app)

class ChatHistory(db.Model):
  __tablename__ = 'history'
  id = db.Column('id', db.Integer, primary_key=True)
  message = db.Column('message',db.String(250))

# socket
@socketio.on('message')
def message(msg):
  print('Message: ', msg)
  message = ChatHistory(message=msg)
  db.session.add(message)
  db.session.commit()
  send(msg, broadcast=True) # send to everyone
  return None

@app.route('/')
def index():
  messages = ChatHistory.query.all()
  return render_template('index.html', messages=messages)
if __name__ == '__main__':
  socketio.run(app, debug=False)