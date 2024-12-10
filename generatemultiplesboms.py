import subprocess
import os

# Base directories
sbom_tool_path = r'D:\SBOMtool\sbom-tool.exe'
base_sbom_directory = r'D:\SBOMtool\sbom1'
repos_directory = r'D:\SBOMtool\repos'

# Create SBOMs for each repo in the repos_directory
for repo_name in os.listdir(repos_directory):
    # Construct the full path to the repo directory
    repo_path = os.path.join(repos_directory, repo_name)

    # Check if it's a directory
    if os.path.isdir(repo_path):
        # Construct a unique SBOM output directory for this repo
        sbom_output_dir = os.path.join(base_sbom_directory, f"{repo_name}-sbom")

        # Ensure the SBOM output directory exists
        if not os.path.exists(sbom_output_dir):
            os.makedirs(sbom_output_dir)

        # Construct the SBOM generation command
        command = [
            sbom_tool_path, 'generate',
            '-b', sbom_output_dir,  # The unique directory for this repo's SBOM
            '-bc', repo_path,       # The path to the actual source code
            '-ps', repo_name,       # The project name, here using the repo_name
            '-pn', 'aaa',           # You might want to customize the project name ('aaa')
            '-pv', '1.00'           # And the project version ('1.00')
        ]

        # Execute the command
        print(f"Generating SBOM for {repo_name} in {sbom_output_dir}...")
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if SBOM was generated successfully
        if result.returncode == 0:
            print(f"SBOM generated successfully for {repo_name} in {sbom_output_dir}")
        else:
            print(f"Failed to generate SBOM for {repo_name}. Error: {result.stderr}")

print("SBOM generation completed for all repositories.")
