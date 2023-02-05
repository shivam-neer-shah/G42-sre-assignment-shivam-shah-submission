from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import os

app = Flask(__name__)

ES_URL = os.environ.get("ES_URL", "http://localhost:9200")
es = Elasticsearch([ES_URL])
index_mapping = {
    "mappings": {
        "properties": {
            "population": {
                "type": "integer"
            }
        }
    }
}
es.indices.delete(index='city_population')
es.indices.create(index='city_population', body=index_mapping)

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

@app.route('/city/population', methods=['POST', 'PUT'])
def add_or_update_city_population():
    city = request.json['city']
    population = request.json['population']
    es.index(index='city_population', id=city, body={'population': population})
    return 'Success'

@app.route('/city', methods=['GET'])
def get_all_cities():
    cities = es.search(index='city_population', body={'query': {'match_all': {}}})
    return jsonify([{'city': city['_id'], 'population': city['_source']['population']} for city in cities['hits']['hits']])

@app.route('/city/<string:city>/population', methods=['GET'])
def get_city_population(city):
    population = es.get(index='city_population', id=city)
    return jsonify({'city': city, 'population': population['_source']['population']})

if __name__ == '__main__':
    app.run(host='0.0.0.0')