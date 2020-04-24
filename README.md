# Workrest

## Introduction
This app provides a basic implementation of a timer for the
[Pomodoro Method](https://en.wikipedia.org/wiki/Pomodoro_Technique).
By default, the timer will run for four *pomodoros* of twenty-five minutes each, separated by a break period of
five minutes. After each set of four pomodoros, the timer will begin a longer break period of twenty minutes.

## Installation
Any version of Python (2/3) should be sufficient to run workrest. 

You will also require `libnotify` and some type of notification server, e.g. [Dunst](https://dunst-project.org/).

After meeting the above requirements, simply download `workrest.py` and place it wherever convenient, invoking it
with either `./workrest.py` or `python workrest.py`.

## Configuration
The global variables `WORK_TIME`, `WORK_PERIODS_BEFORE_LONG_BREAK`, `REST_TIME_SHORT`, and `REST_TIME_LONG`
control the parameters of the timer. These variables can be found on lines 14-17 of the source file.

Note that all times are measured in seconds.
