from selenium import webdriver 
from selenium.webdriver import ActionChains
import time 

driver = webdriver.Chrome('C:\WooooooooooW\etc\chromedriver_win32\chromedriver') 
driver.get("https://www.youtube.com/feed/trending") 

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
html = driver.find_element(By.TAG_NAME, "html")
prev_contents_len = 0 
# while True: 
#     time.sleep(3) 
#     # contents = driver.find_elements(By.CSS_SELECTOR, '#items > ytd-video-renderer')
#     contents = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')

#     # contents = driver.find_elements(By.XPATH, "//html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer[1]/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer")
#     current_contents_len = len(contents)
#     print(current_contents_len)
#     if prev_contents_len == current_contents_len: 
#         break 
#     prev_contents_len = len(contents) 
#     html.send_keys(Keys.END)

#ActionChains생성
action = ActionChains(driver)
#리스트 가져오기
contents = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
#move_to_element를 이용하여 이동
time.sleep(2)
print(len(contents))

cnt = 0
for c in contents:
    time.sleep(2)
    toClick = c.find_element(By.TAG_NAME, "img")
    action.move_to_element(toClick).click().perform()
    # 동영상 클릭
    time.sleep(2)
    html.send_keys(Keys.END)
    time.sleep(0.5)
    html.send_keys(Keys.END)
    print(driver.find_element(By.XPATH, '//*[@id="title"]/h1/yt-formatted-string').text)
    comments = driver.find_element(By.TAG_NAME, "ytd-comments")
    time.sleep(2) 
    try:
        header = comments.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[2]')
        print("댓글 수:", header.text)
    except:
        print("댓글 없음")
    print()

    driver.back()
    cnt += 1
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