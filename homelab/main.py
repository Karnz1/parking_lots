from flask import Flask, render_template, request
import requests
import os, socket

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
PARKING_API_URL = os.environ.get("parking_api_url")

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/parking/tel-aviv", methods=['GET'])
def parking_tlv():
    response = requests.get(PARKING_API_URL)
    data = response.json()
    items = data.get("features")
    hostname = socket.gethostname()
    parking_lot_data = []
    for item in items:
        parking_lot_data.append(item.get("attributes"))
    print(parking_lot_data)
    return render_template('parking_tlv.html', parking_lot_data=parking_lot_data, hostname=hostname)

@app.route("/recipes")
def recipes():
    return render_template('recipes.html')


@app.route("/create_recipe", methods=['GET', 'POST'])
def create_recipe():
    if request.method == 'GET':
        return render_template('create_recipe.html')
    elif request.method == 'POST':
        recipe = {}
        if 'name' in request.form.keys():
            name = request.form['name']
            recipe['name'] = name
        if 'ingredients' in request.form.keys():
            ing = {}
            ingredients = request.form['ingredients']
            for line in ingredients.splitlines():
                key, value = line.split(' ')
                ing[key] = value
            recipe['ingredients'] = ing
        if 'instructions' in request.form.keys():
            instructions = request.form['instructions']
            recipe['instructions'] = instructions
        if 'meal_type' in request.form.keys():
            meal_type = request.form['meal_type']
            recipe['meal_type'] = meal_type
        return recipe


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9000", debug=True)


