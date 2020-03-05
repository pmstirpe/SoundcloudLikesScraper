from selenium import webdriver
import time
import io
import xlwt 
from xlwt import Workbook 
from datetime import datetime

path_to_chromedriver = r"C:\Users\Peter Stirpe\Desktop\SoundcloudLikesScraper\chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

oldTime = time.perf_counter()

browser.get("https://soundcloud.com/peter_stirpe/likes")
last_height = browser.execute_script("return document.body.scrollHeight")
# counter = 0


while True:

    # Scroll down to the bottom.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load the page.
    time.sleep(1)

        # Calculate new scroll height and compare with last scroll height.
    new_height = browser.execute_script("return document.body.scrollHeight")

    if new_height == last_height:

        break
    last_height = new_height


song = browser.find_elements_by_xpath('//div[@class="soundTitle__usernameTitleContainer"]') 
songs=[]

num_items = len(song)
for i in range(num_items):
    songs.append(song[i].text.replace('\n',' : '))


# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 0, 'ARTIST') 
sheet1.write(0, 1, 'SONG NAME') 
for i in range(num_items):
    pair = songs[i].split(':')
    sheet1.write(i+1,0,pair[0].strip())
    sheet1.write(i+1,1,pair[1].strip())
    
#### Save results to a new csv named based on date    
d = datetime.today()
timestr = time.strftime("%Y%m%d-%H%M%S")
wb.save('SoundcloudLikes~' + timestr + '.xls') 
#wb.save('SoundcloudLikes~' + str(d.month) + '-' + str(d.day) + '-' + str(d.year) + '-' + str(d.timestamp) + '.xls') 
print("TOTAL TIME: " + str(time.perf_counter() - oldTime))


browser.close()
