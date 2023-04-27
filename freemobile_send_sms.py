#!/usr/bin/python3

import argparse
import configparser
import getpass
import urllib.parse
import urllib.request
import os
import pwd
import sys

def change_user(user):
    try:
        newuid = pwd.getpwnam(user).pw_uid
        os.setuid(newuid)
        #if user is found change environ to later resolve its home
        pwdentry = pwd.getpwuid(os.geteuid())
        os.environ['HOME'] = pwdentry.pw_dir
        os.environ['LOGNAME'] = pwdentry.pw_name
    except KeyError as e:
        sys.exit(f'User {args.user} not found on the system')

def read_config():
    config = configparser.ConfigParser()
    configfile = os.path.expanduser('~/.freemobileconfig')
    if not os.path.isfile(configfile):
        sys.exit(f'No config file found in {getpass.getuser()} home')
    config.read(configfile)
    if not (config.has_option('id', 'user') and config.has_option('id', 'key')):
        sys.exit('Invalid config file')
    return config['id']['user'], config['id']['key']

def send_sms(msg, user=None):
    if user is not None:
        change_user(user)
    userid, key = read_config()
    f = { 'user' : userid, 'pass' : key, 'msg' : msg}
    url = "https://smsapi.free-mobile.fr/sendmsg?"
    # on encode le tout et on crée l'url d'envoi
    goto = url + urllib.parse.urlencode(f)
    # on envoie
    urllib.request.urlopen(goto)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                    prog='FreeMobile SMS',
                    description='Send a message to a referenced user')
    parser.add_argument('message')
    parser.add_argument('-u', '--user')
    args = parser.parse_args()
    send_sms(args.message, user=args.user)
