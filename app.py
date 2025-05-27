from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer bce-v3/ALTAK-fEzp0TwHviTJPHWwlESjX/e6199b5e118afce4ca5328c2d296e99f5ccf4c53'
    }
    payload = {
        'prompt': prompt,
    }
    response = requests.post('https://qianfan.baidubce.com/v2/images/generations', headers=headers, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
