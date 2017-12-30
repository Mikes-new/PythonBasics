#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('The duck can\'t bark')

    def fur(self):
        print('The duck has feathers')

class Dog:
    def bark(self):
        print('Woof!')

    def fur(self):
        print('The dog has brown and white fur')

    def walk(self):
        print('Walks like a dog')

    def quack(self):
        print('Dogs don\'t quack')

def main():
    donald = Duck()

    fido = Dog()

    for o in (donald, fido):
        o.quack()
        o.walk()
        o.bark()
        o.fur()

    in_the_forest(donald)

def in_the_forest(xyz):
    xyz.bark()
    xyz.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()


if __name__ == "__main__": main()
