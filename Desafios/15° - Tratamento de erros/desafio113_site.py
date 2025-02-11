'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
import urllib
import urllib.request

try:
    urllib.request.urlopen('http://www.youtube.com.br')
except:
    print('Site não está disponível no momento!')
else:
    print('Site está funcionando normalmente.')