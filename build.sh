#!/bin/bash
set -e

database=spacecraftsdb.json
gitsha=$(git rev-parse HEAD)
version=$(git describe --match '*.*.*')
generated=$(date -uIseconds)

jq "{\"spacecrafts\": ., \"version\": \"${version}\", \"gitSha\": \"${gitsha}\", \"generated\":\"${generated}\"}" spacecrafts.data.json > ${database}
sha256sum ${database} > ${database}.sha256 

