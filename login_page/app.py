from flask import Flask

app = Flask(__name__)

@app.route('/signup',methods=['POST'])
def signup(){
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_db[username] = password

    
}