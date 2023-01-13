from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/health')
def health():
    return {"Healthy": "Up"}

@app.route('/status')
def get():
    code = request.args.get('code')
    return Response("{'message','Status Code has been created.', 'code': "+code+"}", status=code, mimetype='application/json')

app.run(host='0.0.0.0', debug=True, port="5000")