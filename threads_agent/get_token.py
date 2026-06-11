"""
Lancez ce script UNE FOIS pour obtenir votre token Threads long-durée (60 jours).
Usage : python get_token.py
"""
import os
import webbrowser
import requests

APP_ID     = "4574716579426590"
APP_SECRET = input("Votre Clé secrète Threads : ").strip()
REDIRECT   = "https://fouetjm-jpg.github.io/FrancisValoren/callback.html"

auth_url = (
    f"https://threads.net/oauth/authorize"
    f"?client_id={APP_ID}"
    f"&redirect_uri={REDIRECT}"
    f"&scope=threads_basic,threads_content_publish"
    f"&response_type=code"
)

print("\nOuverture du navigateur pour autoriser l'application...")
webbrowser.open(auth_url)

print("\nConnectez-vous, autorisez l'app, puis copiez le code affiché sur la page.")
code = input("Collez le code ici : ").strip()

# Token court (1h)
r = requests.post("https://graph.threads.net/oauth/access_token", data={
    "client_id": APP_ID,
    "client_secret": APP_SECRET,
    "grant_type": "authorization_code",
    "redirect_uri": REDIRECT,
    "code": code,
})
r.raise_for_status()
short_token = r.json()["access_token"]
user_id     = r.json()["user_id"]

# Token long (60 jours)
r2 = requests.get("https://graph.threads.net/access_token", params={
    "grant_type": "th_exchange_token",
    "client_secret": APP_SECRET,
    "access_token": short_token,
})
r2.raise_for_status()
long_token = r2.json()["access_token"]

print("\n✅ Copiez ces valeurs dans un fichier .env :\n")
print(f"THREADS_USER_ID={user_id}")
print(f"THREADS_ACCESS_TOKEN={long_token}")
print(f"\nCe token est valable 60 jours.")
