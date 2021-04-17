
import responder
import os
import random

N = 100000
cnt = 0
for i in range(N):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    sum = a + b 

    if sum == 5:
        cnt += 1  # 合計が5の場合

cnt /= N  # 平均をとる。

print(f"サイコロを足して 5になる確率: {cnt:.2f}")  # 




api = responder.API()


@api.route("/")
def index(req, resp):
    resp.text = req.method


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5042))
    api.run(port=port)