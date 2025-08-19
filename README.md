i wnated to start learning fastapi library from beginning.

https://fastapi.tiangolo.com/learn/


## How i am checking this repo?

after i do some code changes i need to keep remember to activate my uv's environment, and then run the below command,
```
fastapi dev main.py


uv run uvicorn main:app --host "0.0.0.0"


IP=$(hostname -I | awk '{print $1}')
uvicorn main:app --host 0.0.0.0 --port 8000 --reload & echo "Your app is running at http://$IP:8000"

```


## How i started the repo?

```
rana-universe@rana-universe-Inspiron-3442:~/workspaces/learn_fastapi_1$ uv init . --python 3.13.0
Initialized project `learn-fastapi-1` at `/home/rana-universe/workspaces/learn_fastapi_1`
rana-universe@rana-universe-Inspiron-3442:~/workspaces/learn_fastapi_1$ git branch -m main
```

if i will use uv, i need to use.
`uv run main.py`