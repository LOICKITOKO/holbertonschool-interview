#!/usr/bin/python3
"""Log parsing script."""

import sys
import re
from collections import defaultdict

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
stats = defaultdict(int)
total_size = 0
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if stats[code]:
            print("{}: {}".format(code, stats[code]))


pattern = re.compile(
    r'^\d{1,3}(?:\.\d{1,3}){3} - \[.*?\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
)

try:
    for line in sys.stdin:
        match = pattern.match(line.strip())
        if match:
            code, size = match.groups()
            if code in status_codes:
                stats[code] += 1
            total_size += int(size)
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
