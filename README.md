# capstone-similarity-model
2025 캡스톤 주제 '대학 커뮤니티 자동화' 중 '게시글 유사도' 기능 관련 레포

### get stated chromadb
```
$ docker pull chromadb/chroma:latest
$ docker run -d -p 8000:8000 --name chroma-db -t chromadb/chroma:latest
```