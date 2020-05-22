import os

istravis = os.environ.get('TRAVIS') == 'true'
if istravis:
    exit(0)
