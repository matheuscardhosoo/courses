# Sharding

## Introducion

- A parallel alternative for vertical scaling.
- MongoDB uses horizontal scaling.
- MongoDB distributes data by Sharding methods.

### Sharding in MongoDB

- In order to guarantee high availability for a **Sharded Cluster**, it is necessary to deploy each shard as a replica set.
- This way, MongoDB ensures a level of fault tolerance against each piece of data regardless of which shard actually contains that data.
- MongoDB uses **MongoS** to provide the data of a **Sharded Cluster**.

### MongoS

- A router process that accepts queries from clients and then figures out which shard should receive that query.
- It is used in between a **Sharded Cluster** and its clients.
- Clients connect to Mongos us instead of connecting to each shard individually.
- It is possible to have any number of **MongoSS** processes so we can service many different applications or requests to the same **Sharded Cluster**.
- It uses the metadata about which data is contained on each shard. That metadata is stored on the **Config Servers**.
- In way to guarantee high availability for **Config Servers**, MongoDB replicates these metadata in a **Config Server Replica Set**.

### Concepts

#### Vertical Scaling

- The improvement of individual machines (more RAM, disk space or powerful CPU) to increase its capacity of provide data.
- It could potentially become very expensive.
- Automatically applied by cloud-based providers, but with some limitations.
  - They'll eventually put a limit on the possible hardware configurations, which would effectively limit our storage layer.

#### Horizontal Scaling

- The use of multiple machines with part of dataset, instead of making the individual machines better.

#### Sharding

- Sharding allows the dataset grown without worrying about being able to store it all on one server. Instead, it divides the dataset into pieces and then distribute the pieces across as many shards as we want.
- Multiple shards make up a Sharded Cluster.