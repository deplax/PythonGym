import time
from datetime import datetime
from selenium import webdriver
from slacker import Slacker
from bs4 import BeautifulSoup
from slack_token import WHALE_BOT_TOKEN, CHANNEL

time_format = "%H:%M"


class FlightCard:
    def __init__(self, airline, departure_time, arrival_time):
        self.airline = airline
        self.departure_time = departure_time
        self.arrival_time = arrival_time


def noti_slack(message):
    token = WHALE_BOT_TOKEN
    slack = Slacker(token)
    slack.chat.post_message(CHANNEL, message)


# 드라이버 선택
# driver = webdriver.Chrome('/Users/deplax/Downloads/chromedriver')
driver = webdriver.PhantomJS('/Users/whale/Downloads/phantomjs')

# 드라이버 세팅
driver.set_page_load_timeout(30)

# 페이지를 가져온다.
driver.get('https://store.naver.com/flights/results/domestic?trip=OW&scity1=CJU&ecity1=GMP&sdate1=2018.10.19.&adult=1&child=0&infant=0&fareType=YC&airlineCode=&nxQuery=항공권')
time.sleep(10)

for x in range(15):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

contents = driver.page_source.encode('utf-8')
driver.close()

# 각 항공사 카드를 가져온다.
soup = BeautifulSoup(contents, "html.parser")
flight_markup_cardlist = soup.select(".trip_result_item")
flight_list = []

for flight_card in flight_markup_cardlist:
    airline = flight_card.select_one(".h_tit_result").text
    time_labels = flight_card.select(".route_info > .txt_time")

    departure_time = datetime.strptime(time_labels[0].text, time_format)
    arrival_time = datetime.strptime(time_labels[1].text, time_format)
    flight_list.append(FlightCard(airline, departure_time, arrival_time))

# 출발시간이 몇시 이후 && 몇시 이전 && 무슨 항공사일 경우 노티
airline = ["진에어", "제주항공"]
start_time = datetime.strptime("15:00", time_format)
end_time = datetime.strptime("17:00", time_format)

for flight_card in flight_list:
    if start_time < flight_card.departure_time < end_time:
        message_info = {
            "airline": flight_card.airline,
            "departure_time": flight_card.departure_time.strftime(time_format),
            "arrival_time": flight_card.arrival_time.strftime(time_format)
        }
        message = "{airline} : {departure_time}~{arrival_time}".format(**message_info)
        noti_slack(message)