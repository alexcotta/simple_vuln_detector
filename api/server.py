from flask import Flask, request, jsonify
from stride.detector import analyze_architecture

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
	data = request.json
	if not data or 'architecture' not in data:
		return jsonify({'error': 'Payload deve conter a chave "architecture"'}), 400

	architecture_description = data['architecture']
	results = analyze_architecture(architecture_description)
	return jsonify(results)
	
if __name__ == '__main__':
	app.run(debug=True)