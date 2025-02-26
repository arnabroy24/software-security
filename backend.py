from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json

def search_advisory_files(ghsa_id):
    advisory_directory = "linear_advisories"
    if not os.path.exists(advisory_directory):
        return None
    
    filename = ghsa_id + ".json"
    if filename in os.listdir(advisory_directory):
        filepath = os.path.join(advisory_directory, filename)
        try:
            with open(filepath, "r") as f:
                advisory_data = json.load(f)
            return advisory_data
        except json.JSONDecodeError:
            print(f"Invalid JSON file: {filename}")
        except Exception as e:
            print(f"Error reading file {filename}: {e}")
    
    return None

app = Flask(__name__)
CORS(app)

@app.route('/api/advisories/<ghsa_id>', methods=['GET'])
def retrieve_json(ghsa_id):
    if not ghsa_id:
        return jsonify({
            'error': 'GHSA ID is required',
            'status': 'failed'
        }), 400
    
    advisory = search_advisory_files(ghsa_id)
    
    if advisory:
        return jsonify(advisory)
    else:
        return jsonify({
            'error': 'Advisory not found',
            'status': 'not_found'
        }), 404

if __name__ == '__main__':
    app.run(debug=True)