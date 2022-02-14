import sys
from src.controlador.AdminController import AdminController
from src.controlador.PartnerController import PartnerController
from src.util.StartChecker import StartChecker
from src.vista.PartnerMenu import PartnerMenu



if __name__=="__main__":
    args=sys.argv
    if len(args)==5 or len(args)==6:
        if "-u" in args[1]:
            if StartChecker.checkDNILogin(args[2]):
                if "-p" in args[3]:
                    if StartChecker.checkPassord(args[2],args[4]):
                        if len(args)==6:
                            if args[5]=="-A":
                                if StartChecker.checkIsAdmin(args[2]):
                                    controller=AdminController()
                                    controller.startMenu()
                                else:
                                    raise SystemExit(f"Este usuario no es administrador")
                            else:
                                raise SystemExit(f"Debes introducir como ultimo parametro \"-A\"")
                        else:
                            controller=PartnerController()
                            controller.startMenu()
                    else:
                        raise SystemExit(f"La contraseña no coincide")
                else:
                    raise SystemExit(f"Como tercer argumento deberas poner \"-p\"")
            else:
                raise SystemExit(f"El DNI no existe")
        else:
            raise SystemExit(f"Introduzca -u para ejecutar")
    else:
        raise SystemExit(f"Minimo 4 argumentos")