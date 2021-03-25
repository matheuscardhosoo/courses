# Mongod

## Configuration File

- A YAML file containing the configuration options needed to run MongoD or MongoS.
- An alternative for command line single approach.
- Improve the readability.
- Main options:
  - [Command line options](https://docs.mongodb.com/manual/reference/program/mongod/#options).
  - [Configuration file options](https://docs.mongodb.com/manual/reference/configuration-options).

| Command Line  | Config File                               | Mean                                                                                                        |
| :------------ | :---------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `--dbpath`    | `storage.db`                              | Database main path.                                                                                         |
| `--logpath`   | `systemLog.path`, `systemLog.destination` | Database log path.                                                                                          |
| `--bind_ip`   | `net.bind_ip`                             | Need to be set to provide network access, otherwise the MongoD accepts only connections from the same host. |
| `--replSet`   | `replication.replSetName`                 | Starts the MongoD in replication mode.                                                                      |
| `--keyFile`   | `security.keyFile`                        | Sets intercluster auth security and user authentication enable.                                             |
| `--tlsPEMKey` | `net.tls.tlsPEMKey`                       | SSL encryption option.                                                                                      |
| `--tlsCAKey`  | `net.tls.tlsCAKey`                        | SSL encryption option.                                                                                      |
| `--tlsMode`   | `net.tlsMode`                             | SSL encryption option.                                                                                      |
| `--fork`      | `processManagement.fork`                  | Runs MongoD as a daemon instead of being tied toa a terminal session.                                       |

- YAML: "YAML Ain't Markup Language".

  - Example:

    ```YAML
    storage:
      dbPath: "/data/db"

    systemLog:
      path: "/data/log/mongod.log"
      destination: "file"

    replication:
      replSetName: M103

    net:
      bindIp : "127.0.0.1,192.168.103.100"

    tls:
      mode: "requireTLS"
      certificateKeyFile: "/etc/tls/tls.pem"
      CAFile: "/etc/tls/TLSCA.pem"

    security:
      keyFile: "/data/keyfile"

    processManagement:
      fork: true
    ```

    ```YAML
    storage:
      dbPath: "/var/mongodb/db"

    systemLog:
      path: "/var/mongodb/db/mongod.log"
      destination: "file"
      logAppend: true

    operationProfiling:
      mode: "slowOp"
      slowOpThresholdMs: 50

    net:
      port: 27000
      bindIp: "localhost,192.168.103.100"

    security:
      authorization: enabled

    processManagement:
      fork: true
    ```

- Invoking MongoD using configuration file:

  ```shell
  mongod --config "/etc/mongod.conf"
  ```