# Spacecraft Database
Spacecraft metadata and configuration database in JSON format.

## Schema
* [JSON](./schema.json)
* [Markdown](./schema.md)
    - Generated using [jsonschema2md](https://github.com/sbrunner/jsonschema2md) for readability

Verify the document:
```
pipx install check-jsonschema
check-jsonschema --schemafile schema.json spacecraftsdb.json
```

