#!/usr/bin/env python

import subprocess
import sys
import time

WORK_TIME = 30
REST_TIME = 10

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["work", "rest"]:
        print(f"usage: {sys.argv[0]} [work | rest]")
        exit(1)

    is_work_timer = (sys.argv[1] == "work")
    start_timer(is_work_timer)

def start_timer(is_work_timer):
    if is_work_timer:
        subprocess.Popen(["notify-send", f"Starting work timer for {WORK_TIME} minutes."])
        time.sleep(WORK_TIME * 60 / 2)

        subprocess.Popen(["notify-send", "Halfway done."])
        time.sleep(WORK_TIME * 60 / 2)
    else:
        subprocess.Popen(["notify-send", f"Starting rest timer for {REST_TIME} minutes."])
        time.sleep(REST_TIME * 60)

    subprocess.Popen(["notify-send", "Time is up!"])

if __name__ == "__main__":
    main()
