# Replication

## Replication Commands

- Some commands to gather information about a replica set.

### `status`

- Used to report on the general health of each node in the set.
- The data it gets from the heartbeat sent in-between nodes in the set.
- Because it relies on heartbeats for this data, it may actually be a few seconds out of date.
- This command gives us the most information for each specific node.
  - `up time`: the number of seconds this note has been running for.
  - `optime`: the last time the node applied an operation from its oplog.
  - `self`: if the command was run from the respective node.

```mongoshell
rs.status()
```

### `isMaster`

- Describes the role of the node where we ran this command from.
- Gives us some information about the replica set itself.
- The output is a lot easier to read than rs.status just because its output is a lot shorter.
- Gives us the name of the primary node in the set regardless of where we ran this command from.
- As a side note, this is the command that the drivers use to discover each node's role in the replica set.

```mongoshell
rs.isMaster()
```

### `serverStatus`

- This command gives us a lot of information about the Mongo D process, but we're just going to look at the section called repl.
- The output from this command is going to be very similar to the output of rs.isMaster.
- Show the `rbid` field, that is not included in rs.isMaster.
  - And all this does is count the number of rollbacks that have occurred on this node.

```mongoshell
db.serverStatus()['repl']
```

### `printReplicationInfo`

- This command only has data about the oplog and specifically only the oplog for the currently connected node.
- It gives the exact time stamps for the first and last events that occurred in the oplog for that node.
- So this is a quick report on the current length of the oplog in time and in megabytes.

```mongoshell
rs.printReplicationInfo()
```