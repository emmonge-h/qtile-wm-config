from libqtile import widget

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def divider(divider_string, font_size):
    return widget.TextBox(
        fmt=f"{divider_string}",
        padding=5,
        fontsize=font_size,
    )

primary_widgets = [
    widget.GroupBox(
        fontsize=20,
        use_mouse_wheel=False,
    ),
    widget.Prompt(),
    widget.WindowName(),
    widget.CurrentLayout(
        fmt=" {}", # nf-cod-multiple_windows
        mouse_callbacks={
            "Button1": None,
            "Button2": None,
            },
        ),
    divider(" ", 15), # nf-oct-dot_fill
    widget.Clock(
        padding=5,
        format="󰃰 %H:%M:%S - %d/%m/%Y", # nf-md-calendar_clock
    ),
    divider(" ", 15), # nf-oct-dot_fill
    widget.Net(
        # Interface name may vary
        interface="wlan0", 
        format=" {interface}: {up}{up_suffix} 󱦲󱦳 {down}{down_suffix}", # nf-fa-feed, nf-md-arrow_up_thin, nf-md-arrow_down_thin 
    ),
    divider(" ", 15), # nf-oct-dot_fill
    widget.Volume(
        padding=5,
        emoji=True,
        emoji_list=[
            "󰸈", # nf-md-volume_variant_off
            "󰕿", # nf-md-volume_low
            "󰖀", # nf-md-volume_medium
            "󰕾" # nf-md-volume_high
        ],
        # Volume app
        volume_app="pavucontrol",
    ),
    widget.Battery(
        padding=5,
        update_interval=30,
        charge_char="󰂏", # nf-md-battery_plus_variant
        discharge_char="󰂌", # nf-md-battery_minus_variant
        empty_char="󰂎", # nf-md-battery_outline
        full_char="󰁹", # nf-md-battery
        not_charging_char="󰂌", # nf-md-battery_minus_variant
        unknown_char="󰂑", # nf-md-battery_unknown
        show_short_text=False,
        format="{char} [{percent:2.0%}]",
    ),
]

secondary_widgets = [
    widget.GroupBox(
        fontsize=20,
        use_mouse_wheel=False,
    ),
    widget.Prompt(),
    widget.WindowName(fontsize=15),
    widget.CurrentLayout(
        fmt=" {}", # nf-cod-multiple_windows
        mouse_callbacks={
            "Button1": None,
            "Button2": None,
            },
        ),
    divider(" ", 15), # nf-oct-dot_fill
    widget.Clock(
        padding=5,
        format="󰃰 %H:%M:%S - %d/%m/%Y", # nf-md-calendar_clock
    ),
]

widget_defaults = dict(
    font="GeistMono Nerd Font Regular",
    fontsize=15,
    padding=1,
)
extension_defaults = widget_defaults.copy()
