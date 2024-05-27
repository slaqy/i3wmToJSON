import json

def i3_config_to_json(config_file, json_file):
    config_dict = {
        "font": "",
        "set": [],
        "workspace_layout": "",
        "new_window": "",
        "gaps": [],
        "floating_modifier": "",
        "bindsym": [],
        "bindcode": [],
        "assign": [],
        "for_window": [],
        "exec": [],
        "client.focused": "",
        "client.unfocused": "",
        "client.focused_inactive": "",
        "client.urgent": "",
        "bar": {
            "font": "",
            "status_command": "",
            "position": "",
            "tray_padding": "",
            "strip_workspace_numbers": "",
            "colors": {}
        }
    }

    with open(config_file, 'r') as file:
        lines = file.readlines()

    current_section = None

    for line in lines:
        line = line.strip()

        if line.startswith("#") or not line:
            continue

        if line.startswith("font "):
            config_dict["font"] = line.split(" ", 1)[1].strip()
        elif line.startswith("set "):
            config_dict["set"].append(line.split(" ", 1)[1].strip())
        elif line.startswith("workspace_layout"):
            config_dict["workspace_layout"] = line.split(" ", 1)[1].strip()
        elif line.startswith("new_window"):
            config_dict["new_window"] = line.split(" ", 1)[1].strip()
        elif line.startswith("gaps"):
            config_dict["gaps"].append(line.split(" ", 1)[1].strip())
        elif line.startswith("floating_modifier"):
            config_dict["floating_modifier"] = line.split(" ", 1)[1].strip()
        elif line.startswith("bindsym "):
            config_dict["bindsym"].append(line.split(" ", 1)[1].strip())
        elif line.startswith("bindcode "):
            config_dict["bindcode"].append(line.split(" ", 1)[1].strip())
        elif line.startswith("assign ["):
            config_dict["assign"].append(line)
        elif line.startswith("for_window ["):
            config_dict["for_window"].append(line)
        elif line.startswith("exec "):
            config_dict["exec"].append(line.split(" ", 1)[1].strip())
        elif line.startswith("client.focused"):
            if len(line.split(" ", 1)) > 1:
                config_dict["client.focused"] = line.split(" ", 1)[1].strip()
        elif line.startswith("client.unfocused"):
            if len(line.split(" ", 1)) > 1:
                config_dict["client.unfocused"] = line.split(" ", 1)[1].strip()
        elif line.startswith("client.focused_inactive"):
            if len(line.split(" ", 1)) > 1:
                config_dict["client.focused_inactive"] = line.split(" ", 1)[1].strip()
        elif line.startswith("client.urgent"):
            if len(line.split(" ", 1)) > 1:
                config_dict["client.urgent"] = line.split(" ", 1)[1].strip()
        elif line.startswith("bar {"):
            current_section = "bar"
        elif current_section == "bar" and line.startswith("font "):
            config_dict["bar"]["font"] = line.split(" ", 1)[1].strip()
        elif current_section == "bar" and line.startswith("status_command"):
            config_dict["bar"]["status_command"] = line.split(" ", 1)[1].strip()
        elif current_section == "bar" and line.startswith("position"):
            config_dict["bar"]["position"] = line.split(" ", 1)[1].strip()
        elif current_section == "bar" and line.startswith("tray_padding"):
            config_dict["bar"]["tray_padding"] = line.split(" ", 1)[1].strip()
        elif current_section == "bar" and line.startswith("strip_workspace_numbers"):
            config_dict["bar"]["strip_workspace_numbers"] = line.split(" ", 1)[1].strip()
        elif current_section == "bar" and line.startswith("colors {"):
            current_section = "colors"
        elif current_section == "colors" and line == "}":
            current_section = "bar"
        elif current_section == "colors":
            key, value = line.split(" ", 1)
            config_dict["bar"]["colors"][key.strip()] = value.strip()
        elif line == "}":
            current_section = None

    with open(json_file, 'w') as file:
        json.dump(config_dict, file, indent=4)

# Use the function
i3_config_to_json('config', 'output.json')

