#!/bin/bash
set -e

database=spacecraftsdb.json
version=$(git rev-parse HEAD)
version=${version:0:8}
generated=$(date -uIseconds)

jq "{\"spacecrafts\": ., \"version\": \"${version}\", \"generated\":\"${generated}\"}" spacecrafts.data.json > ${database}
sha256sum ${database} > ${database}.sha256 

