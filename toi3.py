import json

def json_to_i3_config(json_file, config_file):
    with open(json_file, 'r') as file:
        config_dict = json.load(file)

    lines = []

    if config_dict.get("font"):
        lines.append(f"font {config_dict['font']}")

    for setting in config_dict.get("set", []):
        lines.append(f"set {setting}")

    if config_dict.get("workspace_layout"):
        lines.append(f"workspace_layout {config_dict['workspace_layout']}")

    if config_dict.get("new_window"):
        lines.append(f"new_window {config_dict['new_window']}")

    for gap in config_dict.get("gaps", []):
        lines.append(f"gaps {gap}")

    if config_dict.get("floating_modifier"):
        lines.append(f"floating_modifier {config_dict['floating_modifier']}")

    for bindsym in config_dict.get("bindsym", []):
        lines.append(f"bindsym {bindsym}")

    for bindcode in config_dict.get("bindcode", []):
        lines.append(f"bindcode {bindcode}")

    for assign in config_dict.get("assign", []):
        lines.append(assign)

    for for_window in config_dict.get("for_window", []):
        lines.append(for_window)

    for exec_command in config_dict.get("exec", []):
        lines.append(f"exec {exec_command}")

    if config_dict.get("client.focused"):
        lines.append(f"client.focused {config_dict['client.focused']}")

    if config_dict.get("client.unfocused"):
        lines.append(f"client.unfocused {config_dict['client.unfocused']}")

    if config_dict.get("client.focused_inactive"):
        lines.append(f"client.focused_inactive {config_dict['client.focused_inactive']}")

    if config_dict.get("client.urgent"):
        lines.append(f"client.urgent {config_dict['client.urgent']}")

    if config_dict.get("bar"):
        lines.append("bar {")
        bar = config_dict["bar"]
        if bar.get("font"):
            lines.append(f"    font {bar['font']}")
        if bar.get("status_command"):
            lines.append(f"    status_command {bar['status_command']}")
        if bar.get("position"):
            lines.append(f"    position {bar['position']}")
        if bar.get("tray_padding"):
            lines.append(f"    tray_padding {bar['tray_padding']}")
        if bar.get("strip_workspace_numbers"):
            lines.append(f"    strip_workspace_numbers {bar['strip_workspace_numbers']}")

        if bar.get("colors"):
            lines.append("    colors {")
            for key, value in bar["colors"].items():
                lines.append(f"        {key} {value}")
            lines.append("    }")

        lines.append("}")

    with open(config_file, 'w') as file:
        file.write("\n".join(lines))

# Use the function
json_to_i3_config('output.json', 'config2')

