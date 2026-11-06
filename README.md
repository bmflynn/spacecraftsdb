# Spacecraft Database
Spacecraft metadata and configuration database in JSON format.

## Schema
* [Spacecraft](./schemas/spacecraft.json)
* [Database](./schemas/db.json)
* [Input Data](./schemas/input.json)

Install [check-jsonschema]
```
uv tool install check-jsonschema
```

Verify the spacecrafts
```sh 
./scripts/check.sh
```
