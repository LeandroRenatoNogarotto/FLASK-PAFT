
from flask import Flask,request,Response,render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/date',methods=['GET'])
def date():
    return render_template('date.html')

@app.route('/numbers',methods=['GET'])
def numbers():
    return render_template('numbers.html')

def calculate_dif_dates(start_date,end_date):
    days = (end_date-start_date).days
    weeks = int(days/7)
    months = 12 * (end_date.year - start_date.year) + end_date.month - start_date.month;
    return {
        'days':days,
        'weeks':weeks,
        'months':months
    }

@app.route('/date_service',methods=['GET'])
def date_service_get():
    if 'start_date' in request.args and 'end_date' in request.args:
        start_date = datetime.strptime(request.args.get('start_date'),"%Y-%m-%d");
        end_date = datetime.strptime(request.args.get('end_date'),"%Y-%m-%d");
        return calculate_dif_dates(start_date,end_date)

    return Response("400-BAD REQUEST - Error on input",status = 400)
@app.route('/date_service',methods=['POST'])
def date_service_post():
    if request.is_json and 'start_date' in request.json and 'end_date' in request.json:
        start_date = datetime.strptime(request.json['start_date'],"%Y-%m-%d");
        end_date = datetime.strptime(request.json['end_date'],"%Y-%m-%d");
        return calculate_dif_dates(start_date,end_date)

    return Response("400-BAD REQUEST - Error on input",status = 400)

@app.route('/numbers_service',methods=['POST','GET'])
def numbers_service():
    if request.method == 'POST':
        numbers = request.json['numbers']
    elif request.method == 'GET':
        numbers = request.args.get('numbers')
# 3;2;8;4;1;77;44
    list = numbers.split(';')
    list = [int(x) for x in list]
    dict ={}
    list.sort()
    dict['sorted'] = str(list)
    list.reverse()
    dict['reversed'] = str(list)
    evens = [i for i in list if i%2 == 0]
    dict['evens'] = str(evens)
    return dict    
app.run(debug=True)
