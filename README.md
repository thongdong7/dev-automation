# Refresh Browser

(For Ubuntu only)

A script to change the focus Window to Browser (E.g:Chrome) and send key to refresh browser.

This could be integrated into SublimeText and other idea as a shortcut to improve the productivity of developer

# Install

Install xautomation (used to send keystrokes)

    sudo apt-get install xautomation

Install pygtk (used to change focus to browser window)

    sudo apt-get install python-gtk2-dev python-wnck

Clone this project

# Usage

    ./refresh-browser.py

For Sublime Text, go to `Tools` > `Build System` > `New Build System`

    {
        "shell_cmd": "/usr/bin/python <path_to_dev_automation>/refresh-browser.py"
    }

When you build, it will switch to browser and refresh
