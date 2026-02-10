# 🌍 GeoSearch – Buscador de Ubicaciones con Flask

GeoSearch es un sitio web desarrollado con **Flask** que permite buscar lugares de interés utilizando la **API de Geolocalización de OpenStreetMap (Nominatim)** y visualizar su ubicación en un mapa interactivo.

---

## 🚀 Tecnologías utilizadas

- Python 3
- Flask
- HTML5
- CSS3
- API OpenStreetMap – Nominatim

---

## 📂 Estructura del proyecto

flask_hola_mundo/
│
├── app.py
├── templates/
│ ├── index.html
│ └── map.html
├── venv/
└── README.md


---

## 🌐 Funcionamiento del sistema

1. El usuario ingresa el nombre de un lugar (ciudad, sitio histórico, etc.)
2. Flask envía la solicitud a la API de Nominatim
3. La API responde con coordenadas geográficas en formato JSON
4. El sistema muestra:
   - Nombre del lugar
   - Latitud
   - Longitud
5. Se visualiza la ubicación en un mapa centrado tipo Google Maps

---

## 🔗 API utilizada

**OpenStreetMap – Nominatim**

- Tipo: API REST
- Método: GET
- Formato de respuesta: JSON
- Autenticación: No requiere API Key
- Endpoint:
https://nominatim.openstreetmap.org/search


---

👩‍💻 Autor
Ana María Barrientos
TSU en Desarrollo de Software
Universidad Tecnológica del Norte de Guanajuato
