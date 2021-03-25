# Sharding

## When to Shard

- It is necessary to consider some indicators before apply a Sharding Cluster.

### Sharding Indicators

- Check out if it is still economically viable to vertical scale.
- Another aspect to consider is the impact on your operational tasks.
- Finally, geodistributed data is significantly simple to manage using zone sharding.

#### Economical Indicator

- When we need to address a throughput performance or volume bottleneck, which are generally the technical drivers for adding more resources to your system, the first step would be to check if we can still add more resources and scale up.
- We need to validate that adding more of those vertical resources, such as adding more CPU, network, memory, or disk to your existing servers, is economically viable and possible.
- In beginning stages (small set of servers with low/average performance), where servers can easily improve, vertical scaling probably would be the option.
- You are still able to do so in economical viable manner, but you will eventually reach a point where vertical scaling is no longer economically viable or it's very difficult to say impossible to accomplish.
- At this point, it is probably easier to create new instances (horizontal scaling) than to improve current ones. In addition, new instances increase performance linearly, while vertical scaling shows signs of saturation.

#### Operational Indicator

- Vertical scaling is not always easy to apply considering that all server components are directly or indirectly connected. One improvement done probably would request some others in different scales and sectors.
- Horizontal scaling balanceate service load between multiple machines, providing a linear performance improvement with safe support for action (one time the same schema already has been used).
  - It simplifies the scaling process and avoid unexpected load issues.
- In such a scenario, having horizontal scale and distributing that amount of data across different shards, will allow getting horizontal performance gains like parallelization of the backup, restore, and initial sync processes.
  - This same scenario will also impact positively your operational workload.
  - There are workloads that intrinsically play nicer in distributed deployments that sharing offers, like single threaded operations that can be parallelized and geographically distributed data.
- Data that needs to be stored in specific regional locations or will benefit from being co-located with the clients that consume such data.

#### Geographic Indicator

- Zone sharding allows us to easily distribute data that needs to be co-located.