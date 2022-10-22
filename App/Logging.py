import logging
import datetime as dt


logging.basicConfig(filename = "Log/rice_cloud.log", level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s')
T = dt.datetime.now()
logging.info(f"init_logger at {T}")

class app_logging:

    def error(self,message):
        logging.error(message)
    
    def info(self,message):
        logging.info(message)