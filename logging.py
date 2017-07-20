import logging
import datetime

today = datetime.date.today()
log_name = 'WikiSearch_{}.log'.format(today)
logging.basicConfig(filename=log_name, level=logging.DEBUG)
#log = logging.getLogger('econtext')
#log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
