## FDroid Fetcher

**FDroid-Fetcher** is a mini-tool developed by Python for downloading and cloning open-source Android applications hosted in
the F-Droid repository. The tool will thus be useful to developers, researchers, or anyone else needing to access 
sources of Android apps in bulk for analysis.


### Prerequisites

Before installing **FDroid-Fetcher**, ensure you have the following installed:

- Python 3.6 or later
- Git

### Clone the Repository

```bash
git clone https://github.com/tebmed/parse-pm.git
cd fdroid-fetcher
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Config
Edit the config/settings.properties file depending on your need (you can let him as it is).
 - **number_of_apps**: The number of apps you want to download.
 - **index_url**: URL of the F-Droid application index (f-droid metadata).
 - **base_dir**: This generated directory will contain all the cloned repositories.
 - **csv_file**: This file reports information about the clones apps.

### Run

```bash
python3 src/main.py
```

### Results
  - Consult the logs to know how many apps the script was able to clone regarding the planned number of apps.
  - Consult the **fdroid-apps** directory to see the downloaded apps.
  - Open the file **fdroid_apps_data.csv** to view information about the downloaded apps.


