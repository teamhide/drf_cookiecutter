#!/bin/bash
python3 /home/docker/config/secret_manager.py
source ~/.bashrc
supervisord -c /home/docker/config/supervisor-prod.conf