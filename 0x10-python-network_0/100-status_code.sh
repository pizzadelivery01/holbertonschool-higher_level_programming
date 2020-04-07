#!/bin/bash
#only request status code
curl -o /dev/null -sw "%{http_code}" "$1"
