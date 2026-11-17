
import requests
import bs4


class ForumParser:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def parse_page(self, url: str):
        comments_url = url.rstrip("/") + "/comments/"

        response = requests.get(
            comments_url,
            headers=self.headers,
            timeout=10
        )
        response.raise_for_status()

        return self.parse_html(response.text)

    def parse_html(self, html: str):
        bs = bs4.BeautifulSoup(html, "html.parser")

        comments = bs.find_all(
            "article",
            class_="tm-comment-thread__comment"
        )

        parsed_comments = []

        for comment in comments:
            id_block = comment.find(attrs={"data-comment-body": True})
            comment_id = int(id_block["data-comment-body"])

            author_block = comment.find("a", class_="tm-user-info__username")
            author = author_block.text.strip()

            message_block = comment.find("div", class_="tm-comment__body-content")
            message = message_block.text.strip()

            parsed_comments.append({
                "id": comment_id,
                "name": author,
                "message": message
            })

        return parsed_comments

    def save_to_db(self, parsed_data, repository):
        for comment in parsed_data:
            repository.add(
                comment["id"],
                comment["name"],
                comment["message"]
            )
