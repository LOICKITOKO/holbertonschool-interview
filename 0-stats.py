#!/usr/bin/python3
import sys
import re
from collections import defaultdict

# Define expected status codes
valid_status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
status_counts = defaultdict(int)
total_size = 0
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(valid_status_codes):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

# Regular expression pattern to match valid log lines
pattern = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[.*?\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

try:
    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match:
            status_code, size = match.groups()
            if status_code in valid_status_codes:
                status_counts[status_code] += 1
            total_size += int(size)
            line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

# Print final stats after loop ends
print_stats()
