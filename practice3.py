from pydantic import BaseModel, Field, EmailStr, field_validator,model_validator, computed_field
from typing import Dict, Annotated, List

class Pateint(BaseModel):
    name:str = Annotated[str, Field(max_length=50, description="name of the pateint is ", examples=["john", "abc"])]
    age:int = Field(gt=0, lt=120)
    salary:float = Field(gt=0, lt=120)
    email:EmailStr
    contact_details:Dict[str, str]
    allergies:List[str]
    weight:float
    height:float


    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator("age")
    @classmethod
    def tranform_age(cls, age):
        if 0<age<100:
            return age
        else:
            raise ValueError("invalid valid")
    
    @model_validator(mode="after")
    def validate_pateint(cls, model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("pateint is greater then 60 and there is no emergency details")
        return model
    @computed_field
    @property
    def computed_bmi(self)->float:
        bmi = round((self.weight/self.height**2), 2)
        return bmi


    




def pateint_data(pateint:Pateint):
    print(pateint.name)
    print(pateint.age)
    print(pateint.salary)
    print(pateint.email)
    print(pateint.allergies)
    print("Weight",pateint.weight)
    print("Height",pateint.height)
    print("BMI", pateint.computed_bmi)

    print("data is inserted")
pateint_infor = {"name":"abc", "age":"30", "salary":2.3333, "email":"abc@gmail.com","contact_details":{"phone":"22222222" , "emergency":"5614616"}, "allergies":["poolen", "Dust"], "weight":12.3, "height":13.36}
pateint1 = Pateint(**pateint_infor)
pateint_data(pateint1)


