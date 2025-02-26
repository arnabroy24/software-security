#!/bin/bash

apt-get update && apt-get install -y cron

echo "0 */6 * * * python /app/process-info.py >> /app/process-info.log 2>&1" > /etc/cron.d/process-info-cron

crontab /etc/cron.d/process-info-cron
service cron start

python /app/process-info.py

python /app/backend.py &

wait
