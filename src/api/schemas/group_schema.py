from pydantic import BaseModel
        
class GroupBaseSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True

class GroupCreateRequest(GroupBaseSchema):
    pass

class GroupResponse(GroupBaseSchema):
    id: int