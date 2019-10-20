import json
from arango import ArangoClient

client = ArangoClient()

sys_db = client.db("_system")
if not sys_db.has_database("test_db"):
    sys_db.create_database("test_db")

test_db = client.db("test_db")
if test_db.has_collection("movies"):
    movie_collection = test_db.collection("movies")
else:
    movie_collection = test_db.create_collection("movies")

data_file = open("./data.txt")
movie_lines = data_file.readlines()

for idx, movie_line in enumerate(movie_lines):
    movie = json.loads(movie_line)
    movie["_key"] = str(idx)
    movie = movie_collection.insert(movie, sync=False, overwrite=True)
