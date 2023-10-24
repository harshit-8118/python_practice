'''
# start a browser session
browser = webdriver.Firefox()
# open link in browser
browser.get(https://www.codechef.com)
# login
nameElem = browser.find-element-by-id(edit-name)
nameElem.send-keys(username)
passElem = browser.find—element—by-id(edit-pass)
passElem.send-keys(password)
# open submission page
browser.get(https://mvw.codechef.com/submit/" + problem)
sleep function to let web components load in case of slow internet connnection
ime.sleep(10)
1
# click on toggle button to open simple text mode
browser.
# submit the code
inputElem = browser.find-element-by-id(edit-program)

'''