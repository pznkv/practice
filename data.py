import requests
import logging
if __name__ == '__main__':
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
else:
    log = logging.getLogger(__name__)

a = requests.get('https://api.github.com/events')
b = requests.post('https://httpbin.org/post', data = {'key':'value'})  
log.info(a)
log.info(b)

