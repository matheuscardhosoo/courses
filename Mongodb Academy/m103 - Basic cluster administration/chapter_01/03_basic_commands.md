# Mongod

## Basic Commands

- [optimizedPipeline docs](https://docs.mongodb.com/manual/reference/explain-results/#explain.queryPlanner.optimizedPipeline).

### Shell wrappers

- `db.<method>()`
  - It wrappers the commands that acts in the db instance.
  - `db.<collection>.<method>()`
    - It wrappers the commands that acts in the conllection.
- `rs.<method>()`
  - It wrappers the commands that control the replica set deployment and management.
- `sh.<method>()`
  - It wrappers the commands that control the sharded cluster deployment and management.

### User management commands

- To create an user:

  ```json
  db.createUser(
    {
      "user": "user-name",
      "pwd": "user-passord",
      "roles": [
        {
          "role": "role-name",
          "db": "db-name"
        }
      ]
    }
  );
  ```

- To drop an user:

  ```json
  db.dropUser(
    {
      "user": "user-name"
    }
  );
  ```

### Collection management commands

- To rename a collections:

  ```json
  db.<collection>.renameCollection()
  ```

- To create an index:

  ```json
  db.<collection>.createIndex(
    {
      "product": 1
    },
    {
      "name": "name_index"
    }
  )
  ```

- To drop a collection:

  ```json
  db.<collection>.drop()
  ```

### Database management commands

- To drop a database:

  ```json
  db.dropDatabase()
  ```

- To create a collection:

  ```json
  db.createCollection()
  ```

### Database status commands

- To show the server status:

  ```json
  db.serverStatus()
  ```

### Generic commands

- To run an generic command:

  ```json
  db.runCommand(
    {
      "createIndexes": <collection>
    },
    {
      "indexes": [
        {
          "key": {
            "product": 1
          }
        },
        {
          "name": "name_index"
        }
      ]
    }
  );
  ```