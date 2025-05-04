# chroma-db

## used chroma-db
```sh
docker run -v ./chroma-data:/data -p 8000:8000 chromadb/chroma
```

## used chroma-db console
```sh
$ git clone https://github.com/flanker/chromadb-admin.git
$ docker build -t chromadb-admin .
$ docker run -p 3000:3000 chromadb-admin
```
'http://host.docker.internal:8000' 접속