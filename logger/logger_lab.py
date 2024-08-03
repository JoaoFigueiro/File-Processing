import random
import logging 


FORMAT = '%(levelname)s - %(message)s'

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

for minute in range(60): 
    temperature = random.randrange(20, 40)

    if temperature < 30: 
        logger.debug(f"{temperature} C")
    elif temperature >= 30 and temperature <= 35: 
        logger.warning(f"{temperature} C")
    else: 
        logger.critical(f"{temperature} C")