from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

##Adress kai liye 1 separate pydantic model bnaeingein or usko yha as a field use kareingein

class pateint(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

adress_dict = {"city":"karachi", "state":"haryana", "pin":"75800"}
adress1 = Address(**adress_dict)

patient_dict = {"name":"abc", "gender":"male", "age":"25", "address":adress1}
patient1  = pateint(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.pin)
