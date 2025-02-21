from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "quiz634"
app._static_folder = "static"


socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/control")
def control():
    return render_template("control.html")


@app.route("/control2")
def control2():
    return render_template("control2.html")


@app.route("/control_8o3x")
def control_8o3x():
    return render_template("control_8o3x.html")


@app.route("/api/show_plate", methods=["POST"])
def show_plate():
    data = request.json["data"]
    socketio.emit("show_plate", data)
    return "OK"


@app.route("/api/flip_plate", methods=["POST"])
def flip_plate():
    socketio.emit("flip_plate", {})
    return "OK"


@app.route("/api/flip_plate_except_last", methods=["POST"])
def flip_plate_except_last():
    socketio.emit("flip_plate_except_last", {})
    return "OK"


@app.route("/api/flip_plate_last", methods=["POST"])
def flip_plate_last():
    socketio.emit("flip_plate_last", {})
    return "OK"


@app.route("/api/delete_plate", methods=["POST"])
def delete_plate():
    socketio.emit("delete_plate", {})
    return "OK"


@app.route("/api/prepare_5o2x", methods=["POST"])
def prepare_5o2x():
    data = request.json["data"]
    socketio.emit("prepare_5o2x", data)
    return "OK"


@app.route("/api/update_5o2x", methods=["POST"])
def update_5o2x():
    data = request.json["data"]
    socketio.emit("update_5o2x", data)
    return "OK"


@app.route("/api/delete_5o2x", methods=["POST"])
def delete_5o2x():
    socketio.emit("delete_5o2x", {})
    return "OK"


@app.route("/api/prepare_7o3x", methods=["POST"])
def prepare_7o3x():
    data = request.json["data"]
    socketio.emit("prepare_7o3x", data)
    return "OK"


@app.route("/api/update_7o3x", methods=["POST"])
def update_7o3x():
    data = request.json["data"]
    socketio.emit("update_7o3x", data)
    return "OK"


@app.route("/api/delete_7o3x", methods=["POST"])
def delete_7o3x():
    socketio.emit("delete_7o3x", {})
    return "OK"


@app.route("/api/prepare_8o3x", methods=["POST"])
def prepare_8o3x():
    data = request.json["data"]
    socketio.emit("prepare_8o3x", data)
    return "OK"


@app.route("/api/update_8o3x", methods=["POST"])
def update_8o3x():
    data = request.json["data"]
    socketio.emit("update_8o3x", data)
    return "OK"


@app.route("/api/delete_8o3x", methods=["POST"])
def delete_8o3x():
    socketio.emit("delete_8o3x", {})
    return "OK"


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=7000, debug=True)
