#coding=utf-8
import sys
import xbmcgui
import xbmcplugin
import re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys
import urlparse
#import ssl
#context = ssl.create_default_context(Purpose.CLIENT_AUTH)
#context.options = ssl.PROTOCOL_TLSv1
#context.options &= ~ssl.OP_NO_SSLv3

######################DEFINE FUNCTIONS###################################

def getHTML(url):
  req = urllib2.Request(url)
  req.add_unredirected_header('User-agent','Mozilla/5.0')
  try:
     response = urllib2.urlopen(req)
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
    url = build_url({'mode': 'folder', 'foldername': foldername,'pageurl': pageurl})
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
    html = BeautifulSoup(getHTML(pageurl),"html.parser")
    
    #tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
    tempLink = html.find('a',class_='btn-watch').get('href')
    
    verify = "javascript:alert"
    confirm = [x for x in tempLink if verify in x] 
    if len(confirm) == 0:
   
      html2 = BeautifulSoup(getHTML(tempLink),"html.parser")
      #tempLink2 = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
      tempLink2 = html2.find_all('script',type='text/javascript')
      
      
      if tempLink2[6].get('src')[8:12] == 'grab':
       httpsLink = tempLink2[6].get('src')
       httpLink = httpsLink[0:4] + httpsLink[5:]
       html3 = BeautifulSoup(getHTML(httpLink),"html.parser")
       if html3 != 404:
        
           filelink = re.compile('"file":"(.+?)"').findall(html3.text)
          
          
           if len(filelink) >= 1:
             tlink  = str(filelink[0].replace('\\','').strip('"'))
             link = tlink.replace(';','') 
             li = xbmcgui.ListItem(foldername, iconImage='DefaultVideo.png')
             xbmcplugin.addDirectoryItem(handle=addon_handle, url=link, listitem=li)


xbmcplugin.endOfDirectory(addon_handle)

