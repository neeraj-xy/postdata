from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.options import Options
import time
import os
from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField
from wtforms import validators, ValidationError

app = Flask(__name__)
app.secret_key = '79138462'

baseUrl1 = "https://zerodha.com/open-account?c=ZMPTJT"
baseUrl2 = "https://www.5paisa.com/open-demat-account/?referralcode=56199111"
baseUrl3 = "https://upstox.com/open-account/?f=AX6O"

@app.route("/success", methods = ['GET', 'POST'])
def test():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
    WINDOW_SIZE = "1920,1080"

    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    # for MAC
    try:
        CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/neeraj/Desktop/working/chromedriver")
        chrome_options.binary_location = CHROME_PATH
        driver = webdriver.Chrome(executable_path = DRIVER_BIN, chrome_options = chrome_options)

    # for windows
    except:
        #print('error in mac')
        CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        chrome_options.binary_location = CHROME_PATH
        dir_path = os.getcwd() + '\chromedriver.exe'
        driver =  webdriver.Chrome(executable_path = dir_path, chrome_options = chrome_options)

    # driver.get(baseUrl1)
    # wname =  driver.find_element_by_name('user_name')
    # wmobile =  driver.find_element_by_name('user_mobile')
    # wemail = driver.find_element_by_name('user_email')
    # wname.clear()
    # wname.send_keys(name)
    # wmobile.clear()
    # wmobile.send_keys(phone)
    # wemail.clear()
    # wemail.send_keys(email)
    # openButton = driver.find_element_by_xpath('//*[@id="open_account_proceed_form"]')
    # openButton.click()

    # time.sleep(10)

    # driver.get(baseUrl2)
    # wname =  driver.find_element_by_name('ClientName')
    # wmobile =  driver.find_element_by_name('MobileNo')
    # wemail = driver.find_element_by_name('UserName')
    # wpass = driver.find_element_by_name('Password')
    # wname.clear()
    # wname.send_keys(name)
    # wmobile.clear()
    # wmobile.send_keys(phone)
    # wemail.clear()
    # wemail.send_keys(email)
    # wpass.clear()
    # wpass.send_keys(password)
    # wcheck1 = driver.find_element_by_xpath('//*[contains(text(), "I prefer South Indian language.")]')
    # wcheck1.click()
    # wcheck2 = driver.find_element_by_xpath('//*[contains(text(), "I agree that I have read & accept the ")]')
    # wcheck2.click()
    # regButton = driver.find_element_by_xpath('//*[@id="Register"]')
    # regButton.click()

    # time.sleep(15)

    driver.get(baseUrl3)
    wemail = driver.find_element_by_xpath('//*[@id="txtemail"]')
    wemail.clear()
    wemail.send_keys(email)
    wpass = driver.find_element_by_xpath('//*[@id="txtpassword"]')
    wpass.clear()
    wpass.send_keys(password)
    wmobile = driver.find_element_by_xpath('//*[@id="txtcontact"]')
    wmobile.clear()
    wmobile.send_keys(phone)
    sinButton = driver.find_element_by_xpath('//*[@id="submitsignup"]')
    sinButton.click()

    time.sleep(10)


    return ("Done submitting the data!")

class ContactForm(Form):
    name = TextField("Name",[validators.Required("Please enter your name.")])
   
    email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])

    phone = TextField("Mobile No")

    password = TextField("Password")

    submit = SubmitField("Submit")
 
@app.route("/", methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   return render_template('contact.html', form = form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
