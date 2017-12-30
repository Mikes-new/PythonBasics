#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Animal:
    def talk(self): print('I have something to say!')
    def walk(self): print('Hey! I''m walkin'' here!')
    def clothes(self): print('I have nice clothes.')

class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk() #this pulls from the base class so prints BOTH walk methods (the one under Animal and one line down.
        print('Walks like a duck.')

class Dog(Animal):
    def clothes(self):
        print('I have brown and white fur')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()
    fido = Dog()
    fido.walk()
    fido.clothes()

if __name__ == "__main__": main()
