from flask import Flask, render_template
import requests
import os, socket

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
PARKING_API_URL = os.environ.get("parking_api_url")

@app.route("/", methods=['GET'])
def index():
    response = requests.get(PARKING_API_URL)
    data = response.json()
    items = data.get("features")
    hostname = socket.gethostname()
    parking_lot_data = []
    for item in items:
        parking_lot_data.append(item.get("attributes"))
    print(parking_lot_data)
    return render_template('index.html', parking_lot_data=parking_lot_data, hostname=hostname)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9000", debug=True)


