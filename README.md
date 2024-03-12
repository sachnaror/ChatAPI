# Django Chat App Project (Using Channels)

This project is a basic real-time chat application built using the Django framework and Django Channels. It showcases the use of WebSockets for real-time communication between clients and server.

## Getting Started

These instructions will guide you through setting up the project on your local machine for development and testing purposes.

### Prerequisites

Before you start, ensure you have installed:

- Python 3.8 or higher
- Redis 5.0 or higher

### Setting Up the Development Environment

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sachnaror/ChatAPI
   cd ChatAPI
   ```

2. **Create and Activate a Virtual Environment**

   - For Unix or MacOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - For Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install the Requirements**

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Migrations**

   Apply the database migrations to your local database.

   ```bash
   python manage.py migrate
   ```

5. **Run the Redis Server**

   Ensure the Redis server is running on your local machine. This project assumes Redis is running on its default port (6379).

   ```bash
   redis-server
   ```

6. **Start the Django Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Open your web browser and navigate to <http://localhost:8000> to start using the chat application.

## Acknowledgments

- **Django Channels** for providing the real-time WebSocket communication framework.
- **Redis** for the efficient messaging and storage solution.

```
