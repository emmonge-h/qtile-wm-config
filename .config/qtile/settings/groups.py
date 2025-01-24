from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keys import mod, keys

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Groups / Workspaces:
# - Web browser (nf-md-web)
# - Development (nf-md-microsoft_visual_studio_code)
# - Git (nf-md-git)
# - Terminal (nf-oct-terminal)
# - Files (nf-md-folder)
# - Configs (nf-seti-config)

groups = [Group(i) for i in [
    " 󰖟 ",
    " 󰨞 ",
    " 󰊢 ",
    "  ",
    " 󰉋 ",
    "  "
]]

for i, group in enumerate(groups):
    keyboard_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], keyboard_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], keyboard_key, lazy.window.togroup(group.name))
    ])
