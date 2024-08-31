class Persona:
    def __init__(self, nombre, apellido, telefono, correo, direccion, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_telefono(self):
        return self.telefono

    def get_correo(self):
        return self.correo

    def get_direccion(self):
        return self.direccion

    def get_edad(self):
        return self.edad


class Empleado(Persona):
    def __init__(self, nombre, apellido, telefono, correo, direccion, edad, salario, jefe, experiencia):
        super().__init__(nombre, apellido, telefono, correo, direccion, edad)
        self.salario = salario
        self.jefe = jefe
        self.experiencia = experiencia
        self.cargo = self.calcular_cargo()

    def get_cargo(self):
        return self.cargo

    def get_salario(self):
        return self.salario

    def get_jefe(self):
        return self.jefe

    def get_experiencia(self):
        return self.experiencia

    def calcular_cargo(self):
        if self.salario >= 5000000 and self.experiencia >= 5 and 25 <= self.edad <= 45:
            return "senior"
        elif 900000 <= self.salario <= 1200000 and 1 <= self.experiencia <= 2 and 18 <= self.edad <= 22:
            return "junior"
        else:
            return "ingrese bien los valores establecidos"

    def imprimir(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Dirección: {self.direccion}")
        print(f"Correo: {self.correo}")
        print(f"Edad: {self.edad}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")
        print(f"Jefe inmediato: {self.jefe}")
        print(f"Años de experiencia: {self.experiencia}")
        


nombre1 = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
direccion = input("Ingrese la dirección: ")
telefono = input("Ingrese el teléfono: ")
edad = int(input("Ingrese la edad: "))
email = input("Ingrese el email: ")
salario = int(input("Ingrese el salario: "))
jefeinmediato = input("Ingrese el nombre del jefe inmediato: ")
añosexperiencia = int(input("Ingrese los años de experiencia: "))

empleado = Empleado(nombre1, apellido, telefono, email, direccion, edad, salario, jefeinmediato, añosexperiencia)
empleado.imprimir()
