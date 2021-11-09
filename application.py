from flask import jsonify
from flask import Flask
import numpy as np

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello Sina\n'

@application.route('/random/<n>')
def randomvalues(n):
    values = np.random.randint(0,10,int(n))
    result = {'values' : values.tolist()}
    return jsonify(result)

if __name__ == '__main__':
    application.run('localhost', 5000,debug=True)
