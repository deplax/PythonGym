
import logging
import collections
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(levelname)-8s] %(message)s")
project_id = 'study-jam-whale'
dataSet_name = 'keyword'
table_name = 'naver'

API_KEY = "./bq.json"
BROWSER_PATH = "./chromedriver"

CRAWL_INFO = {
    "google": {
        "url": "https://www.google.com/search?q={keyword}",
        "query_field_name": "q",
        "query_search_selector": "#mKlEF",
        "related_query_selector": ".card-section > div > p"
    },
    "naver": {
        "url": "https://search.naver.com/search.naver?query={keyword}",
        "query_field_name": "query",
        "query_search_selector": ".greenwindow > .bt_search",
        "related_query_selector": "._related_keyword_ul > li"
    },
    "daum": {
        "url": "https://search.daum.net/search?w=tot&q={keyword}",
        "query_field_name": "q",
        "query_search_selector": "#daumBtnSearch",
        "related_query_selector": "#netizen_lists_top > span"
    }
}


class Crawler:
    def __init__(self, service, start_keyword):
        self.service = service
        self.keyword = start_keyword
        self.crawl_data = CRAWL_INFO[self.service]
        self.count = 0
        self.bq = BigQuery()
        if not self.crawl_data:
            raise KeyError

        self.keyword_queue = collections.deque([])
        self.extracted_keyword_set = {start_keyword}

        self.driver = webdriver.Chrome(BROWSER_PATH)

    def start_crawl(self):
        self.open_start_page(self.crawl_data["url"].format(**{"keyword": self.keyword}))

        # 첫번째 키워드 별도 등록
        self.save_bigQuery(None, [self.keyword])

        html = self.get_html(self.keyword)
        keyword_list = self.get_keywords(html)
        self.keyword_queue.extend(keyword_list)
        self.extracted_keyword_set.add(self.keyword)

        self.count += len(keyword_list)
        self.save_bigQuery(self.keyword, keyword_list)
        self.keyword = self.keyword_queue.popleft()
        while True:
            try:
                self.crawl(self.keyword)
            except:
                self.driver.close()
                self.driver = webdriver.Chrome(BROWSER_PATH)
                self.open_start_page(self.crawl_data["url"].format(**{"keyword": self.keyword}))
                continue

    def crawl(self, keyword):
        while self.keyword_queue:
            logging.info("current_keyword : %s, queue_size : %d, query_key_size : %d, keyword_count : %d" %
                         (keyword, len(self.keyword_queue), len(self.extracted_keyword_set), self.count))
            if keyword in self.extracted_keyword_set:
                keyword = self.keyword_queue.popleft()
                continue
            html = self.get_html(keyword)
            keyword_list = self.get_keywords(html)
            self.keyword_queue.extend(keyword_list)
            self.extracted_keyword_set.add(keyword)

            self.count += len(keyword_list)
            self.save_bigQuery(keyword, keyword_list)
            keyword = self.keyword_queue.popleft()

    def get_html(self, keyword):
        query_field = self.driver.find_element_by_name(self.crawl_data["query_field_name"])
        query_field.clear()
        query_field.send_keys(keyword)
        self.driver.find_element_by_css_selector(self.crawl_data["query_search_selector"]).click()
        return self.driver.page_source

    def get_keywords(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return list(map((lambda x: x.text), soup.select(self.crawl_data["related_query_selector"])))

    def open_start_page(self, url):
        self.driver.get(url)

    def save_bigQuery(self, keyword, keyword_list):
        self.bq.save_rows(list(map((lambda x: (self.service, keyword, x, datetime.now())), keyword_list)))

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

    def save_row(self, service, parents_keyword, keyword, timestamp):
        self.client.insert_rows(self.table, [(service, parents_keyword, keyword, timestamp)], self.schema)

    def save_rows(self, data_list):
        if data_list:
            self.client.insert_rows(self.table, data_list, self.schema)


def main():
    logging.info("crawler start!")

    crawler = Crawler("naver", "아이유")
    crawler.start_crawl()


if __name__ == "__main__":
    main()
