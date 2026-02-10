from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        lugar = request.form["lugar"]

        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": lugar,
            "format": "json",
            "limit": 1
        }
        headers = {
            "User-Agent": "flask-geolocalizacion-educativo"
        }

        response = requests.get(url, params=params, headers=headers)
        data = response.json()

        if data:
            resultado = {
                "lat": data[0]["lat"],
                "lon": data[0]["lon"],
                "display_name": data[0]["display_name"]
            }

    return render_template("index.html", resultado=resultado)


# 👉 ESTA RUTA ES LA QUE FALTABA O ESTABA MAL
@app.route("/map")
def map_view():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    return render_template("map.html", lat=lat, lon=lon)


if __name__ == "__main__":
    app.run(debug=True)
