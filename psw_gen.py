import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numb = "123456789"
symb = "{}[]()*;/,_-+@$%!?"

todos = lower + upper+numb+symb

length = 50
senha = "".join(random.sample(todos,length))
print(senha)
