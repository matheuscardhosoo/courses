# Introduction and Setup

## Course curriculum

- Deploying MongoDB.
- Administration tools.
- Mongod:

  - MongoDB Core.
  - Request and access manage.
  - Logs.
  - Availability.
  - Reication.
  - Scalability.
    - Sharding.

## Vagrant Environment

### Why

- Sandbox environment.
- Avoid dependency and system troubleshooting.

### How

- Install Vagrant and VirtualBox.
- Create the vagrant-env.

  - To startt it:
    - Use `--provision` to configure it.

  ```shell
  vagrant up
  ```

  - To connect it:

  ```shell
  vagrant ssh
  ```

  - To stop it:

  ```shell
  vagrant halt
  ```

  - To validate it:

  ```shell
  validate_box
  ```
