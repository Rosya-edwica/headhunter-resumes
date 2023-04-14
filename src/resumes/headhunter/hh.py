from models import Position, City
from bs4 import BeautifulSoup
from headhunter import tools 
import storage
from multiprocessing import Pool
import logging

from headhunter import Scraper

TOTAL_NUMBER_RESUME_LIMIT = 2_000
CURRENT_POSITION_ID = None
CURRENT_CITY_ID = 0

def find_profession(profession: Position) -> None:
    url = tools.create_query(professionName=profession.Title)
    total_number_of_resumes = tools.get_count_of_resumes(url)
    if not total_number_of_resumes: 
        logging.info(f"Не нашлось ни одного резюме по данному запросу: {url}")
        return
    
    global CURRENT_POSITION_ID
    CURRENT_POSITION_ID = profession.Id
    if total_number_of_resumes <= TOTAL_NUMBER_RESUME_LIMIT:
        logging.info(f"Найдено {total_number_of_resumes} резюме. Поиск только по России")
        find_profession_in_Russia(profession)
    else:
        logging.info(f"Найдено {total_number_of_resumes} резюме. Поиск по отдельным городам")
        find_profession_in_all_cities_separately(profession)


def find_profession_in_Russia(profession: Position):
    city = City(Name="Россия", EdwicaId=0, HeadHunterId=113, RabotaRu="russia")
    find_profession_in_currrent_city(profession, city)

def find_profession_in_all_cities_separately(profession: Position):
    cities = storage.GetCities()
    for city in cities:
        CURRENT_CITY_ID = city.EdwicaId
        logging.info(f"Ищем профессию в {city.Name}")
        find_profession_in_currrent_city(profession, city)


def find_profession_in_currrent_city(profession: Position, city: City):
    url = tools.create_query(profession.Title, area=city.HeadHunterId)
    pages = tools.get_count_of_pages(url)
    for page in range(pages):
        logging.info(f"Страница {page+1}:{pages}")
        scrape_professions_in_page(page=f"{url}&page={page}")


def scrape_professions_in_page(page: str) -> None:
    soup = tools.get_soup(page)
    resumes_block = soup.find("div", class_="resume-serp")
    if not resumes_block: return
    blocks = []

    for block in resumes_block.find_all("div", class_="serp-item"):
        blocks.append(block)
    logging.info(f"Доступно резюме на странице: {len(blocks)}")

    with Pool(10) as process:
        process.map_async(
            func=scrape_resume,
            iterable=blocks,
            error_callback=lambda x: logging.fatal(x))
        process.close()
        process.join()

def scrape_resume(block: BeautifulSoup):
    resume_url = "https://hh.ru" + block.find("a", class_="serp-item__title")["href"]
    resume_date_update = block.find("span", class_="bloko-text bloko-text_tertiary").text.replace("Обновлено", "").strip()
    resume_scraper = Scraper(resume_url, CURRENT_POSITION_ID, CURRENT_CITY_ID, resume_date_update)
    save(scr=resume_scraper)
    
def save(scr: Scraper) -> None:
    saved = storage.AddResume(scr.GetResume())
    if saved:
        storage.AddAdditional(scr.GetAdditional())
        storage.AddExperience(scr.GetExperience())
        storage.AddEducation(scr.GetEducation())