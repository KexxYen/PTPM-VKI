import requests
import Bea
class ForumParser():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def parse_page(self, url: str):
        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
        )
        response.raise_for_status()

        bs = Bea