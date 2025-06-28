#!/bin/bash

# Exit if something fails
set -e

prefix="${XDG_DATA_HOME:-$HOME/.local/share}"
krunner_dbusdir="$prefix/krunner/dbusplugins"

rm $prefix/dbus-1/services/org.kde.ssh-runner.service
rm $krunner_dbusdir/ssh-runner.desktop

kquitapp6 krunner
