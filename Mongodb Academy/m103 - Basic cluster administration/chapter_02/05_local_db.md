# Replication

## Local DB

- Configuration database parallel to **admin**.
  - **admin** comprises all the Administration Data and is the place where most of the administration commands are.
- **Does not change anything in local database.**
- Any data written to local database that is not written to oplog.rs or changing any of the system configuration collections will stay there and will not be replicated.

### Standalone mode

- **local** has only one collection: **startup_log**.
  - **startup_log** holds the start up log of this particular node.

### Replica Set

- **local** has the following collections:
  - **oplog.rs**:
    - The central point of our replication mechanism.
    - Is created after initiating a node and adding it to a replica set.
  - **replset.election**:
    - Collection maintained internally by the server.
    - Configuration data.
  - **replset.minvalid**:
    - Collection maintained internally by the server.
    - Configuration data.
  - **statup_log**:
    - Collection maintained internally by the server.
    - Configuration data.
  - **system.replset**:
    - Collection maintained internally by the server.
    - Configuration data.
  - **system.rollback.id**:
    - Collection maintained internally by the server.
    - Configuration data.

#### oplog

- oplog collection that will keep track of all statements being replicated in our replica set. Every single piece of information and operations that need to be replicated will be logged in this collection.
- Every node in replica set has its own oplog with different oplog sizes.
- oplog is idempotence: it stores operation as simple as possible, transforming complexes operations in multiple simple operations.
- It's a capped collection.
  - Capped collection means that the size of this collection is limited to a specific size.
- By default, the oplog.rs collection will take 5% of your free disk, but this value can also be set by configuring it through the oplogSize in megabytes under the replication section of our configuration file.

  ```YAML
  replication:
    oplogSize: 15
  ```

- It accumulates the operations and statements until it reaches the oplog size limit. Once that happens, the first operations in our oplog start to be overwritten with newer operations.
- **Replication Window**: The time node takes to fill in fully its oplog and start rewriting the early statements.
  - The oplog size will determine the replication window.
  - Is a important aspect to monitor because it impacts how much time the replica set can afford a node to be down without requiring any human intervention to auto recover.
  - Once a node go down and return after some time, it can replicate other nodes oplog to apply lost operations.
    - If delayed node does not find its state inside of other oplogs, it enters in recovery mode and wait for a user intervention.
  - To sum up, the replication window measured in hours will be proportional to the load of your system.
- However, if our oplog size is larger and able to accommodate more changes in the system, we can afford our nodes to be down for longer and still be able to reconnect once they're being brought back up again.

##### Status: oplog.rs

- In mongoshell:
  - Querying the oplog after connected to a replica set:

    ```mongoshell
    use local
    db.oplog.rs.find()
    ```
  - Storing oplog stats as a variable called stats:

    ```mongoshell
    var stats = db.oplog.rs.stats()
    ```

  - Verifying that this collection is capped (it will grow to a pre-configured size before it starts to overwrite the oldest entries with newer ones):

    ```mongoshell
    stats.capped
    ```

  - Getting current size of the oplog:

    ```mongoshell
    stats.size
    ```

  - Getting size limit of the oplog:

    ```mongoshell
    stats.maxSize
    ```

  - Getting current oplog data (including first and last event times, and configured oplog size):

    ```mongoshell
    rs.printReplicationInfo()
    ```