import logging

from storage import connect
from storage.config import TABLE_EDUCATION, TABLE_ADDITIONAL
from models import Education


def AddEducation(educationList: list[Education], table: str = TABLE_EDUCATION):
    connection = connect()
    try:
        for education in educationList:
            cursor = connection.cursor()
            query = f"""INSERT INTO {table}(resume_id, title, direction, year_grade)
                VALUES('{education.ResumeId}', '{education.Title}', '{"null" if education.Direction is None else education.Direction}', {"null" if education.YearOfRelease is None else education.YearOfRelease})"""
            cursor.execute(query)
            connection.commit()
            logging.info(f"Успешно добавили образование: {education.ResumeId}")
    except BaseException as err:
        logging.error(f"Не удалось сохранить образование: {err}")
    finally:
        connection.close()


def AddAdditional(additional: Education):
    AddEducation(educationList=additional, table=TABLE_ADDITIONAL)