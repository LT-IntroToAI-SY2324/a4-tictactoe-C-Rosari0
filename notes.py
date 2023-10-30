# object oriented programming

# (define-struct dog [fur_color name age favorite_food])




class Dog:
    def __init__(self,fc = "", a = 0, w = 0.0,n ="") -> None:
   
        self.fur_color = fc
        self.age = a
        self.weight = w
        self.name = n
 
    def __str__(self) -> str:
        s= "Dogs name is"+ self.name +"/n"
        s+= "and the age is" + self.age +"/n"
