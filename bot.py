from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from itertools import combinations
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import winsound
import datetime
import os.path

# ---------------------- credentials needed to be filled ----------------------------- #
username1 = ''
pass1 = ''
username2 = ''
pass2 = ''
username3 = ''
pass3 = ''
username4 = ''
pass4 = ''
comments_goal = 300

accounts = [ [username1, pass1],
             [username2, pass2],
             [username3, pass3],
             [username4, pass4],
           ]
history_directory_path = ''
gecko_driver_exe_path = r''

# ------------------------------------------------------------------------------------- #

filename=""
comCounter = 0
bigErrorCounter = 0
f = None

def create_file():
    global filename
    path = history_directory_path
    filename = "out"
    x = datetime.datetime.now()
    filename = "out" + str(x)
    #filename = filename.replace("-", "_")
    filename = filename.replace(".", "-")
    filename = filename.replace(":", "-")
    filename = filename.replace("out20", "out-20")
    filename = filename.replace(" ", "-")
    filename = os.path.join(path, filename + ".txt")

def myPrint(text, end="\n"):
    #print(text, end=end)
    text = text + end
    f.write(text)

def alarm():
    winsound.Beep(500, 1000)  # Beep at 500 Hz for 1090 ms
    winsound.Beep(500, 1000)  # Beep at 500 Hz for 1000 ms
    winsound.Beep(500, 1000)  # Beep at 500 Hz for 1000 ms   

def random_sleep(a, b):
    cur = a
    step = 0.01
    timesList = []
    while cur<=b:
        cur = cur + step
        timesList.append(cur)
    sleep(random.choice(timesList)+2)

def usernameList(username):
    if username == username1:
        usernames = ["@"+username2, "@"+username3, "@"+username4]
    elif username == username2:
        usernames = ["@"+username1, "@"+username3, "@"+username4]
    elif username == username3:
        usernames = ["@"+username1, "@"+username2, "@"+username4]
    else: # username == username4:
        usernames = ["@"+username1, "@"+username2, "@"+username3]
    return usernames

def usersStr(usernames):
    userCombs = list(combinations(usernames, 3))
    temp = random.choice(userCombs)
    usersPart = random.sample(temp, 3)
    res = usersPart[0] + " " + usersPart[1] + " " + usersPart[2]
    return res

def messageStr():
    messages = ["pame", "pamee", "to xoume", "pame na kerdisoume!", "mporoume na to kerdisoume!!", "to theloume!!", "poso teleio!!",
                "yperoxo dwro!!", "kataplhktiko dwro!!", "fantastiko!", "fantasou na to kerdisoume!!", "", "", "" , "",
                "pame na to paroume!", "tsekarete to!", "euxaristoume!", "thanks!", "thank you!", "edw eimaste", 
                "piasthke to xeri mou apo ta sxolia!", "piasthkan ta xeria mas!", "ta plhktrologia phran fwtia!", 
                "den stamatame ta sxolia!", "pame na to paroume!", "as to palepsoume!", "teleios diagwnismos", "teleio giveaway", 
                "yperoxh idea", "euxaristw!", "akrivws o,ti xreiazomoun!", "poly shmantiko dwro!", "let's go!", 
                "tha eimaste oi nikhtes!", "niwthw tyxeros!", "deleastiko", "deleastikooo", "to xreiazomaste!", "mporoume aderfia!", 
                "mporoume!", "comments olh mera!!", "vamoss", "vamos", "comments olh mera!!", "synexeia comments!!", 
                "comments kai ksero pswmi!!", "den stamatame na sxoliazoume!", "teleio dwro!", "poly xrhsimo dwro", 
                "makari na yphrxan ki alloi tetoioi diagwnismoi", "ma ti dwro!!", "dwro apo ta liga!!", "top diagwnismos", 
                "koryfaio giveaway!!", "koryfaio dwro!!", "dwrara!!", "tairiazei teleia sto spiti mou!!", "tairiazei ganti sto spiti mas!!",
                "t e l e i o", "theloume na eimaste oi nikhtes!!", "plhsiazei h klhrwsh!!", "makari na fanw tyxeros!!", 
                "as einai h tyxh me to meros mou", "makari h tyxh na einai mazi mou!!", "mporoumeeee", "thankssss", "apisteutoo", 
                "k o r y f a i o", "makari na to parw!!", "posa sxolia na kanw pia!!", "ekei tha paizoume", "tha sas mathw pro edw!!", "olh mera pro!!",
                "kante tag bros mhn fovaste!", "panta to ithela!", "eiste etoimoi gia kapsimo?", "edw tha mathete fifa!", "fifa 21 edw!!!",
                "tha kaoume sto cod", "fifa olh mera!", "pro olh mera", "synexeia fifa!", "thn vapsate!", "edw den tha xanw pote!", 
                "mono nikes edw", "ahtthtos tha eimai kai se auto!!!", "e re stoixhmata pou tha pesoun!", "tha to kapsoume", 
                "erxontai tromeres vradies pro!", "poios tha to krathsei an to paroume?", "elpizw na mhn thelete na to moirastoume!!",
                "pelates pali!", "pame na to paroume pelates mou!", "tha xanete synexeia gatakia!"]
    res = random.choice(messages)
    return res

def emojiStr():
    emoList1=["😀", "😃", "😄", "😁", "😆", "😅", "😊",
            "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰",
            "😋", "😛", "😝", "😜", "🤪", "🧐", "🤓",
            "😎", "🤩", "🥳", "🤯", "😳", "😱", "😨",
            "🤗", "😯", "😦", "😧", "😮", "😲", "🤤",
            "😵", "🤚 🖐 ✋", "🤙", "👆👆", "👍", "🙏🙏",
            "💪💪💪", "💦💦", "🔥"]

    emoList2=["😀", "😁", "😃🤲", "😄", "😅", "😉", "😊", 
              "😋", "😍", "😎", "🙂", "😏", "🤗", "😮😮", "😮",
              "😯", "🤤", "🙃", "😱😎", "🤪", "💦😎", "🔥🙏🙏",
              "⚡🔥🔥", "", "", "🏃‍♂️", "✌", "🤘", "🤙🤙", "🖐", "✋☝️",
              "✋", "👏", "👌", "👍", "✊🙌", "🤲", "🙌", "👐",
              "👋", "🤝", "✋👏", "❤❤", "❤", "👀👀",
              "🙏🙏", "💪", "💪💪💪", "☝️☝️", "🌊"]

    res = random.choice(emoList2)
    return res

def commentText(username):
    usernames = usernameList(username)
    str1 = usersStr(usernames)
    str2 = messageStr()
    str3 = emojiStr()
    res = ""
    p = random.randrange(1, 12)
    if p==1:
        res = str1
    elif p==2:
        res = str1 + " " + str2
    elif p==3:
        res = str2 + " " + str1
    elif p==4:
        res = str3 + " " + str1
    elif p==5:
        res = str1 + " " + str3
    elif p==6:
        res = str1 + " " + str2 + " " + str3
    elif p==7:
        res = str2 + " " + str1 + " " + str3
    elif p==8:
        res = str1 + " " + str3 + " " + str2
    elif p==9:
        res = str3 + " " + str1 + " " + str2
    elif p==10:
        res = str2 + " " + str3 + " " + str1
    elif p==11:
        res = str3 + " " + str2 + " " + str1
    res = res + " "
    return res

class Instabot:
    
    def check_exists_by_xpath(self, xpath1, xpath2):
        try:
            self.driver.find_element_by_xpath(xpath1)
        except (NoSuchElementException):
            print("Eskase ena error")
            myPrint("Eskase ena error")
            return xpath2
        return xpath1

    def my_sleep(self, x):
        sleep(x)

    def go_google(self):
        self.driver.get("https://www.google.com/")
        random_sleep(8, 10)
        #self.driver.find_element_by_css_selector('#introAgreeButton > span:nth-child(3) > span:nth-child(1)').click()
        # #introAgreeButton > span:nth-child(3) > span:nth-child(1)
        # introAgreeButton
        # #introAgreeButton > span:nth-child(3)
        # .A28uDc
        #self.driver.find_element_by_xpath('//*[@id="introAgreeButton"]').click()
        #self.driver.find_element_by_css_selector("#introAgreeButton").click()
        #self.driver.find_element_by_xpath('/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form').click()

    def search_google1(self, key): 
        x1 = "/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input"
        x2 = "/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input"
        x = self.check_exists_by_xpath(x1, x2)
        self.driver.find_element_by_xpath(x).send_keys(key)
        random_sleep(1, 2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        random_sleep(7,9)
        y1 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/a"
        y2 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/a"
        x1 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/a"
        x2 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/a"
        y = self.check_exists_by_xpath(y1, y2)
        x = self.check_exists_by_xpath(x1, x2)
        f = self.check_exists_by_xpath(x, y)
        self.driver.find_element_by_xpath(f).click()
        random_sleep(6,8)

    def search_google2(self, key): 
        self.driver.find_element_by_xpath("/html/body/div[4]/form/div[2]/div[1]/div[2]/div/div[2]/input").send_keys(key)
        random_sleep(1, 2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        random_sleep(7,10)
        y1 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/a"
        y2 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/a"
        x1 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/a"
        x2 = "/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/a"
        y = self.check_exists_by_xpath(y1, y2)
        x = self.check_exists_by_xpath(x1, x2)
        f = self.check_exists_by_xpath(x, y)
        self.driver.find_element_by_xpath(f).click()
        random_sleep(6,8)   

    def search_the_first_site(self, key):
        self.go_google()
        self.search_google1(key)
        self.scroll_up_and_down2(random.randrange(10)>8)
        self.driver.execute_script("window.history.go(-1)")
        random_sleep(4, 7)
        for a in range(len(key)+1):
            self.driver.find_element_by_xpath("/html/body/div[4]/form/div[2]/div[1]/div[2]/div/div[2]/input").send_keys(Keys.BACK_SPACE)                       
            random_sleep(1,2)
        print("gyrisa apo ena site")
        myPrint("gyrisa apo ena site")
        random_sleep(3,5)

    def go_insta_from_google(self):
        self.go_google()
        self.search_google1("instagram")
        #self.scroll_up_and_down2(False)
        #self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        random_sleep(4,7)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('aOOlW')).click().perform()
        #self.driver.find_element_by_class_name('aOOlW').click()
        random_sleep(4, 7)
        print("Eftasa sto insta")
        myPrint("Eftasa sto insta")

    def check_activity(self):
        navs = self.driver.find_elements_by_class_name('Fifk5')
        navs[3].click()
        random_sleep(2, 5)
        navs = self.driver.find_elements_by_class_name('Fifk5')
        navs[3].click()
        random_sleep(2, 5)
        print("tsekara activity")
        myPrint("tsekara activity")

    def follow_from_home(self):
        p = random.randrange(1,16)
        if p==1:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button')).click().perform()
            random_sleep(2,4)
        elif p==3:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button')).click().perform()
            random_sleep(2,4)
        elif p==4:            
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button')).click().perform()
            random_sleep(2,4)
        elif p==5:            
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button')).click().perform()
            random_sleep(2,4)
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button')).click().perform()
            random_sleep(2,4)
        elif p==6:            
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button')).click().perform()
            random_sleep(2,4)
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button')).click().perform()
            random_sleep(2,4)
        elif p==7:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button')).click().perform()
            random_sleep(2,4)
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button')).click().perform()
            random_sleep(2,4)           
        elif p==8:
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button')).click().perform()
            random_sleep(2,4)
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[2]/div[3]/button')).click().perform()
            random_sleep(2,4)
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/div[3]/button')).click().perform()
            random_sleep(2,4)
        else:
            random_sleep(2,4)

    def follow_walkaround(self):
        if random.randrange(10)>=3:
            # some follows from home feed
            self.insta_go_not_first_home_pop_ups()
            self.wait_for_button_click_or_skip("Turn On")
            print("")
            myPrint("")
            self.follow_from_home()
            print("isws ekana kapoia follow")
            myPrint("isws ekana kapoia follow")

    def search_after_first_some_sites(self, sites):
        x = random.randrange(4,7)
        y = random.randrange(2,x)
        for i in range(1,y):
            current = random.choice(sites)
            self.search_google2(current)
            self.scroll_up_and_down2(random.randrange(10)>7)
            self.driver.execute_script("window.history.go(-1)")
            random_sleep(4, 7)
            for a in range(len(current)+1):
                self.driver.find_element_by_xpath("/html/body/div[4]/form/div[2]/div[1]/div[2]/div/div[2]/input").send_keys(Keys.BACK_SPACE)                       
                random_sleep(1, 2)
        print("gyrisa apo ena site")
        myPrint("gyrisa apo ena site")
        random_sleep(3,5)

    def seacrh_some_sites(self, all):
        self.search_the_first_site(random.choice(all))
        self.my_sleep(4)
        self.search_after_first_some_sites(all)
        self.my_sleep(4)
    
    def go_insta(self):
        self.driver.get("https://www.instagram.com/")
        random_sleep(4, 7)
        #self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('aOOlW')).click().perform()
        random_sleep(2, 3)
        print("Eftasa sto insta")
        myPrint("Eftasa sto insta")

    def shuffle_to_insta(self, websites):
        p = random.randrange(10)
        if p >= 8:
            self.seacrh_some_sites(websites)
            self.my_sleep(2)
            self.search_google2("instagram")
            self.my_sleep(2)
            #self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
            ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('aOOlW')).click().perform()
            random_sleep(4, 7)
            print("Eftasa sto insta")
            myPrint("Eftasa sto insta")
        elif p >= 3:
            self.go_insta_from_google()
        else:
            self.go_insta()

    def insta_log_in(self, username, password):
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        random_sleep(4, 7)

    def insta_log_out(self):
        if random.randrange(10)>=3:
            navs = self.driver.find_elements_by_class_name('Fifk5')
            navs[4].click()              
            random_sleep(2,3)
            subNavs = self.driver.find_elements_by_class_name('-qQT3')
            subNavs[4].click()                                  
            random_sleep(4,6)
            print("ekana log out")
            myPrint("ekana log out")

    def insta_first_home_pop_ups(self):
        #self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        self.my_sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name('yWX7d')).click().perform()
        random_sleep(4, 7)
        #self.driver.find_element_by_xpath("//button[text()='Turn On']").click()
        self.my_sleep(2)
        #ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('button.aOOlW:nth-child(2)')).click().perform()
        self.wait_for_button_click_or_skip("Turn On", True)
        print("")
        myPrint("")

    def insta_welcome(self, username, password):
        # welcome to instagram
        self.insta_log_in(username, password)
        print("ekana log in")
        myPrint("ekana log in")
        self.insta_first_home_pop_ups()
        #myPrint("eskasa ta pop ups")

    def wait_for_button_click_or_skip(self, text, last=False):
        random_sleep(2, 4)
        try:
            if last:
                print("tsekara gia pop up", end=" -> ")
                myPrint("tsekara gia pop up", end=" -> ")
            self.driver.find_element_by_xpath("//button[text()='%s']" %text)
        except (NoSuchElementException):
            if last:
                print("den eida", end=" -> ")
                myPrint("den eida", end=" -> ")
            random_sleep(0.5, 2)
            return
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath("//button[text()='%s']" %text)).click().perform()
        if last:
            print("eida, to eskasa", end=" -> ")
            myPrint("eida, to eskasa", end=" -> ")
        random_sleep(0.5, 2)
        return

    def insta_go_not_first_home_pop_ups(self):
        # Go home
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()
        urlHome = "www.instagram.com"
        if self.driver.current_url != urlHome:
            navs = self.driver.find_elements_by_class_name('Fifk5')
            navs[0].click()
            random_sleep(3, 5)
        # !!!!! maybe we need it
        self.wait_for_button_click_or_skip("Turn On")
        self.wait_for_button_click_or_skip("Turn On", True)
        print("")
        myPrint("")
        random_sleep(1, 2)
  
    def insta_go_my_profile(self):
        navs = self.driver.find_elements_by_class_name('Fifk5')
        navs[4].click() 
        random_sleep(4, 7)
        subNavs = self.driver.find_elements_by_class_name('-qQT3')
        subNavs[0].click()
        random_sleep(4, 7)

    def insta_go_saved(self, username):
        urlSaved = "www.instagram.com/%s/saved/" %username
        if self.driver.current_url == urlSaved:
            random_sleep(0.1, 0.4)
        else:       
            #self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()
            navs = self.driver.find_elements_by_class_name('Fifk5')
            navs[4].click()        
            random_sleep(1, 2)
            subNavs = self.driver.find_elements_by_class_name('-qQT3')
            subNavs[1].click()
            random_sleep(4, 6)

    def insta_open_comment_close_1st_saved(self, contestComments, close = True):
        opened = False
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[1]/img').click()
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a').click()
        try:
            print("dokimazw click sto div", end = " -> ")
            myPrint("dokimazw click sto div", end = " -> ")
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]').click()
            print("petyxe", end = " -> ")
            myPrint("petyxe", end = " -> ")
            opened = True
        except:
            print("apetyxe", end= " -> ")
        random_sleep(2, 4)
        if opened:
            self.giveaway_comment_opened_and_close(contestComments, close)
        
    def giveaway_comment_opened_and_close(self, comment, close):
        #random_sleep(2, 3)
        commentArea = self.driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        comment = comment + " "
        self.driver.execute_script("document.querySelector('.Ypffh').innerHTML = '%s';" %comment)
        self.my_sleep(0.5)
        self.driver.find_element_by_class_name('Ypffh').send_keys(Keys.BACK_SPACE)
        random_sleep(1, 2)
        try:
            su = self.driver.find_elements_by_class_name('sqdOP')
            su[18].click()
        except:
            print("de mporesa na kanw submit")
            myPrint("de mporesa na kanw submit")
            sleep(2)
        random_sleep(3, 4)
        if close:
            self.close_opened()

    def scroll_up_and_down(self):
        a = random.randrange(500, 1000)
        b = random.randrange(500, 1000)
        c = random.randrange(500, 1000)
        d = random.randrange(500, 1000)
        e = random.randrange(500, 1000)
        self.driver.execute_script("window.scrollTo(0,%s)" %a)
        random_sleep(4, 7)
        self.driver.execute_script("window.scrollTo(0,%s)" %b)
        random_sleep(1, 3)
        self.driver.execute_script("window.scrollTo(0,%s)" %c)
        random_sleep(2, 4)
        self.driver.execute_script("window.scrollTo(0,%s)" %(d))
        random_sleep(1, 6)
        self.driver.execute_script("window.scrollTo(0,%s)" %(e))
        random_sleep(4, 7)
        self.driver.execute_script("window.scrollTo(0,%s)" %(-a))
        random_sleep(4, 7)
        self.driver.execute_script("window.scrollTo(0,%s)" %(-b))
        random_sleep(3, 4)
        self.driver.execute_script("window.scrollTo(0,%s)" %(-c))
        random_sleep(1, 10)
        self.driver.execute_script("window.scrollTo(0,%s)" %(-d))
        random_sleep(1, 2)
        self.driver.execute_script("window.scrollTo(0,%s)" %(-e))
        random_sleep(1, 3)

    def scroll_up_and_down2(self, big):
        print("skrollarw up down")
        myPrint("skrollarw up down")
        lista = []
        if big:
            h = random.randrange(7, 20)
            self.arrows_down(h)
            self.arrows_up(h)
            #y = random.randrange(8, 30)
        else:    
            y = random.randrange(2, 10)
            x = random.randrange(1, y)
            for i in range(x):
                lista.append(random.randrange(500, 1500))
                self.driver.execute_script("window.scrollTo(0,%s)" %lista[i])
                random_sleep(1, 3)
            for i in range(x):
                self.driver.execute_script("window.scrollTo(0,%s)" %(-lista[i]))
                random_sleep(1, 2)
        
    def scroll_up_and_down_home(self, username, comm=False):
            self.insta_go_not_first_home_pop_ups()
            print("scrollarw home")
            myPrint("scrollarw home")
            h1 = random.randrange(15, 50)
            h2 = random.randrange(4, h1)
            h3 = random.randrange(3, h2)
            h4 = random.randrange(1, min(h2, h3))

            self.arrows_down(h2)
            random_sleep(2, 4)
            if random.randrange(10)>4 and comm:
                self.maybeOneComment(username)
                self.insta_go_not_first_home_pop_ups()

            self.arrows_down(h1)
            random_sleep(2, 4)
            if random.randrange(10)>7 and comm:
                self.maybeOneComment(username)
                self.insta_go_not_first_home_pop_ups()
            
            self.arrows_down(random.randrange(h1, h1+20))
            self.arrows_up(h4)
            random_sleep(1,5)

    def insta_go_public_feed(self):
        self.wait_for_button_click_or_skip("Turn On", True)
        print("")
        myPrint("")
        # go to public feed
        sleep(4)
        navs = self.driver.find_elements_by_class_name('Fifk5')
        navs[2].click()
        print("phga feed", end=" -> ")
        myPrint("phga feed", end=" -> ")
        random_sleep(4, 7)

    def like_opened_and_close(self, last=False):
        #if random.randrange(1, 10)>3:
        if last:
            next = random.randrange(5, 15)
            for i in range(1, next):
                if (random.randrange(1, 10)>7):
                    ActionChains(self.driver).double_click(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[2]')).perform()
                    random_sleep(2,3)
                ActionChains(self.driver).send_keys(Keys.ARROW_RIGHT).perform()
                random_sleep(2, 3)
        else:
            xpath3 = '/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[2]'
            xpath4 = '/html/body/div[4]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div'
            x = self.check_exists_by_xpath(xpath3, xpath4)
            ActionChains(self.driver).double_click(self.driver.find_element_by_xpath(x)).perform()
            # /html/body/div[4]/div[2]/div/article/div[2]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div                                                                        
        #else:
        #    self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
        random_sleep(1, 2) 
        self.close_opened()

    comments = ['GOAT🔥','The best 🔥🔥', 'What a player 🔥🔥', 'Amazing player', 'Unbelievable', 'The best of all',
                    'Generational talent', 'Talents like him come only once every 100 years', 'What an inspiration',
                    'What a talent', 'Pure genius', 'Pure talent', 'Born ready', 'Leader 🤯🤯🤯', ' Amazing 🤯🤯', 'Inspiration 🔥🔥🤯🔥🔥',
                    'Admiration 🔥🤯🔥', 'Idol 🔥', 'Example 🔥🤯', 'Amazing 🔥🔥', 'Spectacular 😯🔥😯', 'What a man 🔥😯😯', 'Hero 🔥', 'Superman 🔥', 'Gifted', 'Talented', 'Supernatural']
 
    def comment_opened_and_close(self, comments=comments):
        comment = random.choice(comments)
        self.my_sleep(2)
        commentArea = self.driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        self.driver.execute_script("document.querySelector('.Ypffh').innerHTML= '%s ';" %comment)
        self.my_sleep(0.5)
        self.driver.find_element_by_class_name('Ypffh').send_keys(Keys.BACK_SPACE)
        random_sleep(2,4)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
        random_sleep(3,6)
        self.close_opened()

    def close_opened(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
        except:
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            random_sleep(0.1, 0.2)
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            random_sleep(2, 4)

    def save_opened_and_close(self):
        random_sleep(5, 8)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[3]/div/div/button').click()
        random_sleep(3, 6)                  
        self.close_opened()

    def arrows_down(self, arr):
        for i in range(arr):
            ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
            if random.randrange(10)>=2:
                random_sleep(0.02, 0.3)
            else:
                random_sleep(0.4, 1)

    def arrows_up(self, arr):
        for i in range(arr):
            ActionChains(self.driver).send_keys(Keys.ARROW_UP).perform()
            random_sleep(0.2, 0.4)

    def feed_click_line_special(self, i, j1, j2):
        if random.randrange(10)>=5:
            j=j1
        else:
            j=j2
        xpath1 = "/html/body/div[1]/section/main/div/div[1]/div/div[%s]/div[%s]/div/a/div/div/img" %(i, j)
        xpath2 = "/html/body/div[1]/section/main/div/div[1]/div/div[%s]/div[%s]/div/a/div/img" %(i, j)
        x = self.check_exists_by_xpath(xpath1, xpath2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(x)).click().perform()
        random_sleep(5, 8)

    def feed_click_line_other(self, i):
        p2 = random.randrange(1,10)
        if p2>=7:
            j=1
        elif p2>=4:
            j=2
        else:
            j=3
        xpath1 = "/html/body/div[1]/section/main/div/div[1]/div/div[%s]/div[%s]/div/a/div/div/img" %(i, j)
        xpath2 = "/html/body/div[1]/section/main/div/div[1]/div/div[%s]/div[%s]/div/a/div/img" %(i, j)
        x = self.check_exists_by_xpath(xpath1, xpath2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(x)).click().perform()
        random_sleep(3, 5)

    def profile_line_xpath_play(self, xpath1, p1):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(xpath1)).click().perform()
        random_sleep(4, 6)
        if p1>3:
            ActionChains(self.driver).double_click(self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]')).perform()                                                            
            print("ekana like se post ths")
            myPrint("ekana like se post ths")
            random_sleep(1, 3)
        else:
            print("den ekana tipota")
            myPrint("den ekana tipota")
            random_sleep(1, 3)
        self.close_opened()

    def profile_line_all(self, i):
        p2 = random.randrange(1,10)
        if p2>=7:
            j=1
        elif p2>=4:
            j=2
        else:
            j=3    
        xpath1 = "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[%s]/div[%s]/a/div/div[1]/img" %(i, j)
        xpath2 = "/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[%s]/div[%s]/a/div/div[1]/img" %(i, j)
        p1 = random.randrange(1,10)
        try:
            self.profile_line_xpath_play(xpath1, p1)
            print("Komple")
            myPrint("Komple")
        except (NoSuchElementException):
            try:
                self.profile_line_xpath_play(xpath2, p1)
                print("Komple")
                myPrint("Komple")
            except (NoSuchElementException):
                print("Eskase ena error")
                myPrint("Eskase ena error")
                random_sleep(2,3)

    # when it's called, i have the line-1 on the top of the viewport
    def profile_line_play_close(self, line):
        print("anoigw grammh %s tou profile" %line, end=" -> ")
        myPrint("anoigw grammh %s tou profile" %line, end=" -> ")
        if line%4==0:
            self.arrows_down(6)
        else:
            self.arrows_down(5)
        self.profile_line_all(line)
        
    def play_with_opened_profile_pic_and_close(self):
        p = random.randrange(0,10)
        if p>=7:
           self.profile_like_opened_pic_and_close()
        else:
            self.close_opened()

    def play_with_opened_and_close(self, last=False):
        #myPrint("anoija dhmosieush sto feed")
        p = random.randrange(0,10)
        #if p>=9:
        #    self.save_opened_and_close()
        #if p>=9:
        #    self.comment_opened_and_close()
        if p>=4:
            print("ekana like", end=" -> ")
            myPrint("ekana like", end=" -> ")
            self.like_opened_and_close(last)
        else:
            print("den ekana kati", end=" -> ")
            myPrint("den ekana kati", end=" -> ")
            self.close_opened()

    def normal_line_go_play_close(self, line, last=False):
        if last:
            print("anoigw grammh %s tou feed" %line, end=" -> ")
            myPrint("anoigw grammh %s tou feed" %line, end=" -> ")
        else:
            print("anoigw grammh %s tou feed" %line, end=" -> ")
            myPrint("anoigw grammh %s tou feed" %line, end=" -> ")
        if line==2:
            self.arrows_down(6)
        else:
            self.arrows_down(7)
        try:
            self.feed_click_line_other(line)
            self.play_with_opened_and_close(last)
        except (NoSuchElementException): #, MoveTargetOutOfBoundsException):
            print("Eskase ena error")
            myPrint("Eskase ena error")
            random_sleep(2, 3)

    def special_line_go_play_close(self, line, j1, j2, last=False):
        if last:
            print("anoigw grammh %s tou feed" %line, end=" -> ")
            myPrint("anoigw grammh %s tou feed" %line, end=" -> ")
        else:
            print("anoigw grammh %s tou feed" %line, end=" -> ")
            myPrint("anoigw grammh %s tou feed" %line, end=" -> ")
        self.arrows_down(7)
        try:
            self.feed_click_line_special(line, j1, j2)
            self.play_with_opened_and_close(last)
        except (NoSuchElementException): #, MoveTargetOutOfBoundsException):
            print("Eskase ena error")
            myPrint("Eskase ena error")
            random_sleep(2, 3)

    def skip_line(self, line):
        print("skiparw grammh %s tou feed" %line, end = " -> ")
        myPrint("skiparw grammh %s tou feed" %line, end = " -> ")
        if line==1 or line==3: 
            self.arrows_down(7)
        elif line==2 or line==4:
            self.arrows_down(7) # or 6 better i guess

    def skip_prof_line(self, line):
        print("skiparw grammh %s tou profile" %line, end = " -> ")
        myPrint("skiparw grammh %s tou profile" %line, end = " -> ")
        if line%2==0:
            self.arrows_down(5)
        else:
            self.arrows_down(6)

    def insta_feed_scroll(self):
        
        p = random.randrange(1, 32)
        print("kanw feed scroll, periptwsh %s" %p, end = " -> ")
        myPrint("kanw feed scroll, periptwsh %s" %p, end = " -> ")
        #p = 10
        '''
        [(1,), (2,), (3,), (4,), (5,)]
        [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
        [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
        [(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5)]
        [(1, 2, 3, 4, 5)]
        '''    
     
        if p==1: # 1 only
            self.special_line_go_play_close(1, 1, 3, True)

        elif p==2: # 2 only
            self.skip_line(1)
            self.normal_line_go_play_close(2, True)

        elif p==3: # 3 only
            self.skip_line(1)
            self.skip_line(2)
            self.normal_line_go_play_close(3, True)
            
        elif p==4: # 4 only
            self.skip_line(1)
            self.skip_line(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2, True)

        elif p==5: # 5 only
            self.skip_line(1)
            self.skip_line(2)
            self.skip_line(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)

        elif p==6: # 1 + 2
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2, True)

        elif p==7: # 1 + 3
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.normal_line_go_play_close(3, True)

        elif p==8: # 1 + 4
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2, True)

        elif p==9: # 1 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.skip_line(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)

        elif p==10: # 2 + 3
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3, True)

        elif p==11: # 2 + 4
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2, True)

        elif p==12: # 2 + 5
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.skip_line(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)

        elif p==13: # 3 + 4
            self.skip_line(1)
            self.skip_line(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2, True)
            
        elif p==14: # 3 + 5
            self.skip_line(1)
            self.skip_line(2)
            self.normal_line_go_play_close(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)

        elif p==15: # 4 + 5
            self.skip_line(1)
            self.skip_line(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)

        elif p==16: # 1 + 2 + 3
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3, True)

        elif p==17: # 1 + 2 + 4
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2, True)

        elif p==18: # 1 + 2 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.skip_line(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)

        elif p==19: # 1 + 3 + 4
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2, True)

        elif p==20: # 1 + 3 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.normal_line_go_play_close(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)  

        elif p==21: # 1 + 4 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)             

        elif p==22: # 2 + 3 + 4
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2, True)
            
        elif p==23: # 2 + 3 + 5
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)                        

        elif p==24: # 2 + 4 + 5            
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)

        elif p==25: # 3 + 4 + 5
            self.skip_line(1)
            self.skip_line(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)

        elif p==26: # 1 + 2 + 3 + 4
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2, True)

        elif p==27: # 1 + 2 + 3 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3)
            self.skip_line(4)
            self.normal_line_go_play_close(5, True)  

        elif p==28: # 1 + 2 + 4 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.skip_line(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)  

        elif p==29: # 1 + 3 + 4 + 5
            self.special_line_go_play_close(1, 1, 3)
            self.skip_line(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True) 

        elif p==30: # 2 + 3 + 4 + 5
            self.skip_line(1)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)
        
        elif p==31:
            self.special_line_go_play_close(1, 1, 3)
            self.normal_line_go_play_close(2)
            self.normal_line_go_play_close(3)
            self.special_line_go_play_close(4, 1, 2)
            self.normal_line_go_play_close(5, True)
        print("")
        myPrint("")
        self.scroll_up_and_down2(True)
        #self.insta_go_not_first_home_pop_ups()

    def insta_profile_scroll(self):
        print("kanw profile scroll", end = " -> ")
        myPrint("kanw profile scroll", end = " -> ")
        last_line = random.randrange(1, 10)

        for line in range(last_line):
            if line==0:
                self.arrows_down(5)
                print("skiparw line 0 tou profile", end = " -> ")
                myPrint("skiparw line 0 tou profile", end = " -> ")
            else:
                p = random.randrange(1, 100)
                if p>=60:
                    #myPrint("paizw me line %s" %line)
                    self.profile_line_play_close(line)
                else:
                    self.skip_prof_line(line)
                    #myPrint("skiparw line %s" %line)
        print("")
        myPrint("")

    def insta_search_visit_first_profile(self, key):
        # search at the bar
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(key)
        self.driver.find_element_by_class_name("XTCLo").send_keys(key)
        
        random_sleep(5, 7)
        # click on the first result
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        random_sleep(1,2)
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        #xpath1 = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]"
        #xpath2 = "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]"
        #x = self.check_exists_by_xpath(xpath1, xpath2)
        #self.driver.find_element_by_xpath(x).click()
        print("episkeptomai profile %s" %key)
        myPrint("episkeptomai profile %s" %key)
        random_sleep(3, 5)

    def insta_visit_a_profile(self, insta_searches):
            self.insta_search_visit_first_profile(random.choice(insta_searches))
            if random.randrange(1,10)>4:
                self.insta_profile_scroll()

    # if i give x=1, it will only visit one profile
    def insta_visit_some_profiles_and_back_home(self, username, insta_searches, x=random.randrange(1, 4)):
        for i in range(x):
            self.insta_visit_a_profile(insta_searches)
            self.maybeOneComment(username)
            #self.insta_go_not_first_home_pop_ups()
            if i==x-1:
                #self.insta_go_not_first_home_pop_ups()
                #self.scroll_up_and_down2(True)
                print("eida kapoia profiles")
                myPrint("eida kapoia profiles")

    def insta_next_story(self):
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[2]').click()        
        ActionChains(self.driver).send_keys(Keys.ARROW_RIGHT).perform()
        random_sleep(2, 3)

    def insta_previous_story(self):
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[1]').click()
        ActionChains(self.driver).send_keys(Keys.ARROW_LEFT).perform()
        random_sleep(2, 3)

    def insta_see_some_stories_begin_from_first(self):
        # open stories section
        print("vlepw kapoia story")
        myPrint("vlepw kapoia story")
        self.my_sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[1]/div[1]/div/div/div/div/ul/li[3]/div/button/div[1]/span/img').click()
        random_sleep(2, 7)
        for j in range(1, 10):
            # check next story
            self.insta_next_story()
            # rarely press more button and cancel back
            #if random.randrange(30)<2:
            #    self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/header/div/div[2]/button').click()
            #    ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            #    random_sleep(1, 2)
            #    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/button[2]').click()
            #    random_sleep(1, 2)
            # sometimes press the previous story button
            if random.randrange(1,10)==1 and j>1:
                self.insta_previous_story()
        self.my_sleep(2)
        # close stories section
        #self.driver.find_element_by_xpath('/html/body/div[1]/section/div/div/section/div[2]/button[3]').click()
        #                                  /html/body/div[1]/section/div/div/section/div[2]/button[3]
        #                                  /html/body/div[1]/section/div[3]/button
        #                                  .K_10X > button:nth-child(1)
        #self.driver.find_element_by_css_selector('.K_10X > button:nth-child(1)').click()                                                 
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        random_sleep(2, 4)
        # We are back home, fix the pop up menu
        self.my_sleep(2)
        self.wait_for_button_click_or_skip("Turn On", True)
        print("")
        myPrint("")

    def zoom_out(self):
        zoom = random.randrange(30, 60)
        self.driver.execute_script("document.body.style.transform = 'scale(0.8)'")
        #body = self.driver.find_element_by_tag_name('body')
        #body.send_keys(Keys.CONTROL,'-')
        #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('-').perform()
        #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('-').perform()
        #random_sleep(2,4)
        #body.send_keys(Keys.CONTROL,'-')
        #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('-').perform()
        #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('-').perform()
        random_sleep(2,4)

    def go_my_profile_or_stories_and_back(self):
        p = random.randrange(1,10)
        if p>=7:
            self.insta_go_my_profile()
            #self.insta_go_not_first_home_pop_ups()
        else:
            self.insta_go_not_first_home_pop_ups()
            self.wait_for_button_click_or_skip("Turn On")
            self.insta_see_some_stories_begin_from_first()
    
    def my_prof_stories_walkaround(self):
        if random.randrange(10)>=2:
            # first walking around
            self.wait_for_button_click_or_skip("Turn On")
            self.wait_for_button_click_or_skip("Turn On", True)
            print("")
            myPrint("")
            self.go_my_profile_or_stories_and_back()
            print("eida stories h profil mou")
            myPrint("eida stories h profil mou")

    def explore_feed_and_back(self):
        self.insta_go_public_feed()
        self.driver.execute_script("window.location.reload();")
        self.my_sleep(5)
        self.insta_feed_scroll()
        #self.insta_go_not_first_home_pop_ups()
        print("eida feed")
        myPrint("eida feed")

    def random_explore_feed_profiles_and_back(self, insta_searches, username):
        p = random.randrange(1, 10)
        #self.scroll_up_and_down_home()
        if p==1 or p==9:
            self.maybeOneComment(username)
            self.explore_feed_and_back()
            self.insta_visit_some_profiles_and_back_home(username, insta_searches, 1)
            self.maybeOneOrTwoComments(username)
        elif p==2 or p==8:
            self.insta_visit_some_profiles_and_back_home(username, insta_searches)
            self.maybeOneOrTwoComments(username)
        elif p==3:
            self.explore_feed_and_back()
            self.maybeOneOrTwoComments(username)
        elif p==4:
            self.explore_feed_and_back()
            self.maybeOneOrTwoComments(username)
            self.insta_visit_some_profiles_and_back_home(username, insta_searches, 1)
            self.explore_feed_and_back()
            self.maybeOneOrTwoComments(username)
        elif p==5:
            self.insta_visit_some_profiles_and_back_home(username, insta_searches)
            self.maybeOneOrTwoComments(username)
            self.explore_feed_and_back()
            self.maybeOneComment(username)
        elif p==6:
            self.maybeOneOrTwoComments(username)
            self.insta_visit_some_profiles_and_back_home(username, insta_searches, 1)
            self.maybeOneOrTwoComments(username)
            self.insta_visit_some_profiles_and_back_home(username, insta_searches)
        elif p==7:
            self.insta_visit_some_profiles_and_back_home(username, insta_searches)
            self.maybeOneOrTwoComments(username)
            self.explore_feed_and_back()
            self.maybeOneOrTwoComments(username) 
            self.insta_visit_some_profiles_and_back_home(username, insta_searches, 1)
            self.maybeOneComment(username) 

    def profiles_feed_walkaround(self, insta_searches, username):
        if random.randrange(10)>=2:
            # feed and profiles mix
            self.wait_for_button_click_or_skip("Turn On", True)
            print("")
            myPrint("")
            self.random_explore_feed_profiles_and_back(insta_searches, username)
            print("eida feed h profiles kai gyrisa pisw")  
            myPrint("eida feed h profiles kai gyrisa pisw")  

    def GiveAwayOneComment(self, username):
        #now i have the text of the comment
        text = commentText(username)
        print("Tha kanw to comment: %s" %text)
        myPrint("Tha kanw to comment: %s" %text)
        random_sleep(1, 2)
        self.insta_go_saved(username)
        self.insta_open_comment_close_1st_saved(text, True)
        print("Komple me ta comments")
        myPrint("Komple me ta comments")
        #self.insta_go_not_first_home_pop_ups()

    def GiveAwayMultipleComments(self, username):
        try :
            #now i have the text of the comment
            text1 = commentText(username)
            text2 = commentText(username)
            print("Tha kanw to comment1: %s" %text1)
            myPrint("Tha kanw to comment1: %s" %text1)
            print("Tha kanw to comment2: %s" %text2)
            myPrint("Tha kanw to comment2: %s" %text2)
            random_sleep(1, 2)
            self.insta_go_saved(username)
            self.driver.execute_script("window.location.reload();")
            random_sleep(3, 4)
            print("comment 1", end=" -> ")
            myPrint("comment 1", end=" -> ")
            self.insta_open_comment_close_1st_saved(text1)
            print("petyxe", end=", comment 2 ->")
            myPrint("petyxe", end=", comment 2 ->")
            random_sleep(1, 2)
            self.insta_open_comment_close_1st_saved(text2)
            print("petyxe", end=" -> ")
            myPrint("petyxe", end=" -> ")
            random_sleep(1, 2)
        except:
            self.close_opened()
            self.close_opened()
            print("apetyxe", end=" -> ")
            myPrint("apetyxe", end=" -> ")
        print("Komple me ta multiple comments")
        myPrint("Komple me ta multiple comments")
        #self.insta_go_not_first_home_pop_ups()

    def maybeOneComment(self, username, sure=False):
        global comCounter
        if (sure or random.randrange(10)>=3):
            # first comment on giveaway
            self.wait_for_button_click_or_skip("Turn On")
            self.wait_for_button_click_or_skip("Turn On", True)
            print("")
            myPrint("")
            comCounter = comCounter + 1
            print("TRYING GIVEAWAY COMMENT no. %s" %comCounter)
            myPrint("TRYING GIVEAWAY COMMENT no. %s" %comCounter)
            self.GiveAwayOneComment(username)

    def maybeTwoComments(self, username, sure=False):
        global comCounter
        if (sure or random.randrange(10)>=5):
            # first comment on giveaway
            self.wait_for_button_click_or_skip("Turn On")
            self.wait_for_button_click_or_skip("Turn On", True)
            print("")
            myPrint("")
            comCounter = comCounter + 2
            print("TRYING (TWO) GIVEAWAY COMMENTs no. %s" %comCounter)
            myPrint("TRYING (TWO) GIVEAWAY COMMENTs no. %s" %comCounter)
            self.GiveAwayMultipleComments(username)

    def maybeOneOrTwoComments(self, username):
        p = random.randrange(10)
        if p>=5:
            self.maybeTwoComments(username, True)
        elif p>=1:
            self.maybeTwoComments(username)
        elif p==0:
            self.maybeOneComment(username, True)

    def checkMessagesAndBack(self):
        self.wait_for_button_click_or_skip("Turn On")
        self.wait_for_button_click_or_skip("Turn On", True)
        print("")
        myPrint("")
        random_sleep(1,2)
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a").click() 
        navs = self.driver.find_elements_by_class_name('Fifk5')
        navs[1].click()
        print("phga messages", end=" -> ")
        myPrint("phga messages", end=" -> ")
        self.wait_for_button_click_or_skip("Turn On")
        self.wait_for_button_click_or_skip("Turn On", True)
        random_sleep(1, 3)
        #self.insta_go_not_first_home_pop_ups()

    def checkActivityOrMessages(self):
        p = random.randrange(10)
        if p>=7:
            self.checkMessagesAndBack()
        elif p>=5:
            self.check_activity()
        else:
            self.checkMessagesAndBack()
            self.check_activity()

    def shuffleMain(self, username, insta_searches, first=False):
        actions = [1,2,3,4,5]
        random.shuffle(actions)
        positions = [1,2,3,4,5]
        walls = random.choices(positions, k=3) 
        i = 1
        for action in actions: 
            if random.randrange(10)>3:
                if action==1:
                    self.checkActivityOrMessages()
                elif action==2:
                    # from home page
                    self.my_prof_stories_walkaround()
                elif action==3:
                    self.scroll_up_and_down_home(username, first)
                elif action==4:
                    # from home page
                    self.follow_walkaround()
                elif action==5:
                    self.profiles_feed_walkaround(insta_searches, username)
            if i in walls:
                l2 = [1,2,2,2,2,2,2,2,2,2,2,3,3]
                index = random.choice(l2)
                if index==1:
                    self.maybeOneComment(username)
                elif index==2:
                    self.maybeOneOrTwoComments(username)
                elif index==3:
                    self.maybeOneComment(username)
            i = i + 1

    def __init__(self,username,password):
        self.driver=webdriver.Firefox(executable_path=gecko_driver_exe_path)
        self.driver.maximize_window()
        global bigErrorCounter

        insta_searches = [  "cristiano",
                            "leo",
                            "eden hazard",
                            "griezmann",
                            "psg",
                            "manchester united",
                            "dani alves",
                            "man city",
                            "iniesta",
                            "barca",
                            "benzema",
                            "real madrid",
                            "atletico mardid",
                            "luis suarez", 
                            "dybala",
                            "juventus",
                            "milan",
                            "salah",
                            "liverpool",
                            "sergio ramos",
                            "paul pogba",
                            "gareth bale",
                            "tottenham hotspur",
                            "harry kane",
                            "streling",
                            "grealish",
                            "Mbappe",
                            "di maria", 
                            "cavani",
                            "icardi",
                            "zlatan",
                            "adriano",
                            "ronaldo",
                            "ronaldinho",
                            "marcelo",
                            "david luiz",
                            "james rodriguez",
                            "carlo ancelloti",
                            "everton",
                            "iwobi",
                            "ronaldinho", 
                            "puyol",
                            "pique",
                            "shaqira",
                            "champions league",
                            "premier league",
                            "beckham",
                            "skysports",
                            "luis nani",
                            "bruno fernandes",
                            "neymar",
                            "vinicius",
                            "heskey",
                            "pastore",
                            "huntelaar",
                            "de jong",
                            "podolski",
                            "mertesacker",
                            "drogba",
                            "peter chech",
                            "peter crouch",
                            "L. Messi",
                            "Cristiano Ronaldo",
                            "Neymar Jr",
                            "De Gea",
                            "K. De Bruyne",
                            "E. Hazard",
                            "L. Modrić",
                            "L. Suárez",
                            "Sergio Ramos",
                            "J. Oblak",
                            "R. Lewandowski",
                            "T. Kroos",
                            "D. Godín",
                            "David Silva",
                            "N. Kanté",
                            "P. Dybala",
                            "H. Kane",
                            "A. Griezmann",
                            "M. ter Stegen",
                            "T. Courtois",
                            "Sergio Busquets",
                            "E. Cavani",
                            "M. Neuer",
                            "S. Agüero",
                            "G. Chiellini",
                            "K. Mbappé",
                            "M. Salah",
                            "Casemiro",
                            "J. Rodríguez",
                            "L. Insigne",
                            "Isco",
                            "C. Eriksen",
                            "Coutinho",
                            "P. Aubameyang",
                            "M. Hummels",
                            "Marcelo",
                            "G. Bale",
                            "H. Lloris",
                            "G. Higuaín",
                            "Thiago Silva",
                            "S. Handanovič",
                            "G. Buffon",
                            "S. Umtiti",
                            "M. Icardi",
                            "K. Koulibaly",
                            "P. Pogba",
                            "K. Navas",
                            "R. Lukaku",
                            "C. Immobile",
                            "Jordi Alba",
                            "D. Mertens",
                            "J. Vertonghen",
                            "M. Hamšík",
                            "I. Rakitić",
                            "Piqué",
                            "L. Sané",
                            "Bernardo Silva",
                            "Ederson",
                            "S. Mané",
                            "V. van Dijk",
                            "R. Sterling",
                            "Roberto Firmino",
                            "R. Varane",
                            "M. Verratti",
                            "Alex Sandro",
                            "Douglas Costa",
                            "T. Müller",
                            "Thiago",
                            "M. Reus",
                            "Azpilicueta",
                            "L. Bonucci",
                            "T. Alderweireld",
                            "M. Pjanić",
                            "M. Benatia",
                            "M. Özil",
                            "Fernandinho",
                            "Iniesta",
                            "M. Škriniar",
                            "S. Milinković-Savić",
                            "Marco Asensio",
                            "N. Fekir",
                            "Alisson",
                            "J. Kimmich",
                            "Saúl",
                            "R. Mahrez",
                            "D. Alaba",
                            "Koke",
                            "A. Lacazette",
                            "K. Manolas",
                            "N. Otamendi",
                            "Parejo",
                            "Paulinho",
                            "W. Szczęsny",
                            "A. Sánchez",
                            "Y. Brahimi",
                            "J. Boateng",
                            "A. Vidal",
                            "I. Perišić",
                            "E. Džeko",
                            "S. Khedira",
                            "Diego Costa",
                            "R. Nainggolan",
                            "Naldo",
                            "B. Matuidi",
                            "Miranda",
                            "K. Benzema",
                            "Filipe Luís",
                            "V. Kompany",
                            "Pepe",
                            "Z. Ibrahimović",
                            "D. Sánchez",
                            "J. Giménez",
                            "Alex Telles",
                            "A. Laporte",
                            "Bruno Fernandes",
                            "N. Süle",
                            "A. Martial",
                            "D. Alli",
                            "Fabinho",
                            "Marquinhos",
                            "William Carvalho",
                            "Jorginho",
                            "F. Thauvin",
                            "Carvajal",
                            "M. Depay",
                            "H. Son",
                            "A. Lopes",
                            "S. de Vrij",
                            "M. Perin",
                            "J. Cuadrado",
                            "Iago Aspas",
                            "B. Leno",
                            "N. Matić",
                            "L. Hrádecký",
                            "Illarramendi",
                            "K. Walker",
                            "I. Gündoğan",
                            "José Callejón",
                            "A. Di María",
                            "M. Mandžukić",
                            "Willian",
                            "Sergio Asenjo",
                            "E. Banega",
                            "A. Witsel",
                            "D. Payet",
                            "Jonas",
                            "Sokratis",
                            "S. Ruffier",
                            "Falcao",
                            "K. Schmeichel",
                            "Raúl Albiol",
                            "A. Gómez",
                            "A. Barzagli",
                            "Quaresma",
                            "A. Robben",
                            "O. Dembélé",
                            "Gabriel Jesus",
                            "Ronaldo Cabrais",
                            "Josué Chiamulera",
                            "Louri Beretta",
                            "P. Kimpembe",
                            "N. Keïta",
                            "C. Tolisso",
                            "T. Lemar",
                            "K. Coman",
                            "J. Tah",
                            "Anderson Talisca",
                            "T. Werner",
                            "A. Rabiot",
                            "L. Goretzka",
                            "Q. Promes",
                            "H. Ziyech",
                            "Lucas Vázquez",
                            "Y. Carrasco",
                            "Gerard Moreno",
                            "Felipe",
                            "M. Kovačić",
                            "Kepa",
                            "Manu Trigueros",
                            "S. Gnabry",
                            "J. Pickford",
                            "S. Savić",
                            "J. Stones",
                            "Suso",
                            "J. Draxler",
                            "Felipe Anderson",
                            "Lucas Moura",
                            "Danilo Pereira",
                            "Nacho Fernández",
                            "T. Horn",
                            "Allan",
                            "F. Acerbi",
                            "Sergi Roberto",
                            "Rodrigo",
                            "Pizzi",
                            "K. Kampl",
                            "Neto",
                            "O. Baumann",
                            "I. Gueye",
                            "H. Mkhitaryan",
                            "Marcos Alonso",
                            "D. Subašić",
                            "K. Glik",
                            "K. Strootman",
                            "B. Dost",
                            "Oscar",
                            "M. Balotelli",
                            "Luiz Gustavo",
                            "Giuliano",
                            "David Luiz",
                            "R. Fährmann",
                            "Juan Mata",
                            "Adán",
                            "Rui Patrício",
                            "Y. Sommer",
                            "Javi Martínez",
                            "L. Bender",
                            "Lucas Leiva",
                            "S. Mandanda",
                            "Cesc Fàbregas",
                            "M. Dembélé",
                            "F. Ribéry",
                            "R. Jarstein",
                            "D. De Rossi",
                            "Pepe Reina",
                            "J. Pavlenka",
                            "M. de Ligt",
                            "Rodri",
                            "Arthur",
                            "G. Donnarumma",
                            "Rosberto Dourado",
                            "Juiano Mestres",
                            "Raphaelito Anjos",
                            "Gelson Martins",
                            "Gonçalo Guedes",
                            "L. Torreira",
                            "Malcom",
                            "Pau López",
                            "L. Hernández",
                            "C. Lenglet",
                            "A. Kramarić",
                            "A. Robertson",
                            "Dani García",
                            "F. Bernardeschi",
                            "J. Brandt",
                            "D. Rugani",
                            "Samu Castillejo",
                            "João Cancelo",
                            "A. Romagnoli",
                            "T. Partey",
                            "Fred",
                            "J. Vardy",
                            "A. Belotti",
                            "E. Forsberg",
                            "J. Lingard",
                            "F. Vázquez",
                            "E. Višća",
                            "A. Rüdiger",
                            "A. Florenzi",
                            "H. Maguire",
                            "T. Meunier",
                            "S. Sané",
                            "G. Kondogbia",
                            "Rafinha",
                            "Gabriel Paulista",
                            "Morata",
                            "J. Cillessen",
                            "W. Ben Yedder",
                            "C. Bakambu",
                            "Pablo Sarabia",
                            "W. Zaha",
                            "Luis Alberto",
                            "Jonathan Viera",
                            "Bartra",
                            "S. Coates",
                            "Willian José",
                            "Mário Fernandes",
                            "Víctor Ruiz",
                            "T. Delaney",
                            "K. Casteels",
                            "M. Götze",
                            "S. Mustafi",
                            "J. Pastore",
                            "Pedro",
                            "G. Bonaventura",
                            "R. Bürki",
                            "Taison",
                            "S. Nzonzi",
                            "Marlos",
                            "A. Ramsey",
                            "K. Trippier",
                            "A. Kolarov",
                            "G. Sigurðsson",
                            "S. Giovinco",
                            "M. Arnautović",
                            "N. Gaitán",
                            "J. Henderson",
                            "M. Kruse",
                            "M. Parolo",
                            "L. Fejsa",
                            "A. Rami",
                            "V. Ćorluka",
                            "G. Wijnaldum",
                            "F. Fazio",
                            "O. Giroud",
                            "Marcano",
                            "A. Guardado",
                            "E. Garay",
                            "Jardel",
                            "S. Sirigu",
                            "E. Viviano",
                            "L. Koscielny",
                            "A. Consigli",
                            "L. Biglia",
                            "Dani Alves",
                            "David Villa",
                            "Aduriz",
                            "P. Čech",
                            "Casillas",
                            "M. Rashford",
                            "Laure Santeiro",
                            "L. Bailey",
                            "M. Akanji",
                            "F. de Jong",
                            "Nélson Semedo",
                            "Pablo Fornals",
                            "Fabián",
                            "E. Bailly",
                            "Dani Ceballos",
                            "H. Lozano",
                            "Morales",
                            "J. Seri",
                            "M. Politano",
                            "M. Brozović",
                            "Williams",
                            "A. Correa",
                            "A. Christensen",
                            "João Mário",
                            "T. Strakosha",
                            "E. Hysaj",
                            "P. Zieliński",
                            "Ricardo Pereira",
                            "Grimaldo",
                            "R. Guerreiro",
                            "A. Doucouré",
                            "J. Martínez",
                            "C. Bacca",
                            "A. Plea",
                            "B. Davies",
                            "M. Nastasić",
                            "A. Milik",
                            "M. Sabitzer",
                            "B. Mendy",
                            "C. Kramer",
                            "S. Vrsaljko",
                            "T. Hazard",
                            "K. Bellarabi",
                            "S. Zaza",
                            "F. Ghoulam",
                            "B. Lecomte",
                            "J. Iličić",
                            "K. Volland",
                            "Paco Alcácer",
                            "Vitolo",
                            "G. Xhaka",
                            "D. Tadić",
                            "C. Aránguiz",
                            "S. Verdi",
                            "D. Lovren",
                            "G. Medel",
                            "X. Shaqiri",
                            "J. Corona",
                            "A. Areola",
                            "K. Vogt",
                            "Ander Herrera",
                            "E. Salvio",
                            "S. El Shaarawy",
                            "C. Smalling",
                            "Hulk",
                            "S. Kagawa",
                            "M. Lanzini",
                            "F. Smolov",
                            "L. Stindl",
                            "O. Toprak",
                            "D. Perotti",
                            "F. Muslera",
                            "B. Höwedes",
                            "S. Kjær",
                            "S. Bender",
                            "M. Valbuena",
                            "Pedro León",
                            "K. Boateng",
                            "L. Piszczek",
                            "A. Candreva",
                            "D. Wass",
                            "E. Lamela",
                            "D. Rose",
                            "C. Vela",
                            "Renato Augusto",
                            "A. Valencia",
                            "L. Fabiański",
                            "João Moutinho",
                            "Borja Valero",
                            "F. Quagliarella",
                            "B. Gomis",
                            "Manuel Fernandes",
                            "H. Herrera",
                            "Raffael",
                            "Nani",
                            "J. Milner",
                            "J. Mathieu",
                            "Joaquín",
                            "M. Gómez",
                            "K. Havertz",
                            "T. Ndombele",
                            "H. Aouar",
                            "Carlos Soler",
                            "Odriozola",
                            "M. Almirón",
                            "Welington Dano",
                            "Everton Andrão",
                            "Oyarzabal",
                            "F. Balbuena",
                            "M. Marega",
                            "B. Pavard",
                            "W. Ndidi",
                            "A. Onana",
                            "G. Lo Celso",
                            "M. Acuña",
                            "Rúben Neves",
                            "Mariano",
                            "Raúl",
                            "M. Caldara",
                            "M. Vecino",
                            "T. Bakayoko",
                            "M. Dahoud",
                            "Rafa",
                            "K. Baldé",
                            "G. Rulli",
                            "F. Armani",
                            "Rony Lopes",
                            "Santi Mina",
                            "K. Demirbay",
                            "Gayà",
                            "André Gomes",
                            "N. Tagliafico",
                            "M. Sanson",
                            "Pacheco",
                            "E. Can",
                            "H. Çalhanoğlu",
                            "M. Ginter",
                            "M. Keane",
                            "L. Paredes",
                            "T. Stepanenko",
                            "L. Shaw",
                            "Z. Feddal",
                            "S. Haller",
                            "Bernard",
                            "T. Inui",
                            "Portu",
                            "M. Batshuayi",
                            "E. Zahavi",
                            "T. Vaclík",
                            "N. Pope",
                            "Héctor Bellerín",
                            "P. Kadeřábek",
                            "J. Butland",
                            "J. Vestergaard",
                            "J. Tarkowski",
                            "Deulofeu",
                            "E. Dier",
                            "J. Murillo",
                            "M. Badelj",
                            "Ismaily",
                            "N. Schulz",
                            "L. Digne",
                            "M. Uth",
                            "Cristian Tello",
                            "D. Vida",
                            "L. Muriel",
                            "V. Aboubakar",
                            "A. Oxlade-Chamberlain",
                            "S. Aurier",
                            "J. Matip",
                            "Y. Rakitskyi",
                            "Sergi Enrich",
                            "A. Yarmolenko",
                            "Hugo Mallo",
                            "André Almeida",
                            "D. Didavi",
                            "R. Rodríguez",
                            "R. Pereyra",
                            "Mario Gaspar",
                            "Maicon",
                            "D. Blind",
                            "J. Zoet",
                            "A. Ljajić",
                            "Canales",
                            "Iago Falqué",
                            "L. de Jong",
                            "Guaita",
                            "Muniain",
                            "Susaeta",
                            "S. Rudy",
                            "K. Trapp",
                            "V. Wanyama",
                            "N. Nkoulou",
                            "R. Boudebouz",
                            "Camacho",
                            "S. Ulreich",
                            "M. Musacchio",
                            "C. Stuani",
                            "P. Gulácsi",
                            "Bruno",
                            "F. Delph",
                            "A. Lallana",
                            "Marcelo",
                            "S. Coleman",
                            "Alexandre Pato",
                            "Antunes",
                            "Nacho Monreal",
                            "Beñat",
                            "A. Fernández",
                            "K. Gameiro",
                            "I. Piatti",
                            "V. Birsa",
                            "S. Romero",
                            "D. Criscito",
                            "D. Valeri",
                            "D. Sturridge",
                            "Raúl García",
                            "S. Defour",
                            "M. Škrtel",
                            "S. Radu",
                            "G. Cahill",
                            "L. Diarra",
                            "L. Perrin",
                            "Dante",
                            "A. Granqvist",
                            "A. Gignac",
                            "M. Gómez",
                            "I. Akinfeev",
                            "I. Denisov",
                            "Juanfran",
                            "Diego López",
                            "Santi Cazorla",
                            "Jesús Navas",
                            "J. Mascherano",
                            "A. Mirante",
                            "D. Srna",
                            "B. Schweinsteiger",
                            "Moyá",
                            "W. Rooney",
                            "Fernando Torres",
                            "S. Sorrentino",
                            "V. Tsygankov",
                            "Rúben Dias",
                            "David Neres",
                            "Raphinha",
                            "A. Harit",
                            "Richarlison",
                            "L. Martínez",
                            "F. Kessié",
                            "Luimo Boas Santos",
                            "Gabri Prestão",
                            "Melvin Parrela",
                            "Antônio Chiamuloira",
                            "Maikel Catarino",
                            "A. Lunev",
                            "André Silva",
                            "C. Pulisic",
                            "M. Dmitrović",
                            "L. Tousart",
                            "Marcos Llorente",
                            "B. Verbič",
                            "S. Bergwijn",
                            "A. Diallo",
                            "A. Golovin",
                            "M. Campaña",
                            "C. Pavón",
                            "K. Toko-Ekambi",
                            "Granell",
                            "F. Cervi",
                            "J. Weigl",
                            "V. Lindelöf",
                            "A. Rebić",
                            "A. Sanabria",
                            "R. Battaglia",
                            "M. Philipp",
                            "A. Saint-Maximin",
                            "D. Zappacosta",
                            "D. Benedetto",
                            "I. Marcone",
                            "J. Gbamin",
                            "J. Lerma",
                            "Ricardo Horta",
                            "R. Zobnin",
                            "M. Meyer",
                            "Bruma",
                            "R. Centurión",
                            "Jonny",
                            "Otávio",
                            "J. Hofmann",
                            "N. Aké",
                            "J. Hector",
                            "S. Kolašinac",
                            "G. Pizarro",
                            "Roger",
                            "Sergio Rico",
                            "L. Milivojević",
                            "D. Baselli",
                            "K. Rekik",
                            "Denis Suárez",
                            "W. Orban",
                            "Mário Rui",
                            "Iñigo Martínez",
                            "K. Zouma",
                            "Roque Mesa",
                            "J. Brooks",
                            "L. Karius",
                            "Zé Luís",
                            "D. Klaassen",
                            "M. Elyounoussi",
                            "L. Bittencourt",
                            "Sergi Darder",
                            "J. Roussillon",
                            "D. Demme",
                            "J. Gouweleeuw",
                            "M. Rojo",
                            "J. Veretout",
                            "L. Kurzawa",
                            "G. Ramírez",
                            "David López",
                            "C. Tătăruşanu",
                            "A. Mandi",
                            "D. Sidibé",
                            "Y. Konoplyanka",
                            "S. Berghuis",
                            "H. Vanaken",
                            "Campaña",
                            "M. van Ginkel",
                            "Nolito",
                            "M. Gregoritsch",
                            "Ibai Gómez",
                            "Danilo",
                            "R. Barkley",
                            "M. Ryan",
                            "Sergio León",
                            "B. Stambouli",
                            "J. Guilavogui",
                            "Sérgio Oliveira",
                            "D. Caligiuri",
                            "C. Wilson",
                            "P. Jones",
                            "Borja García",
                            "Y. Belhanda",
                            "G. Pezzella",
                            "Jaume Costa",
                            "C. Tosun",
                            "Escudero",
                            "Kike García",
                            "Elkeson",
                            "Ricardo Goulart",
                            "J. Guðmundsson",
                            "N. Clyne",
                            "M. Hitz",
                            "De Marcos",
                            "B. Mee",
                            "Rafael",
                            "Iborra",
                            "J. Wilshere",
                            "B. Hübner",
                            "Souza",
                            "F. Coquelin",
                            "Alex Teixeira",
                            "A. Dzagoev",
                            "I. Smolnikov",
                            "Y. M'Vila",
                            "K. Asamoah",
                            "R. Zieler",
                            "D. Drinkwater",
                            "N. Kalinić",
                            "Mariano",
                            "S. Feghouli",
                            "Adrien Silva",
                            "Fernando",
                            "I. Traoré",
                            "G. Mercado",
                            "N. Petersen",
                            "O. Karnezis",
                            "M. Sakho",
                            "Sidnei",
                            "S. Jovetić",
                            "Eder",
                            "J. Hernández",
                            "Fabricio",
                            "Kiko Casilla",
                            "Ángel",
                            "M. Schneiderlin",
                            "M. Fellaini",
                            "P. Wernbloom",
                            "D. Ospina",
                            "S. Mignolet",
                            "A. Begović",
                            "N. Şahin",
                            "R. Bertrand",
                            "A. Masiello",
                            "T. Walcott",
                            "Charles",
                            "T. Heaton",
                            "H. Ben Arfa",
                            "D. Abraham",
                            "E. Lavezzi",
                            "S. Kalou",
                            "J. Farfán",
                            "R. Babel",
                            "A. Young",
                            "J. Hart",
                            "L. López",
                            "D. Baier",
                            "B. Yılmaz",
                            "R. Adler",
                            "S. Lichtsteiner",
                            "E. Adebayor",
                            "E. Belözoğlu",
                            "Loren",
                            "Éder Militão",
                            "F. Chiesa",
                            "M. Lazzari",
                            "A. Hakimi",
                            "S. Nakajima",
                            "L. Jović",
                            "S. Ascacíbar",
                            "A. Lafont",
                            "T. Alexander-Arnold",
                            "F. Krovinović",
                            "Sidney Pessinho",
                            "Everticinho",
                            "Claudio Coíntra",
                            "Ronaldo Esler",
                            "P. Lees-Melou",
                            "B. Chilwell",
                            "João Novais",
                            "D. Calabria",
                            "F. Mendy",
                            "L. Pellegrini",
                            "Soares",
                            "Daniel Podence",
                            "M. Díaz",
                            "G. Martínez",
                            "M. Eggestein",
                            "Trezeguet",
                            "N. Amiri",
                            "Vallejo",
                            "J. Gomez",
                            "Diogo Jota",
                            "Joan Jordán",
                            "Dyego Sousa",
                            "A. Marušić",
                            "David Soria",
                            "V. Rongier",
                            "W. Weghorst",
                            "O. Al Soma",
                            "M. Nakamba",
                            "Petros",
                            "Pablo Maffeo",
                            "Y. Mina",
                            "M. Dúbravka",
                            "Diego Carlos",
                            "D. Djené",
                            "G. Simeone",
                            "M. Meza",
                            "Bastos",
                            "S. Lobotka",
                            "Y. Tielemans",
                            "Marcelo Goiano",
                            "K. Tete",
                            "Capa",
                            "M. Sportiello",
                            "Jemerson",
                            "N. Maksimović",
                            "D. Zapata",
                            "J. Correa",
                            "E. Rigoni",
                            "C. Izquierdoz",
                            "W. Barrios",
                            "J. Mojica",
                            "A. Selikhov",
                            "A. Iwobi",
                            "D. Laxalt",
                            "N. Bentaleb",
                            "N. Stark",
                            "M. Lemina",
                            "L. Dendoncker",
                            "Ricardo Esgaio",
                            "P. Sisto",
                            "P. Max",
                            "R. Gagliardini",
                            "Pere Pons",
                            "D. Berardi",
                            "M. Halstenberg",
                            "J. Quintero",
                            "Tiago Volpi",
                            "Óliver Torres",
                            "Omar Mascarell",
                            "H. Sakai",
                            "Andreas Pereira",
                            "A. Januzaj",
                            "B. Cristante",
                            "Matheus",
                            "B. Traoré",
                            "Y. Poulsen",
                            "L. Trossard",
                            "M. Arnold",
                            "M. De Sciglio",
                            "Leo Baptistao",
                            "V. Chiricheş",
                            "L. Pavoletti",
                            "A. Cragno",
                            "L. Castro",
                            "N. Füllkrug",
                            "F. Fajr",
                            "R. Jiménez",
                            "E. Sala",
                            "S. García",
                            "B. Reynet",
                            "Pozuelo",
                            "A. Trebel",
                            "J. Lascelles",
                            "T. Kongolo",
                            "A. Carrillo",
                            "Álvaro",
                            "G. Defrel",
                            "Fernando",
                            "V. Darida",
                            "R. Saponara",
                            "Pedro Mendes",
                            "C. Schindler",
                            "N. Chadli",
                            "Arbilla",
                            "L. Dunk",
                            "P. Hernández",
                            "J. Guidetti",
                            "Sergi Gómez",
                            "Oriol Romeu",
                            "Lucas Pérez",
                            "B. Natcho",
                            "Cláudio Ramos",
                            "F. Lejeune",
                            "G. Krychowiak",
                            "N. Lodeiro",
                            "O. Özyakup",
                            "C. Tévez",
                            "K. Papadopoulos",
                            "M. Gradel",
                            "M. Debuchy",
                            "V. Moses",
                            "Z. Junuzović",
                            "Granero",
                            "J. Baumgartlinger",
                            "Fábio Coentrão",
                            "B. Costil",
                            "Hilton",
                            "N. Gudelj",
                            "L. Pratto",
                            "E. Hernández",
                            "Jurado",
                            "R. Cabella",
                            "Rafael Tolói",
                            "C. Bravo",
                            "Hernanes",
                            "K. Honda",
                            "A. Dzyuba",
                            "J. Holebas",
                            "Javi García",
                            "Sergio",
                            "M. Cáceres",
                            "Daniel Carriço",
                            "J. Cork",
                            "J. Tomkins",
                            "Guilherme",
                            "Gervinho",
                            "J. Shelvey",
                            "R. Eremenko",
                            "R. Vormer",
                            "J. Lens",
                            "Adriano",
                            "S. Cook",
                            "L. Podolski",
                            "C. Ansaldi",
                            "Manu García",
                            "R. Alessandrini",
                            "J. Ward-Prowse",
                            "M. Harnik",
                            "B. Moukandjo",
                            "G. Pereiro",
                            "G. Castro",
                            "Aarón Martín",
                            "F. Johnson",
                            "L. López",
                            "M. Dossevi",
                            "Caiuby",
                            "Gabriel",
                            "Iván Ramis",
                            "M. Suchý",
                            "T. Vilhena",
                            "E. Çolak",
                            "V. Germain",
                            "G. Hoarau",
                            "Sergio García",
                            "E. Choupo-Moting",
                            "J. Pinola",
                            "J. Hendrix",
                            "J. Izquierdo",
                            "S. Sydorchuk",
                            "C. Grenier",
                            "T. Strobl",
                            "V. Odjidja-Ofoe",
                            "N. Guzmán",
                            "F. Fabra",
                            "J. Maddison",
                            "K. El Ahmadi",
                            "M. Carcela-González",
                            "M. Gabbiadini",
                            "Gomes",
                            "M. Ritchie",
                            "G. Bou",
                            "Javi Fuego",
                            "E. Akbaba",
                            "J. Amavi",
                            "R. Malinovskyi",
                            "D. Welbeck",
                            "G. Conti",
                            "Bruno",
                            "Garry Rodrigues",
                            "A. Schwolow",
                            "L. Cook",
                            "P. Pérez",
                            "Gazzolisco",
                            "Jonatan Soriano",
                            "Rubén Peña",
                            "Mikel San José",
                            "P. Groß",
                            "L. Baines",
                            "A. Ogbonna",
                            "Juan Jesus",
                            "J. Martínez",
                            "N. Elvedi",
                            "G. Moreno",
                            "J. Valdivia",
                            "A. Carroll",
                            "Luís Neto",
                            "A. Pyatov",
                            "T. Gutiérrez",
                            "Álex Remiro",
                            "Wilson Eduardo",
                            "Jorge Meré",
                            "M. Elneny",
                            "D. Torres",
                            "Y. Bounou",
                            "A. Prijović",
                            "A. Jahanbakhsh",
                            "J. Calleri",
                            "Simão Acunha",
                            "N. Müller",
                            "L. Ocampos",
                            "J. Rodriguez",
                            "V. Ibišević",
                            "S. Rondón",
                            "Victor Sánchez",
                            "D. Suárez",
                            "K. Huntelaar",
                            "L. Dubois",
                            "André Pinto",
                            "K. Lala",
                            "O. Kıvrak",
                            "A. Bertolacci",
                            "E. Giaccherini",
                            "A. Živković",
                            "R. Ábila",
                            "P. Diop",
                            "D. Garmash",
                            "T. Chandler",
                            "R. Klavan",
                            "A. Miranchuk",
                            "D. Da Silva",
                            "D. Benaglio",
                            "T. Rincón",
                            "M. Pereira",
                            "C. Borges",
                            "J. Sand",
                            "Markel Bergara",
                            "Vágner Love",
                            "B. Bourigeaud",
                            "R. Soriano",
                            "D. Kuzyaev",
                            "R. Sambueza",
                            "Montoya",
                            "A. Poli",
                            "C. Austin",
                            "L. Tonelli",
                            "M. Zárate",
                            "J. Sancho",
                            "D. Basta",
                            "Marçal",
                            "Munir",
                            "G. Sio",
                            "J. McCarthy",
                            "J. Aquino",
                            "H. Pérez",
                            "Jô",
                            "R. Gurtner",
                            "C. Sánchez",
                            "M. Sissoko",
                            "W. Anton",
                            "E. Skhiri",
                            "Rúben Vezo",
                            "Jorge Molina",
                            "M. Hasebe",
                            "A. Schürrle",
                            "O. Ighalo",
                            "L. Acosta",
                            "V. Babacan",
                            "R. Aguilar",
                            "Yeray",
                            "J. Defoe",
                            "L. Schøne",
                            "C. Ünder",
                            "M. Dabbur",
                            "Roberto",
                            "Djaniny",
                            "Wallace",
                            "Pedro Obiang",
                            "D. Heintz",
                            "N. Mukiele",
                            "T. Vermaelen",
                            "I. Abate",
                            "Diego Llorente",
                            "C. Wood",
                            "Formosandrinho",
                            "E. Pulgar",
                            "V. Vasin",
                            "V. Grifo",
                            "A. Turan",
                            "J. dos Santos",
                            "D. Schwaab",
                            "M. Schmelzer",
                            "L. Spinazzola",
                            "A. Dragović",
                            "D. Pröpper",
                            "R. Inglese",
                            "A. Marchesín",
                            "R. De Paul",
                            "C. Gentner",
                            "G. Murray",
                            "Rafael Carioca",
                            "A. McCarthy",
                            "L. Chichizola",
                            "D. Zakaria",
                            "G. Dzhikiya",
                            "N. Castillo",
                            "D. Origi",
                            "O. Yokuşlu",
                            "D. Cheryshev",
                            "D. Selke",
                            "Wendell",
                            "M. Layún",
                            "Y. Sabaly",
                            "P. Cutrone",
                            "F. Marchetti",
                            "W. Cyprien",
                            "G. Paletta",
                            "F. Caicedo",
                            "Jordi Masip",
                            "B. Espinosa",
                            "M. Benassi",
                            "P. Jagielka",
                            "J. Kucka",
                            "R. Brady",
                            "A. Szymanowski",
                            "W. Reid",
                            "Cédric",
                            "R. Civelli",
                            "R. Loftus-Cheek",
                            "S. De Maio",
                            "S. Brown",
                            "A. Mitrović",
                            "P. Skjelbred",
                            "D. Cvitanich",
                            "K. Lasagna",
                            "R. Palacio",
                            "M. Wolf",
                            "E. Gigliotti",
                            "N. Jørgensen",
                            "Laguardia",
                            "J. Lukaku",
                            "J. Augustin",
                            "M. Diakhaby",
                            "Douglas",
                            "N. Pejčinović",
                            "D. van de Beek",
                            "Borja Iglesias",
                            "G. Shibasaki",
                            "W. Hughes",
                            "S. Boufal",
                            "T. Kehrer",
                            "M. Lang",
                            "E. Gutiérrez",
                            "D. Upamecano",
                            "Jefferson",
                            "W. Benítez",
                            "E. Bardhi",
                            "K. Mbodji",
                            "B. Sarr",
                            "F. Ferreyra",
                            "Danilo",
                            "A. Ayew",
                            "K. Mitroglou",
                            "J. Villar",
                            "P. Herrmann",
                            "D. da Costa",
                            "V. Fischer",
                            "Wesley",
                            "D. Ginczek",
                            "F. Kostić",
                            "R. Fraser",
                            "Cote",
                            "H. Winks",
                            "K. Mbabu",
                            "M. Hinteregger",
                            "L. Acosta",
                            "Sidcley",
                            "M. Jørgensen",
                            "M. Fabián",
                            "Carlos Eduardo",
                            "Rubén Castro",
                            "L. Augustinsson",
                            "S. Aziz",
                            "G. Ochoa",
                            "P. Hetemaj",
                            "André André",
                            "Vinícius Júnior",
                            "B. Džemaili",
                            "Juanpe",
                            "K. Fortounis",
                            "M. Vorm",
                            "B. Oczipka",
                            "R. Bentancur",
                            "T. Hernández",
                            "M. Lowton",
                            "I. Diop",
                            "B. André",
                            "C. Piccini",
                            "Paulinho",
                            "A. Diawara",
                            "Yuri Berchiche",
                            "F. Kamano",
                            "F. Cartabia",
                            "E. Ünal",
                            "I. Radovanović",
                            "Renan Ribeiro",
                            "Jony",
                            "D. Buonanotte",
                            "Tomás Pina",
                            "N. Pallois",
                            "D. Latza",
                            "F. Belluschi",
                            "O. Abdulrahman",
                            "O. Trejo",
                            "N. Barella",
                            "Angeliño",
                            "Vieirundinho",
                            "F. Orellana",
                            "F. Grillitsch",
                            "C. Ortíz",
                            "Bruno Viana",
                            "J. Maidana",
                            "R. Funes Mori",
                            "D. Kohr",
                            "F. Higuaín",
                            "A. Barák",
                            "F. Andone",
                            "Adrián",
                            "G. González",
                            "Otávio",
                            "D. Janmaat",
                            "R. Funes Mori",
                            "P. Schick",
                            "Aleix Vidal",
                            "A. Schöpf",
                            "W. Boly",
                            "Alberto Moreno",
                            "C. Villanueva",
                            "M. Weiser",
                            "G. Escalante",
                            "M. Holgate",
                            "J. Hopf",
                            "D. Zurutuza",
                            "Juanmi",
                            "K. Gibbs",
                            "F. Fernández",
                            "L. Kalinić",
                            "N. Radoja",
                            "N. Blandi",
                            "David Juncà",
                            "Wu Lei",
                            "Gabriel Boschilia",
                            "Iuri Medeiros",
                            "M. Phillips",
                            "Iván Cuéllar",
                            "J. Lössl",
                            "Mario Suárez",
                            "W. Bony",
                            "S. Doumbia",
                            "D. Reyes",
                            "Bernat",
                            "V. Behrami",
                            "S. Langkamp",
                            "J. Sosa",
                            "A. Touré",
                            "Jesé",
                            "D. Ings",
                            "M. Esser",
                            "F. Acheampong",
                            "R. Knoche",
                            "O. Vlachodimos",
                            "J. Denayer",
                            "S. Rode",
                            "Wendel",
                            "A. Nagy",
                            "Alfa Semedo",
                            "A. Barnes",
                            "Alan Kardec",
                            "Marcelo",
                            "E. Boateng",
                            "Dalbert",
                            "A. Halilović",
                            "I. Popov",
                            "T. Cleverley",
                            "M. Livaja",
                            "M. Uribe",
                            "P. Bargfrede",
                            "J. Jankto",
                            "Junior Firpo",
                            "D. D'Ambrosio",
                            "D. Boyko",
                            "M. Díaz",
                            "S. Vokes",
                            "Héldon",
                            "Mario Hermoso",
                            "F. Bartels",
                            "K. Malcuit",
                            "R. Marin",
                            "Ayoze Pérez",
                            "Júnior Moraes",
                            "V. Berisha",
                            "R. Freuler",
                            "Ganso",
                            "Vicente Gómez",
                            "M. Pašalić",
                            "Vitor Hugo",
                            "B. Fornaroli",
                            "R. Snodgrass",
                            "Francisco Geraldes",
                            "I. Ordets",
                            "D. Santon",
                            "M. Niang",
                            "O. Wendt",
                            "C. Riveros",
                            "F. Benković",
                            "M. Torres",
                            "M. Noble",
                            "M. Rashica",
                            "C. Benteke",
                            "Rômulo",
                            "D. Pabón",
                            "Embarba",
                            "C. Kerbrat",
                            "L. Teodorczyk",
                            "Alexo Baia",
                            "David Seijalbo",
                            "N. Nández",
                            "L. Rupp",
                            "Jordi Amat",
                            "W. Caballero",
                            "F. Di Francesco",
                            "O. El Kaddouri",
                            "T. Rogić",
                            "G. Töre",
                            "M. Destro",
                            "Josué",
                            "Ki Sung Yueng",
                            "H. Onyekuru",
                            "N. Pépé",
                            "Matheus Pereira",
                            "Y. Salibur",
                            "E. Vargas",
                            "L. Magallán",
                            "Danny",
                            "C. Hérelle",
                            "E. Mangala",
                            "O. Selnæs",
                            "Víctor Vázquez",
                            "Diego Mariño",
                            "Carles Planas",
                            "G. Fernández",
                            "Soldado",
                            "A. Ekdal",
                            "Gedson Fernandes",
                            "M. Darmian",
                            "N. Chalobah",
                            "R. Pizarro",
                            "André Simões",
                            "S. Tshabalala",
                            "L. Rossettini",
                            "F. Viviani",
                            "M. de Roon",
                            "Rubén Duarte",
                            "Y. Ōsako",
                            "Gil",
                            "A. Ruiz",
                            "P. van Aanholt",
                            "S. Meïté",
                            "K. Dolberg",
                            "Juli Freitinho",
                            "L. Vietto",
                            "A. Izzo",
                            "A. Paloschi",
                            "G. Gönül",
                            "Llorente",
                            "J. Morel",
                            "G. Kakuta",
                            "João Pedro",
                            "S. García",
                            "Eltildo Correia",
                            "Kenedy",
                            "M. Moralez",
                            "N. Vukčević",
                            "F. Borini",
                            "I. Sarr",
                            "C. Clark",
                            "Mata",
                            "M. Albrighton",
                            "A. Gray",
                            "F. Guarín",
                            "Yoel",
                            "J. Cuadrado",
                            "S. Widmer",
                            "B. Dzsudzsák",
                            "P. Mantalos",
                            "S. Proto",
                            "A. Mehmedi",
                            "Pablo",
                            "I. Slimani",
                            "C. Erkin",
                            "D. Chygrynskyi",
                            "Beto",
                            "A. Samaris",
                            "G. Lapadula",
                            "Dênildo Stein",
                            "S. Padt",
                            "S. Taïder",
                            "F. Klaus",
                            "H. Nordtveit",
                            "L. Zuffi",
                            "Emilio Piodão",
                            "S. Zuber",
                            "J. Palomino",
                            "Y. Mutō",
                            "J. Altidore",
                            "M. Barbosa",
                            "G. Laborde",
                            "P. Baysse",
                            "Eric Botteghin",
                            "Iván Alejo",
                            "S. Blanco",
                            "Thiago Mendes",
                            "D. Brosinski",
                            "T. Monconduit",
                            "Andrés Fernández",
                            "Eraso",
                            "S. Hanni",
                            "M. Konaté",
                            "C. Théréau",
                            "A. Donatti",
                            "T. Jedvaj",
                            "Pedro Henrique",
                            "J. Briand",
                            "F. Lustenberger",
                            "J. Ayew",
                            "S. Sanogo",
                            "R. Thomas",
                            "Rafael Cachoira",
                            "N. Sansone",
                            "E. Bičakčić",
                            "J. Veltman",
                            "A. Knockaert",
                            "Douglas Santos",
                            "S. Bocchetti",
                            "M. Dembélé",
                            "E. Valencia",
                            "F. Mollet",
                            "D. Dumfries",
                            "Koo Ja Cheol",
                            "A. Petagna",
                            "De Tomás",
                            "E. Balanta",
                            "T. Koubek",
                            "J. Allen",
                            "Alan Carvalho",
                            "S. Ristovski",
                            "Maicón",
                            "D. Quintero",
                            "P. Højbjerg",
                            "I. Santini",
                            "Vieirinha",
                            "M. Boselli",
                            "L. Antonelli",
                            "B. Embolo",
                            "V. Eysseric",
                            "C. Salcedo",
                            "A. Ranocchia",
                            "L. Unnerstall",
                            "T. Baumgartl",
                            "F. Bustos",
                            "P. Jansson",
                            "W. Vainqueur",
                            "S. Kverkvelia",
                            "Rubén Blanco",
                            "P. Aguilar",
                            "A. Ndiaye Diedhiou",
                            "Rafinha",
                            "D. Limberský",
                            "G. Cabral",
                            "J. De Guzmán",
                            "S. Terodde",
                            "J. Fernandes",
                            "Kiko Femenía",
                            "Recio",
                            "A. Samedov",
                            "A. Smith",
                            "Maurício",
                            "D. Stephens",
                            "Miguel Lopes",
                            "I. Belfodil",
                            "J. Campbell",
                            "Marc Roca",
                            "M. Veljković",
                            "J. Willems",
                            "A. Lennon",
                            "F. Forster",
                            "Júnior Caiçara",
                            "C. Biraghi",
                            "Aritz Elustondo",
                            "Fred Aníbão",
                            "O. Romero",
                            "Nelsildo Reis",
                            "V. Koziello",
                            "A. Cresswell",
                            "Alex Berenguer",
                            "C. Davies",
                            "C. Kouyaté",
                            "Y. Kobayashi",
                            "Camarasa",
                            "J. Martin",
                            "J. Grealish",
                            "D. Pelkas",
                            "J. Montero",
                            "J. Forrest",
                            "Varela",
                            "M. Antenucci",
                            "R. Durmisi",
                            "P. Schwegler",
                            "A. Hunt",
                            "Aday Benítez",
                            "K. Tierney",
                            "Jaume",
                            "S. Gigot",
                            "I. Brizuela",
                            "A. Souquet",
                            "A. Delort",
                            "P. Zabaleta",
                            "Andeson Trigo",
                            "J. Gnagnon",
                            "Mosquera",
                            "I. Bebou",
                            "R. Morrison",
                            "L. Christodoulopoulos",
                            "J. McArthur",
                            "R. Olsen",
                            "W. Hoedt",
                            "R. Holding",
                            "F. Montero",
                            "N. Sliti",
                            "J. Vázquez",
                            "Rodrigo Ely",
                            "M. Benítez",
                            "Y. Yazıcı",
                            "Y. Sankharé",
                            "A. N'Diaye",
                            "S. Bell",
                            "K. Linetty",
                            "F. Uduokhai",
                            "M. Samatta",
                            "Barragán",
                            "R. Hamouma",
                            "L. Skorupski",
                            "Toño García",
                            "A. Szalai",
                            "Raúl Navas",
                            "B. Koné",
                            "J. Brekalo",
                            "Diego Tardelli",
                            "A. Hegazi",
                            "M. Sels",
                            "D. Gray",
                            "M. Pjaca",
                            "M. Arambarri",
                            "A. Ćorić",
                            "T. Gebre Selassie",
                            "C. Nkunku",
                            "M. Topal",
                            "Léo Matos",
                            "F. Kainz",
                            "B. Henrichs",
                            "Victildinho",
                            "D. Praet",
                            "A. Umar",
                            "J. Orozco",
                            "N. El Zhar",
                            "O. Colley",
                            "J. Aholou",
                            "G. Clichy",
                            "Rubén Sobrino",
                            "J. Iturbe",
                            "H. Soudani",
                            "M. Bradley",
                            "Z. Labyad",
                            "D. Mbokani",
                            "T. Mangani",
                            "A. Lunin",
                            "E. Insúa",
                            "N. Domingo",
                            "D. Yedlin",
                            "D. González",
                            "T. Kraft",
                            "M. Simon",
                            "Davi Parrela",
                            "N. Domínguez",
                            "C. Dawson",
                            "A. Rusnák",
                            "Paulo Oliveira",
                            "A. Gomis",
                            "H. Tekin",
                            "Tozé",
                            "R. Ruidíaz",
                            "J. Hogg",
                            "L. Holtby",
                            "A. Djiku",
                            "O. Alonso",
                            "S. Berge",
                            "C. Zambrano",
                            "M. Antonio",
                            "J. Clasie",
                            "Diego Rico",
                            "Mossoró",
                            "G. Donsah",
                            "Felipe",
                            "S. Fofana",
                            "Pablo Santos",
                            "J. Svensson",
                            "E. Roco",
                            "F. Midtsjø",
                            "Francis",
                            "Ivi",
                            "Unai Núñez",
                            "L. Lerager",
                            "P. De Blasis",
                            "M. Zajc",
                            "J. Stanislas",
                            "Lucas Evangelista",
                            "M. Stoch",
                            "S. van Beek",
                            "Fabrio Farinha",
                            "M. Kozáčik",
                            "Fran Sol",
                            "R. Otero",
                            "G. Maripán",
                            "M. Braithwaite",
                            "E. Dilaver",
                            "R. Álvarez",
                            "A. Masuaku",
                            "Rolando",
                            "Fran Rico",
                            "D. Tarasov",
                            "Alcalá",
                            "Alan Patrick",
                            "L. Refaelov",
                            "Y. Gazinskiy",
                            "Palhinha",
                            "Balenziaga",
                            "R. Petrović",
                            "K. Ansarifard",
                            "M. Ninković",
                            "A. Talavera",
                            "A. Barrada",
                            "J. Korb",
                            "F. Gutiérrez",
                            "T. Bongonda",
                            "Simão Donatinho",
                            "Luís Hernández",
                            "L. Balogun",
                            "M. Rog",
                            "B. Dočkal",
                            "J. Durmaz",
                            "T. Kádár",
                            "E. Andrada",
                            "Z. Steffen",
                            "M. Lestienne",
                            "M. Alustiza",
                            "Borja Mayoral",
                            "D. Bonera",
                            "Saúl Berjón",
                            "C. Beauvue",
                            "Danilo",
                            "J. Hernández",
                            "J. Hendrick",
                            "M. Lopez",
                            "F. Hanin",
                            "D. Machís",
                            "A. Potuk",
                            "Idris",
                            "N. Cardozo",
                            "Javi López",
                            "G. Pandev",
                            "Júlio Tavares",
                            "D. Liénard",
                            "Y. Pelé",
                            "L. Sepe",
                            "J. Bruma",
                            "O. Duarte",
                            "A. Franco",
                            "Dani Olmo",
                            "F. Di Santo",
                            "Jozabed",
                            "G. Carrillo",
                            "M. Zeegelaar",
                            "G. Ferrari",
                            "O. Şahiner",
                            "I. Traoré",
                            "T. Arslan",
                            "N. Araújo",
                            "S. Armstrong",
                            "K. Billiat",
                            "Ivan Cavaleiro",
                            "E. Cabaco",
                            "Silas Almeim",
                            "C. Kameni",
                            "Hélder Costa",
                            "E. Durm",
                            "Emerson",
                            "G. Haraguchi",
                            "C. Fuchs",
                            "E. Kalinski",
                            "Rafael",
                            "F. Frei",
                            "M. Risse",
                            "V. Cáceres",
                            "Renan Bressan",
                            "Lucas Lima",
                            "M. Silvestre",
                            "Portillo",
                            "F. Rønnow",
                            "N. Spolli",
                            "S. Rajković",
                            "R. Berić",
                            "V. Hernández",
                            "Claudemir",
                            "T. Jantschke",
                            "L. Schaub",
                            "P. Tschauner",
                            "Gabrisco Aníbal",
                            "B. Feilhaber",
                            "A. Grassi",
                            "N. Vikonis",
                            "P. Ntep",
                            "L. Vangioni",
                            "S. Okazaki",
                            "Diego Castro",
                            "C. Jallet",
                            "O. Pineda",
                            "A. Mounier",
                            "Sandro",
                            "N. Redmond",
                            "Gálvez",
                            "A. Song",
                            "E. Badu",
                            "M. Agu",
                            "Jason",
                            "S. Cristóforo",
                            "L. Butelle",
                            "Allan Bardinho",
                            "P. Dummett",
                            "H. Villalba",
                            "K. Amian",
                            "José Mirazar",
                            "A. Hernández",
                            "Ailton Guevara",
                            "O. Akhmedov",
                            "Naldo",
                            "Y. Ayoub",
                            "A. Ring",
                            "B. Ndiaye",
                            "Kaku",
                            "Adilson Edrada",
                            "A. Ibargüen",
                            "Iraizoz",
                            "N. Nikolić",
                            "J. Kurtić",
                            "K. Wimmer",
                            "A. Mejía",
                            "A. Barreca",
                            "Gil Dias",
                            "J. Locadia",
                            "S. Kryvtsov",
                            "O. Peralta",
                            "C. Budescu",
                            "A. Raggi",
                            "R. Donk",
                            "Edgar Méndez",
                            "L. De Silvestri",
                            "M. Saracchi",
                            "D. Congré",
                            "M. Fritzler",
                            "T. Kolodziejczak",
                            "Caio Nunson",
                            "Felipe Vizeu",
                            "J. Damm",
                            "Guilherme",
                            "G. Nkoudou",
                            "Joel Robles",
                            "B. Zungu",
                            "Otávio Cairinho",
                            "P. Gouano",
                            "C. Domínguez",
                            "R. Falk",
                            "André Ramalho",
                            "G. Schennikov",
                            "M. Morozyuk",
                            "J. van der Heijden",
                            "A. Musa",
                            "A. Diaby",
                            "G. İnler",
                            "L. Cigarini",
                            "Júnior Urso",
                            "B. Butko",
                            "R. Thomas",
                            "M. Jensen",
                            "Burgui",
                            "A. Meret",
                            "M. Gonalons",
                            "D. Valdés",
                            "Marafona",
                            "R. Karsdorp",
                            "I. Opara",
                            "K. Laimer",
                            "O. Kamara",
                            "S. Gentiletti",
                            "Serey Dié",
                            "A. Westwood",
                            "C. Ciano",
                            "A. Conti",
                            "Bojan",
                            "C. Vargas",
                            "Éder",
                            "Y. Benzia",
                            "W. Hennessey",
                            "E. Thommy",
                            "Bustinza",
                            "Bernardo",
                            "P. Cissé",
                            "Oier",
                            "D. Gayle",
                            "Joelinton",
                            "A. Pérez",
                            "B. Jones",
                            "J. Drmić",
                            "M. Mount",
                            "A. McGregor",
                            "O. Elabdellaoui",
                            "R. Steffen",
                            "K. Kanga",
                            "J. Ananidze",
                            "S. Ilsanker",
                            "A. Blake",
                            "Nicholas Aldair",
                            "R. Sessegnon",
                            "Jorginhson",
                            "Carlitos",
                            "L. Nguyen",
                            "A. Paschalakis",
                            "Fabrício",
                            "M. Coco",
                            "K. Babacar",
                            "Postigo",
                            "Renato Sanches",
                            "M. Caruzzo",
                            "G. Konan",
                            "S. Mounié",
                            "P. Capelle",
                            "T. Davies",
                            "N. Dirar",
                            "J. Toornstra",
                            "Paulinho",
                            "S. Larsson",
                            "P. Tau",
                            "J. Kluivert",
                            "H. Ayala",
                            "Miguel Silva",
                            "D. Rolán",
                            "L. Klostermann",
                            "G. Rodríguez",
                            "M. Locatelli",
                            "F. Caputo",
                            "A. Roa",
                            "Keko",
                            "A. El Khayati",
                            "F. Schär",
                            "A. Haidara",
                            "Chema Rodríguez",
                            "G. dos Santos",
                            "T. Bifouma",
                            "Dani Rochelinhas",
                            "M. Ostrzolek",
                            "Sandro",
                            "L. Deaux",
                            "J. Vuković",
                            "J. Hansen",
                            "Gonçalo Paciência",
                            "Córdoba",
                            "P. Pekarík",
                            "Ximo Navarro",
                            "Pablo Hernández",
                            "G. Kashia",
                            "Cássio",
                            "S. Bamba",
                            "S. Kums",
                            "Fábio Martins",
                            "M. Suárez",
                            "S. Mitrović",
                            "D. Aogo",
                            "B. Engels",
                            "F. Tait",
                            "D. Zagadou",
                            "M. Diamé",
                            "A. Younes",
                            "B. Verstraete",
                            "K. Akpoguma",
                            "B. Santamaria",
                            "E. Moretti",
                            "H. Behrens",
                            "M. Maignan",
                            "Y. Karamoh",
                            "V. Ignatiev",
                            "A. Thomasson",
                            "D. Amartey",
                            "R. Özcan",
                            "A. Donnarumma",
                            "Timor",
                            "C. McGregor",
                            "R. Martínez",
                            "V. Buyalskyi",
                            "H. Arter",
                            "A. Mawson",
                            "F. Guilbert",
                            "M. Lemos",
                            "S. Sturaro",
                            "A. Duncan",
                            "Marlon",
                            "M. Isla",
                            "Thiago Maia",
                            "Y. Aït Bennasser",
                            "O. Toivonen",
                            "J. Urretaviscaya",
                            "Yuri Ribeiro",
                            "N. Tomović",
                            "F. Roncaglia",
                            "R. Botta",
                            "R. Mandragora",
                            "A. Adomah",
                            "D. Samassékou",
                            "M. Yoshida",
                            "N. Viergever",
                            "R. Amalfitano",
                            "D. Cataldi",
                            "Martín",
                            "Tiago Pinto",
                            "Fernandinho",
                            "C. Cueva",
                            "M. Gaćinović",
                            "G. Shoji",
                            "L. Rigoni",
                            "M. Krmenčík",
                            "M. Mevlja",
                            "C. Daniels",
                            "K. Stafylidis",
                            "Sabin Merino",
                            "A. Flint",
                            "Brais Méndez",
                            "Merino",
                            "S. Missiroli",
                            "Serantes",
                            "V. Guzmán",
                            "D. Biseswar",
                            "E. Mas",
                            "Nuno Pinto",
                            "Carlos Mané",
                            "Borja Valle",
                            "Zeca",
                            "C. Toselli",
                            "M. Bizot",
                            "K. Ayhan",
                            "Ricardo Ferreira",
                            "Hernâni",
                            "M. Çağıran",
                            "W. Morgan",
                            "J. Alonso",
                            "M. Wakaso",
                            "K. Traoré",
                            "Y. Mvogo",
                            "Kaíquão Castro",
                            "K. Fofana",
                            "P. Hurtado",
                            "D. Bocanegra",
                            "Melero",
                            "Borja Bastón",
                            "O. Murillo",
                            "O. Onazi",
                            "C. Günter",
                            "I. Amadou",
                            "Unai López",
                            "K. Iheanacho",
                            "C. Söyüncü",
                            "B. Pearson",
                            "F. Niederlechner",
                            "S. Denswil",
                            "G. Rodríguez",
                            "P. Guiñazú",
                            "H. Hateboer",
                            "I. Fernández",
                            "L. Blas",
                            "M. Sarr",
                            "Mikel Rico",
                            "F. Neuhaus",
                            "S. İnan",
                            "C. Maggio",
                            "Mexer",
                            "F. Magnanelli",
                            "J. Figal",
                            "V. Claesson",
                            "F. Helander",
                            "J. Gondorf",
                            "R. Ghezzal",
                            "Adama",
                            "O. Duda",
                            "R. Bensebaini",
                            "L. Depoitre",
                            "N. Vlašić",
                            "Rochina",
                            "M. Doherty",
                            "C. Musonda",
                            "João Teixeira",
                            "S. Ward",
                            "Y. Cardinale",
                            "S. Francis",
                            "Lafortiscinho",
                            "M. Valdifiori",
                            "Rubén Pérez",
                            "D. Boyata",
                            "N. Mendy",
                            "Pedraza",
                            "Ricardo",
                            "Tarantini",
                            "K. Stöger",
                            "C. Mbemba",
                            "A. Limbombe",
                            "K. McDonald",
                            "O. Niasse",
                            "G. Herrera",
                            "R. Borré",
                            "E. Zukanović",
                            "A. Elis",
                            "M. Fernández",
                            "D. Rodríguez",
                            "T. Klose",
                            "A. Cornelius",
                            "Kwon Chang Hoon",
                            "C. Larin",
                            "Tchê Tchê",
                            "M. Leckie",
                            "L. Quiñones",
                            "Fontàs",
                            "K. Vermeer",
                            "A. Surman",
                            "M. Höger",
                            "S. Dann",
                            "Jovane Cabral",
                            "C. Cathcart",
                            "Zaldúa",
                            "Pelé",
                            "M. Kelly",
                            "Y. Bolasie",
                            "L. Zelarayán",
                            "Gelson Fernandes",
                            "D. Glushakov",
                            "Lee Jae Sung",
                            "Baiano",
                            "A. Hurtado",
                            "A. Mierzejewski",
                            "V. Janssen",
                            "E. Paredes",
                            "B. Alemán",
                            "P. Retsos",
                            "J. Hernández",
                            "S. Corchia",
                            "Rubén Pardo",
                            "P. Goltz",
                            "D. Türüç",
                            "B. Mechele",
                            "Kaimo Lima",
                            "R. Rodelin",
                            "Bobô",
                            "L. Ciman",
                            "D. Ba",
                            "H. Medunjanin",
                            "José Cañas",
                            "Y. Osorio",
                            "Titi",
                            "Carles Gil",
                            "P. Lasne",
                            "Lekue",
                            "A. Silva",
                            "A. Danjuma Groeneveld",
                            "C. Luyindama",
                            "L. González Pirez",
                            "Sergio Álvarez",
                            "M. Cornet",
                            "M. Schnatterer",
                            "O. Kharbin",
                            "Sergi Guardiola",
                            "T. Souček",
                            "Y. Ravet",
                            "T. Serero",
                            "B. Douglas",
                            "S. Johnstone",
                            "Medrán",
                            "J. Corona",
                            "I. Fetfatzidis",
                            "S. Romero",
                            "B. Jokič",
                            "J. Córdoba",
                            "Edvaldisco",
                            "G. Sakai",
                            "A. González",
                            "R. Rosales",
                            "J. Dueñas",
                            "N. De Préville",
                            "Diogo Figueiras",
                            "A. El Ghazi",
                            "P. Aguilar",
                            "K. Dolly",
                            "F. Mora",
                            "P. Barrientos",
                            "H. Rodallega",
                            "A. Epureanu",
                            "M. Caraglio",
                            "S. Lung",
                            "Maurício",
                            "A. Boruc",
                            "C. Gordon",
                            "F. Santander",
                            "A. Ramírez",
                            "M. Cabrera",
                            "B. Valdez",
                            "Pozo",
                            "Bruno Gaspar",
                            "N. Rigoni",
                            "I. Kahveci",
                            "Walace",
                            "R. Shawcross",
                            "David Simão",
                            "C. Rius",
                            "B. Martins Indi",
                            "P. Rosario",
                            "Álvaro García",
                            "Kauã Abranches",
                            "A. Gyan",
                            "D. Simpson",
                            "H. Seferović",
                            "R. Sobhi",
                            "P. Gazzaniga",
                            "F. Mussis",
                            "A. Masina",
                            "J. Błaszczykowski",
                            "J. Beausejour",
                            "J. Livermore",
                            "D. Kourmpelis",
                            "Nicolás Formido",
                            "J. Aidoo",
                            "Melendo",
                            "E. Pieters",
                            "Luisinho",
                            "A. Semenov",
                            "Ramalho",
                            "Kévin Rodrigues",
                            "K. Piątek",
                            "R. Vlaar",
                            "R. van Wolfswinkel",
                            "Ilie Sánchez",
                            "Ewerton",
                            "A. Chumacero",
                            "Dani Pacheco",
                            "L. Rodríguez",
                            "A. Jahović",
                            "M. Britos",
                            "M. Rits",
                            "S. Deli",
                            "H. Traoré",
                            "P. Aguedar",
                            "Crespo",
                            "Rafael",
                            "L. Öztunalı",
                            "M. Jojić",
                            "Vitor Bueno",
                            "G. Til",
                            "I. Pussetto",
                            "A. Ajeti",
                            "Luiz Araújo",
                            "A. Besedin",
                            "T. Didillon",
                            "Arana",
                            "Zainadine",
                            "K. Théophile-Catherine",
                            "A. Gianniotis",
                            "Bruno Saltor",
                            "M. Stendera",
                            "S. Kalu",
                            "Juan Cala",
                            "J. Tavernier",
                            "W. McKennie",
                            "W. Tesillo",
                            "A. Mariappa",
                            "S. Morrison",
                            "J. Brenet",
                            "B. Dack",
                            "Y. Kubo",
                            "T. Pukki",
                            "William",
                            "L. Melgarejo",
                            "J. Jones",
                            "I. Sosa",
                            "M. Ekici",
                            "A. Nyom",
                            "K. Konaté",
                            "F. Đorđević",
                            "E. Room",
                            "T. Usami",
                            "Ruben Lima",
                            "Fábio Espinho",
                            "L. Marković",
                            "J. Barrera",
                            "R. Mora",
                            "D. Lazović",
                            "M. Burda",
                            "Tana",
                            "A. Miranchuk",
                            "L. Grabban",
                            "I. Koné",
                            "J. Hušbauer",
                            "A. Soumaoro",
                            "Patric",
                            "P. Diamanka",
                            "A. Pulido",
                            "Roger Guedes",
                            "D. N'Doye",
                            "S. Johansen",
                            "I. Afellay",
                            "A. Zambo Anguissa",
                            "N. Lombaerts",
                            "C. Chambers",
                            "I. Sangaré",
                            "A. Sulu",
                            "M. Pucciarelli",
                            "R. Saïss",
                            "J. Haberer",
                            "E. Dennis",
                            "J. Kana-Biyik",
                            "V. Barkas",
                            "K. Johnsson",
                            "S. Floccari",
                            "S. Prödl",
                            "V. Laurini",
                            "A. Eschenko",
                            "S. Okaka",
                            "J. Kodjia",
                            "A. Oyongo",
                            "S. Bolat",
                            "A. Mitriţă",
                            "A. Behich",
                            "O. Tannane",
                            "F. Haroun",
                            "D. Gosling",
                            "Pedro Santos",
                            "J. Larsen",
                            "F. Bastians",
                            "J. Ralls",
                            "S. Vilakazi",
                            "Victorino Magela",
                            "Marc Navarro",
                            "K. Kamara",
                            "Dória",
                            "S. Serdar",
                            "O. Tufan",
                            "Pedro Rebocho",
                            "I. Strinić",
                            "S. Grytebust",
                            "W. Hahn",
                            "Adrianiscito",
                            "L. Fernández",
                            "A. Lozano",
                            "M. Tisserand",
                            "M. Ruben",
                            "T. Abraham",
                            "R. Neustädter",
                            "Bebé",
                            "M. Vydra",
                            "J. Leca",
                            "Carmona",
                            "C. Lema",
                            "Dentinho",
                            "L. Villafañez",
                            "D. Brasanac",
                            "S. Kljestan",
                            "W. Morelo",
                            "M. Diop",
                            "C. Benavente",
                            "A. del Valle",
                            "R. Ibarra",
                            "J. Musso",
                            "Padilhisco",
                            "F. Forestieri",
                            "A. Bedoya",
                            "A. Romao",
                            "O. Gladkyi",
                            "A. Hack",
                            "D. McCarty",
                            "K. Adénon",
                            "J. Plata",
                            "J. Stephens",
                            "M. Ødegaard",
                            "Rúben Semedo",
                            "Sequeira",
                            "I. Chochev",
                            "M. Gulde",
                            "Bruno César",
                            "F. Jara",
                            "Gabrìel",
                            "M. Bakalorz",
                            "A. Rossi",
                            "Álex Moreno",
                            "F. Hadergjonaj",
                            "O. Kucher",
                            "M. Diouf",
                            "G. Burdisso",
                            "V. Misidjan",
                            "A. Correa",
                            "R. Salin",
                            "F. Valverde",
                            "M. Etxeberría",
                            "R. Haps",
                            "Cho Hyun Woo",
                            "Y. Gourcuff",
                            "Jesus Andradaldo",
                            "P. Mpoku",
                            "D. Musto",
                            "M. Vargas",
                            "A. Baba",
                            "S. Davis",
                            "S. Özbayraklı",
                            "Mattheus Oliveira",
                            "M. Le Marchand",
                            "Régis",
                            "Nacho",
                            "B. Gibson",
                            "C. Taylor",
                            "T. Kędziora",
                            "R. Saravia",
                            "D. Drexler",
                            "S. Falette",
                            "O. Etebo",
                            "A. Cerci",
                            "L. Rodríguez",
                            "R. Hubník",
                            "J. Andersen",
                            "Fran Beltrán",
                            "D. Viera",
                            "F. Zampedri",
                            "H. Lindner",
                            "J. Sánchez Miño",
                            "M. Pavlović",
                            "A. Koné",
                            "J. Ferri",
                            "C. Bassogog",
                            "M. Diagne",
                            "J. Ibe",
                            "D. Heuer Fernandes",
                            "A. Fulgini",
                            "M. Jensen",
                            "A. Bjelland",
                            "J. Fuenzalida",
                            "Juanfran",
                            "S. Kittel",
                            "V. Rosier",
                            "K. Waston",
                            "P. Žulj",
                            "L. Grant",
                            "G. Jara",
                            "S. Lainer",
                            "Óscar Plano",
                            "De la Bella",
                            "R. Cohade",
                            "P. Morales",
                            "D. Arismendi",
                            "N. Stanciu",
                            "D. Ćaleta-Car",
                            "L. Fer",
                            "A. Williams",
                            "J. Bryan",
                            "Ricardo Costa",
                            "Ailton",
                            "R. Cota",
                            "G. Margreitter",
                            "A. Rebrov",
                            "Djavan",
                            "A. Chedjou",
                            "Luna",
                            "F. Ricca",
                            "F. Carrizo",
                            "A. Ragusa",
                            "A. Wan-Bissaka",
                            "J. Biabiany",
                            "B. Mensah",
                            "D. Padelli",
                            "D. Tošić",
                            "E. Bauthéac",
                            "Tiago Silva",
                            "A. Tameze",
                            "V. Manceau",
                            "F. Bardi",
                            "L. Advíncula",
                            "J. Gallardo",
                            "Enaldo Toxeto",
                            "Camilo",
                            "J. Schmid",
                            "Welthon",
                            "Moi Gómez",
                            "Marc Muniesa",
                            "Samu Saiz",
                            "J. Sorbon",
                            "S. Long",
                            "S. Wuytens",
                            "S. Araujo",
                            "André Martins",
                            "S. March",
                            "F. Chafik",
                            "K. Ajer",
                            "K. Grosicki",
                            "Alex Bergantiños",
                            "E. Derdiyok",
                            "David Braz",
                            "D. Roef",
                            "Lombán",
                            "J. Drobný",
                            "A. Acquah",
                            "T. Smith",
                            "R. Nuzzolo",
                            "G. Jung",
                            "M. Iturra",
                            "Molinero",
                            "Pedro Sá",
                            "D. Pérez",
                            "B. Cesar",
                            "D. Braghieri",
                            "C. Álvarez",
                            "Carlos Ponck",
                            "R. Assalé",
                            "M. Miazga",
                            "Léo Bonatini",
                            "B. Fernández",
                            "S. Hutchinson",
                            "S. Rybalka",
                            "N. Acevedo",
                            "J. Lucero",
                            "G. Chakvetadze",
                            "I. Fossum",
                            "V. Karavaev",
                            "T. Leibold",
                            "G. Arias",
                            "T. Huddlestone",
                            "A. Clayton",
                            "K. Nakamura",
                            "L. Koné",
                            "M. Vejinović",
                            "H. Van Crombrugge",
                            "M. Russ",
                            "Pietrson Mendes",
                            "Salvi Sánchez",
                            "E. Pavez",
                            "I. Kovács",
                            "Nildo Petrolina",
                            "Y. Seleznyov",
                            "C. Löwe",
                            "V. Cantillo",
                            "J. Ward",
                            "S. Skrzybski",
                            "Diego Oliveira",
                            "Luis Milla",
                            "A. Ba",
                            "Jaim Abra",
                            "S. von Bergen",
                            "S. Armenteros",
                            "Y. Öztekin",
                            "J. Molina"]

        websites = ["gazzetta.greece",
                    "sport24.gr",
                    "contra.gr",
                    "sportdog.gr",
                    "sportlive.gr",
                    "skysports",
                    "derby.gr",
                    "dokari.gr",
                    "onsports.gr",
                    "in.gr",
                    "cnn",
                    "skai.gr",
                    "ant1.gr"]

        try:
            #self.shuffle_to_insta(websites)
            #self.go_insta_from_google()
            self.go_insta()
            self.insta_welcome(username, password)
            
            self.shuffleMain(username, insta_searches, True)
            print("--2o perasma ston idio account")
            self.shuffleMain(username, insta_searches)

            if random.randrange(10)>7:
                print("--3o perasma ston idio account")
                random_sleep(3, 6)
                self.shuffleMain(username, insta_searches, True)
                if random.randrange(10)<3:
                    print("--4o perasma ston idio account")
                    random_sleep(3, 6)
                    self.shuffleMain(username, insta_searches)


            self.insta_log_out()
            self.driver.close()

        except Exception as e:
            try:
                self.close_opened()
                self.insta_log_out()
                self.driver.close()
                print("eskase error: %s" %e)
                myPrint("eskase error: %s" %e)
            except Exception as e2:
                try:
                    self.insta_log_out()
                    self.driver.close()
                    print("eskase error: %s" %e2)
                    myPrint("eskase error: %s" %e2)
                except Exception as e3:
                    try:
                        self.driver.close()
                        print("eskase error: %s" %e3)
                        myPrint("eskase error: %s" %e3)                    
                    except:
                        sleep(2)
            bigErrorCounter = bigErrorCounter + 1
            print("-->>> Eskase to %so big error, proxwrame ston next account" %bigErrorCounter)
            myPrint("-->>> Eskase to %so big error, proxwrame ston next account" %bigErrorCounter)
        
        #except:
        #    myPrint("-->>> Eskase to big error, proxwrame ston next account")
        #    self.driver.close()

def runComments(goal):
    global comCounter
    global bigErrorCounter
    global filename
    global f

    xInitial = datetime.datetime.now()

    end = False
    k=1
    while True:
        create_file()
        f = open(filename, "a", encoding='utf-8')
        random.shuffle(accounts)
        x = datetime.datetime.now()
        print("->%so TREJIMO jekinaei : %s" %(k, x))
        myPrint("->%so TREJIMO jekinaei : %s" %(k, x))
        j = 1
        for acc in range(4):
            username, password = accounts[acc]
            alarm()
            x = datetime.datetime.now()
            print("----%s-----arxh me %so account------------" %(x, j))
            myPrint("----%s-----arxh me %so account------------" %(x, j))

            Instabot(username, password)

            x = datetime.datetime.now()
            print("----%s-----telos me %so account------------" %(x, j))
            myPrint("----%s-----telos me %so account------------" %(x, j))
            alarm()
            if comCounter>=goal:
                end = True
                break
            j = j + 1
            print("--------->Sleeping...")
            myPrint("--------->Sleeping...")
            print("--------->Sleeping...")
            myPrint("--------->Sleeping...")
            random_sleep(50, 100)

        x = datetime.datetime.now()
        print("->%so TREJIMO teleiwnei : %s" %(k, x))
        myPrint("->%so TREJIMO teleiwnei : %s" %(k, x))
        print("--------------------------------------------------------------")
        myPrint("--------------------------------------------------------------")
        
        if end:
            break
        else:
            k = k + 1
            f.close()
    print("")
    print("")
    myPrint("")
    myPrint("")
    print("Goal of %s comments reached successfully, I posted %s comments" %(goal, comCounter))
    print("BigErrors: %s" %bigErrorCounter)
    myPrint("Goal of %s comments reached successfully, I posted %s comments" %(goal, comCounter))
    print("BigErrors: %s" %bigErrorCounter)
    x = datetime.datetime.now()
    timeDiff = x - xInitial
    print("Execution time: %s" %timeDiff)
    myPrint("Execution time: %s" %timeDiff)
    if end:
        f.close()

runComments(comments_goal)