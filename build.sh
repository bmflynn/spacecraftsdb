#!/bin/bash
set -e

database=spacecraftsdb.json
gitsha=$(git rev-parse HEAD)
version=$(git describe --match '*.*.*' || true)
generated=$(date -uIseconds)

jq -c -s "{\"spacecrafts\": ., \"version\": \"${version}\", \"gitSha\": \"${gitsha}\", \"generated\":\"${generated}\"}" spacecrafts/*.json > ${database}
sha256sum ${database} > ${database}.sha256
