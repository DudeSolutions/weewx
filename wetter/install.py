# $Id$
# installer for wetter.com
# Copyright 2014 Matthew Wall

from setup import Installer

def loader():
    return WetterInstaller()

class WetterInstaller(Installer):
    def __init__(self):
        super(WetterInstaller, self).__init__(
            version="0.1",
            name='wetter',
            description='Upload weather data to wetter.com.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            restful_services='user.wetter.Wetter',
            config={
                'Wetter': {
                    'username': 'INSERT_USERNAME_HERE',
                    'password': 'INSERT_PASSWORD_HERE'}},
            files=[('bin/user', ['bin/user/wetter.py'])]
            )