from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')


@app.route("/", methods=['GET'])
def index():
    response = requests.get("https://gisn.tel-aviv.gov.il/GisOpenData/service.asmx/GetLayer?layerCode=970&layerWhere=&xmin=&ymin=&xmax=&ymax=&projection=")
    data = response.json()
    items = data.get("features")
    parking_lot_data = []
    for item in items:
        parking_lot_data.append(item.get("attributes"))
    print(parking_lot_data)
    return render_template('index.html', parking_lot_data=parking_lot_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9000", debug=True)