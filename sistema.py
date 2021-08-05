import pymongo
from ceClass import CeClass

def menu():
    print("Sismte de Registro de Centros Escolares")
    while(True):
        print("""
        1) Registrar un nuevo Centro Escolar
        2) Visualizar los Centros Escolares registrados
        3) Actualizar un registro de un Centro Escolar
        4) Eliminar registro de un Centro Escolar
        5) Salir del sistema
        """)
        opcion=input()
        if opcion=="1":
            Id = int(input("Digite el ID del centro Escolar (unicamente números): ")) #Capturamos el ID
            Nombre = input(" Nombre de identificación del CE: ") 
            Departamento = input("Ingrese el Deparamento donde se encuentra el CE:") #Capturamos el Dirección
            Municipio = input("Ingrese el Municipio donde se encuentra el CE:")
            Ce=CeClass(Id,Nombre,Departamento,Municipio)
            registrosInsertado=insertar_Ce(Ce)
            print("Centro Escolar Ingresado con éxito: ",registrosInsertado )

        elif opcion=="2":
            visualizar_ce()
        elif opcion=="3":
            Id = int(input("Digite el ID del centro Escolar a actualizar: ")) #Capturamos el ID
            Nombre = input("Nuevo nombre de identificación del CE: ") 
            Departamento = input("Ingrese el Deparamento donde se encuentra el CE:") #Capturamos el Dirección
            Municipio = input("Ingrese el Municipio donde se encuentra el CE:")
            registroActualizado=actualizar_ce(Id,Nombre,Departamento,Municipio)
            print("Registro Actualizado: ",registroActualizado)

        elif opcion=="4":
            Id = int(input("Digite el ID del centro Escolar a eliminar: ")) 
            registroEliminado=borrar_ce(Id)
        elif opcion=="5":
            break
        else:
            print("Opcion no valida, vuelve a intentar")
#Conexión con Mongo
def get_db():
    try:
        client = pymongo.MongoClient("mongodb+srv://emerboss2:certi123@cluster0.nwofk.mongodb.net/test")
        db = client["Evaluacion01"] #BD
        colec = db["Ce"] #Colección
    except ConnectionError:
        print("Error de Conexión")
    return db
#Visualizar Opcion 1
def visualizar_ce():
    db=get_db()
    escuelas=db.Ce.find().limit(10)
    print("{:30}{:20} {:30} {:20}".format("Id","Nombre","Departamento","Municipio"))
    for escuela in escuelas:
        print("{:<30} {:<20} {:<30} {:<20}".format(escuela["Id"], escuela["Nombre"], 
        escuela["Departamento"],escuela["Municipio"]))
# Función para Insertar
def insertar_Ce(ce):
    db=get_db()
    resultado= db.Ce.insert_one(ce.toCollection())
    return resultado.inserted_id
# Función para actualizar
def actualizar_ce(Id,Nombre,Departamento,Municipio):
        db=get_db()
        resultado=db.Ce.update_one(
            {
           "Id": int(Id)
        },
        {
            "$set":{"Nombre": Nombre, "Departamento": Departamento, "Municipio": Municipio
        }}

        )
        return resultado.modified_count
        # Función para borrar
def borrar_ce(Id):
    db=get_db()
    resultado=db.Ce.delete_one({"Id":Id})
    return resultado.deleted_count
     
## Main
menu()