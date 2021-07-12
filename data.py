import requests
a = requests.get('https://api.github.com/events')
b = requests.post('https://httpbin.org/post', data = {'key':'value'})  

