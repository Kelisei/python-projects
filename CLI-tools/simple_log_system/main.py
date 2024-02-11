import csv
import json
import subprocess
import os

LENGTH = 120
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"
REJECT = "No es una opción pa"


def title():
    print("—" * LENGTH)
    print(BLUE + " SISTEMA DE LOGEO DE COMPRAS Y VENTAS ".center(LENGTH) + RESET)
    print("—" * LENGTH)


def main_options():
    print("Opciones:".center(LENGTH))
    print(
        GREEN
        + "Log de transaccion[1] | Ver total [2] | Modificar logs [3] | Modificar cuentas [4] | Limpiar consola [5]".center(
            LENGTH
        )
        + RESET
    )


def log_input():
    print(RED + "¿Egreso [1] o ingreso [2]? Salir[_]" + RESET)
    data = []
    option = input()
    if option != "1" and option != "2":
        print(REJECT)
    else:
        data.append(option == "1")
        account_names = "\n"
        for index, key in enumerate(vars.keys(), start=1):
            account_names += f"[{index}] {key} \n"
        print(RED + "¿Como pagó?" + BLUE + account_names + RESET)
        option = input()
        try:
            option = int(option)
            data.append(list(vars.keys())[option])
        except:
            print(REJECT)
        else:
            data.append(option)
            print(RED + "¿Cuanto?" + RESET)
            try:
                amount = float(input())
            except:
                print(REJECT)
            else:
                data.append(amount)
    if len(data) == 3:
        print(data)
    else:
        print('Fallo el log')
    print(len(data))

vars = {}
try:
    with open("Z:\\Mis logs\\actuales.dat", "r") as archivo:
        vars = json.load(archivo)
except:
    vars = {
        "Cuenta dni": 0.0,
        "Fisico": 0.0,
        "Uala": 0.0,
    }
    with open("Z:\\Mis logs\\actuales.dat", "w") as archivo:
        json.dump(vars, archivo)
logs = []
try:
    with open("Z:\\Mis logs\\logs.dat", "r"):
        reader = csv.reader("Z:\\Mis logs\\logs.dat")
        logs = [line for line in reader]
except:
    with open("Z:\\Mis logs\\logs.dat", "w"):
        pass
    
subprocess.call("clear" if os.name == "posix" else "cls", shell=True)
title()
while True:
    main_options()
    selection = input()
    try:
        selection = int(selection)
    except:
        print(REJECT)
    else:
        match selection:
            case 1:
                log_input()
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                subprocess.call("clear" if os.name == "posix" else "cls", shell=True)
                title()
            case _:
                print("Saliste")
                break
input()
