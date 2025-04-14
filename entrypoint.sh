#!/bin/bash
apt-get update && apt-get install -y cron
echo "0 */6 * * * python /app/process-info.py >> /app/process-info.log 2>&1" > /etc/cron.d/process-info-cron
crontab /etc/cron.d/process-info-cron
service cron start

# Run the data processing script first and wait for it to complete
echo "Running initial data processing..."
python /app/process-info.py

# Create a marker file when the process is done
touch /app/data_ready

# Start the backend app
python /app/backend.py
