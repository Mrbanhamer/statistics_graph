from sqlalchemy import create_engine

def connection():
    engine = create_engine()

class Rate():
    def __init__(self, date, base, qute):
