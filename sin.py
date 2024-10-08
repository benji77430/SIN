VERSION = 1.32
"""
AUTHOR : BENJI77
LAUNCHED : 25 sept. 2024 at 15:48
"""
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


try:
   import os
   import platform
   import subprocess
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
os.system("cls" if system == "Windows" else "clear")
print(Colors.GREEN+ASCII+Colors.END)
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

def check_update():
    if not check_internet_connection():
        print('no internet connection detected !')
        return
    verify = "https://raw.githubusercontent.com/benji77430/SIN/refs/heads/main/version.version"
    response = requests.get(verify)
    if response.status_code == 200:
        content = response.content
        version = float(content.decode())
        if version > VERSION:
            print(f'new update available : {version} !')
            return True
        else: print(f'SIN tools is already up to date !')
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
        progress = 10
        print(f'['+'-'*progress+'>'+' '*(30-progress)+f'] {int(progress*10/3)}%',end='\r')
        time.sleep(0.3)

        if response.status_code == 200:
            content = response.content
            progress += 10
            print(f'['+'-'*progress+'>'+' '*(30-progress)+f'] {int(progress*10/3)}%',end='\r')
            time.sleep(0.3)

            with open(__file__,'w')as f:
                f.write(content.decode())
                progress += 10
                print(f'['+'-'*progress+'>'+' '*(30-progress)+f'] {int(progress*10/3)}%',end='\r')
                time.sleep(0.3)
                print('SIN was updated ! starting new version...')
                return content.decode()
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
def get_bits(n):

    for i in range(0,1000):
        nb = 2**i
        if nb >= n:
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
                    print(f'{Colors.RED}-{Colors.END}'*50)

                    decimal_number = int(input("veuillez entrez un nombre > "))
                    #détail le calcul
                    # Détail du calcul de décimal à hexadécimal
                    print(f"Calcul détaillé pour convertir {decimal_number} en hexadécimal:")
                    
                    # Initialisation
                    quotient = decimal_number
                    remainders = []
                    
                    # Boucle de division successive par 16
                    while quotient > 0:
                        remainder = quotient % 16
                        remainders.append(remainder)
                        print(f"{quotient} ÷ 16 = {quotient // 16} avec un reste de {remainder}")
                        quotient = quotient // 16
                    
                    # Conversion des restes en caractères hexadécimaux
                    hex_chars = "0123456789ABCDEF"
                    hex_result = ""
                    for remainder in reversed(remainders):
                        hex_result += hex_chars[remainder]
                        print(f"Reste {remainder} correspond à '{hex_chars[remainder]}' en hexadécimal")
                    
                    print(f"Résultat final en hexadécimal: {hex_result}")
                    hexadecimal = decimal_to_hexadecimal(decimal_number)
                    print("\nresult : ",hexadecimal)
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
                    print(f'{Colors.RED}-{Colors.END}'*50)
                    
                    
                    hexadecimal = input("Enter Hexadecimal Number: ").strip().upper() 
                    res = 0
                    
                    # computing max power value 
                    size = len(hexadecimal) - 1
                    
                    for num in hexadecimal: 
                        res = res + table[num]*16**size 
                        size = size - 1
                    # Détail du calcul d'hexadécimal à décimal
                    print(f"Calcul détaillé pour convertir {hexadecimal} en décimal:")
                    
                    size = len(hexadecimal) - 1
                    for index, digit in enumerate(hexadecimal):
                        value = table[digit]
                        power = 16 ** (size - index)
                        contribution = value * power
                        print(f"Chiffre '{digit}' à la position {index}:")
                        print(f"  Valeur en décimal: {value}")
                        print(f"  Puissance de 16: 16^{size - index} = {power}")
                        print(f"  Contribution: {value} * {power} = {contribution}")
                        print(f"  Somme partielle: {res + contribution}")
                        res += contribution
                    
                    print(f"Résultat final en décimal: {res}")
                    
            except KeyError:
                pass
        elif choice == "3":
            try:
                print('enter "q" to quit')

                while True:
                    print(f'{Colors.RED}-{Colors.END}'*50)
                    

                    n = int(input('enter the number to translate > '))
                    bit = get_bit(n)
                    bits = bin(n).split('b')[1]
                    bits= str(bits).replace('b','0')
                    if not len(bits) >= int(bit):
                        add = bit-len(bits)
                        bits = "0"*add + bits

                    # Détail du calcul de décimal à binaire
                    print(f"Calcul détaillé pour convertir {n} en binaire:")
                    
                    temp_n = n
                    steps = []
                    while temp_n > 0:
                        remainder = temp_n % 2
                        quotient = temp_n // 2
                        steps.append((temp_n, quotient, remainder))
                        temp_n = quotient
                    
                    steps.reverse()
                    for i, (dividend, quotient, remainder) in enumerate(steps):
                        print(f"Étape {i+1}:")
                        print(f"  {dividend} ÷ 2 = {quotient} reste {remainder}")
                        print(f"  Bit ajouté: {remainder}")
                        partial_result = ''.join(str(step[2]) for step in steps[-(i+1):])
                        print(f"  Résultat partiel: {partial_result}")
                        print('')
                    print(f"Résultat final en binaire: {bits}")

            except ValueError:
                pass
        elif choice == "4":
            try:
                print('enter "q to quit')
                while True:
                    print(f'{Colors.RED}-{Colors.END}'*50)
                    

                    decimal_number = int(input("veuillez entrez un nombre > "),2)
                    # Détail du calcul de binaire à décimal
                    print(f"\nCalcul détaillé pour convertir {bin(decimal_number)[2:]} en décimal:")
                    binary = bin(decimal_number)[2:]
                    total = 0
                    for i, digit in enumerate(binary[::-1]):
                        if digit == '1':
                            value = 2 ** i
                            total += value
                            print(f"Bit {i}: 1 * 2^{i} = {value}")
                            print(f"Somme partielle: {total}")
                        print('')
                    print(f"\nRésultat final: {total}")
            except ValueError:
                pass
        elif choice == "5":
            try:
                print('enter "q" to quit')

                while True:
                    print(f'{Colors.RED}-{Colors.END}'*50)
                    
                    s = input('enter the text > ')
                    if s == "q":
                        break
                    res = ' '.join(str(ord(c)) for c in s)
                    print("\nresult : ",res)
                    print("\nhexadecimal "," ".join(decimal_to_hexadecimal(int(i)) for i in res.split(' ') ) )
                    def bny(n):
                        n = int(n)
                        bit = get_bits(n)
                        bits = bin(n).split('b')[1]
                        bits= str(bits).replace('b','0')
                        if not len(bits) >= int(bit):
                            add = bit-len(bits)
                            bits = "0"*add + bits
                        return bits
                    biny = " ".join(str(bny(i)) for i in res.split(' '))
                    print("\nbinairy : ",biny)
                    # Détailler le calcul pour binaire, hexadécimal et décimal
                    print("\nDétail des calculs pour chaque caractère:")
                    for char in s:
                        ascii_value = ord(char)
                        binary_value = bny(ascii_value)
                        hex_value = decimal_to_hexadecimal(ascii_value)
                        
                        
                        
                        # Détail du calcul décimal vers binaire
                        print("\nDétail de la conversion décimal vers binaire:")
                        temp_n = ascii_value
                        steps = []
                        while temp_n > 0:
                            remainder = temp_n % 2
                            quotient = temp_n // 2
                            steps.append((temp_n, quotient, remainder))
                            temp_n = quotient
                        
                        steps.reverse()
                        for i, (dividend, quotient, remainder) in enumerate(steps):
                            print(f"  Étape {i+1}:")
                            print(f"    {dividend} ÷ 2 = {quotient} reste {remainder}")
                            print(f"    Bit ajouté: {remainder}")
                            partial_result = ''.join(str(step[2]) for step in steps[-(i+1):])
                            print(f"    Résultat partiel: {partial_result}")
                            print('')

                        
                        print(f"  Résultat final en binaire: {binary_value}")
                        
                        # Détail du calcul décimal vers hexadécimal
                        print("\nDétail de la conversion décimal vers hexadécimal:")
                        temp_n = ascii_value
                        steps = []
                        hex_digits = "0123456789ABCDEF"
                        while temp_n > 0:
                            remainder = temp_n % 16
                            quotient = temp_n // 16
                            steps.append((temp_n, quotient, hex_digits[remainder]))
                            temp_n = quotient
                        
                        steps.reverse()
                        for i, (dividend, quotient, remainder) in enumerate(steps):
                            print(f"  Étape {i+1}:")
                            print(f"    {dividend} ÷ 16 = {quotient} reste {remainder}")
                            print(f"    Chiffre hexadécimal ajouté: {remainder}")
                            partial_result = ''.join(step[2] for step in steps[-(i+1):])
                            print(f"    Résultat partiel: {partial_result}")
                            print('')

                        
                        print(f"\nCaractère '{char}':")
                        print(f"ASCII (décimal): {ascii_value}")
                        print(f"Hexadécimal: {hex_value}")
                        print(f"Binaire: {binary_value}\n")
            except ValueError or KeyError:
                pass
        elif choice == "6":
            try:
                print('enter "q" to quit')

                while True:
                    print(f'{Colors.RED}-{Colors.END}'*50)
                    

                    s = input('enter the ASCII > ')
                    if s == "q":
                        break                
                    if s != "q":
                        ascii_values = s.split(' ')
                        for i, ascii_value in enumerate(ascii_values):
                            try:
                                int_value = int(ascii_value)
                                char = chr(int_value)
                                print(f"Étape {i+1}:")
                                print(f"  Valeur ASCII : {int_value}")
                                print(f"  Caractère correspondant : '{char}'")
                                if i == 0:
                                    result = char
                                else:
                                    result += char
                                print(f"  Résultat partiel : '{result}'")
                                print('')
                            except ValueError:
                                print(f"  Erreur : '{ascii_value}' n'est pas une valeur ASCII valide. Ignoré.")
                        print(f"\nRésultat final : '{result}'")
            except ValueError or KeyError:
                pass
        elif choice == "-" or choice == "q":
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

is_update = check_update()
if is_update:
    exec(update())
    os.system(f'python {__file__}')
while True:
    try:
        clear()
        print(Colors.RED+ASCII+Colors.END)
        choice = input(f'''
        1) binary and hexadecimal conversion
        2) exit
        3) {"start processing" if system != "Windows" else "processing can't be started with windows by SIN"}
        4) BENJI77430 github page

{Colors.CYAN}┌──<[{Colors.RED}{getpass.getuser()}@{socket.gethostname()}{Colors.CYAN}]{Colors.END} ~ {Colors.RED}{os.getcwd()}{Colors.END} \n{Colors.CYAN}└──╼ ${Colors.END}  ''')
        if choice == "1":
            binary_and_hex_conversion()
        elif choice == "2":
            print('leaving..')
            exit()            
        elif choice == "3":
            if system != "Windows":
                try:
                    subprocess.Popen("processing")
                except FileNotFoundError:
                    print("tentative d'installation de processing...")
                    if os.path.exists("/etc/os-release"):
                        with open("/etc/os-release", "r") as f:
                            distro_info = f.read()
                        if "Ubuntu" in distro_info or "Debian" in distro_info:
                            os.system("sudo add-apt-repository ppa:processing/ppa")
                            os.system("sudo apt-get update")
                            os.system("sudo apt-get install processing")
                            subprocess.Popen("processing")
                        elif "Fedora" in distro_info:
                            os.system("sudo dnf install processing")
                            subprocess.Popen("processing")
                        elif "Arch" in distro_info:
                            os.system("yay -S processing --noconfirm")
                            subprocess.Popen("processing")      
                        else:
                            print("distribution linux non prise en charge !")
                            time.sleep(1)
                    else:
                        print("détection de la distribution linux impossible !")
                        time.sleep(1)                
                print("installation terminée !")
            else:
                print('installation non prise en charge sur windows !')
                time.sleep(1)
        elif choice == "4":
            if system == "Windows":
                os.system("start https://github.com/benji77430")
            elif system == "Darwin":
                os.system("open https://github.com/benji77430")
            else: 
                os.system("xdg-open https://github.com/benji77430")
    except KeyboardInterrupt:
        exit()
