global ControlCovid19
ControlCovid19 = list()

class Casos:
 
    def _init_(self):
        self.nombre = []
        self.apellido = []
        self.fecha_nacimiento = []
        self.edad = []
        self.documento = []
        self.pais = []
        self.genero = []
        self.status = []
        
    def menu(self):
        opcion = 0
    
        while opcion !=5:
            print("____________________________")
            print ("    B i e n v e n i d o        ")
            print ("------Menu de Opciones-----")
            print ("  [1.-Registrar Personas]")
            print ("  [2.-Status de Personas]")
            print ("  [3.-Mostrar Casos]")
            print ("  [4.-Status Actual]")
            print ("  [5.-Salir]")
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                self.registrar()
            elif opcion == 2:
                self.status()
            elif opcion == 3:
                self.mostrar()
            elif opcion == 4:
                self.statusActual()
            elif opcion == 5:
                self.salir()
            
    def registrar(self):
        print("______Registro de Personas______")
        persona = Casos()

        persona.nombre = input("Ingrese el nombre: ")
        persona.apellido = input("Ingrese el apellido: ")
        persona.fecha_nacimiento = input("Ingrese la fecha de nacimiento: ")
        persona.edad = input("Ingrese la edad: ")
        persona.documento = input ("Ingrese el numero de documento: ")
        persona.pais = input("Ingrese el pais: ")
        persona.genero = input("Ingrese el genero: ")
        persona.status = ("Sospechoso")

        ControlCovid19.append(persona)
        return

    def status(self):
        sintomas = 0
        print("______Status de Personas______")
        documento = input("Ingrese el numero de documento de la persona que busca ")

        for persona in ControlCovid19:
            if persona.documento == documento:
                print(persona.nombre, "-", persona.apellido, "-",persona.fecha_nacimiento, "-", persona.edad, "-",persona.documento, "-",persona.pais, "-", persona.genero, "-",persona.status, "-" )

        print("...A continuacion realizaremos una pequeña prueba")
        print("-----¿Cual de los siguientes sintomas posee?-----")
        print("[1.Fiebre, Tos productiva, Dolor muscular, Moqueo Frecuente, Estornudos]")
        print("[2.Fiebre, Tos seca, Dolor de cabeza, Dificultad Respiratoria, Fatiga]")
        print("[3.Fiebre, Tos seca, Congestion nasal,Picazon, Irritacion, Estornudos]")
        print("[4. SALIR]")
        sintomas = int(input("Ingrese la opcion correspondiente a los sintomas "))
            
        if sintomas == 1:
            print("/////La persona posee un status INACTIVO, presenta sintomas de un Resfriado Comun/////")
            persona.status =("Inactivo")
        elif sintomas == 2:
            print ("/////La persona posee un status ACTIVO, presenta sintomas del COVID19/////")
            persona.status = ("Activo")
        elif sintomas == 3:
            print ("/////La persona posee un status INACTIVO, presenta sintomas de Alergias/////")
            persona.status = ("Inactivo")
        elif sintomas == 4:
            exit
            
    def statusActual(self):
        opcion1=0
        opcion2=0
        print ("______Estado Actual______")
        documento = input("Ingrese el numero de documento de la persona ")
    
        for persona in ControlCovid19:
            if persona.documento == documento:
                print (persona.nombre, "-", persona.apellido, "-",persona.fecha_nacimiento, "-", persona.edad, "-",persona.documento, "-",persona.pais, "-", persona.genero, "-", persona.status, "-")
            opcion1 = int(input("¿La persona posee un Status activo? SI(1) NO(0)"))
            
            if opcion1 == 1:
                opcion2 = int(input("/////¿Su estado actual es recuperado o fallecido? FALLECIDO(0) RECUPERADO(1)/////"))
                if opcion2 == 1:
                    persona.status = ("Recuperado")
                elif opcion2 == 0:
                    persona.status = ("Fallecido")
            elif opcion1 == 0:
                exit
                
    def mostrar(self):
        print("______Mostrar Casos______")

        for persona in ControlCovid19:
            print (persona.nombre, "-", persona.apellido, "-",persona.fecha_nacimiento, "-", persona.edad, "-",persona.documento, "-",persona.pais, "-", persona.genero, "-", persona.status, "-")

    def salir(self):
        print("¡Recuerda lavar tus manos! Hasta luego :) ")
            
control=Casos()
control.menu()








           
