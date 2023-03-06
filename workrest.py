#!/usr/bin/env python

"""
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import GLib, Gtk as gtk, AppIndicator3 as appindicator, GObject
"""
import subprocess
import time
#from threading import Thread

WORK_TIME = (30 * 60)
WORK_PERIODS_BEFORE_LONG_BREAK = 4
REST_TIME_SHORT = (20 * 60)
REST_TIME_LONG = (20 * 60)

def main():
    """
    indicator = appindicator.Indicator.new("workrest", "task-due-symbolic", \
            appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(menu())

    update = Thread(target=run_timers)
    update.setDaemon(True)
    update.start()

    gtk.main()"""
    run_timers()

def menu():
    menu = gtk.Menu()
    
    exit_action = gtk.MenuItem('Quit')
    exit_action.connect('activate', quit)
    menu.append(exit_action)

    menu.show_all()
    return menu

def quit(_):
    gtk.main_quit()

def run_timers():
    workPeriodsDone = 0
    while True:
        subprocess.Popen(["notify-send", "Time to work."])
        time.sleep(WORK_TIME / 2)

        subprocess.Popen(["notify-send", "Halfway done!"])
        time.sleep(WORK_TIME / 2)

        workPeriodsDone = (workPeriodsDone + 1) % WORK_PERIODS_BEFORE_LONG_BREAK
        """
        if workPeriodsDone == 0:
            subprocess.Popen(["notify-send", "Time for a longer break."])
            time.sleep(REST_TIME_LONG)
        else:
        """
        if True:
            subprocess.Popen(["notify-send", "Time to rest."])
            time.sleep(REST_TIME_SHORT)

if __name__ == "__main__":
    main()
