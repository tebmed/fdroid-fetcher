import requests
import subprocess
import os
import csv
from datetime import datetime
import configparser

def get_fdroid_data(index_url):
    response = requests.get(index_url)
    data = response.json()
    return data

def setup_directory(base_dir):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

def extract_source_urls(data, number_of_apps):
    app_data = []
    for app in data['apps'][:number_of_apps]:
        if 'sourceCode' in app and app['sourceCode']:
            last_updated = datetime.fromtimestamp(app.get('lastUpdated', 0) / 1000).strftime('%Y-%m-%d')
            app_data.append({
                'sourceCode': app['sourceCode'],
                'category': ', '.join(app.get('categories', [])),
                'lastUpdated': last_updated
            })
        else:
            print(f"Source code not available for {app.get('name', 'Unknown Application')}")
    return app_data

def clone_repositories(app_data, base_dir):
    successful_clones = []
    for app in app_data:
        repo_name = app['sourceCode'].split('/')[-1].split('.git')[0]
        full_path = os.path.join(base_dir, repo_name)
        try:
            subprocess.run(['git', 'clone', app['sourceCode'], full_path], check=True)
            successful_clones.append(app)
            print(f"Successfully cloned {repo_name} into {full_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to clone repository ({repo_name}): {e}")
    return successful_clones

def write_to_csv(app_data, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['sourceCode', 'category', 'lastUpdated'])
        writer.writeheader()
        for app in app_data:
            writer.writerow(app)

def main():
    config = configparser.ConfigParser()
    config.read('../config/settings.properties')

    number_of_apps = config.getint('Settings', 'number_of_apps')
    index_url = config.get('Settings', 'index_url')
    base_dir = config.get('Settings', 'base_dir')
    csv_file = config.get('Settings', 'csv_file')

    data = get_fdroid_data(index_url)
    setup_directory(base_dir)
    app_data = extract_source_urls(data, number_of_apps)
    successful_app_data = clone_repositories(app_data, base_dir)
    write_to_csv(successful_app_data, csv_file)

    # Summary of the execution
    print(f"Planned to clone {number_of_apps} applications.")
    print(f"Successfully cloned {len(successful_app_data)} applications.")
    print("Cloning and CSV writing processes were successful for cloned projects.")

if __name__ == "__main__":
    main()