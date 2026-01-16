import httpx

r = httpx.get("https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt")
lines = r.text.splitlines("\n")

print(lines[0])  # Tisk prvního řádku jako kontrola