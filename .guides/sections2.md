---
title: Introduction
files:
  - action: close
    path: "#tabs"
layout: 2-panels-tree

---
Learning to program takes time and lots of practice but more importantly should be fun.

On the training day we will be covering sections of this booklet but it would be unrealistic to expect to learn everything over a one day period.

After the training day go back over this booklet. If you are unsure I would recommend starting from the beginning and working through all the tasks. It is one thing to read through the exercises but this is no substitute for doing them yourself. Not only does this help embed the concepts but it also helps you get a feel for the sort of errors your students may come across. Each section contains three tasks a, b and c, each of increasing difficulty.

Once you are comfortable with the material in this booklet it is hoped you will have a strong enough grounding to develop your programming skills in the direction you want.

Remember your trainers will be available to contact after the day itself so please do not hesitate to email them if any questions arise.


> ### Tip
> If you are finding yourself stuck on a programming task it often pays to go and do something completely different for an hour. Watch EastEnders, mow the law, walk the dog anything to take your mind off the problem. It’s amazing how many silly mistakes you will spot when reviewing your code with a fresh pair of eyes.

## Python

he OCR GCSE in Computing can be carried out using any (imperative) language. The fact this course is in Python isn’t to say it is any better than the many alternatives out there but it is certainly a good language to teach with.

Python was designed specifically to be easy to understand and quick to build programs. It is used in real world companies such as Google where its creator Guido Van Rossum worked for a while.
There are currently two versions of Python in use Python 2 and Python 3. Whilst they are both very similar there are important differences. In this course we will be looking at **Python 3**.

---
title: Output to the screen
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 1-screen/start.py
    panel: 0
layout: 2-panels-tree
step: 1-screen

---

---
title: Storing data in variables
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 2-variables/complete-me.py
    panel: 0
    index: 0
    type: file
    arg: 2-variables/complete-me.py
  - action: open
    path: 2-variables/cat-mat.py
    panel: 0
    index: 1
    type: file
    arg: 2-variables/cat-mat.py
  - action: open
    path: 2-variables/start.py
    panel: 0
    index: 2
    type: file
    arg: 2-variables/start.py
layout: ""
step: 2-variables

---
We use variables in our programs to store data. Each variable has a name and stores data of a certain type (string, integer, real etc). In Python we do now have to explicitly state the data type being stored it will work this out for itself when the variable is first used.

In this section we will just use string variables. String is just the programming term for text (i.e. letters, numbers and symbols).

Variable names can contain letters and numbers but should always start with a letter. 

We assign a value to a variable using `=`

## Task A

Copy and run the following program:

```python
name = 'Bob'
print('Hello ' + name)
```

## Task B

Look at the file [complete-me.py](open_file "2-variables/complete-me.py").

Complete the program so it uses the variable language to print

```bash
I am learning to program in Python
```

We can change the value of a variable at any point. The code:

```python
name = 'Bob'
name = 'Liz'
print('Hello ' + name)
```

Will print `Hello Liz` (as the variable name has been overwritten with the value Liz).

We can also change the contents of a variable referring to itself:

```python
name = 'Bob'
name = name + 'by'
print('Hello ' + name)
```

This will print `Hello Bobby`. Whereas

```python
name = 'Bob'
name = name + name
print('Hello ' + name)
```

will print `Hello BobBob`.

We can add spaces just like any other letter:

```python
name = 'Bob'
name = name + ' ' + name
print('Hello ' + name)
```

Will print `Hello Bob Bob`

## Task C
Complete the program in [cat-mat.py](open_file "2-variables/cat-mat.py"), so it uses the variables to print out `the cat sat on the mat`. 

Remember, you will need to add spaces.



---
title: Inputting Data
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 3-input/start.py
    panel: 0
layout: ""
step: 3-input

---
We can now look at starting to make our programs interactive. We are going to take in input from the user using the input command.

```python
name=input('What is your name?')
print('Hello '+name)
```

## Task 3a
Write a program that asks for the town you live in and then replies I love visiting [town name]
e.g.

```bash
Where do you live?  London
I love visiting London
```

## Task 3b
Write a program that asks for your first name then asks for your last name and finally greets you with your full name.

e.g.
```bash
What is your first name? John
What is your last name? Smith
Hello John Smith
```

## Task 3c
Write a program that asks for your name then prints it out 5 times

e.g.
```bash
What is your name? Trevor
Trevor Trevor Trevor Trevor Trevor
```
---
title: Calculations
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 4-calculations/start.py
    panel: 0
layout: ""
step: 4-calculations

---
We can carry out calculations in Python. The arithmetic operators we use to do this are: 

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division

## Task A
Copy and run the following program

```python
print(1+6)
print(7-5)
print(3*9)
print(7/2)
```

## Task B
Try changing the calculations to new ones. We can put the results of calculations into variables. These variables will not be string but integer (whole numbers) or float (decimal).

```python
a=10
b=2
c=a/b
print(c)
```

## Task C
Complete this program so it uses addition on the two variables to print the number 15

```python
a=7
b=8
c= [REMAINDER OF PROGRAM HERE]
```
---
title: Data Types
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 5-data-types/start.py
    panel: 0
layout: ""
step: 5-data-types

---
Every variable has a given data type. The most common data types are:

- **String** - Text made up of numbers, letters and characters.
- **Integer** - Whole numbers. (e.g. 1, 78, 0 and -54)
- **Float** - Decimal numbers (e.g. 3.5683, 98.74634, -6.3). Float comes under the umbrella of what we often refer to as Real numbers.
- **Boolean** - True or False

In some languages we have to tell the computer what data type a variable is going to be. Python, on the other hand, is able to decide the data type of the variable according to what value it is first given (or to use the correct term what it is initialised with). This can cause problems when we try to do something with the wrong data type.

## Task A
Copy and run the following program.

```python
a=input('Enter number 1:')
b=input('Enter number 2:')
c=a+b
print('Adding your numbers together gives:'+c)
```

If you enter the numbers `5` and `4` it will output `54`. This is because Python treats anything received through the input function as a string. We need to tell Python we want to convert this string to an integer before putting it into the variable. This is done using type casting.

To cast data to an integer we use int()

Try the program now:

```python
a = int(input('Enter number 1:'))
b = int(input('Enter number 2:'))
c=a+b
print('Adding your numbers together gives:'+c)
```

This time you will get an error in line 4: `TypeError: Can't convert 'int' object to str implicitly`.

This is because a and b are now integers as they take in strings converted to integers. This means c is now an integer (as it takes in the sum of to integers which in itself is an integer). 

The problem arises when we then try and add c to a sentence: ‘Adding your numbers together gives:’ We can concatenate strings with strings but in Python we can’t concatenate strings with integers.

The solution is to cast c back to a string when we use it using str().

```python
a = int(input('Enter number 1:'))
b = int(input('Enter number 2:'))
c=a+b
print('Adding your numbers together gives:'+str(c))
```

Now the program should work.


## Task B
Write a program that asks for a length and width and outputs the area of a rectangle.

E.g.

```bash
Please enter width:9
Please enter height:5
The area is: 45
```

## Task C
The formula for the volume of a cylinder is `PI*r*r*h` where r is the radius of the upper surface and h is the height.

Assume that the user may enter the radius and height as real numbers. To cast these you will need to use float() Write a program that asks you for the radius and height of a cylinder then calculates the volume and area.

*HNT: use `math.pi` as a special variable that gives PI. In order to use this, you will need to include `import math` at the top of your code.*


---
title: Selection with If
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 6-if/start.py
    panel: 0
layout: ""
step: 6-if

---
Sometimes we only want a program to execute code under certain circumstances. We call this selection. The most commonly used way of doing this is using if. Here we say if a condition is true execute some code.

First we need to make sure we are happy what a condition is. A boolean condition is one that can have only two values true or false.

The boolean comparison operators are as follows:


| Operator |Meaning |
|-|-|
|== |Equal to |
| != | Not equal to |
|< |Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | ￼Greater than or equal to |

So:

```python
letter = 'a'
if letter=='a':
    print('This prints if letter is a')
```

We can add as many statements we want inside the if. Each should be indented.

```python
letter = 'a'
if letter=='a':
     print('This prints if letter is a')
     print('This prints as well')
```

When we want to stop the if we remove the indentation.

```python
if letter=='a':
     print('This prints if letter is a')
     print('This prints as well')
print('This prints out whatever the letter is')
```
We can tell the computer to do something different when the condition isn’t true using the else keyword.

```python
if letter=='a':
     print('This prints if letter is a')
     print('This prints as well')
else:
     print('This prints if the letter is not an a')
     print('As does this line')
print('This prints out whatever the letter is')

if letter=='a':
     print('This prints if letter is a')
     print('This prints as well')
elif letter=='b':
     print('This prints if the letter is b')
else:
     print('This prints if the letter is neither a nor b')
print('This prints out whatever the letter is')
```

## A Note on Indentation
When you start a new line after a colon your code (if writing it inside IDLE) you should find your code indented). Lines will keep indenting until you press backspace. Python knows that anything indented is inside the structure with the colon - in this case the if. Indenting is considered good practice in all programming languages as it makes code easier to read but in Python it is even more important as it affects the code’s meaning.

For more complex conditions we can use and, or and not. When you are confident conditions with if should try to find out about these to make your code more efficient.

```python
x=int(input('Enter a number between 1 and 100: '))
if x>=1 and x<=100:
    print('You have entered a valid number')
else:
print('Your number is not valid')
```

A common mistake would be to write the if line as if x>=1 and <=100 missing out the second x. This is wrong and will generate an error.

## Task A
Copy and run the code below.

```python
city=input('What is the capital of France?')
if city== 'Paris':
     print('Well done')
elif city=='Lyon':
     print('Right country, wrong city')
elif city=='F':
     print('Terrible joke and wrong answer.')
else:
     print('Sorry wrong answer')
```

Change the question so it asks for the capital of England and gives appropriate answers to different entries.

## Task B
Below is a program that asks for three numbers and outputs SNAP if they all match. Use your knowledge of the and, or and not operators to make the program more efficient.

```python
one=int(input('Please enter number 1: '))
two=int(input('Please enter number 2: '))
three=int(input('Please enter number 3: '))
if(one==two):
    if(two==three):
        print('SNAP!')
    else:
        print('They do not all match')
else:
    print('They do not all match')
```

## Task C
The grade boundaries for a test are: 

```bash
U below 40
D – 40
C – 50
B – 60
A – 70
```

Write a program that asks for a mark and then says what grade it is worth.


---
title: Code readability
files:
  - action: close
    path: "#tabs"
layout: ""
step: 7-readability

---
In the last section we looked at indentation as a way of making your code easier to read. In the development section of A453 one of the descriptors for the top mark band is:

*“The code will be well organised with meaningful variable names and detailed annotation indicating the function of each section.”*

Annotation in your code would usually be in the form of commenting. A comment is purely for the person reading it. The computer completely ignores comments but they make your program much more understandable to anyone trying to follow your code. The key to good commenting is to assume the reader is a competent programmer but doesn’t know what your program is meant to do. There is a fine art to being able to strike the right balance between under and over commenting.

Commenting in Python is done using the hash # character. A comment can be put at the end of a line or on a line by itself.

```python
#Question to ask user the capital of France
print('What is the capital of France?')
if city== 'Paris':
     print('Well done')
elif city=='Lyon': #Handle common wrong answer
     print('Right country, wrong city')
elif city=='F':
     print('Terrible joke and wrong answer.')
else: #any other wrong answer.
     print('Sorry wrong answer')
```

## Variable Names
The final thing you should consider are your variable names. a, b and c are fine in trivial 4 line programs but as your programs get bigger this becomes quickly confusing. 

Meaningful variable names help make your code much more readable.


---
title: Loops
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 8-iteration1/start.py
    panel: 0
layout: ""
step: 8-iteration1

---
One of the things that makes computers so useful is the speed at which they do things. This means we can get them to do something over and over again. We call this iteration or looping. We will look at two types of loop, the first of which is a count controlled loop. This is when a program carries out a set of instructions a certain number of times. To do a count controlled loop we use for. Note how anything inside the loop is indented.

```python
for i in range(0,5):
     print('looping')
```

Will output

```bash
looping
looping
looping
looping
looping
```

In the loop for `i in range(x,y)` x is the starting value of i and y is the one above what it will get to. So above it runs with i equal to 0,1,2,3 and 4.

Traditionally loops tend to use the variables i,j and k and you may see lots of code that conforms to this convention. There is, however, no reason why you can’t use any other variable name especially if it makes your code more readable.

## Task A
Write a program that outputs the word computing 15 times. We can use the variable i inside the loop.

```python
for i in range(0,5):
    print(str(i)+' looping')
```

Produces the followin output

```bash
0 looping
1 looping
2 looping
3 looping
4 looping
```

## Task B
Write a program that takes in a letter and number then, using a for loop, prints out that letter that many times.

E.g.
```bash
Please enter a letter: T
Please enter a number: 6
TTTTTT
```

## Task C
Write a program that asks for a number then outputs it’s 10 times table.
E.g.

```bash
Please enter a number: 7
1 times 7 is 7
2 times 7 is 14
3 times 7 is 21
4 times 7 is 28
5 times 7 is 35
6 times 7 is 42
7 times 7 is 49
8 times 7 is 56
9 times 7 is 63
10 times 7 is 70
```


---
title: Conditional Loops
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 9-iteration2/start.py
    panel: 0
layout: ""
step: 9-iteration2

---
We have looked at count controlled loops, we will now look at condition controlled loops. These are loops which continue to repeat code while a condition is true.

These are exactly the same type of conditions we looked at when using `if`

```python
x=0
while x<5:
     print('looping')
```

If we run the above code (don’t) you will find it goes on forever printing looping. that is because x remains 0 and so is always less than 5. Let’s fix it:

```python
x=0
while x<5:
     print('looping')
     x=x+1
```
Now try running the above code.

## Task A
Write a program that asks for a password and keeps asking until the correct password, `apple` is entered and then says `Accepted`

## Task B
The sequence 1,4,9,16,25 is made up of square numbers (i.e.1=1^2, 4 = 2^2, 9=3^2 etc.). Write a program that writes out all the square numbers under 5000.

## Task C
The following code will create an integer x that is a random number between 1 and 100.

```python
import random
x=random.randint(1,100)
```

The line import random has to be put at the very top of the program you can use random.randint(1,100) wherever you want after that.

Write a program in which the computer thinks of a number between 1 and 100 (i.e. picks number at random). It should then ask the user to guess what number it is thinking of. It should then say whether the number the computer is thinking of is higher or lower than the one guessed. If the user guess correctly it should say well done and say how many guesses it took them if not it asks them to guess again.

```bash
I am thinking of a number between 1-100.  Can you guess what it is? 50
No, the number I am thinking of is higher than 50.  Can you guess what it is? 80
No, the number I am thinking of is lower than 80.  Can you guess what it is? 60
No, the number I am thinking of is higher than 60.  Can you guess what it is? 64
Well done! The answer was 64 and you found it in 4 guesses.

```


---
title: Procedures and Functions
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 10-subs-functions/start.py
    panel: 0
layout: ""
step: 10-subs-functions

---
It is possible to write a whole program as one big block but where possible we want to break it down into subroutines. There are several advantages to this:

- The program becomes easier to read.
- The program becomes easier to test. If you have tested a subroutine you don’t have to worry about it when you subsequently use it.
- Subroutines can often be reused meaning code does not need to be rewritten.

We will start off with a function that prints out This is my subroutine 3 times. Note how the subroutines come before the main program.

```python
#Subroutine that prints out sentence 3 times
def myFirstSubroutine():
    for i in range(1,3):
        print('This is a subroutine')
        
#Main Program
print('Start of main program')
myFirstSubroutine()
print('End of program')
```

This would output:

```bash
Start of main program
This is a subroutine
This is a subroutine
This is a subroutine
End of program
```

We can use parameters to make subroutines even more useful. The parameters in the subroutine below are text and times.

```python
#Subroutine that prints out sentence 3 times
def myFirstSubroutine(text, times):
    for i in range(0,times):
        print(text)
        
#Main Program
print('Start of main program')
myFirstSubroutine('Sample text',5)
print('End of program')
```
The subroutines we have looked at so far are procedures. The other type of subroutine we use is a function. A function is a subroutine that returns a value. That means we can use it within other statements. We use the return keyword to send the value back to the main program.

```python
#Function to double a number
def double(number):
    twicenum=2*number
    return twicenum
#Main Program
a=6
print('Double a is')
print(double(6))
```

## Task A
Write a function called `circleArea` that takes in a float representing the radius and returns the area of a circle.

(Area of a circle is PI*r^2￼ ￼ where r is the radius)

Call your function from this main program:
```python
print(circleArea(1.0))
print(circleArea(2.0))
print(circleArea(3.0))
```

## Task B
Write a function called journeyCost. It should take in the number of miles of the journey, price per litre of fuel in pence and how many miles it a car travels to the litre. It should return the journey price in pounds.

i.e.

```python
journeyCost(miles, pricePerLitre, milesPerLitre)
so
print(journeyCost(50, 140, 7))
```

Would output
```bash
9.99
```

## Task C
Write a function called rectangle that takes in a width and length. This should print out a rectangle of Xs using those dimensions. (NB as the character X is higher than it is wide the dimensions will not be perfectly to scale.)
e.g.

The program

```python
rectangle(5,3)
```

will output

```bash
XXXXX
XXXXX
XXXXX
```
and

```python
rectangle(3,2)
rectangle(6,3)
```

will output

```bash
XXX
XXX
XXXXXX
XXXXXX
XXXXXX
```

---
title: Lists
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 11-lists/start.py
    panel: 0
layout: ""
step: 11-lists

---
If we think of a variable as a box we can think of a list as a collection of boxes containing data. Each “box” has an address starting at 0.

The following code produces a list called names.

```python
names=['Alf','Betsy','Charlie','David']
```
names:

| Alf | Betsy | Charlie | David |
|-|-|-|-
| 0 | 1 | 2 | 3 |

We can then access any element of the list by giving its index in square brackets.

```python
names=['Alf','Betsy','Charlie','David']
print(names[2])
```

Will print `Charlie`

We can also alter the contents of the list by referring to the elements by their index.

```python
names=['Alf','Betsy','Charlie','David']
names[2]='Bob'
print(names[2])
```

Changes the list to:

| Alf | Betsy | Bob | David |
|-|-|-|-
| 0 | 1 | 2 | 3 |


So it will print `Bob`

If we start off with our list as empty we can create it with just two empty square brackets. `names=[]`

To add entries to the list we then call the append function.

```python
names=[]
names.append('Betsy')
names.append('Anita')
names.append('Murshed')
names.append('Hamish')
print(names)
```

Will output `['Betsy', 'Anita', 'Murshed', 'Hamish']`

To remove an item from the list we use the pop method if we want to remove by index

```python
names=[]
names.append('Betsy')
names.append('Anita')
names.append('Murshed')
names.append('Hamish')
names.pop(1)
print(names
```

Will output `['Betsy', 'Murshed', 'Hamish']`

If we know the item we want to remove we can use the remove function which deletes the first instance of it.

```python
names=[]
names.append('Betsy')
names.append('Anita')
names.append('Murshed')
names.append('Hamish')
names.remove('Anita')
print(names)
```

Will also output `['Betsy', 'Murshed', 'Hamish']`

To get the number of items in a list we use len. 

```python
x=len(names)
```

Makes `x` the number of names in the list.

We can cycle through a list with a for loop.

```python
names=['Anita','Betsy', 'Murshed', 'Hamish']
for i in names:
  print(i)
```

to print

```bash
Anita
Betsy
Murshed
Hamish
```

## Arrays vs Lists
Most languages use arrays rather than lists so you may come across the term array being used in a similar context. (Python does have arrays available but lists are much more commonly used.)

The two main differences between the two are:

- Lists can hold different sorts of data whereas an array (usually, depending on the language) only holds one data type.
- Lists change size as new items are added where as in most languages arrays have their size declared at the start.

## Task A
Write a program that keeps asking for names until the word `END` is entered at which point it prints out the list of names.

```bash
Please enter a name: Alfred
Please enter a name: Bradley
Please enter a name: Connor
Please enter a name: David
Please enter a name: Emily
Please enter a name: END
You have entered 5 names.
['Alfred', 'Bradley', 'Connor', 'David', 'Emily'] 
```

Keep your code safe for this answer you will need it in Task B.


## Task B
Write a program that asks the user to enter 5 names which it stores in a list. Next, get it to pick one of these names at random and declare that person as the winner. 

*HINT: you will need to generate random numbers as in Task 9c*

E.g.

```bash
Please enter name 1:
Sarah
Please enter name 2:
Nathan
Please enter name 3:
Aniela
Please enter name 4:
Safiya
Please enter name 5:
Bob
Well Done Bob you are the winner!
```

## Task C
Adapt your program from 11a so it takes in a list of names but prints the out in the opposite order to which they were entered.

```bash
Please enter a name: Alfred
Please enter a name: Bradley
Please enter a name: Connor
Please enter a name: David
Please enter a name: Emily
Please enter a name: END
You have entered 5 names. These are, in reverse order:
Emily
David
Connor
Bradley
Alfred
```

---
title: String handling
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 12-strings/start.py
    panel: 0
layout: ""
step: 12-strings

---
A *string* is a set of characters strung together, so `a`, `hello`, `hello world`, 'ABC&^%def' or even `jkh askjha skja s`.

Often we want to perform operations on strings. This may involve cycling through letters in the string. This is particularly easy in Python as we can do it in a for loop.

## Task A
Copy and run the following program.

```python
sentence = 'The cat sat on the mat.'
for letter in sentence:
    print(letter)
```

Sometimes we might just want part of the string. We can do this by treating the string as a list of characters.

|S|a|n|d|w|i|c|h|
|-|-|-|-|-|-|-|-|
|0|1|2|3|4|5|6|7|

We can then refer to letters by their index (remembering that a list starts at index 0). So,

```python
text='Sandwich' print(text[2])
```

will output the letter `n`.

If you want a group of letters this is done using the following notation.

```bash
Stringname[position of first letter:position after last letter]
```

So

```python
text= 'Sandwich'
print(text[0:4])
```

produces `Sand`

and

```python
text= 'Sandwich'
print(text[1:5])
```

produces `andw`

If we want the length of a string we use len just like we did with lists. So:

```python
text= 'Sandwich'
a=len(text)
print(a)
```

outputs

`8`

￼## Task B
Change the previous program so it counts the number of occurrences of the lowercase letter a.

## Task C
Write a program that takes in a word and says whether or not it is a palindrome. A palindrome is a word that is the same backwards as forwards like noon and radar.

## Specimen Exercise
A good exercise to test your understanding of string handling is the password strength exercise in the Specimen A453 tasks.

Design, code test and evaluate a system to accept and test a password for certain characteristics.

- It should be at least 6, and no more than 12 characters long
- The system must indicate that the password has failed and why, asking the user to re enter their choice until a successful password is entered.
- A message to indicate that the password is acceptable must be displayed.
- Password strength can be assessed against simple criteria to assess its suitability; for example a password system using only upper and lower case alphabetical characters and numeric characters could assess the password strength as:
    WEAK if only one type used, eg all lower case or all numeric MEDIUM if two types are used
    STRONG if all three types are used.

For example

  hilltop, 123471324, HAHGFD are all WEAK
  catman3 and 123456t are MEDIUM 
  and RTH34gd is STRONG
    
A message to indicate the password strength should be displayed after an acceptable password is chosen.

It would be excellent practice to give this a go. On the next page is one version of what the solution could look like in Python.

## Worked Password Example
**NB** This is just the code section. To score full marks in A453 you would need design, testing and evaluation as appropriate.

```python
#Program to assess strength of password
#Ask for password until one of correct length is entered
passwordValid=False
while passwordValid==False:
    password=input('Please enter your password ')
    if len(password)<6:
        print('Password too short - must be 6 or more characters')
    elif len(password)>12:
        print('Password too long - must be 12 or fewer
characters')
    else:
        print('Password Accepted')
        passwordValid=True
        
#Cycle through the password character by character counting
#the number of each 'type' of character.
lowerCount=0
upperCount=0
numberCount=0
for letter in password:
    if letter>='a' and letter<='z':
        lowerCount=lowerCount+1
    elif letter>='A' and letter<='Z':
        upperCount=upperCount+1
    elif letter>='0' and letter<='9':
        numberCount=numberCount+1
        
#Count up the types of character
typesOfChar=0
if lowerCount>0:
    typesOfChar=typesOfChar+1
if upperCount>0:
    typesOfChar=typesOfChar+1
if numberCount>0:
    typesOfChar=typesOfChar+1
    
#Print out the strength of the password
if typesOfChar==1:
    print('This is a WEAK password')
elif typesOfChar==2:
    print('This is a MEDIUM password')
else:
    print('This is a STRONG password')
```
---
title: Files
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 13-files/start.py
    panel: 0
layout: ""
step: 13-files

---
## Writing to Files
Most real world programs need to be able to read and write data to files. Fortunately Python makes this process extremely easy to do.

To get Python to write to a file we first open it, write what we want to it and finally close it.

```python
myFile = open('example.txt', 'wt')
myFile.write('I have written to a file.')
myFile.close()
```

Copy and run this code. If you look in the same directory where you saved your program you should now see the file example.txt. When writing to a file Python creates it if it does not yet exist.

If we want multiple lines we can use the `\n` newline escape sequence.

```python
# Write a file
myFile = open('example.txt', 'wt')
myFile.write('I have written to a file.\nIt now has three
lines\nThe third being this one')
myFile.close()
Alternatively we can use spread it out over several lines (but note we still need the \n)

# Write a file
myFile = open('example.txt', 'wt')
myFile.write('I have written to a file.\n')
myFile.write('It now has three lines.\n')
myFile.write('The third being this one.\n')
myFile.close()
```

## Reading From Files
Reading from files is equally as straight forward.

Make sure you have run one of the above programs so you have the file `example.txt` containing:

```bash
I have written to a file.
It now has three lines.
The third being this one.
```

Copy and run the following code:

```python
myFile = open('example.txt', 'rt')
contents = myFile.read()
print(contents)
myFile.close()
```

If all has worked the contents of your file should appear in your programming console.

The rt and wt that appear in the open command stand for read text and write text. They tell Python the type of file you are opening and what access you need to it.

Sometimes we want to read a file line at a time. We do this using the readline command. If we want it to read all the lines in the file we can use a while loop. We tell the program to `readline` while we are not reading in an empty line (and so the end of the file). Of course you could, of course, change this to keep reading until it reaches any other string of your choice.

```python
myFile = open('example.txt', 'rt')
line = myFile.readline()
while line!='':
print(line)
    line = myFile.readline()
myFile.close()
```

An more elegant solution is to use a for loop.

```python
myFile = open('example.txt', 'rt')
for line in myFile:
     print(line)
myFile.close()
```

You will notice with both of these options there are blank lines in between each line of text. To prevent this change print(line) to print(line,end='').

**NB** two single quotation marks not one double.


## Task A
Write a program that reads a list of numbers from a file then outputs the average. So if your file contained

```bash
3 45 83 21
```

Your program would output: `38`

## Task B
In Task A of 'Lists' you had to write a program that takes in names and stored them in a list until `END` is entered. 

This time you are going to change it so it stores the names in between times the program is run. Adapt the program so that when it loads it looks for the file names.txt and reads any names into the list. 

The user should then be able to enter new names as before. When END is typed it should output the new list (i.e. loaded names and entered names) then save it to the file `names.txt`.

## Task C
When you are confident with using read and write why not try the specimen A453 task:

## High scores database
Design, code and test a system to store and manage user names and their highest score. The system must be able to

- create a file
- add data to a file
- locate data in the file by name and their highest score
- delete an item and its associated data from the file
- locate and update a high score for a user

The system need only cater for 10 items


## Challenge Exercises
These exercises are significantly more challenging than the ones encountered so far. They are a good way of practicing skills you have acquired.

### Challenge Exercise One
Write a procedure called triangle that takes in a number and then prints out a triangle of that height. so

``python
triangle(4)
```

would print out:

```bash
   *
  ***
 *****
*******
```

Call your function from this main program:

```python
triangle(2)
triangle(3)
triangle(4)
```

it should output:

```bash
   *
  ***
   *
  ***
 *****
   *
  ***
 *****
*******
```

### Challenge Exercise Two
The Sieve of Eratosthenes is an algorithm to find prime numbers. 

The algorithm goes as follows:

To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
2. Initially,letpequal2,thefirstprimenumber.
3. Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list. These will be multiples of p: 2p, 3p, 4p, etc.; note that some of them may have already been marked.
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.

When the algorithm terminates, all the numbers in the list that are not marked are prime.

To find all the prime numbers less than or equal to 30, proceed as follows. 

First generate a list of integers from 2 to 30:

```bash
2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
```

First number in the list is 2; cross out every 2nd number in the list after it (by counting up in increments of 2), i.e. all the multiples of 2:

```bash
 2  3  5  7  9  11 13 15 17 19 21 23 25 27 29 
 ```
 
Next number in the list after 2 is 3; cross out every 3rd number in the list after it (by counting up in increments of 3), i.e. all the multiples of 3:

```bash
 2  3  5  7  11 13 17 19 23 25 29 
```

Next number not yet crossed out in the list after 3 is 5; cross out every 5th number in the list after it (by counting up in increments of 5), i.e. all the multiples of 5:

```bash
 2  3  5  7  11 13 17 19 23 29 
```

Next number not yet crossed out in the list after 5 is 7; the next step would be to cross out every 7th number in the list after it, but they are all already crossed out at this point, as these numbers (14, 21, 28) are also multiples of smaller primes because 7*7 is greater than 30. The numbers left not crossed out in the list at this point are all the prime numbers below 30:

```bash
 2  3     5     7           11    13          17    19          23                29
 ```
 
[Look up the Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼￼Write a program that prints out all the primes below 10,000.

*HINT: you will need to use % which gives the remainder of a division operation. So `x=11%5` would give `1` as 11/5=2 remainder 1*
---
title: Useful Resources
files: []

---
- [The Official Python Website](http://docs.python.org/py3k/). Here you will find tutorials and official reference materials.
- [Learn Python](http://www.learnpython.org/) an excellent set of online Python tutorials that cover the topics in this booklet and beyond.
- [Computing At School](http://www.computingatschool.org.uk/) CAS is an organisation that seeks to promote the teaching of computing in schools. It is an active and friendly community with a thriving forum that is always a good source of help and ideas.
- [The British Informatics Olympiad](http://www.olympiad.org.uk/) is an annual programming competition open to students 18 and under. The site has a collection of past papers with questions that vary from challenging to extremely difficult.
- [Project Euler](http://projecteuler.net/) is a collection of mathematical programming challenges with different levels of difficulty.