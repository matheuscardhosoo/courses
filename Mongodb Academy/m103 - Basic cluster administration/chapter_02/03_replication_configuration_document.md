# Replication

## Replication Configuration Document

- Simple BSON document that we manage using a JSON representation where the configuration or replica sets is defined and is shared across all the nodes that are configured in the sets.
- Can be manually set or by the mongodb shell commands.

  ```shell
  rs.add
  rs.initiate
  rs.remove
  rs.reconfig
  rs.config
  ```

- Configuration structure:

  ```json
  {
    _id: <string>,
    version: <int>,
    members: [
      {
        _id: <int>,
        host: <string>,
        arbiterOnly: <boolean>,
        hidden: <boolean>,
        priority: <int>,
        slaveDelay: <int>
      },
      ...
    ],
    settings: {
      ...
    }
  }
  ```

  - `_id`
    - The name of the replica set.
    - It should match with the server defined replica set name. In case of different values from the configuration _id and the defined replica set name, the server end up with an error message.
  - `version`
    - Integer that gets incremented every time the current configuration of replica set changes.
    - Every time we changed a topology, changed a replica set configuration at all or do something like changing the number of votes of a given host, that will automatically increment the version number.
  - `members`
    - Where the topology of our replica set is defined.
    - Each element of the members array is a sub-document that contains the replica set node members.
      - `_id`: member id.
      - `host`: comprised of the host name and port.
      - `arbiterOnly`: this means that the node will not be holding any data, and its contribution to the set is to ensure quorum in elections.
        - false by default.
      - `hidden`: sets the node in hidden role. An hidden node is not visible to the application, which means that every time we emit something like an RS is master command, this node will not be listed.
        - false by default.
      - `priority`: integer value that allows us to set a hierarchy within the replica set.
        - Between 0 and 1,000.
        - Members with higher `priority` tend to be elected in primaries more often.
        - A change in the `priority` of a node will trigger an election because it will be perceived as a topology change.
        - Setting `priority` to 0 effectively excludes that member from ever becoming a primary.
        - In case, we are setting a member to be `arbiterOnly` or `hidden`, that implies that the `priority` needs to be set to 0.
      - `slaveDelay`: determines a replication delay interval in seconds.
        - 0 by default.
        - These delayed members maintain a copy of data reflecting a state in some point in the past, applying that delay in seconds.
        - By setting this slave the option, it also implies that your node will be hidden, and the priority will be set to 0.
  - `settings`: other configurations.