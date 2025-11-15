"""
Database for ParentAdvocateAI
"""
import sqlite3
import os

DATABASE_PATH = "parentadvocate.db"

def init_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        full_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        document_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        document_name TEXT,
        document_type TEXT,
        ai_analysis TEXT,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS violations (
        violation_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        violation_type TEXT,
        severity TEXT,
        violation_date DATE,
        law_violated TEXT,
        description TEXT,
        status TEXT DEFAULT 'open'
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS requirements (
        requirement_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        requirement_text TEXT,
        category TEXT,
        deadline DATE,
        status TEXT DEFAULT 'not_started',
        completion_date DATE
    )
    """)
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DATABASE_PATH, check_same_thread=False)

if not os.path.exists(DATABASE_PATH):
    init_database()
