from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from bs4 import BeautifulSoup
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests #only use this for the others functions,else comment this one this is not required for the final one 

# def simple_scrapping():
#     html_text=requests.get('https://apna.co/jobs/jobs-in-bhubaneswar').text
#     soup=BeautifulSoup(html_text,'lxml')
#     print(html_text)

#     card=soup.find('div', class_="w-full flex-1")
#     card_loc=soup.find('div',class_="flex items-center gap-1")
#     card_salary=soup.find('div',class_="flex items-center gap-[4px]")
#     jobs_tag_information=soup.find('div',{'data-testid':'job-tags-info'})
#     # print(jobs_tag_information)
#     title=card.find('h2',class_="m-0 w-full text-[16px] font-semibold leading-[24px]").text
#     company_name=card.find('div',class_="JobListCardstyles__JobCompany-ffng7u-8 gguURM").text
#     job_loc=card_loc.find('p',class_="m-0 text-sm leading-[20px] text-[#8C8594]").text
#     job_salary=card_salary.find('p',class_="m-0 truncate text-sm leading-[20px] text-[#8C8594]").text
#     # if jobs_tag_information:
#     #     tags=[p.get_text(strip=True)for p in jobs_tag_information.find_all('p')]
#     #     print(tags)
#     # else:
#     #     print("No div tags")
#     tags=[]
#     for p in jobs_tag_information.find_all('p'):
#         text=p.get_text(strip=True)
#         tags.append(text)
#     print("COMPANY NAME:",company_name)
#     print("JOB TITLE:",title)
#     print("JOB LOCATION:",job_loc)
#     print("JOB SALARY:",job_salary)
#     print("JOB TAGS:",tags)

# For Single card # 
def single_card_scrapping():
    html_text=requests.get('https://apna.co/jobs/jobs-in-bhubaneswar').text
    soup=BeautifulSoup(html_text,'lxml')
    card=soup.find('div',{'data-testid':'job-card'})
    card_title=card.find('h2',{'data-testid':'job-title'}).text
    card_company_name=card.find('div',{'data-testid':'company-title'}).text
    card_job_loaction=card.find('p',{'data-testid':'job-location'}).text
    card_job_salary=card.find('p',{'data-testid':'job-salary'}).text
    card_tag_info=soup.find('div',{'data-testid':'job-tags-info'})
    tags=[]
    for p in card_tag_info.find_all('p'):
        text=p.get_text(strip=True)
        tags.append(text)
    print("COMPANY NAME:",card_company_name)
    print("JOB TITLE:",card_title)
    print("JOB LOCATION:",card_job_loaction)
    print("JOB SALARY:",card_job_salary)
    print("JOD TAGS:",tags)

# for dynamic card Scrapping #
def dynamic_card_scrapping():
    html_text=requests.get('https://apna.co/jobs/jobs-in-bhubaneswar').text
    soup=BeautifulSoup(html_text,'lxml')
    card=soup.find_all('div',{'data-testid':'job-card'})
    for index, card in enumerate(card, start=1):
        try:
            card_title = card.find('h2', {'data-testid': 'job-title'}).get_text(strip=True)
            card_company_name = card.find('div', {'data-testid': 'company-title'}).get_text(strip=True)
            card_job_location = card.find('p', {'data-testid': 'job-location'}).get_text(strip=True)
            card_job_salary = card.find('p', {'data-testid': 'job-salary'}).get_text(strip=True)

            card_tag_info = card.find('div', {'data-testid': 'job-tags-info'})
            tags = [p.get_text(strip=True) for p in card_tag_info.find_all('p')] if card_tag_info else []

            print(f"\n=== JOB {index} ===")
            print("COMPANY NAME:", card_company_name)
            print("JOB TITLE:", card_title)
            print("JOB LOCATION:", card_job_location)
            print("JOB SALARY:", card_job_salary)
            print("JOB TAGS:", tags)

        except AttributeError:
            # In case any field is missing for some cards
            print(f"\n=== JOB {index} ===")
            print("Skipped: Some details missing.")


#store the Scrapped data #
def store_scrapped_data():
    html_text=requests.get('https://apna.co/jobs/jobs-in-bhubaneswar').text
    soup=BeautifulSoup(html_text,'lxml')
    cards=soup.find_all('div',{'data-testid':'job-card'})
    all_jobs=[]
    for card in cards:
        try:
            card_title = card.find('h2', {'data-testid': 'job-title'}).get_text(strip=True)
            card_company_name = card.find('div', {'data-testid': 'company-title'}).get_text(strip=True)
            card_job_location = card.find('p', {'data-testid': 'job-location'}).get_text(strip=True)
            card_job_salary = card.find('p', {'data-testid': 'job-salary'}).get_text(strip=True)

            card_tag_info = card.find('div', {'data-testid': 'job-tags-info'})
            tags = [p.get_text(strip=True) for p in card_tag_info.find_all('p')] if card_tag_info else []

            #adding the results to a dictionary
            all_jobs.append({
                'company Name':card_company_name,
                'Job Title':card_title,
                'Job Location':card_job_location,
                'Job Salary':card_job_salary,
                'Job Tags':', '.join(tags) 
            })
        except AttributeError:
            continue

    df =pd.DataFrame(all_jobs)

    df.to_excel('jobs.xlsx',index=False)
    print("Data saved as xlsx")

# get and store the data dynamically #

def webscrape_apna_jobs():
    # --- Setup driver ---
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = "https://apna.co/jobs/jobs-in-bhubaneswar"
    driver.get(url)

    time.sleep(3)

    all_jobs = []

    page_number = 1
    # for i in range(1,6):
    while True:
        print(f"\n📄 Scraping page {page_number}...")
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "lxml")
        cards = soup.find_all("div", {"data-testid": "job-card", "class": "min-h-full cursor-pointer rounded-lg border border-solid border-[#E8E7EA] bg-white p-[12px] shadow-100 md:m-0"})

        print(f"Found {len(cards)} jobs on page {page_number}")

        for card in cards:
            try:
                title = card.find("h2", {"data-testid": "job-title"}).get_text(strip=True)
                company = card.find("div", {"data-testid": "company-title"}).get_text(strip=True)
                location = card.find("p", {"data-testid": "job-location"}).get_text(strip=True)
                salary = card.find("p", {"data-testid": "job-salary"}).get_text(strip=True)
                tag_info = card.find("div", {"data-testid": "job-tags-info"})
                tags = [p.get_text(strip=True) for p in tag_info.find_all("p")] if tag_info else []
                
                all_jobs.append({
                    "Job Title": title,
                    "Company Name": company,
                    "Job Location": location,
                    "Job Salary": salary,
                    "Job Tags": ", ".join(tags)
                })
            except Exception:
                continue

        # --- Go to Next Page ---
        try:
            next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
            # check if button is disabled
            if "disabled" in next_button.get_attribute("class").lower() or not next_button.is_enabled():
                print("Next button is disabled — reached last page.")
                break

            # scroll and click
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", next_button
            )
            time.sleep(1)
            next_button.click()
            time.sleep(4)
            page_number += 1

        except (NoSuchElementException, ElementClickInterceptedException):
            print(" No Next button found — stopping early.")
            break

    # --- Save to Excel ---
    df = pd.DataFrame(all_jobs)
    df.to_excel("jobs.xlsx", index=False)
    print(f"Saved {len(df)} jobs to Excel file 'jobs.xlsx'")

    driver.quit()

if __name__ == "__main__":
    #only called this one as this is the final fucntion which includes all the functionalities the other ones are just for reference and the process of building this final function
    webscrape_apna_jobs() 