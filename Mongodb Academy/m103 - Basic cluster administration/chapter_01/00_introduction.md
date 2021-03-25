# Mongod

## Introduction

### What

- The main daemon process to MongoDB.
  - Daemon is a program / process that meant to be run but not interacted with directly.
  - It handles connections, requests and persists data.
  - Manage the database security, distribution and consistence for multiple servers.
  - Interacts only with the database client.

### How to communicate with

- Command line:

  - To connect to mongod log output.

    ```shell
    mongod
    ```

  - To interact with mongod using the database client.

    ```shell
    mongo admin --host 192.168.103.100:27000 -u m103-admin -p m103-pass
    ```

### Default configuration

- port: 27017

  - The port on which mongod will listen for client connections.
  - To set a different port:

    ```shell
    mongod --port <port number>
    ```

- dbpath: /data/db

  - Stores data and journaling information.
  - To set a different dbpath:

    ```shell
    mongod --dbpath <directory path>
    ```

- auth: disable.

  - Enables authentication to control which users can access the database.
  - When auth is specified, all database clients who want to connect to mongod first need to authenticate.
  - To enable the auth option:

    ```shell
    mongod --auth
    ```

  - bind_ip:

    - Allows us to specify which IP addresses mongod should bind to.
    - When mongod binds to an IP address, clients from that address are able to connect to mongod.
    - If using the bind_ip option with external IP addresses, it's recommended to enable auth to ensure that remote clients connecting to mongod have the proper credentials.
    - To bind multiple addresses and/or hosts:

      ```shell
      mongod --bind_ip localhost,123.123.123.123
      ```

### Launching Mongod

- To launch a mongod instance:

  - That run on port `27000`;
  - That data are stored in `/data/db`;
  - That listens `localhost` and `192.168.103.100`;
  - That authentication is enable.

  ```shell
  mongod --port '27000' --dbpath '/data/db' --auth --bind_ip 'localhost','192.168.103.100'
  ```

- To create a new user in database:

  - Role: root on admin database.
  - Username: m103-admin.
  - Password: m103-pass.

  ```shell
  mongo admin --host localhost:27000 --eval '
    db.createUser({
      user: "m103-admin",
      pwd: "m103-pass",
      roles: [
        {role: "root", db: "admin"}
      ]
    })
  '
  ```

  ```YAML
  storage:
    dbPath: "/data/db"

  net:
    port: 27000
    bindIp : "localhost,192.168.103.100"

  security:
    authorization: enabled
  ```