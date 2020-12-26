# encoding: utf-8
import matplotlib.pyplot as plt
import requests
from lxml import etree

BASE_DOMMAIN = "https://dytt8.net/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMMAIN + url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    movie = {}
    response = requests.get(url, headers=HEADERS)
    text = response.content.decode('gbk', 'ignore')
    html = etree.HTML(text)
    zoomE = html.xpath("//div[@id='Zoom']")[0]

    def parse_info(info, rule):
        return info.replace(rule, "").strip()

    infos = zoomE.xpath(".//text()")
    for info in infos:
        if info.startswith("◎片　　名"):
            movie['片名'] = parse_info(info, "◎片　　名")
        elif info.startswith("◎译　　名"):
            movie['译名'] = parse_info(info, "◎译　　名")
        elif info.startswith("◎类　　别"):
            movie['类别'] = parse_info(info, "◎类　　别")
        elif info.startswith("◎年　　代"):
            movie['年代'] = parse_info(info, "◎年　　代")
        elif info.startswith("◎产　　地"):
            movie['产地'] = parse_info(info, "◎产　　地")
    movie['下载地址'] = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    return movie


def spyder():
    list = []
    base_url = "https://dytt8.net/html/gndy/dyzz/list_23_{}.html"
    for x in range(4, 5):
        detail_urls = get_detail_urls(base_url.format(x))
        for detail_url in detail_urls:
            list.append(parse_detail_page((detail_url)))
    return list


# list=spyder()
list = [{'译名': '蝴蝶梦/丽贝卡/新版蝴蝶梦', '片名': 'Rebecca', '年代': '2020', '产地': '英国', '类别': '剧情 / 爱情 / 悬疑 / 惊悚',
         '下载地址': 'ftp://ygdy8:ygdy8@yg69.dydytt.net:8026/阳光电影www.ygdy8.com.蝴蝶梦.BD.1080p.中英双字幕.mkv'},
        {'译名': '大卫·伯恩的美国乌托邦/美国乌托邦', '片名': "David Byrne's American Utopia/American Utopia", '年代': '2020', '产地': '美国', '类别': '纪录片 / 音乐 / 歌舞',
         '下载地址': 'ftp://ygdy8:ygdy8@yg78.dydytt.net:6007/阳光电影www.ygdy8.com.大卫·伯恩的美国乌托邦.BD.1080p.中英双字幕.mkv'},
        {'译名': 'Love You Forever', '片名': '我在时间尽头等你/穿越时空的爱', '年代': '2020', '产地': '中国大陆', '类别': '爱情/奇幻',
         '下载地址': 'ftp://ygdy8:ygdy8@yg18.dydytt.net:6028/阳光电影www.ygdy8.com.我在时间尽头等你.HD.1080p.国语中字.mp4'},
        {'译名': '然后我们跳了舞/以你的舞步撩动我(港)', '片名': 'And Then We Danced', '年代': '2019', '产地': '瑞典,格鲁吉亚,法国', '类别': '剧情 / 同性',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:7006/阳光电影www.ygdy8.com.然后我们跳了舞.BD.1080p.中字.mkv'},
        {'译名': '我们保守的秘密/地下弒的秘密(台)', '片名': 'The Secrets We Keep', '年代': '2020', '产地': '美国', '类别': '剧情 / 悬疑 / 惊悚 / 犯罪',
         '下载地址': 'ftp://ygdy8:ygdy8@yg78.dydytt.net:7006/阳光电影www.ygdy8.com.我们保守的秘密.BD.1080p.中英双字幕.mkv'},
        {'译名': '美味的校餐 剧场版/美味午餐大作戰(台)', '片名': '劇場版 おいしい給食 Final Battle/School Meals Time Final Battle', '年代': '2020', '产地': '日本', '类别': '喜剧',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:4109/阳光电影www.ygdy8.com.美味的校餐剧场版.BD.1080p.日语中字.mkv'},
        {'译名': '女人四十玩说唱/四十岁版本', '片名': 'The 40-Year-Old Version/40 冲一波/The Forty-Year-Old Version', '年代': '2020', '产地': '美国', '类别': '喜剧',
         '下载地址': 'ftp://ygdy8:ygdy8@yg69.dydytt.net:8025/阳光电影www.ygdy8.com.女人四十玩说唱.BD.1080p.中英双字幕.mkv'},
        {'译名': '热情花招/Hot Gimmick: Girl Meets Boy/女孩遇见男孩', '片名': 'ホットギミック ガールミーツボーイ', '年代': '2019', '产地': '日本', '类别': '剧情',
         '下载地址': 'ftp://ygdy8:ygdy8@yg78.dydytt.net:5004/阳光电影www.ygdy8.com.热情花招.BD.1080p.日语中字.mkv'},
        {'译名': '试着死了一次/靠北少女(台)/老豆死开一阵先(港)', '片名': '一度死んでみた/Not Quite Dead Yet', '年代': '2020', '产地': '日本', '类别': '喜剧',
         '下载地址': 'ftp://ygdy8:ygdy8@yg18.dydytt.net:6027/阳光电影www.ygdy8.com.试着死了一次.BD.1080p.日语中字.mkv'},
        {'译名': 'Suk Suk', '片名': '叔·叔', '年代': '2019', '产地': '中国香港', '类别': '剧情/同性',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:5102/阳光电影www.ygdy8.com.叔·叔.BD.1080p.粤语中字.mkv'},
        {'译名': '芝加哥七君子审判/芝加哥七人案：惊世审判', '片名': 'The Trial of the Chicago 7', '年代': '2020', '产地': '美国,英国,印度', '类别': '剧情 / 惊悚 / 历史',
         '下载地址': 'ftp://ygdy8:ygdy8@yg78.dydytt.net:6006/阳光电影www.ygdy8.com.芝加哥七君子审判.BD.1080p.中英双字幕.mkv'},
        {'译名': '自由主义者：间谍的时代/二战女谍', '片名': 'A Call to Spy/Liberté: A Time to Spy', '年代': '2019', '产地': '美国', '类别': '悬疑/剧情',
         '下载地址': 'ftp://ygdy8:ygdy8@yg78.dydytt.net:6005/阳光电影www.ygdy8.com.自由主义者：间谍的时代.BD.1080p.中英双字幕.mkv'},
        {'译名': '雪谷之狼', '片名': 'The Wolf of Snow Hollow/The Werewolf', '年代': '2020', '产地': '美国', '类别': '喜剧 / 惊悚 / 恐怖',
         '下载地址': 'ftp://ygdy8:ygdy8@yg18.dydytt.net:6026/阳光电影www.ygdy8.com.雪谷之狼.BD.1080p.中英双字幕.mkv'},
        {'译名': '本人之死/我之死/我的死法', '片名': 'The Death of Me/Death of Me', '年代': '2020', '产地': '美国', '类别': '恐怖/惊悚/悬疑',
         '下载地址': 'ftp://ygdy8:ygdy8@yg69.dydytt.net:8024/阳光电影www.ygdy8.com.本人之死.BD.1080p.中英双字幕.mkv'},
        {'译名': '数码宝贝：最后的进化/数码宝贝大冒险：最后的进化·羁绊 / 数码宝贝大冒险剧场版', '片名': 'デジモンアドベンチャー LAST EVOLUTION 絆 / Digimon Adventure: Last Evolution Kizuna',
         '年代': '2020', '产地': '日本', '类别': '动画/冒险', '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:4108/阳光电影www.ygdy8.com.数码宝贝：最后的进化.BD.1080p.日语中字.mkv'},
        {'译名': 'Love You Forever/穿越时空的爱', '片名': '我在时间尽头等你', '年代': '2020', '产地': '中国大陆', '类别': '爱情 / 奇幻',
         '下载地址': 'ftp://ygdy8:ygdy8@yg69.dydytt.net:6016/阳光电影www.ygdy8.com.我在时间尽头等你.HD.1080p.国语中字.mp4'},
        {'译名': "I'm Livin' It/I’m Living It", '片名': '麦路人/麦难民/麥路人', '年代': '2019', '产地': '中国香港', '类别': '剧情',
         '下载地址': 'ftp://ygdy8:ygdy8@yg18.dydytt.net:8071/阳光电影www.ygdy8.com.麦路人.HD.1080p.国粤双语中字.mkv'},
        {'译名': '纳尔齐斯与歌尔德蒙', '片名': 'Narziss und Goldmund', '年代': '2020', '产地': '德国', '类别': '剧情',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:8006/阳光电影www.ygdy8.com.纳尔齐斯与歌尔德蒙.BD.1080p.中英双字幕.mkv'},
        {'译名': '乐队男孩', '片名': 'The Boys in the Band', '年代': '2020', '产地': '美国', '类别': '剧情/同性',
         '下载地址': 'ftp://ygdy8:ygdy8@yg78.dydytt.net:7005/阳光电影www.ygdy8.com.乐队男孩.BD.1080p.中英双字幕.mkv'},
        {'译名': "剧场版 架空OL日记/Fictitious Girl's Diary", '片名': '劇場版 架空OL日記', '年代': '2020', '产地': '日本', '类别': '剧情 / 喜剧',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:4107/阳光电影www.ygdy8.com.剧场版架空OL日记.BD.1080p.日语中字.mkv'},
        {'译名': '托米莉斯女王/托米利斯女王', '片名': 'Tomyris/The Legend of Tomiris/Томирис', '年代': '2019', '产地': '哈萨克斯坦', '类别': '剧情 / 历史',
         '下载地址': 'ftp://ygdy8:ygdy8@yg18.dydytt.net:6025/阳光电影www.ygdy8.com.托米莉斯女王.BD.1080p.中字.mkv'},
        {'译名': '神啊来救救我吧/神来救救我吧', '片名': 'Save Yourselves!', '年代': '2020', '产地': '美国', '类别': '喜剧/科幻',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:8005/阳光电影www.ygdy8.com.神啊来救救我吧.BD.1080p.中英双字幕.mkv'},
        {'译名': 'Chronical/Subject 14', '片名': '2067', '年代': '2020', '产地': '澳大利亚', '类别': '科幻',
         '下载地址': 'ftp://ygdy8:ygdy8@yg72.dydytt.net:8350/阳光电影www.ygdy8.com.2067.BD.1080p.中英双字幕.mkv'},
        {'译名': '休比的万圣节/万圣节救星修比/湖比万圣节', '片名': 'Hubie Halloween', '年代': '2020', '产地': '美国', '类别': '喜剧/恐怖',
         '下载地址': 'ftp://ygdy8:ygdy8@yg69.dydytt.net:3037/阳光电影www.ygdy8.com.休比的万圣节.BD.1080p.中英双字幕.mkv'},
        {'译名': '看门人/夺命守门人(台)', '片名': 'Doorman', '年代': '2020', '产地': '美国', '类别': '动作 / 惊悚',
         '下载地址': 'ftp://ygdy8:ygdy8@yg90.dydytt.net:8004/阳光电影www.ygdy8.com.看门人.BD.1080p.中英双字幕.mkv'}]


def format(dictsd={}, lls=[]):
    for i in list:
        for j, k in i.items():
            dictsd.setdefault(j, []).append(k)
    for k in dictsd.values():
        counttt = {}
        for i in k:
            if i not in counttt:
                counttt[i] = k.count(i)
        lls.append(counttt)
    return lls

llsr=format()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.pie([i for i in llsr[3].values()], labels=[i for i in llsr[3].keys()], autopct='%1.1f%%')
plt.title("饼图示例-电影天堂前125名最新电影分布情况")
plt.show()
