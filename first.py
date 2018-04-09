import urllib2
request = urllib2.Request("http://mail.163.com/js6/main.jsp?sid=jCuKzySZrLXuZImUtOZZOaPqpCxpKIha&df=unknow#module=read.ReadModule%7C%7B%22area%22%3A%22normal%22%2C%22isThread%22%3Afalse%2C%22viewType%22%3A%22%22%2C%22id%22%3A%2215%3A1tbiDwsjWlUMFjdWOQAAsq%22%2C%22fid%22%3A1%7D")
try:
    response = urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason
with open('test.html', 'w') as f:
    f.write(response.read())
print response.read()
