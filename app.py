from flask import Flask

from checker import has_open_port

app = Flask(__name__)

@app.route("/check/ip/<string:ip>/port/<string:port>")
def hello_world(ip, port):
    res = has_open_port(ip, port)
    return f'{res}'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)