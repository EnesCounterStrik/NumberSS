import requests

MOBIL_URL = "https://raw.githubusercontent.com/EnesCounterStrik/NumberSS/refs/heads/main/jsonlar/mobilhat.json"

def mobil_sorgula(mnc):
    try:
        res = requests.get(MOBIL_URL, timeout=5)
        if res.status_code != 200:
            return None
        data = res.json()
    except Exception:
        return None

    data_sorted = sorted(data, key=lambda x: len(str(x.get("MNC", ""))), reverse=True)

    for kayit in data_sorted:
        if str(kayit.get("MNC", "")).strip() == mnc:
            kayit_kopya = kayit.copy()
            kayit_kopya.pop("MNC", None)
            return kayit_kopya

    return None
