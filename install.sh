#! /bin/bash

set -e

mkdir -p ~/.local/share/kservices5/
mkdir -p ~/.local/share/dbus-1/services/

cp ssh-runner.desktop ~/.local/share/kservices5/
sed "s|%{BASE_DIR}|${PWD}|g" ssh-runner.service > ~/.local/share/dbus-1/services/com.selfcoders.ssh-runner.service

kquitapp5 krunner