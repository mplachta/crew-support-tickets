import os
import shutil
import subprocess

# Clone the repository
subprocess.run(["git", "clone", "https://github.com/crewAIInc/crewAI.git", "knowledge-prep/crewai"])

# Create the destination directory if it doesn't exist
os.makedirs("knowledge/oss-docs", exist_ok=True)

# Copy files from docs folder to oss-docs
source_dir = "knowledge-prep/crewai/docs"
dest_dir = "knowledge/oss-docs"

for item in os.listdir(source_dir):
    s = os.path.join(source_dir, item)
    d = os.path.join(dest_dir, item)
    if os.path.isfile(s):
        shutil.copy2(s, d)
    elif os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)

# Clean up: remove the cloned repository
shutil.rmtree("knowledge-prep/crewai")
