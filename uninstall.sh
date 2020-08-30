#! /bin/bash

set -e

rm ~/.local/share/kservices5/ssh-runner.desktop
rm ~/.local/share/dbus-1/services/com.selfcoders.ssh-runner.service

kquitapp5 krunner