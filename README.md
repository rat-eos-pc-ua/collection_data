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
Please check the following link: [https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu) or 
[https://medium.com/@tomer.klein/step-by-step-tutorial-installing-docker-and-docker-compose-on-ubuntu-a98a1b7aaed0](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-install-Docker-and-docker-compose-on-Ubuntu](https://medium.com/@tomer.klein/step-by-step-tutorial-installing-docker-and-docker-compose-on-ubuntu-a98a1b7aaed0)
### Step 2:  Build and Run the Docker Container

#### For Linux:

```bash
docker-compose up --build
```


