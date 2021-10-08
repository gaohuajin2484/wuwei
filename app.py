from flask import Flask,jsonify,request,render_template

from tools.data_makes import simple_date_make

app = Flask(__name__)


@app.route('/wuwei/simple_date_make/api',methods=['POST'])
def hello_world():
    data = request.data
    run = simple_date_make.Simple_date_make(data)
    result = run.to_result()
    response_data = {"data":result}
    return jsonify({response_data})

if __name__ == '__main__':
    app.run()