#coding=utf-8
import sys
import xbmcgui
import xbmcplugin
import re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys
import urlparse

######################DEFINE FUNCTIONS###################################

def getHTML(url):
  req = urllib2.Request(url)
  req.add_unredirected_header('User-agent','Mozilla/5.0')
  try:
     response = urllib2.urlopen(req).read()
  except urllib2.HTTPError, e:
     response = e.getcode()
  return response

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def addFolder(url):
  soup = BeautifulSoup(getHTML(url),"html.parser")
  list = soup.find('ul',class_='cfv')
  pagination = soup.find('div',class_='pagination')
  
  for item in list.select('li'):
   
    foldername = u' '.join(item.a.get('title')).encode('utf-8').strip()
    pageurl = item.a.get('href')
    img = item.img.get('src')
    url = build_url({'mode': 'folder', 'foldername': foldername,'pageurl': pageurl,'image': img})
    li = xbmcgui.ListItem(foldername, iconImage=img)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)
  for item in pagination.select('a'):
     pageurl = item['href']
     foldername = "Page " + str(item.contents[0])
     url = build_url({'mode': 'folder', 'foldername': foldername,'pageurl': pageurl})
     li = xbmcgui.ListItem(foldername, iconImage='DefaultFolder.png')
     xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,listitem=li, isFolder=True)	
  xbmcplugin.endOfDirectory(addon_handle)

#######################END FUNCTION#################################################

#######################INITIALIZATION###############################################
base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
xbmcplugin.setContent(addon_handle, 'movies')
mode = args.get('mode', None)
url = "http://xemphimso.com/xem-phim-chieu-rap.html"

#######################MAIN#########################################################
# by year url http://xemphimso.com/xem-phim-chieu-rap.html?c=0&r=0&y=
#search_url = "http://xemphimso.com/tim-kiem/kungfu+panda/"

#--------------------------------------------------------#
#create playlist
#--------------------------------------------------------#
if mode is None:
  addFolder(url)

elif mode[0] == 'folder':
   foldername = str(args['foldername'][0])
   pageurl = args['pageurl'][0]
   if foldername[:4] == "Page":
      addFolder(pageurl)
   else:
    html = getHTML(pageurl)
    img = args['image'][0]
    tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
    verify = "javascript:alert"
    confirm = [x for x in tempLink if verify in x] 
    if len(confirm) == 0:
   
      html2 = getHTML(tempLink[0])
      tempLink2 = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
      search = "grab."
      result = [s for s in tempLink2 if search in s]
      if len(result) > 0:
       html3 = getHTML(result[0])
       if html3 != 404:
        
           filelink = re.compile('"file":"(.+?)","label"').findall(html3)
          
          
           if len(filelink) >= 1:
             link  = filelink[len(filelink)-1].replace('\\','').strip('"')
             li = xbmcgui.ListItem(foldername, iconImage=img)
			 #li = xbmcgui.ListItem(foldername, iconImage='DefaultVideo.png')
             xbmcplugin.addDirectoryItem(handle=addon_handle, url=link, listitem=li)


xbmcplugin.endOfDirectory(addon_handle)