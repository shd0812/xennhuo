from flask import Flask,render_template

app = Flask(__name__)

from XH_View import xnho
app.register_blueprint(xnho,url_prefix='/home')


if __name__ == '__main__':
	#manager.run()
	app.run(host='192.168.110.53',port=1314,debug=True)