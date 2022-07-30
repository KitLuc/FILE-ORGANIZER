import os


class Heirachy:
    def __init__(self) -> None:
        self.routes_globales:list = [r'E:/Folders_Global',
                                     r'E:/Folders_Global/Librery_Global',
                                     r'E:/Folders_Global/UNIs',
                                     r'E:/Folders_Global/Proyects_Programming',
                                     r'E:/Folders_Global/Diplomas']

        self.subroutes_librery:list = [r'E:/Folders_Global/Librery_Global/Mathematics',
                                       r'E:/Folders_Global/Librery_Global/Philosofic',
                                       r'E:/Folders_Global/Librery_Global/Programming']

        self.subroutes_university:list = [r'E:/Folders_Global/UNIs/Pascual_Bravo',
                                          r'E:/Folders_Global/UNIs/UNAL',
                                          r'E:/Folders_Global/UNIs/UdeA']

        self.subroutes_programming:list = [r'E:/Folders_Global/Proyects_Programming/Python',
                                           r'E:/Folders_Global/Proyects_Programming/Java',
                                           r'E:/Folders_Global/Proyects_Programming/Cshard',
                                           r'E:/Folders_Global/Proyects_Programming/JavaScript',
                                           r'E:/Folders_Global/Proyects_Programming/PhP']
        
    def _exist(self, folders:list) -> None:
        for folder in range(0, len(folders)):
            if not os.path.exists(folders[folder]):
                os.makedirs(folders[folder])
                
