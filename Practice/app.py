from flask import Flask, render_template, jsonify, request
from webCrawler import extract
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/extract')
def webCrawler():
	args1 = request.args.get('args1')
	args2 = request.args.get('args2')
	args3 = request.args.get('args3')
	return extract(args1,args2,args3)


if __name__ == '__main__':
	app.run(debug=True, port=5000)
