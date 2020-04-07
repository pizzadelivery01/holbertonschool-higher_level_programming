#!/bin/bash
# sends post request
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
