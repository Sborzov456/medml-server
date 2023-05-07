#!/bin/sh
echo "$PWD"
cd ./server/ 
python3 server.py

exec "$@"