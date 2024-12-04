from os import path, environ
import configparser
from keyrings.cryptfile.cryptfile import CryptFileKeyring
import platform 

pltfrm = platform.system()

USER = environ['SUDO_USER'] if 'SUDO_USER' in environ else environ['USER']
CONFIG = configparser.ConfigParser()
if pltfrm == "Linux" or pltfrm == "Darwin":
    KEYRINGDIR = path.join(path.expanduser('~' + USER), ".meile-gui")
else:
    KEYRINGDIR = path.join(path.expanduser('~'), '.meile-gui')
CONFIG.read(path.join(KEYRINGDIR, "config.ini"))
PASSWORD = CONFIG['wallet'].get('password', '')
KEYNAME = CONFIG['wallet'].get('keyname', '')
    

def get_private_key_from_keyring(keyring_passphrase: str, wallet_name: str):
    kr = CryptFileKeyring()
    kr.filename = "keyring.cfg"
    kr.file_path = path.join(KEYRINGDIR, kr.filename)
    kr.keyring_key = keyring_passphrase

    return kr.get_password("meile-gui", wallet_name)
    
private_key_hex = get_private_key_from_keyring(PASSWORD, KEYNAME)
print(private_key_hex)