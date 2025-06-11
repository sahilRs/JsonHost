from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    data = {
        "a": {
            "a": 1,
            "b": 2
        },
        "b": {
            "a": 3,
            "b": 4
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
  
