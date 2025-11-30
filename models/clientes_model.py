from database import run_query, run_actions
from datetime import date

class ClientesModel:
    def __init__(self, id="", cliente="", tel="", proyecto="", fecha=date.today()):
        self.id = id
        self.cliente = cliente
        self.tel = tel
        self.proyecto = proyecto
        self.fecha = fecha  
    
    @staticmethod
    def get_all():
        return [ClientesModel(**cliente) for cliente in run_query("SELECT * FROM clientes")]
    
    @staticmethod
    def getClienteById(id):
        row = run_query("SELECT * FROM clientes WHERE id = %s", (id,))
        return ClientesModel(**row[0]) if row else None
    
    @staticmethod
    def create(cliente, tel, proyecto, fecha):
        run_actions("INSERT INTO clientes (cliente, tel, proyecto, fecha) VALUES (%s, %s, %s, %s)", (cliente, tel, proyecto, fecha))
    
    @staticmethod
    def update(id, cliente, tel, proyecto, fecha):
        pass
    
    @staticmethod
    def delete(id):
        pass