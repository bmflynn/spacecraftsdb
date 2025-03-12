# Spacecraft Database
Spacecraft metadata and configuration database in JSON format.

## Schema
* [Database](./schemas/db.json)
* [Input Data](./schemas/input.json)

Verify the document:
```
pipx install check-jsonschema
check-jsonschema --schemafile schemas/db.json spacecraftsdb.json
```

Verify the document input
```
pipx install check-jsonschema
check-jsonschema --base-uri="" --schemafile schemas/input.json spacecrafts.data.json
```
