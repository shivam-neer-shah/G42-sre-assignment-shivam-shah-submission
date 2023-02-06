from elasticsearch import Elasticsearch
import os

class Elastic:
    def __init__(self):
        ES_URL = os.environ.get("ES_URL", "http://localhost:9200")
        self.es = Elasticsearch([ES_URL])
        self.index_mapping = {
            "mappings": {
                "properties": {
                    "population": {
                        "type": "integer"
                    }
                }
            }
        }
        self.es.indices.create(index='city_population', body=self.index_mapping, ignore=400)

    def index_city_population(self, city, population):
        self.es.index(index='city_population', id=city, body={'population': population})

    def get_all_city_populations(self):
        return self.es.search(index='city_population', body={'query': {'match_all': {}}})

    def get_city_population(self, city):
        return self.es.get(index='city_population', id=city)
