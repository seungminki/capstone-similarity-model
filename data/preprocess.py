import re
import pandas as pd
from datetime import datetime

from load_data import load_df

output_path = "output.json"


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    # 링크에서 게시판 코드와 게시물 코드 추출
    codes = df["post_link"].apply(split_post_link)
    df["board_code"], df["post_code"] = zip(*codes)

    # 중복된 데이터 제거하고, 'crawled_time'에 따라 내림차순 정렬
    df = df.sort_values("crawled_time", ascending=False).drop_duplicates(
        subset=["board_code", "post_code"], keep="first"
    )

    # 불필요한 열 삭제
    df = df.drop(columns=["post_link", "crawled_time"])

    # title + content = text
    df["text"] = df["title"].fillna("") + " " + df["content"].fillna("")
    df = df.drop(columns=["title", "content"])

    # 'text' 열에서 개행 문자 제거
    df["text"] = df["text"].str.replace("\n", " ", regex=False)

    # 너무 짧은 텍스트는 제외
    df = df[df["text"].str.len() > 3]

    return df


def split_post_link(post_link: str) -> tuple:
    """
    post_link에서 게시판 코드(board_code)와 게시물 코드(post_code) 추출.
    예시 링크 형식: "https://everytime.kr/370451/v/374409981"
    """
    match = re.search(r"everytime\.kr/(\d+)/v/(\d+)", post_link)
    if match:
        return match.group(1), match.group(2)
    return None, None


if __name__ == "__main__":
    df = load_df()
    df = preprocess(df)
    df.to_json(
        output_path,
        orient="records",
        lines=True,
        force_ascii=False,
    )
