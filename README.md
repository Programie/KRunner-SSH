# SSH Runner

A KRunner backend for connecting to SSH hosts listed in your known_hosts file.

## Installation

* Copy [ssh-runner.desktop](ssh-runner.desktop) to ~/.local/share/kservices5
* Restart KRunner (`killall krunner; krunner` or logout & login)
* Start `runner.py <terminal command>` (add it to your startup applications)

## Terminal Command

As every terminal emulator has different options on how to start a new SSH session, you have to specify the command to open the SSH session as argument passed to `runner.py`.

The `{}` placeholder will be replaced by the hostname.

Example for [Tilix](https://gnunn1.github.io/tilix-web/): `tilix -e 'ssh {}'`

## Usage

Open KRunner (usually Alt+F2) and search for a host listed in your known_hosts file.