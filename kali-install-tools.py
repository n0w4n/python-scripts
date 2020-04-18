#!/usr/bin/env python3

import subprocess

# update apt sources
subprocess.run(["sudo", "apt", "update"])

# installing terminator
subprocess.run(["sudo", "apt", "install", "terminator", "-y"])

# installing sublime texteditor
# step 1 - install GPG key
subprocess.run(["wget", "-qO", "-", "https://download.sublimetext.com/sublimehq-pub.gpg", "|", "sudo", "apt-key", "add", "-"])
# step 2 - ensure apt is set up to work with https sources
subprocess.run(["sudo", "apt-get", "install", "apt-transport-https"])
# step 3 - add sublime repo to apt database
subprocess.run(["echo", "'deb https://download.sublimetext.com/ apt/stable/'", "|", "sudo", "tee", "'/etc/apt/sources.list.d/sublime-text.list'"])
# step 4 - update apt sources
subprocess.run(["sudo", "apt", "update"])
# step 5 - install sublime-text
subprocess.run(["sudo", "apt", "install", "sublime-text", "-y"])

# installing GoBuster (web bruteforce tool)
subprocess.run(["sudo", "apt", "install", "gobuster", "-y"])
