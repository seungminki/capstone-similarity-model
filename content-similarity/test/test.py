from sentence_transformers import SentenceTransformer, util
import pandas as pd
import time

# 1. 모델 로드
start = time.time()
model = SentenceTransformer("jhgan/ko-sroberta-multitask")  # 자동 tokenizer
end = time.time()
print(f"모델 불러오는 실행 시간: {end - start:.3f}초")

# 2. 전체 데이터셋 로드
df = pd.read_json("output.json", orient="records", lines=True)
corpus = df["text"]

# 3. 유저가 검색한 문장
query = "레포트 작성 언제까지였지?"

# 4. 임베딩 계산
start = time.time()
corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
end = time.time()
print(f"df 유사도 실행 시간: {end - start:.3f}초")

query_embedding = model.encode(query, convert_to_tensor=True)

# 5. 코사인 유사도 계산
start = time.time()
cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
end = time.time()
print(f"코사인 유사도 실행 시간: {end - start:.3f}초")

# 6. 유사도 높은 순으로 정렬
start = time.time()
top_results = cos_scores.argsort(descending=True)
end = time.time()
print(f"코사인 유사도 정렬 실행 시간: {end - start:.3f}초")

sentence_count = 200
print(f"\n🧠 '{query}'와 의미상 유사한 문장 Top {sentence_count}:")
top_result_list = top_results[:sentence_count]
for idx in top_results[:sentence_count]:
    i = idx.item()  # tensor → int
    print(f"- {corpus[i]} (유사도: {cos_scores[i]:.3f})")

    # if "시험" not in corpus[i]:
    #     print(f"- {corpus[i]} (유사도: {cos_scores[i]:.3f})")
