#coding=utf-8
import sys
import xbmcgui
import xbmcplugin
import re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys
import urlparse

def getHTML(url):
  req = urllib2.Request(url)
  req.add_unredirected_header('User-agent','Mozilla/5.0')
  try:
     response = urllib2.urlopen(req).read()
  except urllib2.HTTPError, e:
     response = e.getcode()
  return response

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

url = "http://xemphimso.com/xem-phim-chieu-rap.html"

mList = []
titleList = []
linkList = []
imgList = []
pageList = []
yearList = []



soup = BeautifulSoup(getHTML(url),"html.parser")
list = soup.find('ul',class_='cfv')
count = 0
lastPage = 0


# by year url http://xemphimso.com/xem-phim-chieu-rap.html?c=0&r=0&y=
#search_url = "http://xemphimso.com/tim-kiem/kungfu+panda/"

#get movies list by year
#for y in soup.find_all(')
# get pagination
for page in soup.find_all('a',class_='pagelink'):
  tempPage = str(page.get('href'))
  if page.text == "LAST":
     lastIndex = len(page.get('href')) - 6
     lastPage = int(page.get('href')[lastIndex -1:lastIndex + 1])
     currentLen = len(pageList)
     while currentLen <= lastPage:
       newPage = tempPage[0:45] + str(currentLen) + ".html"
       pageList.append(newPage)
       currentLen = currentLen + 1
  else:
    pageList.append(page.get('href'))

if mode is None:
  while count <= lastPage :
    pageNum = count + 1
    foldername = 'Page ' + str(pageNum)
    url = build_url({'mode': 'folder', 'foldername': foldername})
    li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
    count = count +1
  xbmcplugin.endOfDirectory(addon_handle)

count = 0

if mode == 'folder':
  foldername = args['foldername'][0]
  pNum = int(foldername[4:]) - 1
 
  if pNum >= 1:
    soup = BeautifulSoup(getHTML(pageList[pNum]),"html.parser")
    list = soup.find('ul',class_='cfv')
 
for item in list.select('li'):
   mList.append(item.a.get('href'))
   titleList.append(item.a.get('title'))
   imgList.append(item.img.get('src'))

while count < len(mList) - 1:
 
  html = getHTML(mList[count]) 
  tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
  verify = "javascript:alert"
  confirm = [x for x in tempLink if verify in x] 
  if len(confirm) == 1:
   
   mList.remove(mList[count])
   del titleList[count]
   del imgList[count]
   continue
  else:
   html2 = getHTML(tempLink[0])
   tempLink2 = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
   search = "grab."
   result = [s for s in tempLink2 if search in s]
   if len(result) > 0:
      html3 = getHTML(result[0])
      if html3 == 404:
          del mList[count]
          del titleList[count]
          del imgList[count]
          continue
      else:
          filelink = re.compile('"file":"(.+?)","label"').findall(html3)
          
          if len(filelink) == 0:
            link = tempLink[0]
          if len(filelink) >= 1:
            link  = filelink[len(filelink)-1].replace('\\','').strip('"')
          title = titleList[count]
          image = imgList[count]
          li = xbmcgui.ListItem(title, iconImage=image)
          xbmcplugin.addDirectoryItem(handle=addon_handle, url=link, listitem=li)
   else:
     del mList[count]
     continue 
  count = count + 1    


xbmcplugin.endOfDirectory(addon_handle)

