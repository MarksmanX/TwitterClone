This is a Flask application that functions as a Twitter clone. 
Follow the instructions below to set up and run the application on your 
local machine.

## Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- PostgreSQL (if using PostgreSQL) or SQLite (if using SQLite)
- pip (Python package installer)

## Setup

1. **Clone the Repository**

   First, clone the repository to your local machine:

   git clone https://github.com/MarksmanX/TwitterClone.git
   
   cd TwitterClone

3. Create a Virtual Environment

python -m venv venv

source venv/bin/activate        # On Windows, use `venv\Scripts\activate`

3. Install Dependencies

Install the required Python packages listed in requirements.txt:

pip install -r requirements.txt

4. Configure the Database

For SQLite: Ensure the RazorPagesDemo.db file is present in the project directory. This file should be included in the repository.

For PostgreSQL: Update the DATABASE_URL environment variable in your .env file 
(create one if it doesn’t exist). Example format:

DATABASE_URL=postgresql://username:password@localhost/dbname
Make sure PostgreSQL is running and that the database and user specified 
in the DATABASE_URL exist.

5. Run Migrations

If using PostgreSQL and you need to set up the database schema, run:

flask db upgrade

6. Run the Application

You can now start the Flask application:

flask run

The application will be available at http://localhost:5000.
