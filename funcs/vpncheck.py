import requests
def vpncheck(ip:str) -> bool:
    s = requests.get(f"http://ip-api.com/json/{ip}?fields=16908288")
    data = s.json()

    if s.status_code == 429:
        return False

    if data["proxy"]:
        return True
    
    return False