import sqlite3
import json
import os

# --- GENRE CONFIGURATION ---
ALL_GENRES = [
    "Mystery", "Fantasy", "Science", "History", "Biography", 
    "Adventure", "Space", "Nature", "Sports", "Technology", 
    "Art", "Geography", "Mythology", "Poetry", "Romance"
]

def get_allowed_genres(age_group):
    """Filters which genres the user sees based on their age group."""
    if age_group == "5-7":
        return ALL_GENRES[:5]  # Mystery, Fantasy, Science, History, Biography
    elif age_group == "8-10":
        return ALL_GENRES[:10]  # Top 10, no Romance
    elif age_group == "11-13":
        return ALL_GENRES[:12]  # Most genres, no Romance/Poetry
    elif age_group == "14+":
        return ALL_GENRES  # All genres
    else:
        return ALL_GENRES[:5]  # Default for unknown age groups

# Mapping between UI level names and JSON level names
LEVEL_MAPPING = {
    "Beginner": "Novice",
    "Intermediate": "Intermediate",
    "Advanced": "Advanced",
    "Expert": "Advanced"
}

def get_books_for_selection(age_group, genre, level):
    """
    Pure JSON Pull:
    Finds library.json, loads it, and returns books for the specific Genre and Level.
    Maps the UI level names to JSON level names.
    """
    # Map the UI level to JSON level
    json_level = LEVEL_MAPPING.get(level, "Novice")
    
    # Locates the library.json in the same folder as this script
    file_path = os.path.join(os.path.dirname(__file__), 'library.json')
    
    if not os.path.exists(file_path):
        print(f"ERROR: library.json not found at {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            database = json.load(f)
            
        # Drill down: database -> Genre (e.g. "Fantasy") -> Level (e.g. "Novice")
        genre_data = database.get(genre, {})
        books = genre_data.get(json_level, [])
        
        # Returns the list found in JSON (Empty list if keys don't match)
        return books
        
    except Exception as e:
        print(f"ERROR: Could not read library.json: {e}")
        return []

def init_db():
    """Initializes the SQLite database for user progress."""
    conn = sqlite3.connect('reading_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS progress 
        (id INTEGER PRIMARY KEY, age TEXT, level TEXT, points INTEGER)''')
    conn.commit()
    conn.close()

