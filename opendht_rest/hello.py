import connexion
import os

def post_greeting(name: str) -> str:

    f = open("guru99.txt","w+")
    return 'Hello {name}'.format(name=name)