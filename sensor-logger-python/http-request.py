import requests
# ploads = {'things':2,'total':25}
r = requests.get('http://192.168.1.49:8000')
print(r.text)
print(r.url)