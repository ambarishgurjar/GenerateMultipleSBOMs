import pandas as pd
import subprocess
import os

# Excel file name
excel_file_name = 'todownload.xlsx'

# The folder where you want to save the repositories, here we name it 'repos'
destination_folder = 'repos'

# Create the destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

def download_github_repo(git_url, destination):
    """
    Clones a GitHub repository into a specified folder.
    """
    # Ensure the .git extension is present in the URL
    if not git_url.endswith('.git'):
        git_url += '.git'
    
    # Extract the repo name for the folder
    repo_name = git_url.split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]
    
    # Construct the destination path
    repo_path = os.path.join(destination, repo_name)
    
    # Clone the repository if the directory does not already exist
    if not os.path.exists(repo_path):
        print(f"Cloning {git_url} into {repo_path}")
        subprocess.run(['git', 'clone', git_url, repo_path])
    else:
        print(f"Directory {repo_path} already exists, skipping clone.")

# Load the Excel file with openpyxl
df = pd.read_excel(excel_file_name, engine='openpyxl')

# Assuming the first column contains the GitHub links
github_links = df.iloc[:, 0]

# Download all the repositories
for link in github_links:
    download_github_repo(link, destination_folder)