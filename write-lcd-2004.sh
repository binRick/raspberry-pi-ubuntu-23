#!/usr/bin/env bash
set -eou pipefail
cd "${0%/*}"
TEXT="${@}"
./write-lcd-2004.py "$TEXT"
