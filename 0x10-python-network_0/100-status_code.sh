#!/bin/bash
#only request status code
curl -so /dev/null -w "%{http_code}\n" "$1"
