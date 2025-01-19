# Multimonitor support

import os
from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
import subprocess

bg_wallpaper = os.path.join(os.path.expanduser("~"), ".config/qtile/wallpaper.jpg") 

def status_bar(widgets):
    return bar.Bar(widgets, 45)

screens = [Screen(
    wallpaper=bg_wallpaper,
    wallpaper_mode="fill",
    top=status_bar(primary_widgets)
)]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(
            wallpaper=bg_wallpaper,
            wallpaper_mode="fill",
            top=status_bar(secondary_widgets)
            )
        )
