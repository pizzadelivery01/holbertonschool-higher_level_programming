#!/bin/bash
#shows all methods allowed
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
