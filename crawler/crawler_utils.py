import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

from settings import (
    EVERYTIME_ID,
    EVERYTIME_PASSWORD,
)


def login(driver, login_url):
    try:
        driver.get(login_url)

        driver.implicitly_wait(2)
        driver.find_element(by=By.NAME, value="id").send_keys(EVERYTIME_ID)

        driver.implicitly_wait(2)
        driver.find_element(by=By.NAME, value="password").send_keys(EVERYTIME_PASSWORD)

        time.sleep(5)
        driver.implicitly_wait(2)
        driver.find_element(
            by=By.XPATH, value='//input[@type="submit" and @value="에브리타임 로그인"]'
        ).click()

        time.sleep(5)
    except Exception as e:
        print("로그인 중 오류:", e)


def extract_page_links(driver, page_url) -> list:
    try:
        driver.get(page_url)
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.list"))
        )

        articles = driver.find_elements(By.CSS_SELECTOR, "article.list")
    except Exception as e:
        print(f"페이지 불러오는 중 오류 발생 {page_url}: ", e)

    post_links = []

    for article in articles:
        try:
            a_tag = article.find_element(By.TAG_NAME, "a")
            link = a_tag.get_attribute("href")
            post_links.append(link)
        except Exception as e:
            print(f"링크 추출 중 오류 발생 {page_url}: ", e)

    return post_links


def extract_post_details(driver, post_links) -> list:
    posts = []
    for idx, post_link in enumerate(post_links, start=1):
        try:
            driver.get(post_link)  # 해당 글 페이지로 이동
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "article.item"))
            )

            title = driver.find_element(By.CSS_SELECTOR, "h2.large").text
            content = driver.find_element(By.CSS_SELECTOR, "p.large").text

            crawled_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            post = {  # 1개의 게시물
                "post_link": post_link,
                "title": title,
                "content": content,
                "crawled_time": crawled_time,
            }
            posts.append(post)

        except Exception as e:
            print(f"[글 내용을 가져오는 중 오류 발생 {post_link}:", e)

    return posts
