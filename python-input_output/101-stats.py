#!/usr/bin/python3
"""
script to parse and collect stats on web server logs
"""

import sys
import signal


def summarise(total_file_size, status_codes_frequency):
    # Print the file size
    print("File size:", total_file_size)

    # Print status codes
    keys = list(status_codes_frequency.keys())
    keys.sort()
    for status_code in keys:
        print(f'{status_code}: {status_codes_frequency[status_code]}')


def main():
    status_codes_frequency = {}
    total_file_size = 0
    count = 0

    # Summarise and reset on SIGINT signal
    def on_sig_int():
        nonlocal status_codes_frequency
        nonlocal total_file_size

        summarise(total_file_size, status_codes_frequency)

    signal.signal(signal.SIGINT, on_sig_int)

    # Loops each line in stdin
    for line in sys.stdin:
        # parse line to extract info
        try:
            fields = line.strip().split()
            status_code = int(fields[-2])
            file_size = int(fields[-1])

            # Checking if status code is not valid
            if type(status_code) is not int:
                raise Exception()

            if status_code < 200 or status_code >= 600:
                raise Exception()

            # Add status_code to our hash
            if status_code in status_codes_frequency:
                status_codes_frequency[status_code] += 1
            else:
                status_codes_frequency[status_code] = 1

            # increase total_file_size
            total_file_size += file_size
        except:
            pass
        finally:
            # increment count
            count += 1

            # check if we should summarise
            if count % 10 == 0:
                summarise(total_file_size, status_codes_frequency)

    # If we run out lines before a sigint or get a multiple of 10
    # We just summarise what we currently have
    summarise(total_file_size, status_codes_frequency)

if __name__ == "__main__":
    main()
