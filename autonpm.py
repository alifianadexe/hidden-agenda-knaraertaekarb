import os
import json
import uuid
import randomname
from lorem_text import lorem

def create_folder(folder_name):
    try:
        # Create folder
        os.makedirs(folder_name, exist_ok=False)
        print(f"Folder '{folder_name}' created successfully.")
    except:
        print("Error Create Folder")

def create_file_package(file_name, code_snippet, project_name):
    try:
        # Replace variable in code snippet
        code_snippet_json = json.loads(code_snippet)
        code_snippet_json["name"] = project_name
        updated_code_snippet = json.dumps(code_snippet_json, indent=2)

        # Create file
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write(updated_code_snippet)
        print(f"File '{file_name}' created successfully in '{folder_name}' folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_file(file_name, code_snippet):
    try:
        # Create file
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write(code_snippet)
        print(f"File '{file_name}' created successfully in '{folder_name}' folder.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage


package_code = """\
{
  "name": "test-empty-project",
  "version": "1.2.1",
  "license": "MIT",
  "homepage": "https://github.com/dropout7",
  "type": "module",
  "repository": "https://github.com/nihuman",
  "workspaces": [
    "packages/*",
    "e2e/*"
  ]
}
"""

readme_init = """\
---
Purpose Life is At Door function
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
"""

app_init = "console.log('" + lorem.sentence() + "');"

file_package = "package.json"
file_app = "app.js"
file_readme = "README.md"

for i in range(5):
 
    folder_name = "MyFolder-" + str(uuid.uuid4().hex)[:8]
 
    project_name = randomname.get_name() + "-catea"

    create_folder(folder_name)
    create_file_package(file_package, package_code, project_name)
    create_file(file_readme, readme_init)
    create_file(file_app, app_init)

    os.chdir(folder_name)

    os.system("npm i express-adexe")
    os.system("npm publish")

    print(f"Command executed successfully in '{folder_name}' folder.")
    
    print("repeat")
    
