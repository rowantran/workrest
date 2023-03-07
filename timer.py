#!/usr/bin/env python

import subprocess
import sys
import time

MIN_LENGTH_NOTIFY_HALFWAY = 30

def main():
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print(f"usage: {sys.argv[0]} [minutes]")
        exit(1)

    minutes = int(sys.argv[1])
    start_timer(minutes)

def start_timer(minutes):
    subprocess.Popen(["notify-send", f"Starting timer for {minutes} minutes."])

    if minutes >= MIN_LENGTH_NOTIFY_HALFWAY:
        time.sleep(minutes * 60 / 2)
        subprocess.Popen(["notify-send", "Halfway done."])
        time.sleep(minutes * 60 / 2)
    else:
        time.sleep(minutes * 60)

    subprocess.Popen(["notify-send", "Time is up!"])

if __name__ == "__main__":
    main()
