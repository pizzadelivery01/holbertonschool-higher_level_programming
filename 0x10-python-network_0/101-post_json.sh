#!/bin/bash
# sends post request
curl -s -X POST -d @"$2" "Content_Type: application/json" "$1"
