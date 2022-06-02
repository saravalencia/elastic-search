from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search

app = FastAPI()


class Text(BaseModel):
    text: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])


@app.get("/")
def simple_search():
    data = es.search(index="test", body={"query": {"match_all": {}}})
    test_list = []
    if data:
        for i in data['hits']['hits']:
            test_list.append(i['_source'])
    return test_list


@app.get("/search/{query}")
def search_es(query):
    data = es.search(index="test", body={"query": {
        "multi_match": {
            "query": query
        },
    }})
    test_list = []
    for i in data['hits']['hits']:
        test_list.append(i['_source'])
    return test_list


@app.get("/search-dsl")
def search_dsl():
    q = Search(using=es, index="test").query("query")
    res = q.execute()
    test_list = []
    if res:
        for hit in res:
            test_list.append(hit)
    return test_list