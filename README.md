# collection_data


This repository contains an script that listens to data we are receiving in our platform.

## Prerequisites

- Docker installed
- Docker Compose installed
- Access to a running Kafka cluster
- A`config.json` file with your Kafka connection details


## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:rat-eos-pc-ua/collection_data.git
cd collection_data
```

### 2. Install Docker and Docker-Compose
Please check the following link: [https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu) 

### Step 2:  Build and Run the Docker Container
#### For Linux:

```bash
docker-compose up --build
```

### Step 3:  Data model
The following link [https://atnog-iot4fire.av.it.pt/swagger-ui/](https://atnog-iot4fire.av.it.pt/swagger-ui/) provides a comprehensive guide to the data fields available in the platform. These data fields define how data is stored in the platform database. Understanding these fields is crucial for effectively querying and analysing the data collected from several environmental sensors and sources.
The data model will be updated periodically as new data fields are added to the platform.

### Step 4:  Adjust the script as needed
This script allows to listen and shows all data we are receiving in our platform. If needed, it can be expanded with additional development like, for example, implementing database storage capabilities. Therefore, it allows to not only fetch and display data but also store it efficiently for long-term analysis and reporting.

