# File Structure

## Table of contents

- [File Structure](#file-structure)
  - [Table of contents](#table-of-contents)
  - [Storage Engine](#storage-engine)
  - [Data Files](#data-files)
  - [Diagnostic Files](#diagnostic-files)
  - [Journal Files](#journal-files)
  - [Lock File](#lock-file)
  - [Temporary Files](#temporary-files)

## Storage Engine

- Ref: [WiredTiger](https://docs.mongodb.com/manual/core/wiredtiger/).
- Locks the folders inside of `dbpath`.
- Not designed for user access.

## Data Files

- **Collections** and **Indexes** data are stored into multiple `.wt` files.
- Each collection and index get its own file.
- Exists by default.

## Diagnostic Files

- Data generated by [Full Time Diagnostic Data Collection (FTDC)](https://docs.mongodb.com/manual/administration/analyzing-mongodb-performance/#full-time-diagnostic-data-capture) mechanism.
- FTDC data files are compressed, are not human-readable, and inherit the same file access permissions as the MongoDB data files.
- MongoDB processes run with FTDC on by default.

## Journal Files

- Ref: [Journaling](https://docs.mongodb.com/manual/core/journaling/).
- WiredTiger uses checkpoints to provide a consistent view of data on disk and allow MongoDB to recover from the last checkpoint. However, if MongoDB exits unexpectedly in between checkpoints, journaling is required to recover information that occurred after the last checkpoint.
- Operations synced every 50 ms.
- Max size of 100 mb.
- WiredTiger use a rotated log.

## Lock File

- Locks the folder for Mongo process.

## Temporary Files

- Mongo-Shell session  history: `/tmp/mongo-shell`
- Socket file: `/tmp/mongo.sock`
