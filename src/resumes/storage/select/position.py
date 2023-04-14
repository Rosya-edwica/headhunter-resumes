from storage.config import connect, TABLE_POSITION
from models import Position


def GetPositions() -> list[Position]:
    connection = connect()
    cursor = connection.cursor()
    query = f"SELECT id, parent_id, level, title, prof_area, other_names FROM {TABLE_POSITION} WHERE parsed=false"
    cursor.execute(query)
    positions: list[Position]  = [Position(*i) for i in cursor.fetchall()]
    connection.close()
    return positions


def SetParsedToProfession(id: int) -> None:
    connection = connect()
    cursor = connection.cursor()
    query = f"UPDATE {TABLE_POSITION} SET parsed=true WHERE id={id}"
    cursor.execute(query)
    connection.commit()
    connection.close()