#!/bin/bash
# sends post request
curl -sX POST -d "@$2" -H "Content_Type: application/json" -H "Accept: application/json" "$1"
