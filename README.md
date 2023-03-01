# Fetch Rewards Data Engineering Take Home: ETL off a SQS Queue

## Overview

### 1. Project Setup and Execution

i. Download/clone the repository via Github or using the following command:

```
git clone https://github.com/manishwvn/Fetch_Rewards_DE.git
```

ii. Move into the directory Fetch_Rewards_DE using the following command:

```
cd Fetch_Rewards_DE
```

iii. Install python3 and pip3 if not already installed on your system.
This can be done by downloading the latest version of python3 from the following link: https://www.python.org/downloads/ or via Homebrew installation on Mac OS using the command

    brew install python3

iv. Install the required python packages using the following command:

```
pip3 install -r libraries.txt
```

v. Docker installation:
This can be done by downloading the latest version of Docker from the following link: https://www.docker.com/products/docker-desktop

vi. Download the required docker images for SQS Server and Postgres Database using the following commands:

```
docker pull fetchdocker/data-takehome-postgres

docker pull fetchdocker/data-takehome-localstack
```

vii. Additional installations:

- Postgres Installation: This can be installed using the following command:

  ```
  brew install postgresql
  ```

- AWS CLI Installation for python3: This can be installed using the following command:

  ```
  pip3 install awscli-local
  ```

viii. Run the following command to start the SQS Server and Postgres Database:

```
docker-compose up
```

ix. Execute the project using the following command:

```
python3 sqs_to_ps.py
```

### 2. Answering the Questions

- Q1. How would you deploy this application in production?

  Ans. Production deployment would depend on the amount of data generated.
  If the data is not too large, then the application can be deployed on a single machine and scheduled to run at regular intervals.

  If the data is large, then the application can be deployed on a cluster of machines and scheduled to run at regular intervals using a scheduler like AWS Lambda.

- Q2. What other components would you want to add to make this production ready?

  Ans. The following components can be added to make the application production ready:

  - Logging: Logging can be added to the application to keep track of the data being processed and the errors encountered during the process.
  - Monitoring: Monitoring can be added to the application to keep track of the data being processed and the errors encountered during the process.
  - Alerting: Alerting can be added to the application to notify the user in case of any errors encountered during the process.
  - Testing: Testing can be added to the application to ensure that the application is working as expected.
  - Error Handling: Error handling can be added to the application to handle any errors encountered during the process.
  - In addition to this, suitable measures to unmask the data for internal users such as Data Analysts and Data Scientists can be added to the application.

- Q3. How can this application scale with a growing dataset.

  Ans. The application can be scaled with a growing dataset by adding more machines to the cluster. This can be done by adding more machines to the cluster and scheduling the application to run at regular intervals on the cluster.

- Q4 How can PII be recovered later on?

  Ans. There is no direct way to recover the PII as the data is hashed and hence highly secure.

  One way to unmask the data, we can match masked data with the original data and store the hashed values to compare them with input data. If the hashed values match, then we can unmask the data.

  Another way is to use a two-way encryption algorithm to encrypt the data and store the encrypted data. This can be decrypted later on to unmask the data.
  Important thing to note is the security will depend on the strength of the encryption algorithm used.

- Q5 What are the assumptions you made?

  Ans. The following assumptions were made:

  - The take-home assignment is essentially an ETL process where data is extracted from a SQS queue, transformed and loaded into a Postgres database.
    This can be done using various languages based on the requirement of the user. For this assignment, I have used Python3 as the language of choice owing to ease of development and availability of libraries.

  - The intuition behind most of the implementation is on sole understanding of the problem statement and the data provided.
