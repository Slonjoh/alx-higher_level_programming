#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""


import sys
import signal
import re


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
                '405': 0, '500': 0}
total_size = 0
line_count = 0


def print_metrics():
    """
    Print the current file size and status code metrics.
    """
    print("File size: {}".format(total_size))
    sorted_status = sorted(status_codes.items(), key=lambda x: x[0])
    for code, count in sorted_status:
        if count > 0:
            print("{}: {}".format(code, count))


def signal_handler(sig, frame):
    """
    Handle keyboard interrupt (Ctrl + C) and print metrics.
    """
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = re.split(r' ', line)
        if len(parts) < 9:
            continue
        status_code = parts[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_size += int(parts[-1])
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()
    except Exception:
        pass

print_metrics()
