
import responder
import os

api = responder.API()


@api.route("/")
def index(req, resp):
    resp.text = req.method


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5042))
    api.run(port=port)