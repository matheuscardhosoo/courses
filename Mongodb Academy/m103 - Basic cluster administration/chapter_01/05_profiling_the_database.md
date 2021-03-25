# Mongod

## Profiling the Database

- Used in conjunction with database logs.
- Used for debug slow operations.
- Enabled in database level.
  - Each database has its own profile configurations.
- Restores the data for all operations on a given database.
  - CRUD operations.
  - Administrative operations.
  - Configuration operations.
- Store collected data in a new collection called `system.profile`.

### Settings:

| Level | Description                                                                         |
| :---- | :---------------------------------------------------------------------------------- |
| 0     | Profiler off. It does not collect any data. This is the default value.              |
| 1     | The Profiles collects data only for slow operations (> slowms - 100 ms in default). |
| 2     | The Profiler collects data for all operations.                                      |

- Obs.: Level 2 can generates too much output information, what increase the chance of overheat the server.

### Commands

- To get the profiler level:

  ```json
  db.getProfilingLevel()
  ```

- To set the profiler level:

  ```json
  db.setProfilingLevel(1, { "slowms": 200 })
  ```