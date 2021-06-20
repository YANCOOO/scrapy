import scrapy
from lxml import etree
from scrapyTest.items import ScrapytestItem


class CatchballSpider(scrapy.Spider):
    name = 'catchBall'
    allowed_domains = ['http://kaijiang.500.com/shtml/ssq/21061.shtml']
    start_urls = ['http://kaijiang.500.com/shtml/ssq/21061.shtml']

    def start_requests(self):

        # ==============================传统=============================
        urlslist = []
        for i in range(21050, 21061):
            url = 'http://kaijiang.500.com/shtml/ssq/{}.shtml'.format(i)
            urlslist.append(url)

        for urls in urlslist:
            yield scrapy.Request(urls, callback=self.parse)

        # ===============================================================

    def parse(self, response):
        ballLists = ScrapytestItem()

        # ==============================传统=============================
        content = etree.HTML(response.text)
        red = content.xpath('//li[@class="ball_red"]/text()')
        blue = content.xpath('//li[@class="ball_blue"]/text()')
        periods = content.xpath('//font[@class="cfont2"]/strong/text()')

        ballLists['redBall1'] = red[0]
        ballLists['redBall2'] = red[1]
        ballLists['redBall3'] = red[2]
        ballLists['redBall4'] = red[3]
        ballLists['redBall5'] = red[4]
        ballLists['redBall6'] = red[5]
        ballLists['blueBall'] = blue[0]
        ballLists['periods'] = periods[0]
        # ballLists.append(red + blue)
        yield ballLists
        print(red)
        print(blue)
        print(periods)

        # ==============================================================

        # ============================自动化=============================
        # 加启动配置
        # # chrome_options = webdriver.ChromeOptions();
        # # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
        # #
        # # driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Update\chromedriver.exe',
        # #                           chrome_options=chrome_options)
        # driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Update\chromedriver.exe')
        # driver.get(response.url)
        # driver.implicitly_wait(1)
        # a_list = driver.find_elements_by_class_name('ball_red')
        # print(a_list)
        # ==============================================================

    # pass

# ==================pymysql===========================
# def conMysql(self):
#     # 连接数据库
#     conn = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='1',
#         database='win',
#         charset='utf8',
#         # 如果插入数据，是否自动提交。 和conn.commit()功能一致。
#         autocommit=True
#     )
#
#     cursor = conn.cursor()
#
#     # 插入sql语句
#     sql = "insert into ball (red1,red2,red3,red4,red5,red6,red7,bull) values (%s,%s,%s,%s,%s,%s,%s,%s)"
#
#     for list1 in ballLists:
#         for list in list1:
#             red1 = list[0]
#             red2 = list[1]
#             red3 = list[2]
#             red4 = list[3]
#             red5 = list[4]
#             red6 = list[5]
#             red7 = list[6]
#             bull = list[8]
#
#         # 执行插入操作
#         insert = cursor.execute(sql, (red1, red2, red3, red4, red5, red6, red7, bull))
#     cursor.close()
#     conn.commit()
#     conn.close()
# ==================pymysql===========================
