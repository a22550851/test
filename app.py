from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    result = data['number1'] + data['number2']  # 简单的加法运算示例
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
