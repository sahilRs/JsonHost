from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/my.json", methods=["GET"])
def get_data():
    data = [
        {
            "id": "8fc23be1465d94c4",
            "key": "key11",
            "expiresAt": "2026-05-30",
            "allowOffline": True,
        },
        {
            "id": "ali456",
            "key": "key2",
            "expiresAt": "2025-06-15",
            "allowOffline": False,
        },
        {
            "id": "370aadebb16b8920",
            "key": "MITRACUSTOM1122",
            "expiresAt": "2026-06-20",
            "allowOffline": True,
        },
        {
            "id": "f0a09d2316ae125a",
            "key": "MITRACUSTOM3344",
            "expiresAt": "2026-06-20",
            "allowOffline": True,
        },
         {
            "id": "4f992c7022c0565f",
            "key": "BIZOMCUSTOM272",
            "expiresAt": "2026-06-20",
            "allowOffline": True,
        },
        {
            "id": "09b6959b5da928f0",
            "key": "MITRACUSTOM510",
            "expiresAt": "2026-06-20",
            "allowOffline": True,
        },
        {
            "id": "7096c83f9746c967",
            "key": "SALESASSISTCUSTOM272",
            "expiresAt": "2026-07-20",
            "allowOffline": True,
        },
         {
            "id": "a0edb4fca8334a97",
            "key": "MITRACUSTOM5790",
            "expiresAt": "2026-07-20",
            "allowOffline": True,
        },
        
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run()
