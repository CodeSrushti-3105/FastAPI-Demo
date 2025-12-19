from sqlachemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://posgtgres:9022331505@localhost:5432/telusko"
engine = create_engine(db_url)
Session = sessionmaker(autocommit = False, autoflush = False, bind = engine)