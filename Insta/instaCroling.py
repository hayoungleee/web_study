import requests
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time
import re


def login(id, pw):
    login_section = '/html/body/div[5]/div[2]/div/div/div/div/div[1]/div/form'
    driver.find_element_by_xpath(login_section).click()
    time.sleep(2)

    elem_login = driver.find_element_by_name("username")
    elem_login.clear()
    elem_login.send_keys(id)

    elem_login = driver.find_element_by_name('password')
    elem_login.clear()
    elem_login.send_keys(pw)

    time.sleep(1)

    xpath = "/html/body/div[5]/div[2]/div/div/div/div/div[1]/div/form/div[4]/button"
    driver.find_element_by_xpath(xpath).click()

    time.sleep(4)


keyword = "영등포맛집"
url = "https://www.instagram.com/explore/tags/{}/".format(keyword)
instagram_tags = []

# Firefox : https://github.com/mozilla/geckodriver/releases
# Chrome : https://sites.google.com/a/chromium.org/chromedriver/downloads
# Edge : https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
driver = wd.Chrome("Insta/chromedriver")
driver.get(url) # 리턴은 없지만 , driver한테 url을 던져주는 과정
time.sleep(3)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click() # 첫번째 순서의 게시물 클릭.

time.sleep(1)

login("<인스타 아이디>", "<인스타 비번>") # 게시물 열람시 필요한 로그인과정


xpath = "/html/body/div[1]/section/main/div/div/div/div/button" # 다시 첫번째 과정으로 돌아간다.
driver.find_element_by_xpath(xpath).click()

time.sleep(3)

driver.find_element_by_css_selector('div.v1Nh3.kIKUG._bz0w').click()

time.sleep(1)

for i in range(300):
    time.sleep(1)
    data = driver.find_element_by_css_selector('.C7I1f.X7jCj')

    # C7I1f X7jCj
    tag_raw = data.text
    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
    tag = ''.join(tags).replace("#", " ")  # "#" 제거

    tag_data = tag.split()

    for tag_one in tag_data:
        instagram_tags.append(tag_one)

    print(instagram_tags)
    driver.find_element_by_css_selector(
        'body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow').click()

    time.sleep(3)
driver.close()
