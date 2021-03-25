# Replication

## Reads and Writes on a Replica Set

### Starting env

- Starting replica set nodes, connecting to the primary and Checking replica set topology:

  ```mongoshell
  mongod -f lectures/node1.conf
  mongod -f lectures/node2.conf
  mongod -f lectures/node3.conf
  mongo --host "m103-example/m103:27011" -u "m103-admin" -p "m103-pass" --authenticationDatabase "admin"
  rs.isMaster()
  ```

### Writing in primary node

- Inserting one document into a new collection in prymary node:

  ```mongoshell
  use newDB
  db.new_collection.insert( { "student": "Matt Javaly", "grade": "A+" } )
  ```

### Reading in secondary node

- Connecting to a secondary node:

  ```mongoshell
   mongo --host "m103:27012" -u "m103-admin" -p "m103-pass" --authenticationDatabase "admin"
  ```

- Attempting to execute a read command on a secondary node (this should fail):

  ```mongoshell
  show dbs
  ```

- Enabling read commands on a secondary node:

  ```mongoshell
  rs.slaveOk()
  ```

- Reading from a secondary node:

  ```mongoshell
  use newDB
  db.new_collection.find()
  ```

- Attempting to write data directly to a secondary node (this should fail, because we cannot write data directly to a secondary):
  - The purpose of this is to enforce strong consistency on our cluster.

  ```mongoshell
  db.new_collection.insert( { "student": "Norberto Leite", "grade": "B+" } )
  ```

- Shutting down the server (on both secondary nodes):

  ```mongoshell
  use admin
  db.shutdownServer()
  ```

- It's not possible operate the replica set if only the minority of nodes (<2) is online.