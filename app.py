from flask import Flask, request, jsonify
import flask
app = Flask(__name__)

@app.route('/')
def handle():
    return "home"
    
@app.route('/interface')
def hello():
    return flask.redirect('http://192.168.0.153:8081/main.html', code=302)    
    #return "none"
    
if __name__ == '__main__':
    port = 9999
    app.run(host='192.168.0.153', port=port)
