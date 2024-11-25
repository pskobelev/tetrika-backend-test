import csv
from collections import defaultdict

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def scrape_animal_data(wiki_url):
    driver = webdriver.Chrome()
    driver.get(wiki_url)

    animals = defaultdict(int)

    while True:
        elems = driver.find_elements(
            By.CSS_SELECTOR, "#mw-pages .mw-category-group ul li a"
        )

        for elem in elems:
            animals[elem.text[0].upper()] += 1

        try:
            next_page_link = driver.find_element(By.LINK_TEXT,
                                                 "Следующая страница")
        # Выходим из цикла, если нет новых страниц
        except NoSuchElementException:
            driver.quit()
            break
        else:
            next_page_link.click()

    return animals


def save_to_csv(data, filename="beasts.csv"):
    with open(filename, "w+") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        for key, value in data.items():
            writer.writerow([key, value])


if __name__ == "__main__":
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    animal_data = scrape_animal_data(url)
    save_to_csv(animal_data)
