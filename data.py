import requests
import logging
if __name__ == '__main__':
    log = logging.getLogger()
    log.level = logging.DEBUG
    log.addHandler(logging.StreamHandler(sys.stderr))
else:
    log = logging.getLogger(__name__)
a = requests.get('https://api.github.com/events')
next_response = requests.post('http://example.com/', cookies=response.cookies)
log.info(request.get)
log.info(request.post)



