import re
import urllib
def getHtml(url):
    page = urllib.open(url)
    html = page.read()
    return html

ll = getHtml("http://wallhaven.cc/random?seed=0NShqJ&page=6")
