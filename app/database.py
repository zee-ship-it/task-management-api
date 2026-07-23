import os 
import psycopg2
from psycopg2.extras import RealDictCursor

##.env file connection 
def get_db_connection():
    # Asal string environment variable se uthao, agar na mile toh fallback string use karo
    DATABASE_URL = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:mysecretpassword@db:5432/task_db"
    )
    
    try:
        # Connection string ko direct pass karna hai
        connection = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise e