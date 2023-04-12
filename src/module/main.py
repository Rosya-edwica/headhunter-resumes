import sys
import time
import logging
import os
from dotenv import load_dotenv

import headhunter
import storage

loaded_env = load_dotenv(".env")
if not loaded_env:
    exit("Не найден .env файл!")

sys.setrecursionlimit(int(os.getenv("RECURSION_LIMIT")))

logging.basicConfig(filename="info.log", filemode='w', format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("selenium").setLevel(logging.WARNING)


def main():
    start = time.perf_counter()
    logging.warning("Парсятся не все резюме, т.к некоторые резюме доступны только для авторизированных пользователей или работадателей")
    positions = storage.GetPositions()
    for profession in positions:
        logging.info(f"Ищем профессию {profession.Id}: {profession.Title}")
        headhunter.find_profession(profession)
        
        logging.info(f"Профессия спарсена {profession.Id}: {profession.Title}")
        print(f"Профессия спарсена {profession.Id}: {profession.Title}")
        storage.SetParsedToProfession(profession.Id)
    
    print(f"Time: {time.perf_counter() - start} seconds.")

        
if __name__ == "__main__":
    main()  
    