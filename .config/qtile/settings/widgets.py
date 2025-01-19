from libqtile import widget

primary_widgets = [
    widget.GroupBox(fontsize=25),
    widget.Prompt(),
    widget.WindowName(fontsize=15),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Battery(
        update_interval=5,
        charge_char='󰂏', # nf-md-battery_plus_variant
        discharge_char='󰂌', # nf-md-battery_minus_variant
        empty_char='󰂎', # nf-md-battery_outline
        full_char='󰁹', # nf-md-battery
        not_charging_char='󰂌', # nf-md-battery_minus_variant
        unknown_char='󰂑', # nf-md-battery_unknown
        show_short_text=False,
        format='{char} [{percent:2.0%}]'
    ),
    widget.Clock(
        format="(%a) %d/%m/%Y - %I:%M:%S %p"
    )
]

secondary_widgets = [
    widget.GroupBox(fontsize=25),
    widget.Prompt(),
    widget.WindowName(fontsize=15),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Clock(
        format="(%a) %d/%m/%Y - %I:%M:%S %p"
    )
]

widget_defaults = dict(
    font="GeistMono Nerd Font SemiBold",
    fontsize=20,
    padding=3,
)
extension_defaults = widget_defaults.copy()
