import urllib
import sys
# on récupère l'argument "message" passé dans le shell
msg = sys.argv[1]
# user : votre identifiant freemobile, du type 11111111
user = '1111111'
# pass : votre clé d’identification générée automatiquement par notre service
pass = 'AAAAAAAAAAAAAAA'

f = { 'user' : user, 'pass' : pass, 'msg' : msg}
url = "https://smsapi.free-mobile.fr/sendmsg?"
# on encode le tout et on crée l'url d'envoi
goto = url + urllib.urlencode(f)
# on envoie
urllib.urlopen(goto)
