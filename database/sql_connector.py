from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

def connection():
    load_dotenv()
    # Good practice: Provide defaults or check if these are None
    user = os.getenv("secret_user")
    pw = os.getenv("secret_password")
    host = os.getenv("secret_host")
    port = os.getenv("secret_port")
    db = os.getenv("secret_database_name")
    
    url = f"mysql+pymysql://{user}:{pw}@{host}:{port}/{db}"
    return create_engine(url)

#def make_database():
    

if __name__ == "__main__":
    engine = connection()
    try:
        # The 'with' block actually attempts to open a connection
        with engine.connect() as conn:
            # We run a tiny query to prove the database responded
            conn.execute(text("SELECT 1"))
        print("✅ Successfully connected to the database!")
    except Exception as e:
        print(f"❌ Connection failed: {e}")