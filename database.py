from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db_uri = 'postgresql+psycopg2://%s:%s@%s:%s/%s' % (
    # ARGS.dbuser, ARGS.dbpass, ARGS.dbhost, ARGS.dbname
    os.environ.get('DBUSER', 'bety'),
    os.environ.get('DBPASS', 'bety'),
    os.environ.get('DBHOST', 'localhost'),
    os.environ.get('DBPORT', '5432'),
    os.environ.get('DBNAME', 'bety')
)

# add echo=True to see actual queries executed
engine = create_engine(db_uri, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def get_engine():
    return engine
#Base = declarative_base()
#Base.query = db_session.query_property()

#def init_db():
#    # import all modules here that might define models so that
#    # they will be registered properly on the metadata.  Otherwise
#    # you will have to import them first before calling init_db()
#    import yourapplication.models
#    Base.metadata.create_all(bind=engine)
