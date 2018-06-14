import urllib2

with open('urls.txt', 'r') as f:
    urls = []
    for url in f:
        urls.append(url.strip())

html = {}
for url in urls:
    urlFile = urllib2.urlopen(url)
    html[url] = urlFile.read()
    urlFile.close()

print (html)
