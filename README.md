# phase-4..2

# Overview
This Flask API manages guest appearances on a late-night show. It allows for CRUD operations on episodes, guests, and their appearances.


# Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:Thazar-r/phase-4..2.git
   cd phase-4..2

* Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your database:

Ensure you have SQLite installed or modify the DATABASE_URL in the .env file for a different database.
Seed the database:

bash
Copy code
python seeds.py

* Run the application:

bash
Copy code
python app.py

# API Endpoints
Get All Episodes
GET /episodes
Returns a list of episodes.
Get All Guests
GET /guests
Returns a list of all guests.
Create a New Appearance
POST /appearances
Requires JSON body:
json
Copy code
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Summary
This setup creates a simple Flask API that can manage guest appearances using a CSV file as the source of data. 


