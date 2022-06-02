from requests import get, exceptions
import msvcrt
from tqdm import tqdm
def check_connection():
    try:
        get('http://google.com', timeout = 3)
        print('Google connected')
        get('https://www.facebook.com', timeout=4)
        print('Facebook connected')
        get('https://www.youtube.com', timeout=5)
        print('Youtube connected')
        get('https://www.xvideos.com', timeout=6)
        print('Xvideos connected')
    except exceptions.ConnectionError:
        print('not connected')
def msg():
    print("Haciendo ping")
def carga_malota():
        for i in tqdm(range(int(4))):
            pass
msg()
carga_malota()
check_connection()
msvcrt.getch()



