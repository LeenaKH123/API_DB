"""

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

"""
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:MyNewPass@localhost/sakila")
connection = engine.connect()
<<<<<<< HEAD
# metadata = sqlalchemy.MetaData()
# actor = sqlalchemy.Table('actor', metadata, autoload=True, autoload_with=engine)

# print(actor.columns.keys())
# print(repr(metadata.tables['actor']))
=======
metadata = sqlalchemy.MetaData()
film = sqlalchemy.Table("film", metadata, autoload=True, autoload_with=engine)
category = sqlalchemy.Table("category", metadata, autoload=True, autoload_with=engine)

print(repr(metadata.tables["film"]))
print(repr(metadata.tables["category"]))
>>>>>>> 7856ef653394a526e65c67837963d4168e968336
