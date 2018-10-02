import os
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from google.cloud import bigquery

# GCP_KEY_PATH = os.path.join(os.path.dirname(__file__), './gcpkey.json')
project_id = 'study-jam-whale'
dataSet_name = 'keyword'
table_name = 'keyword'

API_KEY = "/Users/whale/Downloads/bq.json"

start_keyword = "아이유"


class Crawler:
    def __init__(self, start_keyword):
        self.urlList = []
        self.keyword_set = {start_keyword}
        pass

    def start_crawl(self):
        pass

    def get_keywords(self, html):
        pass

    def save_bigQuery(self):
        pass

    def save_file(self):
        pass


class BigQuery:
    def __init__(self):
        self.client = bigquery.Client.from_service_account_json(json_credentials_path=API_KEY)
        self.dataSet = self.client.dataset(dataSet_name)
        self.table = self.dataSet.table(table_name)
        self.schema = [
            bigquery.SchemaField('service', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('parents', 'STRING', mode='NULLABLE'),
            bigquery.SchemaField('keyword', 'STRING', mode='REQUIRED'),
            bigquery.SchemaField('timeStamp', 'TIMESTAMP', mode='REQUIRED')
        ]

    def save_single(self, service, parents_keyword, keyword, timestamp):
        self.client.insert_rows(self.table, [(service, parents_keyword, keyword, timestamp)], self.schema)

    def save(self, data_list):
        self.client.insert_rows(self.table, data_list, self.schema)


def main():
    # init

    # bq = BigQuery()
    # bq.save_single("google", "아이유", "아이유사진", datetime.now())

    # crawler = Crawler(start_keyword)
    # crawler.start_crawl()

    driver = webdriver.Chrome('/Users/whale/Downloads/chromedriver')
    try:
        driver.get("http://www.google.com")
        driver.find_element_by_name("q").send_keys(start_keyword)
        driver.find_element_by_name("btnK").click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        soup.select(".card-section > p > a")

    finally:
        driver.close()

    print(html)

    # driver.get("http://www.naver.com")

    # 메인 페이지를 방문한다.
    # 연관 검색어를 set 에 넣는다.
    # 연관 검색어를 DB에 저장한다.
    # 연관 검색어 페이지를 방문한다.
    # 리스트에 없는


if __name__ == "__main__":
    main()
