# Replication

## Introduction

- MongoDB uses asynchronous, statement-based replication because it's platform independent adn allows more flexibility within replica set.
- Replication is the concept of maintaining multiple copies of your data.
  - Improve availability using redundancy.
  - It's necessary because MongoDB does not grants that all its servers will always be available.
  - BASE principle:
    - Basic Availability.
    - Soft-state.
    - Eventual consistency
- In MongoDB, a group of nodes that each have copies of the same data is called a replica set.
  - By default, all data is handled in one of the nodes (**primary node**).
  - The remaining (**secondary nodes**) nodes asynchronously sync the data (part or total) from/to primary node. 
  - **Secondary nodes** can become a **primary node** if this gone down.
    - **Secondary nodes** vote in each other (election) to define which will become the **primary node** (**failover**).
    - Once the node comes back up, it simply sync the last copy of the data and rejoin the replica set.

### Types

|                                     | Binary replication | Statement-based replication |
| ----------------------------------- | ------------------ | --------------------------- |
| Log type                            | Binary log         | Oplog (OPeration log)       |
| Replicated unit                     | Bytes              | Operations                  |
| Performance                         | High               | Medium                      |
| Memory usage                        | Low                | Medium                      |
| System dependency                   | Yes                | No                          |
| Architecture dependency             | Yes                | No                          |
| Database service version dependency | Yes                | No                          |

### Idempotency

- MOngoDB uses Statement-based replication.
- Database operation reduce.
- Every command is transformed before to be saved in oplog.
- Only single and simple operations area seved and used in replica process.
