# Medium-Article-Automation

This Python script uses Selenium to scrape article titles, subtitles, and links from the website "https://medium.com/". It saves the scraped data to a CSV file for further analysis.

# Prerequisites
Before running the script, make sure you have the following installed:  

Python (version 3.6 or higher)  

Selenium library  

Chrome web driver  

You can install the Selenium library using pip with the following command:  

Copy code  

pip install selenium  

You also need to download the Chrome web driver from the official Chrome driver website (https://sites.google.com/a/chromium.org/chromedriver/downloads) and specify the path to the executable in the path variable in the script.  


# Usage
Clone the repository or download the script to your local machine.

Install the required dependencies (Selenium).

Update the path variable in the script to the correct path of your Chrome driver executable.

Run the script using a Python interpreter.

Copy code  

python scraper.py  

Wait for the script to load the articles from the Medium website. The script includes a delay of 5 seconds to allow the articles to load.  

Once the script completes, it will save the scraped data to a CSV file named "medium.csv" in the same directory as the script.  


# Output
The script will generate a CSV file named "medium.csv" which will contain the scraped data in a tabular format with columns for article title, subtitle, and link.

# Contributing
If you wish to contribute to this project, feel free to submit a pull request or open an issue with your suggestions or improvements.


# Disclaimer
Please note that web scraping may be against the terms of service of some websites. It's important to review and comply with the website's policies and guidelines before scraping any data. The author of this script is not responsible for any misuse or violation of terms of service by users of this script.

Happy scraping!
