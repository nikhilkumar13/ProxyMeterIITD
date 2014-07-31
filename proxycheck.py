#!/usr/bin/python

import appindicator
import pynotify
import gtk
import os

username="yourusername"
password="yourpassword"
frequency=15*60*1000  #15 minutes
iconPath='/Path/to/icon'   #set path to your own icon


a = appindicator.Indicator('tubecheck', iconPath, appindicator.CATEGORY_APPLICATION_STATUS)
a.set_status(appindicator.STATUS_ACTIVE)
m = gtk.Menu() 
qi = gtk.MenuItem( 'Quit' )
ch=gtk.MenuItem('Check')
m.append(ch)
m.append(qi)

a.set_menu(m)
ch.show()
qi.show()
def getData(username,password):
	command= 'curl -k -d'+ '"uid='+username+'&magic_word='+password+'&1=Proxy Usage"'+' https://proxy22.iitd.ernet.in/squish/'+ ' | sed -n "35,35p;35q"'+'| grep -o "[1-9]\S*[Gb|mb]"'
	p=os.popen(command,"r")
	data=p.readline()
	return  data.strip()
def Check(item):
	data=getData(username,password)
	a.set_label("(" +data +")")
	return True
def update():
	data=getData(username,password)
	a.set_label("(" +data +")")
	return True
def quit(item):
	gtk.main_quit()
qi.connect('activate', quit)
ch.connect('activate',Check)
data=getData(username,password)
a.set_label("(" +data +")")
gtk.timeout_add(frequency, update)
gtk.main()


