'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://leena:leena@localhost/sakila')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

print(actor.columns.keys())
print(repr(metadata.tables['actor']))