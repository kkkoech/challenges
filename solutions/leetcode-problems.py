from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import time


geckodriver_location = r'geckodriver.exe'

#add browser options, e.g. in this case we want browser to be headless
options = FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--disable-notifications")
options.add_argument("--headless")

driver = webdriver.Firefox(options=options, executable_path=geckodriver_location)
url = "https://leetcode.com/problemset/all/"
driver.get(url)
time.sleep(5)

#click 'pick one' button to get one random question
def get_question():
    driver.find_element_by_xpath('//*[@id="question-app"]/div/div[2]/div[1]/div[2]/span/a').click()
    time.sleep(5)
    question = driver.find_element_by_xpath('//*[@id="question-title"]').text

    #check if question in file, meaning it's already been attempted
    done_file = open('leetcode_done.txt','w+')
    done_questions = [f.strip('\n') for f in done_file.readlines()]
    done_file.close()

    #implement binary search to see if it's among the daone questions?

    #
    if question not in done_questions:
        return f"{question} --> {driver.current_url}"
        done_file = open('leetcode_done.txt', 'a')
        done_file.writelines(f'{str(question)} --> {driver.current_url}' + '\n')
        done_file.close()
        
    else:
        get_question()

print(get_question())
driver.quit()