#!/bin/bash

SCRIPT_DIRECTORY="$(dirname -- "$(readlink -f -- "${BASH_SOURCE[0]}")")"
cd "${SCRIPT_DIRECTORY}" || exit

docker run \
  --interactive \
  --name 'codewars-python311' \
  --rm \
  --tty \
  --volume "pipcache":/.cache \
  --volume "${PWD}":/codewars/python311 \
  andrerademacher/codewars-python311 "$@"
