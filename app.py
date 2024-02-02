from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Liste pour stocker les points
points = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_point', methods=['POST'])
def add_point():
    data = request.json
    points.append(data)
    # Sauvegarder dans un fichier JSON
    with open('lieu.json', 'w') as f:
        json.dump(points, f, indent=4)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)