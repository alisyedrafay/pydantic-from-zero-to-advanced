from pydantic import BaseModel
class Adress(BaseModel):
    state:str
    city:str
    pincode:int

class Pateint(BaseModel):
    name:str
    age:int
    adress:Adress

adress_dict = {"state":"sindh", "city":"karachi", "pincode":75800}
adress1 = Adress(**adress_dict)

pateint_infor = {"name":"syed rafay ali", "age":30, "adress":adress1}
pateint1 = Pateint(**pateint_infor)

print(pateint1.name)
print(pateint1.adress.pincode)

print(type(pateint1))

temp = pateint1.model_dump()
print(temp)

temp1 = pateint1.model_dump_json(include=["name", "age"])
print(temp1)
