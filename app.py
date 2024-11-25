import os
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

ASCII_ART_FOLDER = 'ascii_art'

def get_ascii_art(category):
    try:
        file_path = os.path.join(ASCII_ART_FOLDER, f'{category}.txt')
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()
        else:
            return None
    except Exception as e:
        return str(e)

def get_random_category():
    try:
        return random.choice(os.listdir(ASCII_ART_FOLDER)).replace('.txt', '')
    except Exception as e:
        return str(e)

@app.route('/generate_ascii', methods=['GET'])
def generate_ascii():
    category = request.args.get('category', '').lower()
    if not category:
        category = get_random_category()
    ascii_art = get_ascii_art(category)
    if ascii_art is None:
        return jsonify({
            'error': f'No ASCII art found for category "{category}". Please choose a valid category.'
        }), 404
    return jsonify({
        'category': category,
        'ascii_art': ascii_art
    })

if __name__ == '__main__':
    app.run(debug=True)
