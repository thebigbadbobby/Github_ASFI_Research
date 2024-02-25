from flask import Flask, send_file
import os
import random
from PIL import Image

app = Flask(__name__)

@app.route('/generate-image', methods=['GET'])
def generate_image():
    images_dir = './images'
    random_filename = random.choice([
        os.path.join(images_dir, filename)
        for filename in os.listdir(images_dir)
        if not filename.startswith('.')  # Exclude hidden files
    ])
    
    return send_file(random_filename, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)