from flask import Blueprint
from flask import render_template,request
from test import send_post
from flask import jsonify

xnho = Blueprint('xnho', __name__)


@xnho.route('/', methods=['GET', 'POST'])
def home():
    return render_template('hello.html')

@xnho.route('/next', methods=['GET', 'POST'])
def next():
    print(1111)
    print(request.method)
    #type = request.form['apitype']
    parm_str=request.form['parm_str']
    name = request.form['query_name']
    data = send_post(name, parm_str)
    print(data)
    return jsonify(data)