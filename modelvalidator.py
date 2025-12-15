from pydantic import BaseModel, EmailStr, AnyUrl,model_validator
from typing import List, Dict
class Pateint(BaseModel):
    #ideal schema define here
   name:str 
   email:EmailStr
   linkedin_url:AnyUrl
   age:int 
   
   #constraint
   weight:float 
   married:bool
   allergies:List[str]
   contact_details:Dict[str, str]

   @model_validator(mode="after")
   def validate_emergency_contact(cls, model):
      if model.age >60 and "emergency" not in model.contact_details:
         raise ValueError("patients older than 60 must have an emergency contact")
      return model
   




def insert_patient( pateint:Pateint):
   print(pateint.name)
   print(pateint.age)
   print(pateint.weight)
   print(pateint.married)
   print(pateint.allergies)
   print(pateint.contact_details)
   print(pateint.email)
   print(pateint.linkedin_url)



   print("inserted")


pateint_info = {"name":"nitish", "age":65,"email":"abc@gmail.com",  "weight":70, "married":True, "allergies":["poolen", "dust"], "contact_details":{ "phone":"302342312", "emergency":"1234444"}, "linkedin_url":"http://linkedin.com/1322"}

patient1 = Pateint(**pateint_info)

insert_patient(patient1)

