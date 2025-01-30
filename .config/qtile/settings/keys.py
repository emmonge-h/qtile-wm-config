from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [   
    # ----- Window Actions -----

    # Switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "space", lazy.layout.next()),

    # Move windows between left/right columns or move up/down in current stack
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Grow windows with keyboard
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),

    # Reset windows
    ([mod], "n", lazy.layout.normalize()),

    # Toggle window mode
    ([mod], "f", lazy.window.toggle_fullscreen()),
    ([mod], "t", lazy.window.toggle_floating()),
    ([mod], "Tab", lazy.next_layout()),
    # Kill window
    ([mod], "w", lazy.window.kill()),

    # ----- Qtile Actions -----

    # Restart Qtile 
    ([mod, "control"], "r", lazy.restart()),

    # Shutdown Qtile
    ([mod, "control"], "q", lazy.shutdown()),
    
    # Open (spawn) application
    ([mod], "o", lazy.spawncmd()),
    
    # ----- App Configs -----
    
    # Terminal
    ([mod], "Return", lazy.spawn("terminator")),

    # App launcher (rofi)
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),    

    # Screenshot
    ([mod], "s", lazy.spawn("scrot 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mkdir -p ~/images/screenshots/ | mv $f ~/images/screenshots/'")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s 'screenshot_%Y-%m-%d-%T_$wx$h.png' -e 'mkdir -p ~/images/screenshots/ | mv $f ~/images/screenshots/'")),

    # ----- Hardware Configs -----

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),	

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-")),
]]

