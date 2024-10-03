### Description
The Bug Bounty Tool is a specialized utility designed to assist security researchers and bug bounty hunters in identifying reflected Cross-Site Scripting (rXSS) vulnerabilities in web applications.

### Key Features:
Single URL Testing: Easily test a specific URL for potential rXSS vulnerabilities.
Batch URL Testing: Input a list of URLs to check for vulnerabilities in bulk, streamlining the assessment process.

### How It Works:
To utilize the tool, simply append the word FUZZ to the parameter you wish to test in the URL. Upon running the tool, it will automatically send requests to the specified URL(s) and analyze the responses to determine whether the input is reflected in the output. If the input is reflected, this may indicate a potential rXSS vulnerability, allowing you to take further action or report the issue

Example : python3 main.py example.com/search?q=FUZZ


### Automate
sed 's/=\([^&]*\)/=FUZZ/' urls.txt > updated_urls.txt
- it will automatically add Fuzz word in the parameter, if you have long list of url's then use this command

## Clone the Repository

- git clone https://github.com/Srinunaik000/Xss_Fuzz.git
- cd Xss_Fuzz


### Install Dependencies
Install the required packages using pip:

- pip install -r requirements.txt

### Set Permissions
chmod +x main.py


### Usage
You can run the tool using the following command:

- python3 main.py --file path/to/your/urls.txt

- Command-Line Arguments
- --file, -f: Path to a file containing URLs (one URL per line).
- --url, -u: Single URL to test for XSS.
- --payloads, -p: Path to a file containing custom XSS payloads.
- --check-headers: Check headers for reflected XSS.
- --show-positive: Only show results where payloads are reflected.


### Example
To test URLs from a file:

python3 main.py --file urls.txt
- To test a single URL:

python3 main.py --url https://example.com

### Contributing
If you would like to contribute to the project, please fork the repository and create a pull request. Make sure to write tests for any new features or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Beautiful Soup for HTML parsing.
Requests for making HTTP requests.
