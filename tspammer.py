import requests
import os
import time

def menu():
  os.system("cls")
  os.system("color 2")
  try:
    print("""
    _______                                            
   |__   __|                                           
      | |___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
      | / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
      | \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
      |_|___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
            | |                                        
            |_|  
    """)
    webhook = input('\n[+] Ingresa el link de la webhook: ')
    mensaje = input('[+] Ingresa el mensaje que quieres enviar en la webhook: ')
    while True:
      requests.post(webhook, json={'username': 'Spammer', 'content': mensaje})
      print('\n[~] Enviando mensaje...')
  except KeyboardInterrupt:
    print('\n[~] Saliendo del programa...')
    time.sleep(1)
    exit()

menu()
