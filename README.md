## Usage

### Initializing the Database
To initialize the database, run the following command:
flask --app flaskr init-db

### Running the Application Locally
To run the application locally with debugging enabled, use the following command:
flask --app flaskr run --debug

## Endpoints

- **Get All Blogs:** `GET /`

- **Create Blog:** `POST /blog/create`
  - Body:
    ```json
    {
        "title": "Blog Title",
        "body": "Blog main content"
    }
    ```

- **Get Blog by ID:** `GET /blog/<id>`