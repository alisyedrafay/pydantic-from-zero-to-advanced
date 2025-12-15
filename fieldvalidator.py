from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Pateint(BaseModel):
    #ideal schema define here
   name:str 
   email:EmailStr
   linkedin_url:AnyUrl
   age:int 
   
   #constraint
   weight:float 
   married:Optional[bool] = None
   allergies:Optional[ List[str]] = None
   contact_details:Dict[str, str]

#yha pr ye field validator btaega kai ye kis field pr validate hoga
   @field_validator("email" , mode="after")
   @classmethod
   def email_validator(cls, value):
      value_domain = ["meezan.com", "hbl.com"]
      #@gmail.com 
      domain_name = value.split("@")[-1]
      if domain_name not in value_domain:
         raise ValueError("not a valid domain")
      return value
   @field_validator("name")
   @classmethod
   def transform_name(cls, value):
      return value.upper()
   
   @field_validator("age", mode="after")
   @classmethod
   def validate_age(cls, value):
      if 0<value<100:
         return value
      else:
         raise ValueError("age should be between 0 and 100")
    
   
       
   




def insert_patient( pateint:Pateint):
   print(pateint.name)
   print(pateint.age)
   print(pateint.weight)
   print(pateint.married)
   print(pateint.allergies)
   print(pateint.contact_details)
   print(pateint.email)
   print("inserted")



pateint_info = {"name":"nitish", "age":30,"email":"abc@meezan.com",  "weight":70, "married":True, "allergies":["poolen", "dust"], "contact_details":{"email":"nitish@gmail.com", "phone":"302342312"}, "linkedin_url":"http://linkedin.com/1322"}

patient1 = Pateint(**pateint_info)

insert_patient(patient1)
