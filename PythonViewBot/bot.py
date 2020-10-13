import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 60

#youtube link
link = 'https://www.youtube.com/watch?v=TltKqcm998s'

#number of views
views = 10

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
