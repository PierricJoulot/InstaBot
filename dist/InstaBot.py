from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

delay = 5

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Safari()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(delay)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        try:
            login_button.click()
        except Exception as e:
            IGB.closeBrowser()
        time.sleep(delay)
        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(delay)

    def like_photo(self, hashtag):
        print("")
        count = 0
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(delay)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(delay)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        max_pic = len(hrefs)
        
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']").click()
                count += 1
                time.sleep(20)
                print("\r", hashtag, ": " , "|" , int(30*count/max_pic)*"█" , (30 - int(30*count/max_pic))*" " , "|" , " " , str(int(100*count/max_pic)) , "%", end="", sep="")
            except Exception as e:
                time.sleep(delay-1)
                count += 1
                print("\r", hashtag, ": " , "|" , int(30*count/max_pic)*"█" , (30 - int(30*count/max_pic))*" " , "|" , " " , str(int(100*count/max_pic)) , "%", end="", sep="")
        

x = input("Username: ")
y = input("Password: ")

hashtags_str = input("Hashtags (with spaces in between each one): ")
hashtags_array = []

word = ''

for i in hashtags_str + ' ':
        if i == ' ':
            hashtags_array += [word]
            word = ''
        else:
            word += i
        
if len(hashtags_array) > 20:
    print('Calm your tits! Less than 20 hashtags at a time!')

IGB = InstagramBot(x,y)

IGB.login()

for i in hashtags_array:
    IGB.like_photo(i)

IGB.closeBrowser()