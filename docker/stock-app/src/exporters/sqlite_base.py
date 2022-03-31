import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

class SqliteBase:

    Base = declarative_base()

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        engine = sqlalchemy.create_engine(self.db)
        
        # Create database if it does not exist.
        if not database_exists(engine.url):
            create_database(engine.url)
        else:
            # Connect the database if exists.
            engine.connect()

        SqliteBase.Base.metadata.create_all(engine)

        # Starting a session
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = Session()
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.commit()
        self.session.close()

