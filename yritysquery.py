import requests
import json
import concurrent.futures

subdomains = [
    "imatranseutu", "lappeenrannanseutu", "jpyp", "kuusiokunnat", "ilmajoki", "kauhajoki", "seinajoki",
    "savonlinna", "mikseimikkeli", "hameenlinna", "fyk", "kamk", "kaustisenseutu", "kosek", "jamsa",
    "konnevesi", "laukaa", "muurame", "saarijarvi", "viitasaari", "aanekoski", "cursor", "kinno", "inari",
    "meri-lappi", "rovaniemi", "epirkanmaa", "sastamala", "hameenkyro", "ikaalinen", "kangasala",
    "kehitysparkki", "lempaala", "palkane", "vesilahti", "virrat", "krs", "concordia", "vasek",
    "haapavesi-siikalatva", "kalajoki", "naturpolis", "ylivieska", "juuka", "lieksa", "iisalmi",
    "varkaudenseutu", "savogrow", "kiuruvesi", "lapinlahti", "siilinjarvi", "ladec", "satakunta",
    "rauma", "novago", "jarvenpaa", "karkkila", "kirkkonummi", "lohja", "posintra", "raasepori",
    "siuntio", "tuusula", "vihti", "auranmaa", "kaarina", "ukipolis", "loimaa", "parainen", "raisio"
]

api_endpoint = "https://{}.yrityshakemistot.fi/Api/Companies"
params = {
    'page': 1,
    'pageSize': 20
}

results = {}

def check_subdomain(subdomain):
    url = api_endpoint.format(subdomain)
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            try:
                response.json()
                return subdomain, "Toimii"
            except ValueError:
                return subdomain, "Ei toimi - ei JSON-vastausta"
        else:
            return subdomain, f"Ei toimi - statuskoodi {response.status_code}"
    except requests.RequestException as e:
        return subdomain, f"Ei toimi - {str(e)}"

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(check_subdomain, subdomain): subdomain for subdomain in subdomains}
    for future in concurrent.futures.as_completed(futures):
        subdomain, status = future.result()
        results[subdomain] = status


with open("tulokset.json", "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4, ensure_ascii=False)


for subdomain, status in results.items():
    print(f"{subdomain} - {status}")