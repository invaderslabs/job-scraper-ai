# Job Scraper with Proxy Support

## Project Overview

This project is a Python-based job scraper that retrieves job postings from LinkedIn and other job boards using SOCKS5 proxies. The tool offers robust duplicate handling, dynamic proxy switching, and detailed logging for analytics.

## Features

- Scrape job postings from LinkedIn.
- Support for SOCKS5 proxy connections.
- Dynamic proxy loading from a file.
- Duplicate job handling to avoid redundant data.
- Logs to track scraping statistics (new jobs, duplicates, etc.).
- CSV file storage for scraped data.
- Compatibility with Python 3.8+.

## Installation

Follow the steps below to set up and run the project:

### Prerequisites

1. **Python 3.8+**: Make sure Python is installed on your system. You can download Python from [here](https://www.python.org/downloads/).
2. **Pip**: Ensure you have pip installed for managing Python packages.
3. **Virtual Environment (optional)**: It’s recommended to use a virtual environment to manage dependencies.

### Steps

1. **Clone the repository**:

    ```bash
    git clone https://github.com/invaderslabs/job-scraper-ai.git
    cd job-scraper-ai
    ```

2. **Create and activate a virtual environment (optional)**:

    On macOS/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    On Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the proxies**:

    - Create a file named `socks` in the `content/` directory.
    - Add one proxy per line in the following format:

    ```plaintext
    socks5://username:password@proxy_address:port
    ```

    Replace `username`, `password`, `proxy_address`, and `port` with actual values. If the proxy does not require authentication, omit `username:password@`.

5. **Configure job search parameters in the `main()` function**:

    - Open `job_scraper.py`.
    - Update the following values as needed:

    ```python
    site_name = ["linkedin"]
    location = "Ireland"
    search_term = "Marketing Analyst"
    results_wanted = 100
    ```

6. **Run the script**:

    ```bash
    python3 job_scraper.py
    ```

## Usage

### Log Outputs

The script provides detailed logs during execution, including:

- Proxy being used.
- Number of new jobs scraped.
- Duplicate handling.
- Saving data to CSV.

### CSV Files

Scraped job data is saved to a CSV file in the same directory as the script. Each run appends new data while avoiding duplicates.

### Debugging

A temporary CSV file containing all new jobs is created for debugging purposes. Logs include relevant information to identify issues or analyze data.

## Roadmap

### Current Features (v1.0.0)

- Job scraping from LinkedIn with SOCKS5 proxy support.
- Save job data to CSV with duplicate handling.
- Dynamic proxy loading from a file.

### Planned Features

#### v1.1.0 (Expected Q1 2024)

- Improved logging for requests and statistics tracking.
- Retry logic for failed requests.
- Additional job board integrations (e.g., Indeed, Glassdoor).

#### v1.2.0 (Expected Q3 2024)

- Automated notifications for new job postings.
- Data mining using Groq API.
- Integration of LLaMA for advanced job description analysis.

#### v2.0.0 (Expected Q4 2025)

- Web-based interface for configuration and data visualization.
- Machine learning for job relevance scoring and filtering.
- Multilingual support for job scraping and parsing.
- Cloud-based deployment for scaling.
- Integration with applicant tracking systems (ATS).

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes. Ensure that your code is well-documented and includes tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
