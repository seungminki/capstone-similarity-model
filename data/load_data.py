import glob
import re
import pandas as pd

input_path_prefix = "crawler/raw"


def load_df():
    file_list = [load_each_df(369475), load_each_df(370451)]
    # TODO: load to config.py
    return pd.concat(file_list, ignore_index=True)


def load_each_df(board_num: int) -> pd.DataFrame:
    file_list = sort_input_path(board_num)
    df_list = [pd.read_json(file) for file in file_list]
    df = pd.concat(df_list, ignore_index=True)

    return df


def sort_input_path(board_num: int) -> list:
    def extract_number(filename):
        # 숫자 추출해서 정렬 기준으로 사용
        match = re.search(r"\d+", filename)
        return int(match.group()) if match else -1

    file_list = sorted(
        glob.glob(f"{input_path_prefix}/{board_num}/*.json"), key=extract_number
    )

    return file_list
