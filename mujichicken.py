# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import datetime
import bs4
import random
import chromedriver_binary
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#Macの場合、次を追加

#現在時刻を出力する関数
def now_time():
   dt_now = datetime.datetime.now()
   return dt_now.strftime('%m/%d %H:%M')+' '
    
#USER INFO
username = 'sp_sb0'
password = 'Y161634y'
#params
tagName = random.choice(['カフェ巡り好きな人と繋がりたい'])
print(tagName)
#いいね数を設定
likedMax = 200

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size('1200', '1000')
# webdriver.Chrome(DRIVER)

#ブラウザに接続
#Windowsの場合：chromedriver.exeの格納先を指定する
#例　r"C:\Users\username\Python\chromedriver.exe"
driver.implicitly_wait(10)
time.sleep(5)
#Macの場合：次の記載とする
 #driver = webdriver.Chrome()

#インスタのURLにアクセス
driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
time.sleep(1)
#メアドと、パスワードを入力
usernames = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
usernames.clear()
usernames.send_keys(username)
time.sleep(1)
driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input").send_key(password)
time.sleep(1)

#ログインボタンを押す
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
time.sleep(3)
print(now_time()+'instagramにログインしました')
time.sleep(1)

#タグ検索
instaurl = 'https://www.instagram.com/explore/tags/'
driver.get(instaurl + tagName)

time.sleep(3)
print(now_time()+'tagで検索を行いました')
time.sleep(1)

#最新の投稿に画面をスクロール
target = driver.find_elements_by_class_name('_9AhH0')[10]
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
print(now_time()+'最新の投稿まで画面を移動しました')
time.sleep(3)

#すでにいいねしたかをチェック
def check_Like():
    html = driver.page_source.encode('utf-8')
    soup = bs4.BeautifulSoup(html, "lxml")
    a = soup.select('span.fr66n')
    return  not '取り消す' in str(a[0])

#最初の投稿にいいねする
try:
    driver.find_elements_by_class_name('_9AhH0')[9].click()
    time.sleep(random.randint(3, 5))
    print(now_time()+'投稿をクリックしました')
    time.sleep(4)

    if check_Like():
        driver.find_element_by_class_name('fr66n').click()
        print(now_time()+'投稿をいいね(1回目)')
        time.sleep(random.randint(3, 5))
    else:
        print(now_time()+'いいね済みです')

except WebDriverException:
    print(now_time()+'エラーが発生しました')

#次へボタンを押して、いいねを繰り返す
for i in range(likedMax-1):
    try:
        driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
        print(now_time()+'次の投稿へ移動しました')
        time.sleep(random.randint(10, 20))

    except WebDriverException:
        print(now_time()+'{}つ目の位置でエラーが発生しました'.format(i+2))
        time.sleep(random.randint(4, 10))

    try:
        if check_Like():
            driver.find_element_by_class_name('fr66n').click()
            print(now_time()+'投稿をいいね({}回目)'.format(i+2))
            time.sleep(random.randint(3, 5))
        else:
            print(now_time()+'いいね済みです')
       
    except WebDriverException:
        print(now_time()+'{}つ目の位置でエラーが発生しました'.format(i+3))

## 処理終了
print(now_time()+'いいね終了')
driver.close()
driver.quit()
