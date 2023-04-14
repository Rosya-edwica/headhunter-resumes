import logging

from storage import connect
from storage.config import TABLE_RESUME
from models import Resume


def AddResume(resume: Resume) -> bool:
    connection = connect()
    try:
        cursor = connection.cursor()
        query = f"""INSERT INTO {TABLE_RESUME}(id, city_id, city, position_id, title, salary, currency, specializations, experience_in_months, languages, skills, date_update, url)
            VALUES('{resume.Id}', {resume.CityId}, '{resume.City}', {resume.PositionId}, '{resume.Title}', {resume.Salary}, '{resume.Currency}', '{'|'.join(resume.Specialization)}',
            {resume.ExperienceDuration}, '{'|'.join(resume.Languages)}', '{'|'.join(resume.Skills)}', '{resume.DateUpdate}', '{resume.Url}')"""
        cursor.execute(query)
        connection.commit()
        logging.info(f"Успешно добавили резюме {resume.Url}")
        connection.close()
        return True
    except BaseException as err:
        logging.error(f"Не удалось сохранить резюме: {err}")
        connection.close()
        return False
