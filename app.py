from flask import Flask, jsonify

app = Flask(name)


@app.route("/my.json", methods=["GET"])
def get_data():
    data = [
        {
            "id": "abc123def456ghi789",
            "key": "key1",
            "expiresAt": "2025-05-30",
            "allowOffline": true,
        },
        {
            "id": "ali456",
            "key": "key2",
            "expiresAt": "2025-06-15",
            "allowOffline": false,
        },
    ]
    return jsonify(data)


if name == "main":
    app.run()
