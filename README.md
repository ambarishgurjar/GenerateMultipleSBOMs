# SBOM Tool Tutorial

## Introduction
The SBOM Tool is a highly scalable and enterprise-ready tool for creating SPDX 2.2-compatible SBOMs (Software Bill of Materials) for various artifacts. This tutorial demonstrates how to use the SBOM Tool along with custom Python scripts to automate certain tasks. While the SBOM Tool itself is developed by Microsoft, this repository focuses on teaching you how to integrate it into your workflows.

---

## Table of Contents

- [Introduction](#introduction)
- [Download and Installation](#download-and-installation)
- [Using the SBOM Tool](#using-the-sbom-tool)
  - [Batch SBOM Generation](#batch-sbom-generation)
  - [Downloading Multiple Repositories](#downloading-multiple-repositories)
- [Acknowledgments](#acknowledgments)
- [Telemetry](#telemetry)
- [Contributing](#contributing)
- [Security](#security)
- [Trademarks](#trademarks)

---

## Download and Installation

### Executables for Windows, Linux, macOS
Executables and SBOM files for the tool are available on the [GitHub Releases page](https://github.com/microsoft/sbom-tool/releases). You can download binaries manually or use the following commands to get the latest version for your platform:

#### Package Managers

**WinGet**  
`winget install Microsoft.SbomTool`

**Homebrew**  
`brew install sbom-tool`

#### Manual Download

**Windows (PowerShell)**  
```powershell
Invoke-WebRequest -Uri "https://github.com/microsoft/sbom-tool/releases/latest/download/sbom-tool-win-x64.exe" -OutFile "sbom-tool.exe"
```

**Linux (curl)**  
```bash
curl -Lo sbom-tool https://github.com/microsoft/sbom-tool/releases/latest/download/sbom-tool-linux-x64
chmod +x sbom-tool
```

**macOS (curl)**  
```bash
curl -Lo sbom-tool https://github.com/microsoft/sbom-tool/releases/latest/download/sbom-tool-osx-x64
chmod +x sbom-tool
```

#### Building SBOM Tool as a Docker Image

Clone this repository and build the Docker image:

```bash
git clone https://github.com/microsoft/sbom-tool
cd sbom-tool
docker build . -t ms_sbom_tool
```

You can then use the tool by mounting directories to be scanned using Docker bind mounts.

---

## Using the SBOM Tool

This repository provides Python scripts to extend the functionality of the SBOM Tool. Below is an overview of how to use them:

### Batch SBOM Generation
The `generatemultiplesboms.py` script generates SBOMs for multiple repositories. Place your repositories in a specified folder, update the script's configuration, and run the script to create SBOMs for all repositories automatically.

Steps:
1. Clone or download this repository.
2. Place your repositories in the `repos` folder (or update the folder path in the script).
3. Run the script:
   ```bash
   python generatemultiplesboms.py
   ```
4. SBOMs will be generated in the configured output directory.

### Downloading Multiple Repositories
The `downloadfiles.py` script automates the process of downloading multiple repositories listed in an Excel file. Ensure your Excel file (e.g., `todownload.xlsx`) contains the repository URLs in the first column.

Steps:
1. Update the `downloadfiles.py` script to point to your Excel file.
2. Run the script:
   ```bash
   python downloadfiles.py
   ```
3. The repositories will be cloned into the configured folder.

---

## Acknowledgments
This tutorial builds on the SBOM Tool developed by Microsoft. For more information, visit the [official SBOM Tool repository](https://github.com/microsoft/sbom-tool). We also ackowledge the use of generative intelligence in assisting with the materials of this page, however the materials have been verified and edited by humans before commiting on github.

---

## Telemetry
The SBOM Tool collects anonymous usage data to improve the product. For details, refer to the official privacy documentation.

---

## Contributing
Contributions are welcome! Please follow the [contribution guidelines](https://github.com/microsoft/sbom-tool/blob/main/CONTRIBUTING.md).

---

## Security
If you discover a security vulnerability, please report it as per the [security guidelines](https://github.com/microsoft/sbom-tool/blob/main/SECURITY.md).

---

## Trademarks
Microsoft is registered trademarks of Microsoft Corporation.

---
Enjoy using this tutorial and feel free to share your feedback or create a pull request to enhance the project.

