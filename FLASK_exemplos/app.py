from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def index():
    return "Ola Flask"


@app.route('/get_service', methods=['GET'])
def get_service():
    return Response(reponse="isto é um get",
        status= 200, mimetype="application/html")


@app.route('/post_service', methods=['POST'])
def post_service():
    return "isto é um post"

@app.route('/html')
def html():
    return "<html><body><h1>HTML</h1></body></html>"

#@app.route('/hello/<name>')
@app.route('/hello/<string:name>')
def hello_name(name):
    return "hello " +name


@app.route('/soma1/<int:num>')
def soma1(num):
    return "somou 1: " +str (num+1.)

@app.route('/hello/<string:name>/lastname/<sobrenome>')
def hello_name_lastname(name,sobrenome):
    return "hello " +name + " " + sobrenome

@app.route('/soma2/<int:num1>/int:num2')
def soma2(num1,num2):
    return "somou: " +str (num1+num2)

@app.route('/subtract')
def subtrair():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return str(num1 - num2)

@app.route('/multi', methods=['POST'])
def multi():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    return str(num1 * num2)


app.run(debug=True)