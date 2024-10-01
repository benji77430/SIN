VERSION = 1.1
"""
AUTHOR : BENJI77
LAUNCHED : 25 sept. 2024 at 15:48
"""

"""1041011081081114432119111114108100"""
try:
   import os
   import platform
   import time
   import requests
   import socket
   import getpass
except ImportError as e:
    print(f'import error please install libs : {e}')
class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
system = platform.system()
print(system)
if system == "Windows":
    CLEAR = "cls"
elif system == "Darwin":
    CLEAR = "clear"

elif system == "Linux":
    CLEAR = "clear"
else:
    raise OSError(f"Unsupported operating system: {system}")
def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False
def update():
    if not check_internet_connection():
        print('no internet connection detected !')
        return
    verify = "https://raw.githubusercontent.com/benji77430/SIN/refs/heads/main/version.version"
    response = requests.get(verify)
    if response.status_code == 200:
        content = response.content
        version = float(content.decode())
        if version > version:
            print('SIN tools is already up to date !')
            return
        else: print(f'new update available : {version} !')
    url ="https://raw.githubusercontent.com/benji77430/SIN/refs/heads/main/sin.py"
    for _ in range(3):
        response = requests.get(url)
        progress = 3
        print(f'['+'-'*progress+'>'+' '*(10-progress)+f'] {progress*10}%',end='\r')
        time.sleep(0.3)

        if response.status_code == 200:
            content = response.content
            progress += 3
            print(f'['+'-'*progress+'>'+' '*(10-progress)+f'] {progress*10}%',end='\r')
            time.sleep(0.3)

            with open(__file__,'w')as f:
                f.write(content.decode())
                progress += 4
                print(f'['+'-'*progress+'>'+' '*(10-progress)+f'] {progress*10}%',end='\r')
                time.sleep(0.3)
                print(f'update to {version} done you should restart the script to get changes !')
                break
        else:
            print(f'status code : {response.status_code}')
def clear():
    os.system(CLEAR)
def decimal_to_hexadecimal(decimal):
    if decimal < 0:
        print('veuillez entrez un décimale valide !')
        exit()
    return hex(decimal)[2:].upper()
def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal,16)[2:].upper()
def get_bit(n):

    for i in range(0,1000):
        nb = 2**i
        if nb >= n:
            print(f'2^{i} => {n}')
            return i
        
def binary_and_hex_conversion():
    while True:
        clear()
        print(Colors.RED+ASCII+Colors.END)
        choice = input(f'''
    1) decimal to hexadecimal
    2) hexadecimal to decimal
    3) decimal to binary
    4) binary to decimals
    5) text to ASCII
    6) ASCII to text 
    q) main menu

{Colors.CYAN}┌──<[{Colors.RED}{getpass.getuser()}@{socket.gethostname()}{Colors.CYAN}]{Colors.END} ~ {Colors.RED}{os.getcwd()}{Colors.END} \n{Colors.CYAN}└──╼ ${Colors.END}  ''')

        if choice == "1":
            try:
                print('enter "q" to quit')

                while True:
                    decimal_number = int(input("veuillez entrez un nombre > "))
                    hexadecimal = decimal_to_hexadecimal(decimal_number)
                    print(hexadecimal)
            except ValueError:
                pass
        elif choice == "2":
            try:
                print('enter "q" to quit')

                while True:

                    table = {'0': 0, '1': 1, '2': 2, '3': 3,  
                            '4': 4, '5': 5, '6': 6, '7': 7, 
                            '8': 8, '9': 9, 'A': 10, 'B': 11,  
                            'C': 12, 'D': 13, 'E': 14, 'F': 15} 
                    
                    hexadecimal = input("Enter Hexadecimal Number: ").strip().upper() 
                    res = 0
                    
                    # computing max power value 
                    size = len(hexadecimal) - 1
                    
                    for num in hexadecimal: 
                        res = res + table[num]*16**size 
                        size = size - 1
                    
                    print(res) 
            except KeyError:
                pass
        elif choice == "3":
            try:
                print('enter "q" to quit')

                while True:
                    n = int(input('enter the number to translate > '))
                    bit = get_bit(n)
                    #traduction
                    bits = bin(n).split('b')[1]
                    #sécurité pour éviter d'avoir le 0b 
                    bits= str(bits).replace('b','0')
                    #rajouter des 0 a gauche si besoin 
                    if not len(bits) >= int(bit):
                        add = bit-len(bits)
                        bits = "0"*add + bits
                    #output
                    print(bits)

            except ValueError:
                pass
        elif choice == "4":
            try:
                print('enter "q" to quit')
                while True:
                    decimal_number = int(input("veuillez entrez un nombre > "),2)
                    print(decimal_number)
            except ValueError:
                pass
        elif choice == "5":
            try:
                while True:
                        
                    s = input('enter the text > ')
                    if s == "q":
                        break
                    print(' '.join(str(ord(c)) for c in s))
            except ValueError or KeyError:
                pass
        elif choice == "6":
            try:
                while True:
                    s = input('enter the ASCII > ')
                    if s == "q":
                        break
                    print(''.join(chr(int(c)) for c in s.split(' ')))
            except ValueError or KeyError:
                pass
        elif choice == "q":
            return
ASCII = rf"""
    o__ __o       o     o          o  
   /v     v\    _<|>_  <|\        <|> 
  />       <\          / \\o      / \ 
 _\o____          o    \o/ v\     \o/ 
      \_\__o__   <|>    |   <\     |  
            \    / \   / \    \o  / \ 
  \         /    \o/   \o/     v\ \o/ 
   o       o      |     |       <\ |  
   <\__ __/>     / \   / \        < \ 

        [+] created by benji77 {VERSION}                       
                                      """
while True:
    try:
        clear()
        print(Colors.RED+ASCII+Colors.END)
        choice = input(f'''
        1) binary and hexadecimal conversion
        2) exit
        3) update

{Colors.CYAN}┌──<[{Colors.RED}{getpass.getuser()}@{socket.gethostname()}{Colors.CYAN}]{Colors.END} ~ {Colors.RED}{os.getcwd()}{Colors.END} \n{Colors.CYAN}└──╼ ${Colors.END}  ''')
        if choice == "1":
            binary_and_hex_conversion()
        elif choice == "2":
            print('leaving..')
            exit()
        elif choice =="3":
            update()
            os.system(f'python {__file__}')

    except KeyboardInterrupt:
        exit()