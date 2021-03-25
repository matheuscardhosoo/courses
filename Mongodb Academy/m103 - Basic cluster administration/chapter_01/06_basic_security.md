# Mongod

## Basic Security

- MongoDB uses an authentication + authorization security.

### Authentication

- Verifies the Identify of a user.
- Validate credentials.
- MongoDB supports multiple authentication mechanisms.

#### Client Authentication

##### SCRAM

- Salted Challenge Response Authetication Mechanism.
- Default MongoDB authenticaton.
- The most basic client authetication.
- Provided by all MongoDB version.
- MongoDB server presents a question (challenge) to the client who must provide a valid answer.
  - Basically password security.

##### X.509

- Provided by Community version.

##### LDAO

- Lightweight Directory Access Protocol.
- Provided by Enterprise version only.

##### Kerberos

- Power authentication process.

#### Intracluster Authentication

- Mechanism by which nodes in a cluster authenticate to each other.
- Secret handshake.

### Authorization

- Verifies the Privileges of a user.
- `Role` based access control for authorizing an autenticated user.
- High level of responsability isolation among individual users.
- Enabled by `authorizaztion` config flag.
  - It also enable the authentication process (one cannot exist without the other).

#### User

- MongoDB does not provides default users.
  - It is necessary to use the `localhost exception` to connect to MongoDB and create a first administrative root user.
- Users exists per database.
- Users should be created by function in database.
- Each MongoDB `User` has one or more associated `Roles`.
- At the very minimum, it shoulds always configure SCRAM-SHA-1 with a single administrative user protected by a strong password.

##### Localhost Exception

- Allows a `unauthenticated user` to access a MongoDB server that enforces authentication.
  - Does not have configured user for a common authentication.
  - Must run the Mongo Shell from the same host of MongoDB server.
  - It closes after the first user configuration.
- A kind of `temporary user` that has the permissions to only create one user.
- The `localhost exception` should be always used to create a user with administrative privileges in `admin` database.
  - This new user should be used to create others specific users.
- The process:

  - To connect to the `localhost exception`:

    ```shell
    mongo --host 127.0.0.1:27000
    ```

  - In Mongo Shell, to create the admin user:

    ```json
    db.createUser(
      {
        "user": "root",
        "pwd": "root",
        "roles": [
          {
            "role": "root",
            "db": "admin"
          }
        ]
      }
    );
    ```

  - To connect with the new user:

    ```shell
    mongo admin --host 127.0.0.1:27000 -u root -p root --authenticationDatabase admin
    ```

#### Role

- A role assigned to a user will give it all the respective privileges.
- `Role` is composed of set of `Privileges`.

![role_structure](./images/role_structure.png)

- Instead of have a list of `Privileges`, a `Role` can inherit the privileges from other `Roles`.

![role_structure](./images/role_heritage.png)

- `Role` can be composed of set of `Network Authentication Restrictions`.
  - It defines that the given `Role` is allowed to connect from a `clientSource`, or to a `serverAdress`, by specifying it as parameter.

#### Privilege

- `Privileges` defines the `Actions` that can be performed over a `Resources`.

- Example:

  - A role that permits the shutdown of any menber of a specified cluster,

    ```json
    {
      "resource": {
        "cluster": true
      },
      "actions": ["shutdown"]
    }
    ```

#### Resources

- Types:
  - Database.
  - Collection.
  - Set of Collections.
  - Cluster.
    - Replica Set.
    - Shard Cluster.
- Examples:

  - Specific database and collection:

    ```json
    {
      "db": "products",
      "collection": "inventory"
    }
    ```

  - All databases and all collections:

    ```json
    {
      "db": "",
      "collection": ""
    }
    ```

  - Any databases and specific collections:

    ```json
    {
      "db": "",
      "collection": "accounts"
    }
    ```

  - Specific databases and any collections:

    ```json
    {
      "db": "products",
      "collection": ""
    }
    ```

  - Cluster resource:

    ```json
    {
      "cluster": true
    }
    ```

