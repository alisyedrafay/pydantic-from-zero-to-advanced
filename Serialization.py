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


temp = patient1.model_dump(include=["name", "gender"])

#model_dump() existing model ko dictionary mai convert krdega

temp1 = patient1.model_dump_json()
print(temp1)
print(type(temp1))



print(temp)
print(type(temp))


#how to export this model as python dictionary or json called serialization

