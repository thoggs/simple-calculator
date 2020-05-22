import app
import os

istravis = os.environ.get('TRAVIS') == 'true'
if istravis:
    try:
        print(type(app.Calculadora()))
        exit(0)
    except Exception:
        print('Teste ERROR!')
        pass
