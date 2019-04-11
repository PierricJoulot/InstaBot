from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

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
		time.sleep(2)
		login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		login_button.click()
		time.sleep(2)
		username_elem = driver.find_element_by_xpath("//input[@name='username']")
		username_elem.clear()
		username_elem.send_keys(self.username)
		password_elem = driver.find_element_by_xpath("//input[@name='password']")
		password_elem.clear()
		password_elem.send_keys(self.password)
		password_elem.send_keys(Keys.RETURN)
		time.sleep(2)

	def like_photo(self, hashtag):
		count = 0
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
		time.sleep(2)
		for i in range(1, 3):
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(2)
		hrefs = driver.find_elements_by_tag_name('a')
		pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
		# pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        
		for pic_href in pic_hrefs:
			driver.get(pic_href)
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			try:
				driver.find_element_by_xpath("//button[@class='dCJp8 afkep _0mzm-']/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']").click()
				count += 1
				time.sleep(20)
			except Exception as e:
				time.sleep(1)
		print(str(count) + ' ' + hashtag + '\'s photos liked!')
    
                

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
