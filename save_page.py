import requests

url = input("Введите URL: ")
save_path ="/tests/fixtures/comments.html"

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
