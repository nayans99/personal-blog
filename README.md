## Getting Started

### Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/nayans99/personal-blog.git
```

### Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies for your Flask application. Follow these steps to create and activate a virtual environment:

1. Navigate to the root directory of the cloned repository.
2. Run the following command to create a virtual environment named `venv`:

```bash
python -m venv .venv
```
3. Activate the virtual environment:
   
   - On Windows:
   ```bash
   .venv\Scripts\activate
   ```
   - On mac/linux
   ```bash
   source .venv/bin/activate
   ```

### Install Dependencies
Once the virtual environment is activated, install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```
This command will install all the dependencies listed in the `requirements.txt` file.


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