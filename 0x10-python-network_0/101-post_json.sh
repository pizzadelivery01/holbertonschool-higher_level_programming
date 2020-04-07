#!/bin/bash
# sends post request
curl -s -X POST -d "@$2" -H "Content_Type: application/json" "$1"
