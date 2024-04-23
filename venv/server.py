from flask import Flask, request, jsonify
from indexer import Indexer
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Load the indexer
indexer = Indexer()
indexer.load_index('index.pkl')  # Ensure the path is correct

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    if not query:
        logging.error("No query provided")
        return jsonify({'error': 'No query provided'}), 400
    results = indexer.query(query)
    logging.info(f"Query: {query}, Results: {results}")
    if not any(results.flatten()):
        return jsonify({'results': 'No matches found.'}), 404
    return jsonify({'results': results.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)  # Turn off debug for production
