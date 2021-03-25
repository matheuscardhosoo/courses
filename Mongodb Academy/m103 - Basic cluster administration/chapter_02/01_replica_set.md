# Replication

## Replica Set

- Replica sets or groups of mongods that share copies of the same information between them.
- Replica set members can have one of two different roles.
- Failure resilient.
- Should always have at least an odd number of nodes. In case of even number, it is necessary to make sure that the majority is consistently available.
  - It needs to have at least three nodes to be available.
- The list the replica set members in their configuration options defines the replica set topology.
- Any topology change will trigger an election.
  - Adding, failing or changing members or replica set configuration aspects will be perceived as it's topology change.
- The replica set configuration is defined in one of the nodes and then shared between all members through the replication mechanism.
- Now, replica sets can go up to 50 members.
  - This might be useful, especially for geographical distribution of our data where we want copies of our data closer to our users and applications, or just multiple locations for redundancy.
  - But only a maximum of seven of those members can be voting members.
- Supports hidden and delayed nodes.

### Primary node

- Where all reads and all writes are served by this node.
- Every time an application writes some data to the replica set, that right is handled by the primary node and then data gets replicated to the secondary nodes.

### Secondary node

- The responsibility of this node is to replicate all of the information, and then serve as a high availability to node in case of failure of the primary.
- It gets the data from the primary through an asynchronous replication mechanism.

### Asynchronous replication

- Versions:
  - PV1 (default, current).
  - PV0.
- The different versions of the replication protocol will vary slightly on the way durability and availability will be forced throughout the set.

#### Oplog

- The oplog is a segment based lock that keeps track of all write operations acknowledged by the replica sets.
- Every time a write is successfully applied to the primary node, it will get recorded in the oplog in its idempotent form.

#### PV1

- This protocol is based out of the RAFT protocol.
  - Entities: **followers** (Secondary node), **candidates** and **leader** (Primary node).
  - Leader Election.
    - Only one leader can be elected per term.
    - Election timeout: The election timeout is the amount of time a follower waits until becoming a candidate.
      - Randomized to be between 150ms and 300ms.
    - Request Vote: message sent by **candidate** to others **followers** requesting votes.
    - Heartbeat messages:  Append Entries messages sent by **leader** to its **followers**, wich respond each one.
    - Heartbeat Timeout: interval between Heartbeat messages.
    - Algorithm:

      1. The election timeout starts and **followers** decide to become **candidates**.
      2. After the election timeout the follower becomes a **candidate** and starts a new election term.
      3. The **candidates** send out Requests Vote messages to other nodes.
      4. Once a **follower** has not voted yet, it returns the request and restart the election timeout.
      5. The **leader** sends its Heartbeat messages.
      6. This election term will continue until a follower stops receiving heartbeats and becomes a candidate.

  - Log Replication.
    - Uses oplogs to transmit the operations.
    - Once we have a leader elected we need to replicate all changes to our system to all nodes.
    - This is done by using the same Append Entries message that was used for heartbeats.
    - An entry is committed once a majority of followers acknowledge it and a response is sent to the client.
      - It stays uncommitted if not reach the majority of nodes.
      - Uncommitted operations are rolled back if it does not match the leader's log.

  - Algorithm:

    1. All nodes begin as **followers**.
    2. (Leader Election) If no **leader** exists, **followers** can become **candidates** requesting votes from other nodes. The node with the majority of votes became the **leader**.
    3. (Log Replication) All input operations are sent to **leader** by oplog and replicated to **followers**.

  - [**Simple Raft Protocol**](http://thesecretlivesofdata.com/raft/).
  - [**Consensus Algorithm**](https://raft.github.io/)
  - [**The Raft Paper**](https://raft.github.io/raft.pdf)

#### Arbiter node

- Apart from a primary or secondary role, a replica set member can also be configured as an arbiter.
- An arbiter is a member that holds no data.
- Serves as a tiebreaker between secondaries in an election.
- If it has no data, it can never become primary.
- **It causes significant consistency issues in distributed data systems**.
- **The usage of arbiters is a very sensitive and potentially harmful option in many deployments**.

#### Hidden nodes

- Nodes set to not appear in common replication process.
- The purpose of a hidden node is to provide specific read-only workloads, or have copies over your data which are hidden from the application.

#### Delayed nodes

- Nodes set with a delay in their replication process.
- The purpose of having delayed nodes is to allow resilience to application level corruption, without relying on cold backup files to recover from such an event.
- Hot backups (easy and fast recover option).