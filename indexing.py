import requests, json, os
from elasticsearch import Elasticsearch


#os.environ['NO_PROXY'] = '172.19.0.2'
res = requests.get('http://localhost:9200')
print(res)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

"""The next line is the directory path that point to the data that has to be indexed"""

directory = 'data/polyplus'
for filename in os.listdir(directory):

    if filename.endswith(".json"):
        file_path = directory + '/' + filename
        print(file_path)
        f = open(file_path)
        docket_content = f.read()
        # Send the data into es
        es.index(index='test', ignore=400, doc_type='docket', body=json.loads(docket_content))

