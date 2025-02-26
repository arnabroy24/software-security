import os
import subprocess
import shutil

# Define the repository URL and local directory
repo_url = "https://github.com/github/advisory-database.git"
local_repo_dir = "security-advisory-database"
reviewed_folder = os.path.join(local_repo_dir, "advisories/github-reviewed")
destination_directories = "linear_advisories"

def clone_or_update_repo(repo_url, local_repo_dir):
    """Clones or updates the GitHub repository."""
    if os.path.exists(local_repo_dir):
        print(f"Repository already exists in {local_repo_dir}. Updating...")
        subprocess.run(["git", "-C", local_repo_dir, "pull"], check=True)
    else:
        print(f"Cloning repository into {local_repo_dir}...")
        subprocess.run(["git", "clone", "--depth", "1", repo_url, local_repo_dir], check=True)

def process_database():
    """Processes JSON files from the GitHub-reviewed advisories."""
    if not os.path.exists(destination_directories):
        os.makedirs(destination_directories)

    if os.path.exists(reviewed_folder):
        for root, _, files in os.walk(reviewed_folder):
            for file in files:
                if file.endswith(".json"):
                    source_path = os.path.join(root, file)
                    _move_files(file, source_path)

def _move_files(filename, path):
    """Moves JSON files to the destination directory."""
    destination_path = os.path.join(destination_directories, filename)
    shutil.copy(path, destination_path)  # Always copy the file
    print(f"Copied {filename} to {destination_path}")

if __name__ == "__main__":
    clone_or_update_repo(repo_url, local_repo_dir)
    process_database()
