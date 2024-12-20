import os
import pandas as pd
import requests
from jobspy import scrape_jobs

# File name for CSV
csv_filename = "jobs_data.csv"
new_csv_filename = "new_jobs_data.csv"  # Temporary file for new data

def main():
    # Proxy setup
    proxy = "socks5://8.211.42.167:1080"  # Example proxy (will intentionally fail for testing)

    # Test the proxy with a simple request to LinkedIn (or any site)
    try:
        print(f"Attempting to scrape jobs using proxy: {proxy}")
        response = requests.get('https://www.google.com', proxies={'http': proxy, 'https': proxy}, timeout=5)
        response.raise_for_status()  # Raise an error if the proxy does not work
        print(f"Proxy is working: {proxy}")
        
        # If the proxy works, scrape jobs with the proxy
        jobs = scrape_jobs(
            site_name=["linkedin"],
            location="Ireland",
            search_term="Marketing Analyst",
            results_wanted=100,
            proxy=proxy
        )
        print(f"Successfully scraped jobs using proxy: {proxy}")
    
    except requests.exceptions.RequestException as e:
        print(f"Proxy error: {e}. Falling back to direct connection...")
        
        # If proxy fails, scrape without the proxy
        jobs = scrape_jobs(
            site_name=["linkedin"],
            location="Ireland",
            search_term="Marketing Analyst",
            results_wanted=100
        )
        print("Successfully scraped jobs without using a proxy.")

    # Ensure 'date_posted' is in datetime format, with invalid values turned into NaT
    jobs['date_posted'] = pd.to_datetime(jobs['date_posted'], errors='coerce')

    # Define the columns to save
    columns = ['id', 'site', 'job_url', 'title', 'company', 'location', 'date_posted', 'company_url']
    new_data = jobs[columns]

    # Save the new data to a temporary CSV file for debugging
    new_data.to_csv(new_csv_filename, index=False)
    print(f"New jobs saved temporarily in {new_csv_filename}")

    # Check if the main CSV already exists
    if os.path.exists(csv_filename):
        # Load the existing data from the CSV
        existing_data = pd.read_csv(csv_filename)
        
        # Ensure 'id' columns are treated as strings for accurate comparison
        existing_data['id'] = existing_data['id'].astype(str)
        new_data['id'] = new_data['id'].astype(str)

        # Convert 'date_posted' columns to datetime, handling errors as 'NaT'
        existing_data['date_posted'] = pd.to_datetime(existing_data['date_posted'], errors='coerce')

        # Drop rows with invalid or missing 'date_posted' values
        existing_data = existing_data.dropna(subset=['date_posted'])

        # Check the latest existing date
        latest_existing_date = existing_data['date_posted'].max()

        print(f"Latest date in existing data: {latest_existing_date}")

        # Check if any new jobs are duplicates (based on 'id')
        new_jobs = new_data[~new_data['id'].isin(existing_data['id'])]

        print(f"New jobs after removing duplicates: {len(new_jobs)}")
        print(f"New jobs found: {new_jobs}")

        # If there are any new jobs, update the CSV
        if len(new_jobs) > 0:
            # Concatenate new jobs with existing data, removing duplicates
            updated_data = pd.concat([existing_data, new_jobs]).drop_duplicates(subset=['id'])
            updated_data.to_csv(csv_filename, index=False)
            print(f"CSV updated. {len(new_jobs)} new jobs added.")
        else:
            print(f"Out of the {len(new_data)} jobs found, no new jobs were added due to duplicates.")
    else:
        # If no existing CSV, save new data as the initial file
        new_data.to_csv(csv_filename, index=False)
        print(f"CSV created. {len(new_data)} new jobs saved.")

if __name__ == "__main__":
    main()
