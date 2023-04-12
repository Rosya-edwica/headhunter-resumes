from storage.config import connect, TABLE_POSITION
from models import Position


def GetPositions() -> list[Position]:
    positions: list[Position] = []
    connection = connect()
    cursor = connection.cursor()
    query = f"SELECT id, parent_id, level, title, prof_area, other_names FROM {TABLE_POSITION} WHERE parsed=false"
    cursor.execute(query)
    positions = [Position(*i) for i in cursor.fetchall()]
    connection.close()
    return positions
