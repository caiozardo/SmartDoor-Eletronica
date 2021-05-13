#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# Descrição do sistema
#
##

import time  # Usano nas pausas (sleep)
from gpiozero import *  # Bibioteca de controle das gpios

# Variáveis globais representando as ios
# Entrada é lida com button.is_pressed
# Saída é escrita com led.on() e led.off()
signal_rfid = Button(11)
signal_biometria = Button(13)
signal_temp = Button(15)
signal_entrada = Led(7)


# Lê sinal do RFID
def myrfid():
    global signal_rfid

    if signal_rfid.is_pressed:
        return True
    else:
        return False


# Lê sinal da biometria
def mybiometria():
    global signal_biometria

    if signal_biometria.is_pressed:
        return True
    else:
        return False


# Lê sinal da temperatura
def mytemp():
    global signal_temp

    if signal_temp.is_pressed:
        return True
    else:
        return False


# Processa o acesso
def grant_accesss(access: bool):
    global signal_entrada

    if access:  # Envia sinal de abertura por 2 segundos.
        signal_entrada.on()
        time.sleep(2)
        signal_entrada.off()
    else:  # Envia sinal de fechamento.
        signal_entrada.off()


# Loop principal do sistema
while (True):
    # Aguarda 1 segundo
    time.sleep(1)

    # Garante o acesso caso os sinais sejam todos verdadeiros.
    grant_acess(myrfid() and mybiometria() and mytemp())
