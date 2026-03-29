import secrets
import string as s
from secrets import SystemRandom as Sr

#Gerador de senha segura
print("senha:","".join(Sr().choices(s.ascii_letters+s.digits+s.punctuation,k=64)))
print('----------------------------------------')
random = secrets.SystemRandom()
random.seed(1)
'''print(secrets.randbelow(100))
print(secrets.choice([100,5,44,87,99]))'''
num = random.randrange(10,21,2) #Aleatorio inteiro
print(num)
print('----------------------------------------')
num2 = random.randint(3,15) #Aleatorio inteiro
print(num2)
print('----------------------------------------')
num3_float = random.uniform(3.14,50.47)
print(num3_float)
print('----------------------------------------')
lista_original = ["yasmin","dante","josekson"]
random.shuffle(lista_original)
print(lista_original)
print('----------------------------------------')
lista_alterada = random.sample(lista_original,k=3)
print(lista_alterada)
print('----------------------------------------')
lista_alterada = random.choices(lista_original,k=2)
print(lista_alterada)
print('----------------------------------------')
lista_alterada = random.choice(lista_original)
print(lista_alterada)
print('----------------------------------------')
"import string as s;
from secrets import SystemRandom as Sr;

#Gerador de senha segura;
print("senha:","".join(Sr().choices(s.ascii_letters+s.digits+s.punctuation,k=64)))";
print('----------------------------------------');