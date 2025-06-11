from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/my.json", methods=["GET"])
def get_data():
    data = [
        {
            "id": "abc123def456ghi789",
            "key": "key1",
            "expiresAt": "2025-05-30",
            "allowOffline": True,
        },
        {
            "id": "ali456",
            "key": "key2",
            "expiresAt": "2025-06-15",
            "allowOffline": False,
        },
    ]
    return jsonify(data)


if __name__ == "__main__":
    app.run()
