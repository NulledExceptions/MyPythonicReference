import logging
import datetime

today = datetime.date.today()
log_name = 'WikiSearch_{}.log'.format(today)
logging.basicConfig(filename=log_name, level=logging.DEBUG)
log.setLevel(logging.DEBUG)
