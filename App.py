#/usr/bin/env python

import os
import requests
from pyquery import PyQuery as pq

class Jav:

  def play(self, url):
    os.system('mpv ' + url)
    return True

  def create_url(self, plate):
    api = 'https://javzw.com/'
    return api + plate

  def getURL(self, plate = 'DAVK-042'):
    url = self.create_url(plate)
    _res = requests.get(url)
    jQuery = pq(_res.text)
    _p = jQuery('title').html()
    _url = jQuery('#my-player source').attr('src')
    print(_url)
    self.play(_url)
    pass

if __name__ == '__main__':
  dd = Jav()
  dd.getURL()