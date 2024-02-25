from flask import Flask, request, send_file
import torch
from diffusers import StableDiffusionXLPipeline
from PIL import Image
import io

app = Flask(__name__)

# Load the model (consider doing this outside the request handling to save time)
pipe = StableDiffusionXLPipeline.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float32)
pipe = pipe.to("cpu")

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data['prompt']

    # Generate the image
    image = pipe(prompt, num_inference_steps=1, guidance_scale=0.0).images[0]

    # Convert PIL image to byte array
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Return the image
    return send_file(io.BytesIO(img_byte_arr), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
