from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [   
    # ----- Window Actions -----

    # Switch between windows
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows with keyboard
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    # Reset windows
    Key([mod], "n", lazy.layout.normalize()),

    # Toggle window mode
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),

    # Kill window
    Key([mod], "w", lazy.window.kill()),

    # ----- Qtile Actions -----

    # Restart Qtile 
    Key([mod, "control"], "r", lazy.restart()),

    # Shutdown Qtile
    Key([mod, "control"], "q", lazy.shutdown()),
    
    # Open (spawn) application
    Key([mod], "o", lazy.spawncmd()),
    
    # ----- App Configs -----
    
    # Terminal
    Key([mod], "Return", lazy.spawn("terminator")),

    # App launcher (rofi)
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Browser
    Key([mod], "b", lazy.spawn("firefox")),

    # File explorer
    Key([mod], "e", lazy.spawn("thunar")),

    # Redshift
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),    

	# ----- Hardware Configs -----

	# Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),	

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]

