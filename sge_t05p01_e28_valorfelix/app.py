import sys
from src.modelo.Partner import Partner

from src.utilidades.Prueba import Prueba
from src.vista import menuAdministracion
from src.controlador.AdminController import AdminController
from src.modelo import Club



if __name__=="__main__":
    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
    if "-a" in opts:
        
        AdminController.startMenu()
    else:
        raise SystemExit(f"Introduzca -a para ejecutar")