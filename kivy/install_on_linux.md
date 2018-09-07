# Kivy Installation

*Note*: is something not downloading try sudo apt-get update

1. Type the following commands:
   1. sudo apt-get install libsdl2-dev
   2. sudo apt-get install libsdl2-image-dev
   3. sudo apt-get install libsdl2-mixer-dev
   4. sudo apt-get install libsdl2-ttf-dev
       
   5. sudo apt-get install pkg-config
       
   6. sudo apt-get install libgl1-mesa-dev
   7. sudo apt-get install libgles2-mesa-dev
   8. sudo apt-get install python-setuptools
   9. sudo apt-get install libgstreamer1.0-dev
   10. sudo apt-get install git-core
       
   11. sudo apt-get install gstreamer1.0-plugins-{bad,base,good,ugly}
       
   12. sudo apt-get install gstreamer1.0-{omx,alsa}
   13. sudo apt-get install python-dev
   14. sudo apt-get install libmtdev-dev
   15. sudo apt-get install xclip
   16. sudo apt-get install xsel
2. Install the new version of Cython:
   1. sudo pip install --upgrade pip
   2. sudo pip install cython If pip doesn't work reinstall it by typing followings
           1. sudo apt-get remove python-pip
           2. sudo apt-get install python-pip
           3. sudo apt-get upgrade

X. If issues installing Cython:
   sudo apt remove pyhton-pip
   and then:
   sudo pip install cython

3. After that install Kivy globally by typing the following:
   1. sudo pip install git+https*:*//github.com/kivy/kivy.git@master
4. You will need to run some Kivy app in order for Kivy to create a config file unless it can't be found in: ~/.kivy/
5. After the config file appears type:
   1. pi@raspberrypi ~/kivy $ python ~/kivy/examples/demo/pictures/main.py
   2. sudo nano ~/.kivy/config.ini
6. Inside the file find the column with the name:
   
   [input]
   mouse = mouse
   %(name)s=probesysfs, provider=hidinput
   
   
7. Change it to following:
   
   [input]
   mouse = mouse
   mtdev_%(name)s=probesysfs, provider=mtdev
   hid_%(name)s=probesysfs, provider=hidinput
   
   
8. Save the updated file and exit
9. Now everything should work fine
10. Type sudo pip install kivy-garden
11. Type sudo garden install graph
12. Type sudo garden install —upgrade graph
13. Copy graph and matplotlib files into /usr/local/lib/python2.7/dist-packages/kivy/garden
14. Type sudo pip install pytz

*Important note*: kivy app should be run with: python main.py not: sudo python main.app
