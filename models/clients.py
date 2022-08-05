from models.basemodel import BaseModel


class ClientModel(BaseModel):
    __tablename__ = "clients"
    __collection__ = "clients"
    fname = BaseModel.dbpsql.Column(BaseModel.dbpsql.String(40))
    lname = BaseModel.dbpsql.Column(BaseModel.dbpsql.String(40))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Bonjour {self.fname}"

    def add_client(self):
        self.dbpsql.session.add(self)
        self.dbpsql.session.commit()
        self.dbmongo[self.__collection__].insert_one({'firstname': self.fname, 'lastname': self.lname})
