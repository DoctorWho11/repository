
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
    autotools.configure("--with-appdefaultdir=/etc/X11/app-defaults \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
