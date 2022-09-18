from underscore import Underscore


_ = Underscore() # sí, estamos configurando nuestra instancia a una variable que es un underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)

a=_.map([1,2,3], lambda x: x*2) # debería devolver [2,4,6]
b=_.find([1,2,3,4,5,6], lambda x: x>4) # debería devolver el primer valor que sea mayor que 4
c=_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
d=_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]
print(a,b,c,d)