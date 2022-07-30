from structs.hierarchy import Heirachy

class Menu:
    def __init__(self) -> None:
        self.root = Heirachy()
        

    def _Menu(self): #NOSONAR
        opc:int = input("1. Crear Rutas Globales.\n2. Crear SubRutas.\n3. Organizar.\n4. Salir.\nIngrese lo que desea: ")
        
        if opc == 1:
            self.root._exist(self.root.routes_globales)
        elif opc == 2:
            self.root._exist(self.root.subroutes_librery)
            self.root._exist(self.root.subroutes_programming)
            self.root._exist(self.root.subroutes_university)
        elif opc == 4:
            print("-- Saliendo --")
            exit(0)
            

if __name__ == "__main__":
    Heirachy()._exist(Heirachy().subroutes_librery)
    Heirachy()._exist(Heirachy().subroutes_programming)
    
