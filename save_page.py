import requests
import src.parser as parser
import src.database as db
url = "https://habr.com/ru/articles/1108386/"
save_path ="tests/fixtures/comments.html"
db_path = "test.db"
comments_url = url.rstrip("/") + "/comments/"

response = requests.get(
    comments_url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10
)

response.raise_for_status()

with open(save_path, "w", encoding="utf-8") as file:
    file.write(response.text)

print("HTML сохранeн")

parser = parser.ForumParser()
res = parser.parse_page(url)
dbrep = db.DatabaseRepository(db_path)
parser.save_to_db(res, dbrep)

for com in res:
    print(f"id: {com["id"]}\nname: {com["name"]}\ntext: {com["message"]}\n\n")

print(f"Количество комментариев: {len(res)}")