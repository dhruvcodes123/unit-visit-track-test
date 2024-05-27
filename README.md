# Unit Visit Tracker

Unit Visit Tracker is a Django REST Framework (DRF) based API that allows workers to make visits to different units.

## Installation

### Prerequisites

- Python 3.7+
- PostgreSQL

### Steps

1. **Clone the Repository**

    ```bash
    git clone 'https://github.com/dhruvcodes123/unit-visit-track-test.git'
    cd unit-visit-track-test
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**

    Make sure you have PostgreSQL installed and running. Create a database for the project.



5. **Configure Environment Variables**

    Create a `.env` file in the project root directory with the following content:

    ```plaintext
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=5432
    ```

6. **Create and Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a Superuser**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Server**

    ```bash
    python manage.py runserver
    ```

## Postman collection
    Create an environment in postman 
    - Add varialbe "BASE_URL" with this value : "http://127.0.0.1:8000/" 
    - Postman colletion url : https://api.postman.com/collections/30553754-61ed521e-6f3a-430e-88a0-6d141938b743?access_key=PMAT-01HYWWA4838XCTVVHRDWDSSM9B

