# Sharding

## Config DB

- First thing you need to know about the config DB is that you should generally never write any data to it. It's maintained internally by MongoDB, and it's used internally.
- All `sh.status()` informations are actually stored in the config DB.

- Connecting to MongoS:

  ```shell
  mongo --port 26000 --username m103-admin --password m103-pass --authenticationDatabase admin
  ```

- Switch to config DB:

  ```mongoshell
  use config
  ```

### Databases Collection

- Query config.databases:

  ```mongoshell
  db.databases.find().pretty()
  ```

- So this is going to return each database in our cluster as one document.
- It's going to give us the primary shard for each database, and the partition here is just telling us whether or not sharding has been enabled on this database.

### Collections Collection

- Query config.collections:

  ```mongoshell
  db.collections.find().pretty()
  ```

- So this is only going to give us information on collections that have been sharded.
- But for those collections, it will tell us the shard key that we used.

### Shards Collection

- Query config.shards:

  ```mongoshell
  db.shards.find().pretty()
  ```

- This one's going to tell us about the shards in our cluster.
- And here, you can see the hostname contains the replica set name because these shards are deployed as replica sets.

### Chunks Collection

- Query config.chunks:

  ```mongoshell
  db.chunks.find().pretty()
  ```

- The chunks collection is possibly the most interesting collection in this whole database.
- So each chunk for every collection in this database is returned to us as one document.
- The inclusive minimum and the exclusive maximum define the chunk range of the shard key values. That means that any document in the associated collection who's shard key value falls into this chunks range will end up in this chunk, and this chunk only.
  - MinKey, here, means the lowest possible value of sale price or negative infinity, if you want to think about it that way.

### Config Collection

- Query config.mongos:

  ```mongoshell
  db.mongos.find().pretty()
  ```

- The config database also some information on the mongos process currently connected to this cluster, because we can have any number of them.
- It gives us a lot of information on it, including the mongos version that's running on the mongos.