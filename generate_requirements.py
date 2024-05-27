import os
import re

def find_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return re.findall(r'^\s*import\s+(\w+)|^\s*from\s+(\w+)', content, re.MULTILINE)

def main():
    project_dir = '.'  # Change to your project directory
    imports = set()
    
    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                imports.update(find_imports(file_path))
    
    imports = {imp[0] or imp[1] for imp in imports}
    
    with open('requirements.txt', 'w') as req_file:
        for imp in sorted(imports):
            req_file.write(f"{imp}\n")

if __name__ == "__main__":
    main()

