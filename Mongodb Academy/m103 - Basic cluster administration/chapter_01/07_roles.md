# Mongod

## Roles

### Built-In Roles

- Pre-packaged MongoDB roles.
- Built-in Roles for database level:
  - Database User (application users).
    - `read`.
    - `readWrite`.
  - Database Administrator.
    - `dbAdmin`.
    - `userAdmin`.
    - `dbOwner`.
  - Cluster Administrator.
    - `clusterAdmin`.
    - `clusterManager`.
    - `clusterMonitor`.
    - `hostManager`.
  - Backup/Restore.
    - `backup`.
    - `restore`.
  - Super User.
    - `root`.
- Built-in roles for all database level.
  - Database User (application users).
    - `readAnyDatabase`.
    - `readWriteAnyDatabase`.
  - Database Administrator.
    - `dbAdminAnyDatabase`.
    - `userAdminAnyDatabase`.
  - Super User.
    - `root`.

### Custom Roles

- Tailored roles to attend specific needs of sets of users.

### Roles patterns

- After create the root user, the first thing we should do is create a `security_officer` user in `admin` database with `userAdmin` role for the `admin` database.

  - It will do the all users complete management.
  - It cannot administrate data.

  ```json
  db.createUser(
    {
      "user": "security_officer",
      "pwd": "h3ll0th3r3",
      "roles": [
        {
          "db": "admin",
          "role": "userAdmin"
        }
      ]
    }
  );
  ```

- After create the `security_officer` user, we should create a `dba` user in `admin` database with `dbAdmin` role for the `any` database.

  - It will do the complete DDA (Data Definition Language) management for specified databases.
  - It cannot administrate users.
  - It cannot do DML (Data Modification Language) processes.
    - It cant modify|create/remove specific data.

  ```json
  db.createUser(
    {
      "user": "dba",
      "pwd": "c1lynd3rs",
      "roles": [
        {
          "db": "any",
          "role": "dbAdmin"
        }
      ]
    }
  );
  ```

- After create the `dba` user, we can create users with roles restrict to specific databases.

  - The example creates a user to complete manage data and users for the specified database.

  ```json
  db.createUser(
    {
      "user": "m103_dba",
      "pwd": "c1lynd3rs",
      "roles": [
        {
          "db": "m103",
          "role": "dbOwner"
        }
      ]
    }
  );
  ```

  - The example creates a `readWrite` user for the `applicationData` database in `admin` source authentication.

  ```json
  db.createUser(
    {
      "user": "m103-application-user",
      "pwd": "m103-application-pass",
      "roles": [
        {
          "db": "applicationData",
          "role": "readWrite"
        }
      ]
    }
  );
  ```
