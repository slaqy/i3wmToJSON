import json

def generate_readme(config):
    readme_content = f"""
# {config['project_name']}

## Description
{config['description']}

## Installation
{config['installation']}

## Usage
{config['usage']}

## License
{config['license_info']}

## Contributors
{config['contributors']}

## Acknowledgments
{config['acknowledgments']}
    """
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content.strip())

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    
    generate_readme(config)

    print("README.md file generated successfully.")

