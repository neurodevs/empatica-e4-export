import os
import time
import argparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from ChromeWithPrefs import ChromeWithPrefs

def main(email, password, download_dir, driver_path, should_quit_at_end):
    print('Starting the script...')

    sleep_time_sec = 1
    should_quit_at_end = False
    download_dir = os.path.expanduser(download_dir)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    prefs = {
        "download.default_directory": download_dir,
    }

    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("debuggerAddress", "localhost:9222")

    service = Service(driver_path)

    driver = ChromeWithPrefs(service=service, options=options)
    driver.implicitly_wait(60)

    # Step 1: Go to the login page
    driver.get('https://e4.empatica.com/connect/login.php')
    print('Opened login page...')

    # Step 2: Enter email and password
    email_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')

    email_input.send_keys(email)
    password_input.send_keys(password)

    # Step 3: Click the login button
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    print('Logged in successfully...')

    # Step 4: Click the Sessions button
    time.sleep(sleep_time_sec)
    sessions_link = driver.find_element(By.LINK_TEXT, 'Sessions')
    sessions_link.click()
    print('Navigated to Sessions...')

    # Step 5: Click the View All Sessions button
    time.sleep(sleep_time_sec)
    view_all_sessions_button = driver.find_element(By.XPATH, '//button[contains(text(), "View All Sessions")]')
    view_all_sessions_button.click()
    print('Clicked View All Sessions...')

    # Step 6: Click each Download button
    time.sleep(sleep_time_sec)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    buttons = soup.find_all('a', id='fileDownloadCustomRichExperience')
    print('Found', len(buttons), 'buttons...')

    for button in buttons:
        url = button['href']

        try:
            element = driver.find_element(By.XPATH, f'//a[@href="{url}"]')
            element.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error clicking {url}: {e}")

    if should_quit_at_end:
        print('Quitting the browser...')
        driver.quit()
    
    print('Script finished.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate Empatica E4 data export.")

    parser.add_argument('--email', type=str, help='Your email for logging in')
    parser.add_argument('--password', type=str, help='Your password for logging in')
    parser.add_argument('--download_dir', type=str, default='~/Downloads', help='Directory to save downloads')
    parser.add_argument('--sleep_sec', type=int, default=1, help='Sleep time in seconds after each click (default: 1s)')

    parser.add_argument('--driver_path', type=str, default='/usr/local/bin/chromedriver', 
                        help='Path to ChromeDriver (default: /usr/local/bin/chromedriver)')
    
    parser.add_argument('--should_quit_at_end', action='store_true', default=False,
                        help='Flag to quit the browser at the end (default: False)')

    args = parser.parse_args()

    main(args.email, args.password, args.download_dir, args.driver_path, args.should_quit_at_end)
