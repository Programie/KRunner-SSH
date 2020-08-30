#! /usr/bin/env python3
import os
import subprocess
import sys

from gi.repository import GLib
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

objpath = "/ssh"
iface = "org.kde.krunner1"


class Runner(dbus.service.Object):
    def __init__(self, terminal_command):
        self.terminal_command = terminal_command

        dbus.service.Object.__init__(self, dbus.service.BusName("com.selfcoders.ssh-runner", dbus.SessionBus()), objpath)

    @dbus.service.method(iface, out_signature="a(sss)")
    def Actions(self, msg):
        return []

    @dbus.service.method(iface, in_signature="s", out_signature="a(sssida{sv})")
    def Match(self, query):
        query = query.split(" ")
        if len(query) > 1 and query[0] == "ssh":
            query = query[1:]

        query = " ".join(query)

        known_hosts_file = os.path.join(os.path.expanduser("~"), ".ssh", "known_hosts")
        if not os.path.isfile(known_hosts_file):
            return []

        results = []

        with open(known_hosts_file, "r") as file:
            for line in file:
                hostname = line.split(" ")[0].split(",")[0]

                if not hostname.startswith(query):
                    continue

                # actionId, actionName, iconName, Type, relevance (0-1), properties
                results.append((hostname, hostname, "terminal", 100, 0, {}))

        return results

    @dbus.service.method(iface, in_signature="ss")
    def Run(self, matchId, actionId):
        command = []

        for argument in self.terminal_command:
            if "{}" in argument:
                argument = argument.format(matchId)

            command.append(argument)

        subprocess.call(command)


if __name__ == "__main__":
    terminal_command = ["konsole", "-e", "ssh {}"]

    if len(sys.argv) > 1:
        terminal_command = sys.argv[1:]

    runner = Runner(terminal_command)
    loop = GLib.MainLoop()
    loop.run()
