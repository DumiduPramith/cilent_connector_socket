from database.database_handler import add_password
from log import set_logger

logger = set_logger(__name__)

def exec_handler_(raw_data):
    logger.debug(f"exec_handler: {raw_data}")
    data = raw_data.split('/')
    if data[0] == '__pword__':
        add_password(data[1])
