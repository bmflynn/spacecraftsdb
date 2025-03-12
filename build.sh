#!/bin/bash
set -e

database=spacecraftsdb.json
gitsha=$(git rev-parse HEAD)
version=$(git describe --match '*.*.*' || true)
generated=$(date -uIseconds)

jq -c "{\"spacecrafts\": ., \"version\": \"${version}\", \"gitSha\": \"${gitsha}\", \"generated\":\"${generated}\"}" spacecrafts.data.json > ${database}
sha256sum ${database} > ${database}.sha256
