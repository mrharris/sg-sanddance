from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=["POST"])
def route():
    post_dict = request.form.to_dict()
    return jsonify(post_dict)
