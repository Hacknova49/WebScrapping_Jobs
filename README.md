# WebScrapping_Jobs 

A Python-based web scraping project that extracts job listings from Apna.co, focusing on positions in Bhubaneswar. The scraper collects details such as job titles, company names, locations, salaries, and tags, and stores them in an Excel file for data analysis and research purposes.

## 🚀 Features

* Dynamic Scraping: Utilizes Selenium and BeautifulSoup to handle dynamic content.

* Excel Output: Saves scraped data into a structured Excel file.

* Pagination Handling: Automatically navigates through multiple pages to gather comprehensive data.

* Tag Extraction: Collects job tags like "Full Time," "Work from Office," etc.

## 🛠️ Technologies Used

* Python 3.x

* Selenium

* eautifulSoup

* Pandas

* WebDriver Manager

* Requests

## 📦 Installation

Clone the repository:
```
git clone https://github.com/Hacknova49/WebScrapping_Jobs.git
cd WebScrapping_Jobs
```

Install dependencies:
```
pip install -r requirements.txt
```

Note: requirements.txt should list all necessary Python packages.

## 🧪 Usage

Run the main script to start the scraping process:
```
python main.py
```

### This will initiate the scraper, which will:

* Open the Apna.co job listings page for Bhubaneswar.

* Navigate through available pages.

* Extract job details.

* Save the data into jobs.xlsx.

## 📊 Data Output

### The scraper outputs an Excel file (jobs.xlsx) with the following columns:

* Company Name: The hiring company's name.

* Job Title: The title of the job position.

* Job Location: Location of the job.

* Job Salary: Salary offered for the position.

* Job Tags: Tags associated with the job (e.g., "Full Time").

## 🔄 Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your proposed changes.

## 🧾 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
