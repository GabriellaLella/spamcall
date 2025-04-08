from twilio.rest import Client
import sys

# Inserisci le tue credenziali Twilio qui
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_number = '+1XXXXXXXXXX'  # Il numero Twilio

client = Client(account_sid, auth_token)

print("📞 Invio Chiamata via Twilio")
print("📌 Inserisci il numero con prefisso internazionale (Es: 39xxxxxxxxxx)")

try:
    to_number = input("Numero : ").strip()
    if not to_number.startswith("39") or not to_number[2:].isdigit() or len(to_number) != 12:
        raise ValueError("Numero italiano non valido. Deve essere 39 + 10 cifre.")

    print("☎️  Invio della chiamata...")
    
    call = client.calls.create(
        to=f"+{to_number}",
        from_=twilio_number,
        url="http://demo.twilio.com/docs/voice.xml"  # Semplice demo vocale
    )

    print(f"✅ Chiamata inviata! SID: {call.sid}")

except ValueError as ve:
    print(f"❌ Errore: {ve}")
    sys.exit()
except Exception as e:
    print(f"❌ Errore imprevisto: {e}")
    sys.exit()
