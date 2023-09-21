#!/bin/bash
set -e

database=spacecraftsdb.json
gitsha=$(git rev-parse HEAD)
generated=$(date -uIseconds)

jq "{\"spacecrafts\": ., \"version\": \"\", \"gitSha\": \"${gitsha}\", \"generated\":\"${generated}\"}" spacecrafts.data.json > ${database}
sha256sum ${database} > ${database}.sha256 

