# Mongod

## Logging Basics

- [Logging & Diagnostics](https://docs.mongodb.com/manual/release-notes/4.2/#logging-and-diagnostics).
- The process log collects activity info from MongoDB components.
- Each component has an associated verbosity level.
- Bellow the MongoDB log components:

  | Components               | Description                                  |
  | :----------------------- | :------------------------------------------- |
  | `accessControl`          | access control messages (authentication)     |
  | `command`                | database commands messages                   |
  | `control`                | control activities messages (initialization) |
  | `executor`               |                                              |
  | `ftdc`                   | diagnostic data collection messages          |
  | `geo`                    | geospatial parsing messages                  |
  | `index`                  | indexing operations messages                 |
  | `network`                | network activities messages                  |
  | `query`                  | queries and query planner messages           |
  | `replication`            | replica sets messages messages               |
  | `replication.heartbeats` | replica set heartbeats messages              |
  | `replication.rollback`   | rollback operations messages                 |
  | `sharding`               | sharding operations messages                 |
  | `storage`                | storage activities messages                  |
  | `storage.journal`        | journaling activities messages               |
  | `write`                  | write operations messages                    |

- Running the `db.getLogComponents()` to get all database components:

  ```json
  {
    "verbosity": 0,
    "accessControl": {
      "verbosity": -1
    },
    "command": {
      "verbosity": -1
    },
    "control": {
      "verbosity": -1
    },
    "executor": {
      "verbosity": -1
    },
    "geo": {
      "verbosity": -1
    },
    "index": {
      "verbosity": -1
    },
    "network": {
      "verbosity": -1,
      "asio": {
        "verbosity": -1
      },
      "bridge": {
        "verbosity": -1
      }
    },
    "query": {
      "verbosity": -1
    },
    "replication": {
      "verbosity": -1,
      "heartbeats": {
        "verbosity": -1
      },
      "rollback": {
        "verbosity": -1
      }
    },
    "sharding": {
      "verbosity": -1,
      "shardingCatalogRefresh": {
        "verbosity": -1
      }
    },
    "storage": {
      "verbosity": -1,
      "journal": {
        "verbosity": -1
      }
    },
    "write": {
      "verbosity": -1
    },
    "ftdc": {
      "verbosity": -1
    },
    "tracking": {
      "verbosity": -1
    }
  }
  ```

- To get the logs:

  - Using the `getLog` command to get admin database logs:

    ```json
    db.adminCommand({
      "getLog": "global"
    })
    ```

  - Using the `tail -f` command in log file (specifying its location):

    ```shell
    tail -f /var/log/mongodb/mongod.log
    ```

- To set the log level:

  ```json
  db.setLogLevel(0, "index")
  ```

### Log analysis

- Timestamp.
- Severity Level.
- Log component.
- Assiciated connection.
- Specific event information.
- appName: The application that executed the command.
- command> the command itself and its parameters.
- metadata: execution time, ...

### Log verbosity levels

| Level | Description                                                |
| :---- | :--------------------------------------------------------- |
| -1    | Inherit level from parent.                                 |
| 0     | Default verbosity, to include informational messages.      |
| 1 ~ 5 | Debug level. A higher number increase the debug verbosity. |

### Log severity levels

| Level |  Description  | Verbosity Level |
| :---- | :-----------: | :-------------: |
| F     |     Fatal     |        -        |
| E     |     Error     |        -        |
| W     |    Warning    |        -        |
| I     | Informational |        0        |
| D     |     Debug     |       1~5       |