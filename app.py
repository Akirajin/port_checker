from flask import Flask
import os


from checker import has_open_port

app = Flask(__name__)

@app.route("/check/ip/<string:ip>/port/<string:port>")
def hello_world(ip, port):
    res = has_open_port(ip, port)
    return str(res)



if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8080)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
