# Real-Time Data Capture Simulation with Debezium, Kafka, and PostgreSQL

## Summary

This project provides a quick way to set up and experiment with Data Change Capture (DCC) using Debezium, Kafka, and PostgreSQL. It includes a Python script that generates realistic simulated financial transaction data and inserts it into a PostgreSQL database. This data is then ready to be used for exploring Debezium's ability to capture changes in the database in real-time.

## System Overview

The project simulates a data pipeline where transaction data is generated and stored in a Postgres database. A system architecture image shows how these components are interconnected:
![system architecture.png](system%20architecture.png)

## Requirements

Before you begin, make sure you have:
- Python 3.9 or later installed.
- The `psycopg2` and `faker` Python libraries.
- PostgreSQL database available either on your local machine or accessible remotely.
- Docker and Docker Compose installed on your machine.
- A basic understanding of how Docker, Kafka, and Postgres work.

## Setup

1. **Install Python Dependencies:**

   Use pip to install the required libraries:

   ```bash
   pip install psycopg2-binary faker
   ```

## Docker Services Overview:

- **Zookeeper:** Manages the configuration for the Kafka cluster.
- **Kafka Broker:** The core streaming platform for real-time data.
- **Confluent Control Center:** A web-based interface for Kafka monitoring.
- **Debezium:** The DCC platform, captures database changes.
- **Debezium UI:** A web user interface for managing and viewing Debezium.
- **Postgres:** The open-source relational database used to hold transaction data.

## How to Use the Project

1. **Get the Project:**
   If this is part of a repo, clone the repository onto your computer.

2. **Open a Terminal:**
   Navigate to the folder containing the `docker-compose.yml` file.

3. **Start the Services:**
   Run the following command to build and start all of the required services:

   ```bash
   docker-compose up -d
   ```

   This will download necessary docker images and launch the services in the background.
   
5. **Verify Services are Running:**
   You can confirm that all of the services started successfully with this command:

   ```bash
   docker-compose ps
   ```

   All services listed should have a status of "running".

6. **Access the UIs:**
   - Kafka Control Center: `http://localhost:9021`.
   - Debezium UI: `http://localhost:8080`.
   - Postgres: Connect to port `5432`.

7. **Stop and Clean Up:**
   Use this command to stop all of the containers, delete the networks and volumes:
   
   ```bash
   docker-compose down
   ```

## Customization
Feel free to adjust the `docker-compose.yml` file. For instance, you can enable persistent data for the Postgres database by adding a volume configuration.

## Important Notes
This setup is primarily for development and testing. If you plan on deploying this into a production environment, be sure to consider other aspects like security and scalability.
