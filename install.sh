#!/bin/bash

NAME=org.kde.ssh-runner

# Standalone install script for copying files

set -e

prefix="${XDG_DATA_HOME:-$HOME/.local/share}"
krunner_dbusdir="$prefix/krunner/dbusplugins"
services_dir="$prefix/dbus-1/services/"

mkdir -p $krunner_dbusdir
mkdir -p $services_dir

cp ssh-runner.desktop $krunner_dbusdir
printf "[D-BUS Service]\nName=$NAME\nExec=\"$PWD/main.py\"" > $services_dir/$NAME.service

kquitapp6 krunner
