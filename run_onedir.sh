#!/bin/bash

echo "Starting..."

gnome-terminal -x bash -c "python ~/Desktop/Fred/run_server.py" &

sleep 1

python ~/Desktop/Fred/run_client.py

