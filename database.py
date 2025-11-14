"""
Database Schema and Setup for ParentAdvocateAI
"""
import sqlite3
import os

DATABASE_PATH = "parentadvocate.db"

def init_database():
    """Initialize database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        user_type TEXT NOT NULL,
        full_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()
    print("✅ Database initialized")

def get_connection():
    return sqlite3.connect(DATABASE_PATH, check_same_thread=False)

if not os.path.exists(DATABASE_PATH):
    init_database()
