import time

import xlwings as xw
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')  # chrome插件路径
driver.get('http://www.kuwo.cn/rankList')  # 榜单地址
time.sleep(5)  # 进入页面等待五秒

songRankList = []
for tii in range(1, 10):
    try:
        rankList = driver.find_elements_by_class_name("rank_list")[0]
        songLIst = rankList.find_elements_by_class_name("song_item")
        for song in songLIst:
            driver.execute_script("arguments[0].scrollIntoView();", song)  # 滑到标签
            song_name = song.find_elements_by_class_name("song_name")[0].text
            song_artist = song.find_elements_by_class_name("song_artist")[0].text
            song_album = song.find_elements_by_class_name("song_album")[0].text
            song_time = song.find_elements_by_class_name("song_time")[0].text
            thissong = [song_name, song_artist, song_album, song_time]
            songRankList.append(thissong)
            print(thissong)
    except:
        print("失败!!!!!!!!")
        pass
    try:
        nextPageBtn = driver.find_elements_by_class_name("icon-icon_pagedown")[0]
        nextPageBtn.click()
    except:
        print("翻页失败")
    time.sleep(2)  # 休息两秒等待页面加载

time.sleep(3)  # 暂停 1 秒
driver.quit()  # 退出，关闭窗口

wb = xw.Book()
sht = wb.sheets['Sheet1']
sht.range('a1').value = ['歌曲', '歌手', '专辑', '时常']
sht.range('a2').value = songRankList
wb.save(r'C:\Users\sun\Desktop\酷我音乐榜.xlsx')  # 保存到桌面
