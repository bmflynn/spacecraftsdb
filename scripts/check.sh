#!/bin/bash

if [[ -n $1 ]]; then
  exec check-jsonschema --verbose --base-uri="" --schemafile schemas/spacecraft.json $1
fi

for fpath in spacecrafts/*.json; do
  if ! check-jsonschema --base-uri="" --schemafile schemas/spacecraft.json $fpath &>/dev/null; then
    echo "Failed  $fpath"
  else
    echo "Ok      $fpath"
  fi
done
