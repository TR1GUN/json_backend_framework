from jschon import JSONSchema, URI
from genson import SchemaBuilder
import json

builder = SchemaBuilder()

datastore = {"lol":"lol"}
datastore = json.dump(datastore)
builder.add_object(datastore)

builder.to_schema()

empty_schema = JSONSchema({})
print(empty_schema)