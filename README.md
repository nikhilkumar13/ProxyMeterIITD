This is small python code that can show you your IIT-D proxy usage in ubuntu app indicator top bar.
Open the proxycheck.py file  set your username password, path to icon (png) image, frequency of your choice(default is 15 minutes), URL to proxy page whether you are Btech/dual etc.and run the Code. After that you may have to install a dependency, python app indicator package.when done with that re run the code.
Then your proxy meter is all set to check your proxy usage in top bar and will Update it in  every 15 minute or whatever you have set.
Tested! on ubuntu 14.04
Also you can also add this code to startup application to run the proxyMeter automaticaly when system starts.

TODO:
Add the automatic proxy settings. Basically this can act as a single point where we can set the proxy settings and it will automatically update the proxy setting for browsers, apt etc.
Make this as a QT/GTK+ application which could be using a daemon or something underneath it.
