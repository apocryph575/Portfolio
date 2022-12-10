import requests
from bs4 import BeautifulSoup
import csv

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}


man = []
woman = []
w_m = []
def parser():

    page = 0
    while (page<=827):
        page += 1
        url = f"https://unprenom.fr/tous/page-{page}/"
        r = requests.get(url=url, headers=HEADERS)
        soup = BeautifulSoup(r.text, "lxml")
        items = soup.find_all('div', class_='product-inner equal-element')

        for i in items:
            name = i.find("h5", class_="product-name").get_text()
            url = i.find("img").get("src")
            if str(url) == "https://unprenom.fr/theme/images/fille-garcon.jpg":
                w_m.append(name)
            elif str(url) == "https://unprenom.fr/theme/images/fille.jpg":
                woman.append(name)
            elif str(url) == "https://unprenom.fr/theme/images/garcon.jpg":
                man.append(name)
            else:
                continue

        print(f"Page {page} was parsing")

    with open("unprenom.txt", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Woman", "Man", "Uni"]
        )
    ma = max([len(woman),len(man),len(w_m)])
    print(ma)
    print(len(man))
    print(len(woman))
    print(len(w_m))
    while (len(man)<= ma) or (len(w_m)<= ma) or (len(woman)<= ma):
        if len(man) <= ma:
            man.append(" ")
        elif len(woman) <= ma:
            woman.append(" ")
        elif len(w_m) <= ma:
            w_m.append(" ")

    for item in range(ma):
        lis = [woman[item],man[item],w_m[item]]
        print(lis)
        with open("unprenom.txt", "a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                lis
            )


def main():
    parser()

if __name__ == "__main__":
    main()
