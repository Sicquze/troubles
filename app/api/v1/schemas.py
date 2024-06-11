from pydantic import BaseModel


class UserDetails(BaseModel):
	first_name: str = "John"
	last_name: str = "Smith"
	age: int = 30


class UsersResponse(BaseModel):
	count: int = 0
	users: list[UserDetails] = []


