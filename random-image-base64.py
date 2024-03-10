from flask import Flask, jsonify
import requests
from PIL import Image
from io import BytesIO
import base64
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all domains on all routes. For production, specify the origin.
CORS(app)

@app.route('/api/random-image-base64')
def random_image_base64():
    url = 'https://microservice-image-generator-bd1f70093a8a.herokuapp.com/random-image'
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return jsonify(img_str)
    else:
        return jsonify(error="Failed to fetch image"), 500

if __name__ == '__main__':
    app.run(debug=True)
