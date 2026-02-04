import httpx

URL = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

# stažení kurzovního lístku
res = httpx.get(URL)
print("Server odpověděl:", res.status_code)

lines = res.text.split("\n")
print("Kurzy pro den:", lines[0].split(" ")[0])

# nalezení řádku s eurem
line_euro = ""
for line in lines:
    if "|EUR|" in line:
        line_euro = line
        break

if line_euro == "":
    print("Kurz EUR nebyl nalezen.")
    exit()

rate_str = line_euro.split("|")[-1].replace(",", ".")
rate = float(rate_str)

print("Kurz eura je:", rate, "CZK")

# výběr typu převodu
print("\nVyber převod:")
print("1 - EUR → CZK")
print("2 - CZK → EUR")

choice = input("Zadej 1 nebo 2: ")

if choice != "1" and choice != "2":
    print("Neplatná volba.")
    exit()

# zadání částky
try:
    amount = float(input("Zadej částku: ").replace(",", "."))
    if amount <= 0:
        print("Částka musí být kladná.")
        exit()
except ValueError:
    print("Neplatné číslo.")
    exit()

# výpočet
if choice == "1":
    result = amount * rate
    print(f"{amount:.2f} EUR = {result:.2f} CZK")
else:
    result = amount / rate
    print(f"{amount:.2f} CZK = {result:.2f} EUR")
