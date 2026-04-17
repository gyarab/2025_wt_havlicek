import httpx

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

res = httpx.get(URL)
print("Server odpověděl:", res.status_code)

lines = res.text.split("\n")
print("Kurzy pro den:", lines[0].split(" ")[0])

line_euro = ""
for line in lines:
    if "|EUR|" in line:
        line_euro = line
        break

if line_euro == "":
    print("Kurz EUR nebyl nalezen.")
    exit()

rate = float(line_euro.split("|")[-1].replace(",", "."))
print("Kurz eura je:", rate, "CZK")

print("\nVyber převod:")
print("1 - EUR → CZK")
print("2 - CZK → EUR")

choice = input("Zadej 1 nebo 2: ")
while choice not in ("1", "2"):
    print("Neplatná volba.")
    choice = input("Zadej 1 nebo 2: ")

amount_input = input("Zadej částku: ").replace(",", ".")
while True:
    try:
        amount = float(amount_input)
        if amount > 0:
            break
        print("Částka musí být kladná.")
    except ValueError:
        print("Neplatné číslo.")
    amount_input = input("Zadej částku: ").replace(",", ".")

if choice == "1":
    result = amount * rate
    print(f"{amount:.2f} EUR = {result:.2f} CZK")
else:
    result = amount / rate
    print(f"{amount:.2f} CZK = {result:.2f} EUR")