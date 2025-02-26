import os
import subprocess
import json
import shutil

# Define the repository URL and the local directory where you want to clone it
repo_url = "https://github.com/github/advisory-database.git"
local_repo_dir = "security-advisory-database"
reviewed_folder = os.path.join(local_repo_dir, "advisories/github-reviewed")
destination_directories="linear_advisories"

def clone_or_update_repo(repo_url, local_repo_dir):
    # Check if the local repository directory exists
    if os.path.exists(local_repo_dir):
        print(f"Repository already exists in {local_repo_dir}. Updating...")
        
        # Change to the repository directory
        os.chdir(local_repo_dir)
        
        # Pull the latest changes from the remote repository
        subprocess.run(["git", "pull"])
        
        # Change back to the original directory
        os.chdir("..")
    else:
        print(f"Cloning repository into {local_repo_dir}...")
        
        # Clone the repository
        subprocess.run(["git", "clone", repo_url, local_repo_dir])

def process_database():
    if os.path.exists(local_repo_dir):
        for year,month,files in os.walk(reviewed_folder):
            for file in files:
                if file.endswith(".json"):
                    
                    source_path=os.path.join(year,file)
                    
                    _move_files(file,source_path)

def _move_files(filename,path):   
    
    destination_path = os.path.join(os.getcwd(),destination_directories,filename)
    if os.path.exists(destination_path):
        shutil.copy(path,destination_path)


if __name__=="__main__":
    clone_or_update_repo(repo_url, local_repo_dir)
    process_database()