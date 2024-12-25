from typing import Optional, Union, Annotated

# def process_items(items: list[str]):
# 	for item in items:
# 		print(item)



def process_items(prices: dict[str,float]):
	for item_name, item_price in prices.items():
		print(item_name)
		print(item_price)


# names = {'bike': 7700.09,'tractor': 888888.0998}
# print(process_items(names))

print('.......................')

def say_hi(name: str | None = None):
# 	if name is not None:
# 		print(f'Hey, {name}')
# 	else:
# 		print('Hello world')
	return f'Hy, {name}'



# print(say_hi())

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):

	id: int 
	name: str = "John Doe"
	sighnup_ts: datetime | None = None
	friends: list[int] = []


external_data = {
	
	'id': '123',
	'signup_ts': '2017-06-01 10:22',
	'friends': [1, '2', b'3'],

}

user = User(**external_data)

# print(user)



def say_hello(name: Annotated[str, 'this is just metadata']) -> str:
	return f'Hello, {name}'

