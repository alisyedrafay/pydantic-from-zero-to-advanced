from pydantic import BaseModel

class Pateint(BaseModel):
    name:str
    age:int
def insert_pateint(pateint:Pateint):
    print(pateint.name)
    print(pateint.age)
pateint_info = {"name":"abc", "age":30}
pateint1 = Pateint(**pateint_info)
insert_pateint(pateint1)
