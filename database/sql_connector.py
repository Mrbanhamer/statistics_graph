from sqlalchemy import create_engine
from utils.model import Rate

def connection():
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )
    return engine



if __name__ == "__main__":
    try:
        engine = connection()
        print("succesfully connected to db")
    except:
        print("failed connection")
