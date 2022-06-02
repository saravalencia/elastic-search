# Elasticsearch
Elasticsearch, Fastapi, React full stack application
## Requirements: 
 - Docker, and a docker-compose.yml with the image of Elasticsearch and Kibana. (Don't forget to run docker as administrator if you are using windows).
 - Json formatted files to index the data you want to search through.

## 1. Run Docker with Elasticsearch component :
Use the command "docker-compose up -d" inside the folder containing your docker-compose.yml file with the Elasticsearch and kibana containers.
You can find an example of docker-compose.yml with Elasticsearch and Kibana in this repository.

If you are a Windows user : Once your docker containers are running, stop them and allocate space for your elasticsearch with the following commands on your terminal:
- wsl -d docker-desktop 
then:
- sysctl -w vm.max_map_count=262144
This step is important if you want to make the containers on docker work correctly, you will may have to repeat this step if you restart docker. 
You can now go to localhost:9200 to see your Json object of Elasticsearch and localhost:5601 to see Kibana and all the functionalities you can play with. 

## 2. Clone this repo 
This repository contains the indexing script for your data, and a fastApi application to connect to your Search-Bar. 
-First index your data running the indexing.py file. Keep in mind that you have to rename the path of your Json files that you want to index. 
In the line 10 of indexing.py, there is a line containing:  directory = "data/exemple" you just have to modify to the correct path of your choice. 
When you index your Json data, you can verify that your data was indexed correctly by going to Kibana: "localhost:5601" then go to the left menu to the section
"Managment" and to the sub-section "Dev Tools", once here just send a request to the default query already present by pressing the play button in front of it. 
Here you should see a response of your query with a big Json component with information about the data you just indexed, if the section "took" : 0 This means
that the indexation was not successful. 

## 3. Run the app
-Run the command "uvicorn main:app" inside the folder where main.py is located, which will run a server API connected to Elastic.
Then go to the frontend folder and run the command "npm start" to start your frontend server.
Here you can search by words in all your Json files.
