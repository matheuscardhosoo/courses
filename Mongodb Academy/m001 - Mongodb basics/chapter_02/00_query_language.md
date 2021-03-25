# Query Language

## Introduction to CRUD

- Create:
  - Write operation.
  - Examples:
    - insertOne:

      ```json
      db.movieSchatch.insertOne(
        {
          "_id": "tt0084726",
          "title":"Start Trek II: The Wrath of Khan",
          "year": 1982,
          "type": "movie"
        }
      );
      ```

    - insertMany:
      - Create multiple documents based on the input list.
      - Can be ordered or unordered inserts.
      - Ordered inserts consider the input list sequence.
        - Erros break the execution and does not add any othe document.
      - Unordered inserts documents independently.
        - Erros block only broken document.

      ```json
      db.movieSchatch.insertOne(
        [
          {
            "_id" : "tt0084726",
            "title" : "Star Trek II: The Wrath of Khan",
            "year" : 1982,
            "type" : "movie"
          },
          {
            "_id" : "tt0796366",
            "title" : "Star Trek",
            "year" : 2009,
            "type" : "movie"
          },
          {
            "_id" : "tt0084726",
            "title" : "Star Trek II: The Wrath of Khan",
            "year" : 1982,
            "type" : "movie"
          },
          {
            "_id" : "tt1408101",
            "title" : "Star Trek Into Darkness",
            "year" : 2013,
            "type" : "movie"
          },
          {
            "_id" : "tt0117731",
            "title" : "Star Trek: First Contact",
            "year" : 1996,
            "type" : "movie"
          }
        ],
        {
          ordered: false
        }
      );
      ```

- Read:
  - Read operation.
  - Batch of results are separated on sets that can be itarated using cursors (using getMore()).
  - By default, MOngDB returns all document fields.
  - Projections specifies the field that should be returned.
    - By defaultf, Projections always return _id field.
    - _id needs to be explicitly exclude.

  ```json
  db.movieDetails.find(
    {
      "rated": "PG",
      "awards.nominations": 10
    },
    {
      "_id": 0,
      "title": 1
    }
  );
  ```

  - Examples:
    - find (basic equality):
      - Nested objects can be accessed using "." (dot) expression.

      ```json
      db.movieDetails.find(
        {
          "rated": "PG",
          "awards.nominations": 10
        }
      );
      ```

    - find (array perfect match):

      ```json
      db.movies.find(
        {
          "cast": [
            "Jeff Bridges",
            "Tim Robbins"
          ]
        }
      );
      ```

    - find (array single match):

      ```json
      db.movies.find(
        {
          "cast": "Jeff Bridges"
        }
      );
      ```

    - find (array specified position match):

      ```json
      db.movies.find(
        {
          "cast.0": "Jeff Bridges"
        }
      );
      ```

- Update:
  - Write operation.
  - Common update methods:
    - "$inc": increments the specified field by the specified value.
    - "$mul": multiplies  the specified field by the specified value.
    - "$rename": renames the specified field.
    - "$setOnInsert": sets the value if the update results in insert.
    - "$set": completely update or set the specified attribute.
    - "$unset": completely remove the specified attribute.
    - "$min": only updates if the input is greater than the current value.
    - "$max": only updates if the input is less than the current value.
  - Array update methods:
    - "$addToSet": Adds elements to array if it does not exist.
    - "$pop": Pop first/last array item.
    - "$pullAll": Remove all matching values from array.
    - "$pull": Remove all matching values from array.
    - "$pushAll": Adds several items to array.
    - "$push": Adds a item to array.
  - "upert" create a document if it does not exist.
  - Example:
    - updateOne:

    ```json
    db.movieDetails.updateOne(
      {
        "title": "The Martian"
      },
      {
        "$set": {
          "poster": "Poster"
        }
      },
      {
        "upert": true
      }
    );
    ```

    - updateMany:

    ```json
    db.movieDetails.updateMany(
      {
        "rated": null
      },
      {
        "$unset": {
          "rated": ""
        }
      }
    );
    ```

    - replaceOne:
      - Completely replace a document based on a filter.

    ```json
    db.movieDetails.updateMany(filter, document);
    ```

- Delete:
  - Write operation.
  - Example:
    - deleteOne:

    ```json
    db.movieDetails.deleteOne(
      {
        "title": "The Martian"
      }
    );
    ```

    - deleteMany:

    ```json
    db.movieDetails.deleteMany(
      {
        "rated": null
      }
    );
    ```
