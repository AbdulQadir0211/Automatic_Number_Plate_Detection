import csv
import os
import datetime

LOG_FILE = "detections_log.csv"

# Ensure log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Plate Number"])

def log_detection(plate_text):
    """Log detected plate number with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, plate_text])

def read_logs(limit=5):
    """Read last 'limit' logs from the CSV file."""
    log_entries = []
    with open(LOG_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        log_entries = list(reader)[-limit:]
    return log_entries
