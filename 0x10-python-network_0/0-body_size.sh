#!/bin/bash
#curls and displays bytes
curl -so /dev/null -w '%{size_download}\n' "$1"
