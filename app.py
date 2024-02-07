from MT5Manager import ManagerAPI, MTAccount, MTConGroup
import json
manager = ManagerAPI()
manager.Connect('5.101.146.202',5755,'Sv273bdv13')


# Conecta al servidor
if manager:
    print("Conexión exitosa al servidor:")
else:
    print("Error al conectar al servidor:")



for g in manager.GroupRequestArray():
    group: MTConGroup = g
    print(group.Group)
    