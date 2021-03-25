# Replication

## Read Concerns

- Read concern is a companion to write concern.
- An acknowledgment mechanism for read operations where developers can direct their application to perform read operations where the returned documents meet the requested durability guarantee.
- Read concern provides a way of dealing with the issue of data durability during a failover event.
- The read operation only returns data acknowledged as having been written to a number of replica set members specified in the read concern.
- A document that does not meet the specified read concern is not a document that is guaranteed to be lost.
  - It just means that at the time of the read, the data had not propagated to enough nodes to meet the requested durability guarantee.
- Read concern doesn't prevent deleting data using a CRUD operation, such as delete.

### Read Concern Levels

- **Local**:
  - Returns the most recent data in the cluster.
  - Any data freshly written to the primary qualifies for local read concern.
  - There are no guarantees that the data will be safe during a failover event.
  - The default for read operations against the primary.
- **Available**:
  - The same as local read concern for replica set deployments.
  - The default for read operations against secondary members.
  - The main difference between local and available read concern is in the context of sharded clusters.
- **Majority**:
  - Only returns data that has been acknowledged as written to a majority of replica set members.
  - The only way that documents returned by a read concern majority read operation could be lost is if a majority of replica set members went down and the documents were not replicated to the remaining replica set members, which is a very unlikely situation, depending on your deployment architecture.
  - Provides the stronger guarantee compared to local or available writes.
  - The trade-off is that you may not get the freshest or latest data in your cluster.
  - The MMAPv1 storage engine does not support read concern of majority.
- **Linearizeable**:
  - Added in MongoDB 3.4.
  - Like read concern majority, it also only returns data that has been majority committed.
  - Provides read your own write functionality.

### Whent use Read Concerns?

- Depends on the application requirements.
- **Fast**, **safe**, or the **latest data in your cluster**.
- If you want **fast** reads of **the latest data**, **local** or **available** read concern should suit you just fine.
  - But you are going to lose your durability guarantee.
- If you want **fast** reads of **the safest data**, then **majority** read concern is a good middle ground.
  - But again, you may not be getting the latest written data to your cluster.
- If you want **safe reads** of **the latest data** at the time of the read operation, then **linearizeable** is a good choice.
  - But it's more likely to be slower.
  - And it's single document reads only.