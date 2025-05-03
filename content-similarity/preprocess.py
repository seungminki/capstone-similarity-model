from soynlp.normalizer import repeat_normalize, emoticon_normalize
import re
import pandas as pd

input_path = ""
output_path = "output.json"

pattern = re.compile(r"[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z\s]")  # 한글, 영어

letter_ko_pattern = re.compile(r"[^가-힣\s]")  # 한글 초성 제거

url_pattern = re.compile(r"https?://\S+")
dial_pattern = re.compile(r"010-\d{4}-\d{4}|041-\d{3}-\d{4}|02-\d{3}-\d{4}")
email_pattern = re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b")
space_pattern = re.compile(r"\s+")


def load_and_preprocess():
    df = pd.read_json(input_path, lines=True)

    df["text"] = df["text"].apply(clean)
    df = df[df["text"].str.len() > 3]

    return df


def clean(x):
    x = url_pattern.sub("", x)
    x = dial_pattern.sub("", x)
    x = email_pattern.sub("", x)

    x = pattern.sub("", x)
    x = letter_ko_pattern.sub("", x)

    x = space_pattern.sub(" ", x)
    x = x.strip()

    x = emoticon_normalize(x, num_repeats=2)
    x = repeat_normalize(x, num_repeats=1)

    return x


if __name__ == "__main__":
    df = load_and_preprocess()
    df.info()

    df.to_json(
        output_path,
        orient="records",
        lines=True,
        force_ascii=False,
    )
