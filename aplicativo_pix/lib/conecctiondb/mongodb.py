from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['itau']
collection = db['itau_ag1']

@app.route('/dados', methods=['GET'])
def obter_dados():
    dados = list(collection.find())
     # Converter ObjectId para strings
    for item in dados:
        if '_id' in item:
            item['_id'] = str(item['_id'])
            
    return jsonify(dados)

    

if __name__ == '__main__':
    app.run(debug=True)
