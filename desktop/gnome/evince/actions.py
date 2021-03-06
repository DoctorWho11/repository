#!/usr/bin/python

# Created For Evolve OS

from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())


def setup():
    # bashisms. bashisms everywhere.
    shelltools.export("CONFIG_SHELL", "/bin/bash")
    autotools.configure("--enable-introspection \
                         --disable-static")


def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS")
