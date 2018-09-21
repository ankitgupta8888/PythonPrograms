# The standard library modules

# The BeautifulSoup module
from bs4 import BeautifulSoup

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Drivers\\chromedriver.exe") # if you want to use chrome, replace Firefox() with Chrome()
#driver.get("http://www.example.com") # load the web page

# for websites that need you to login to access the information
#elem = driver.find_element_by_id("email") # Find the email input field of the login form
#elem.send_keys("user@example.com") # Send the users email
#elem = driver.find_element_by_id("pwd") # Find the password field of the login form
#elem.send_keys("userpwd") # send the users password
#elem.send_keys(Keys.RETURN) # press the enter key

driver.get("http://fortune.com/fortune500/list/") # load the page that has the video


#WebDriverWait(driver).until(EC.visibility_of_element_located((By.ID, "data")))
readyStateComplete = True
i = 1
while readyStateComplete:
#    print(i)
#    i+=1
    driver.execute_script("window.scrollBy(0, 400000000)")
    print("offset",driver.execute_script("return window.length"))
    if driver.execute_script("return document.readyState") == "complete":
        readyStateComplete = False


# waits till the element with the specific id appears
src = driver.page_source # gets the html source of the page
driver.close()

parser = BeautifulSoup(src,"lxml") # initialize the parser and parse the source "src"
list_of_attributes = {"class" : "column small-5 company-title"} # A list of attributes that you want to check in a tag
tag = parser.findAll('span',attrs=list_of_attributes) # Get the video tag from the source
print("ankit test")
print(tag)

print("ankit end")
#n = 0 # Specify the index of video element in the web page
#url = tag[n]['tr'] # get the src attribute of the video
#wget.download(url,out="path/to/output/file") # download the video

 # closes the driver


