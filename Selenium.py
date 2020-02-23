from selenium import webdriver
import time
import io
import xlwt 
from xlwt import Workbook 

path_to_chromedriver = r"C:\Users\Peter Stirpe\Desktop\chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

browser.get("https://soundcloud.com/peter_stirpe/likes")




last_height = browser.execute_script("return document.body.scrollHeight")
# counter = 0


while True:

    # Scroll down to the bottom.
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load the page.
    time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
    new_height = browser.execute_script("return document.body.scrollHeight")

    if new_height == last_height:

        break
    # if counter > 15:
    #     break

    # counter = counter + 1
    last_height = new_height


song = browser.find_elements_by_xpath('//div[@class="soundTitle__usernameTitleContainer"]') 


songs=[]

num_items = len(song)
for i in range(num_items):
    songs.append(song[i].text.replace('\n',' : '))

#####     Print to a txt file

# with io.open("Rand.txt", "w", encoding="utf-8") as f:
#     for i in range(len(songs)):
#         f.write(songs[i])
#         f.write('\n')
        

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
    
wb.save('Soundcloud Likes.xls') 



browser.close()
