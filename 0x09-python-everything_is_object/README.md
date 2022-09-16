# 0x05. Python - Test-Driven Development

## Resources:books:
Read or watch:
* [9.10. Objects and values](https://intranet.hbtn.io/rltoken/QviwZH0soAr7Muv_aH3g0g)  
* [9.11. Aliasing](https://intranet.hbtn.io/rltoken/0UzI_Te4hnqxpvwWFn2KKA)  
* [Immutable vs mutable types](https://intranet.hbtn.io/rltoken/YKkVykUr-p4BogE28hym-A)
* [Mutation](https://intranet.hbtn.io/rltoken/if0lOY9EiG_pAQNoF7TSnA)  
* [9.12. Cloning lists](https://intranet.hbtn.io/rltoken/pTtyIhiRFDoTNBKAfG65Bg)  
* [Python tuples: immutable but potentially changing](https://intranet.hbtn.io/rltoken/JTKb3-UE9d-TFHYcatbNSA)
  
## Learning Objectives:bulb:
What you should learn from this project:

* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions  

## Tasks:notebook:  

* `0-answer.txt`: what function would you use to print the type of an object? 
* `1-answer.txt`: how do you get a variable's identifier (which is the memory address in the CPython implementation)? 
* `2-answer.txt`: in the following code, do a and b point to the same object?
    > a = 89  
    > b = 100  
* `3-answer.txt`: in the following code, do a and b point to the same object?
    > a = 89  
    > b = 89  
* `4-answer.txt`: in the following code, do a and b point to the same object?
    > a = 89  
    > b = a  
* `5-answer.txt`: in the following code, do a and b point to the same object?
    > a = 89
    > b = a + 1
* `6-answer.txt`: what do these 3 lines print?
    > s1 = "Best School"
    > s2 = s1
    > print(s1 == s2)
* `7-answer.txt`: what do these 3 lines print?
    > s1 = "Best"
    > s2 = s1
    > print(s1 is s2)
* `8-answer.txt`: what do these 3 lines print?
    > s1 = "Best School"
    > s2 = "Best School"
    > print(s1 == s2)
* `9-answer.txt`: what do these 3 lines print?
    > s1 = "Best School"
    > s2 = "Best School"
    > print(s1 is s2)
* `10-answer.txt`: what do these 3 lines print?
    > l1 = [1, 2, 3]
    > l2 = [1, 2, 3]
    > print(l1 == l2)
* `11-answer.txt`: what do these 3 lines print?
    > l1 = [1, 2, 3]
    > l2 = [1, 2, 3]
    > print(l1 is l2)
* `12-answer.txt`: what do these 3 lines print?
    > l1 = [1, 2, 3]
    > l2 = l1
    > print(l1 == l2)
* `13-answer.txt`: what do these 3 lines print?
    > l1 = [1, 2, 3]
    > l2 = l1
    > print(l1 is l2)
* `14-answer.txt`: what does this script print?
    > l1 = [1, 2, 3]
    > l2 = l1
    > l1.append(4)
    > print(l2)
* `15-answer.txt`: what does this script print?
    > l1 = [1, 2, 3]
    > l2 = l1
    > l1 = l1 + [4]
    > print(l2)
* `16-answer.txt`: what does this script print?
    > def increment(n):
    >   n += 1
    >
    > a = 1
    > incremental(a)
    > print(a)
* `17-answer.txt`: what does this script print?
    > def increment(n):
    >   n.append(4)
    >
    > l = [1, 2, 3]
    > incremental(l)
    > print(l)
* `18-answer.txt`: what does this script print?
    > def assign_value(n, v)
    >   n = v
    >
    > l1 = [1, 2, 3]
    > l2 = [4, 5, 6]
    > assign_value(l1, l2)
    > print(l1)
* `19-copy_list.py`: write a function def copy_list(l): that returns a copy of a list  
* `20-answer.txt`: is 'a' a tuple? answer with yes or no.
    > a = ()
* `21-answer.txt`: is 'a' a tuple? answer with yes or no.
    > a = (1, 2)
* `22-answer.txt`: is 'a' a tuple? answer with yes or no.
    > a = (1)
* `23-answer.txt`: is 'a' a tuple? answer with yes or no.
    > a = (1, )
* `24-answer.txt`: what does this script print?
    > a = (1)
    > b = (1)
    > a is b
* `25-answer.txt`: what does this script print?
    > a = (1, 2)
    > b = (1, 2)
    > a is b
* `26-answer.txt`: what does this script print?
    > a = ()
    > b = ()
    > a is b
* `27-answer.txt`: will the last line of this script print 139926795932424? answer with yes or no
    > id(a)
        > 139926795932424
    > a
        > [1, 2, 3, 4]
    > a = a + [5]
        > id(a)
* `28-answer.txt`: will the last line of this script print 139926795932424? answer with yes or no
    > a
        > [1, 2, 3, 4]
    > id(a)
        > 139926795932424
    > a += [4]
        > id(a)


## Author
* **Baylee Duncan** - [b-duncs](https://github.com/b-duncs)
