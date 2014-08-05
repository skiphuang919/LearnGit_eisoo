#!/usr/share/env python
#encoding=utf-8

class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print '%s: %s'%(self.__name,self.__score)

    def get_level(self):
        if self.__score>=90:
            print 'A'
        elif self.__score>=70:
            print 'B'
        else:
            print 'work harder baby'

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'


def calc(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum

def func(a,b,c=0,*args,**kw):
    print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw


   


if __name__=='__main__':
     
    animal=Animal()
    animal.run()
    dog=Dog()
    dog.run()
    cat=Cat()
    cat.run()

    def run_twice(Animal):
        Animal.run()
        Animal.run()
    
        run_twice(animal)
        run_twice(dog)
        run_twice(cat)

        print dir(dog)
