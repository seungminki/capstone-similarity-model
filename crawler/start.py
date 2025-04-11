import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from argparse import ArgumentParser
import time
import json
import os

from crawler_utils import login, extract_page_links, extract_post_details

from settings import (
    EVERYTIME_URL,
    CHROMEDRIVER_PATH,
)

parser = ArgumentParser()
parser.add_argument("--board", type=int, default=None)
parser.add_argument("--start", type=int, default=1)
parser.add_argument("--end", type=int, default=10)

args = parser.parse_args()

board_num = args.board
start_page = args.start
end_page = args.end


chrome_options = Options()
# chrome_options.add_argument("--headless")  # GUI 없이 실행
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

output_dir = f"raw/{board_num}"
os.makedirs(output_dir, exist_ok=True)

login_url = f"{EVERYTIME_URL}/login"
login(driver, login_url)

for cnt in range(start_page, end_page + 1):
    start = time.time()

    print(f"🕷️ page {cnt} 크롤링 중...")
    page_url = f"{EVERYTIME_URL}/{board_num}/p/{cnt}"

    post_links = extract_page_links(driver, page_url)
    posts = extract_post_details(driver, post_links)

    filename = f"{output_dir}/{cnt}.json"
    with open(filename, "w", encoding="utf-8") as jsonfile:
        json.dump(posts, jsonfile, ensure_ascii=False, indent=4)

    end = time.time()
    print(f"실행 시간: {end - start:.3f}초")

driver.quit()
