from flask import Flask, request, jsonify
from es import Elastic

app = Flask(__name__)

elastic = Elastic()

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

@app.route('/city/population', methods=['POST', 'PUT'])
def add_or_update_city_population():
    data = request.json
    if not data:
        return 'Invalid request, please provide city and population in JSON format', 400
    city = data['city']
    population = data['population']
    elastic.index_city_population(city, population)
    return 'Success'

@app.route('/city', methods=['GET'])
def get_all_cities():
    try: 
        cities = elastic.get_all_city_populations()
        return jsonify([{'city': city['_id'], 'population': city['_source']['population']} for city in cities['hits']['hits']])
    except Exception as e:
        return f'Error while fetching all cities population: {e}', 500

@app.route('/city/<string:city>/population', methods=['GET'])
def get_city_population(city):
    try: 
        population = elastic.get_city_population(city)
        return jsonify({'city': city, 'population': population['_source']['population']})
    except Exception as e:
        return f'Error while fetching city population: {e}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0')
