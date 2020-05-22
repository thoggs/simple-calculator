import app
import os

is_travis = 'TRAVIS' in os.environ
if is_travis:
    try:
        print(type(app.Calculadora()))
        exit(0)
    except Exception:
        print('Teste ERROR!')
        pass
