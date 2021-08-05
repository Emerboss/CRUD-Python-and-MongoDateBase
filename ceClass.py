class CeClass:
    #actualizar
    def __init__(self, Id, Nombre, Departamento, Municipio):
       
        self.Id=int(Id)
        self.Nombre=Nombre
        self.Departamento=Departamento
        self.Municipio=Municipio
    def toCollection(self):
        return{
            "Id": self.Id,
            "Nombre": self.Nombre,
            "Departamento": self.Departamento,
            "Municipio": self.Municipio
        }
