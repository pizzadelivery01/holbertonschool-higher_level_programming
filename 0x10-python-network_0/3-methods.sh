#!/bin/bash
#shows all methods allowed
curl -sI "$1" | grep ALLOW |cut -d ' ' -f2
