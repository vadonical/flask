from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from geventwebsocket.websocket import WebSocket
from flask import Flask, request

app = Flask(__name__)


@app.route("/web_socket")
def web_socket():
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    while 1:
        user_msg = user_socket.receive()
        print(user_msg)
        user_socket.send(user_msg)


if __name__ == '__main__':
    http_server = WSGIServer(("0.0.0.0", 9527), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
