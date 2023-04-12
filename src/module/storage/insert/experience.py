import logging

from storage import connect
from storage.config import TABLE_EXPERIENCE_STEP
from models import ExeperienceStep


def AddExperience(experience: list[ExeperienceStep]):
    connection = connect()
    try:
        for step in experience:
            cursor = connection.cursor()
            query = f"""INSERT INTO {TABLE_EXPERIENCE_STEP}(resume_id, post, duration_in_months, interval, branch, subbranch)
                VALUES('{step.ResumeId}', '{step.Post}', '{step.Duration}', '{step.Interval}', '{'|'.join(step.Branch)}', '{'|'.join(step.Subbranch)}')"""
            cursor.execute(query)
            connection.commit()
            logging.info(f"Успешно добавили опыт: {step.ResumeId}: {step.Post}")
    except BaseException as err:
        logging.error(f"Не удалось сохранить опыт: {err}")
    finally:
        connection.close()
