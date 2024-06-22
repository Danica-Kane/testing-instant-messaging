import pusher
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'

pusher_client = pusher.Pusher(
  app_id='1823100',
  key='8f81d7e418718530cd0f',
  secret='154623a0d6e30283db8b',
  cluster='us2',
  ssl=True
)

db = SQLAlchemy(app)

@app.route('/')
def index():
        
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def message():
    
    try:
        username = request.form.get('username')
        message = request.form.get('message')
        
        pusher_client.trigger('chat-channel', 'new-message', {'username' : username, 'message': message})

        
        return jsonify({'result': 'success'})
    except:
        
        return jsonify({'result': 'failure'})
    

if __name__ == '__main__':
    app.run(debug=True)