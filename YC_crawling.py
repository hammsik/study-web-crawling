from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome('C:\WooooooooooW\etc\chromedriver_win32\chromedriver') 
driver.get("https://www.youtube.com/results?search_query=s23") 
html = driver.find_element(By.TAG_NAME, "html")

def loadAllContents(): 
    prev_contents_len = 0 
    while True: 
        time.sleep(2) 
        contents = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer') 
        current_contents_len = len(contents) 
        print("현재 로드된 영상 개수:", current_contents_len) 
        if prev_contents_len == current_contents_len or current_contents_len > 100: 
            break 
        prev_contents_len = len(contents) 
        html.send_keys(Keys.END) 
    return contents

def pickVideo():
    cnt = 0
    for c in contents:
        time.sleep(1)

        # 유튜브프리미엄 광고 팝업 닫기
        try:    
            html.find_element(By.XPATH, '//*[@id="dismiss-button"]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
        except:
            pass

        # 동영상 클릭
        toClick = c.find_element(By.TAG_NAME, "img")
        action.move_to_element(toClick).click().perform()

        time.sleep(2)
        html.send_keys(Keys.END)
        time.sleep(0.3)
        html.send_keys(Keys.END)

        time.sleep(1)
        print("영상제목:", driver.find_element(By.XPATH, '//*[@id="title"]/h1/yt-formatted-string').text)
        comments = driver.find_element(By.TAG_NAME, "ytd-comments")

        try:
            header = comments.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[2]')
            print("댓글 수:", header.text)
        except:
            print("댓글 없음")
        print()

        driver.back()
        cnt += 1

#원하는 영상으로 스크롤 후 클릭하기 위한 ActionChains 객체 생성
action = ActionChains(driver)
contents = loadAllContents()
print("최종 로드된 영상 개수:", len(contents))
pickVideo()
    #mmmmmmmmmmmmmmmm
    # if len(header) == 0: 
    #     driver.back() 
    #     continue 
    #     # 스크롤 끝까지 내리기 
    #     prev_comment_len = 0 
    #     while True: 
    #         time.sleep(3) 
    #         comments = new_contents.find_elements_by_xpath('//ytd-item-section-renderer[@id="sections"]/div[@id="contents"]/ytd-comment-thread-renderer') 
    #         if prev_comment_len == len(comments): 
    #             break 
    #         prev_comment_len = len(comments) 
    #         html.send_keys(Keys.END)