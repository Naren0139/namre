from selenium import webdriver
import time
# Set the path to your ChromeDriver executable
chrome_driver_path = "C:\\Users\\naren\\mynew\\chromedriver-win64\\chromedriver.exe"
time.sleep(5)
# Initialize the WebDriver with the specified path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
time.sleep(5)
# Visit Amazon
driver.get("https://www.amazon.com/")
time.sleep(5)
time.sleep(5)
# Take a screenshot
driver.save_screenshot("amazon_screenshot.png")
time.sleep(5)
# Close the browser
time.sleep(5)
driver.quit()
