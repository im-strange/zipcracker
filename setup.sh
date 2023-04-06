#!/bin/bash

custom_command="alias zipcracker='python zipcracker.py'"
echo "$custom_command" >> ~/.bashrc
source  ~/.bashrc
echo "SUCCESS"
