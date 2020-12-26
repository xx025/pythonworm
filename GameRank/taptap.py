import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')  # chrome插件路径
driver.get('https://www.taptap.com/top/download')  # 榜单地址
time.sleep(5)  # 进入页面等待五秒

songRankList = []


def getinfo(i):
    try:
        listt = []  # 单次汇总
        rankList = driver.find_elements_by_class_name("app-top-list")[0]
        gameLIst = rankList.find_elements_by_class_name("taptap-top-card")
        for game in gameLIst[i:]:
            try:
                gameinfo = {}
                driver.execute_script("arguments[0].scrollIntoView();", game)  # 滑到标签
                # gameinfo["text"]=str(game.text).replace("\n","").replace("\r","")#测试用
                gameinfo["rank"] = game.find_element_by_class_name("top-card-order-text").text
                gameinfo["name"] = game.find_element_by_class_name("card-middle-title").text
                gameinfo["firm"] = game.find_element_by_class_name("card-middle-author").text
                gameinfo["star"] = game.find_element_by_class_name("middle-footer-rating").text
                # gameinfo["card-middle-description"] = game.find_element_by_class_name("card-middle-description").text
                gameinfo["card-middle-category"] = game.find_element_by_class_name("card-middle-category").text
                gameinfo["card-tags"] = [i.text for i in game.find_element_by_class_name("card-tags").find_elements_by_class_name("btn-default")]
                listt.append(gameinfo)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    return listt


def clickmorebtn():
    try:
        nextPageBtn = driver.find_elements_by_class_name("taptap-button-more")[0]
        nextbbbn = nextPageBtn.find_elements_by_class_name("btn-primary")[0]
        nextbbbn.click()
        time.sleep(4)  # 休息两秒等待页面加载
    except Exception as e:
        print(e)
    return None


def main(num=2):
    lisss = []
    for i in range(num):
        lisss.extend(getinfo(i * 30))
        clickmorebtn()
    return lisss


for i in main(5):
    print(i)
