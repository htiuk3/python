import time
from selenium import webdriver

videoFileName = "list.txt"
btnPlaySelector = '#movie_player > div.ytp-cued-thumbnail-overlay > button'

videoFile = open(videoFileName)
listVideo = videoFile.readlines()

NUMBER_OF_TAB = 2
NUMBER_OF_VIDEOS = len(listVideo)
LOOP_TIME = 5
videoIndex = 0
tabIndex = 0
tabCount = 1
viewCount = 0
viewCountFileName = "viewCount.txt"

# open browser
browser = webdriver.Chrome()

#open url 1st = tabIndex = 0
browser.get(listVideo[videoIndex])

# click play
time.sleep(2)
playBtn = browser.find_element_by_css_selector(btnPlaySelector)
playBtn.click()

while True:
    videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEOS
    tabIndex = (tabIndex + 1) % NUMBER_OF_TAB
    
    if tabCount < NUMBER_OF_TAB:
        tabCount = tabCount + 1
        browser.execute_script("window.open('" + listVideo[videoIndex].strip() + "')")
    else:
        browser.switch_to.window(browser.window_handles[tabIndex])
        time.sleep(1)
        browser.get(listVideo[videoIndex])
        
    viewCount = viewCount + 1
    saveFile = open(viewCountFileName, "w")
    saveFile.write(str(viewCount) + ' ')
    saveFile.close()
    
    time.sleep(LOOP_TIME)