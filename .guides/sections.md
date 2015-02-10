---
title: Introduction
files: []
layout: ""

---
Learning to program takes time and lots of practice but more importantly should be fun.

On the training day we will be covering sections of this booklet but it would be unrealistic to expect to learn everything over a one day period.

After the training day go back over this booklet. If you are unsure I would recommend starting from the beginning and working through all the tasks. It is one thing to read through the exercises but this is no substitute for doing them yourself. Not only does this help embed the concepts but it also helps you get a feel for the sort of errors your students may come across. Each section contains three tasks a, b and c, each of increasing difficulty.

Once you are comfortable with the material in this booklet it is hoped you will have a strong enough grounding to develop your programming skills in the direction you want.

Remember your trainers will be available to contact after the day itself so please do not hesitate to email them if any questions arise.


> ### Tip
> If you are finding yourself stuck on a programming task it often pays to go and do something
> completely different for an hour. Watch EastEnders, mow the law, walk the dog anything to take
> your mind off the problem. It’s amazing how many silly mistakes you will spot when reviewing
> your code with a fresh pair of eyes.

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
## Hello World

All programmers start with the program hello world. It’s kind of a rite of passage.

**IMPORTANT** : you will be asked to run you program. To do so, simply press the 'Run File' button in the top menu within this application.

### Task A

Copy and run the following program in Python.

```python
print('Hello World!')
```

You will hopefully see the message `Hello World!`.

### Task B

Change the program so it says `Pleased to meet you.`. 


### Task C

Write a program that says:

```bash
This is
a computer program
that prints on several lines
```

*Hint: use more than one print() command.*

### Challenge

Write a program to say

```bash
This is John's first program
```

The apostrophe makes this trickier than it first may seem
*Hint: Use Google to find out about escape characters in Python

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

Will print `Hello Bob Bob``

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
title: "Applying filters to lists "
files:
  - action: close
    path: "#tabs"
  - action: open
    path: 4-lists/start_2_5_1_a.py
    panel: 0
layout: ""
step: 4-lists

---
The ability to filter lists is very important. Consider a program that is creating a prefect rota. From the list of potential prefects, the program will have to exclude all who are already engaged at a particular time slot, leaving the list of possible
candidates.

## Task 2.5.1a:

The code in [start_2_5_1_a.py](open_file "4-lists/start_2_5_1_a.py") will take the just-in-time created list of numbers `0-9` and filter it to only those over `5` using an appropriately called `function:`

Copy and execute this program, supplying comments where necessary.


```bash
# Expected Output
[6, 7, 8, 9]
```

## Task 2.5.1b

There is more than one way to filter lists and different people end up preferring different types. Replace the line

```python
filtered_li = [x for x in li if over_five(x)]
```

with

```python
filtered_li = list(filter(over_five,li))
```

We are now making use of the built-in Python function to filter lists.

However, this function is being depreciated (its use is discouraged), so make sure you know the other methods, as well.

## Task 2.5.1c

Now replace the line with

```pyhton
filtered_li = [x for x in li if x > 5]
```

Here, we actually simplified our code, instead of a function which is more flexible and efficient, we are checking the condition (`> 5`) in the filtering statement itself. If the first two methods were too complicated, this is the one to use.

You should see no difference in output, they are all equivalent. Can you comment on their readability and easy of understanding – which option do you like more?

You can read [here](http://www.artima.com/weblogs/viewpost.jsp?thread=98196) what Python’s inventor has to say about this.

There is another commonly used list function called `map`. It runs a specified function on every list item.

### Task 2.5.1d

Replace the line

```python
filtered_li = [x for x in li if over_five(x)]
```

with

```python
filtered_li = list(map(over_five,li))
```

```bash
# Expected Output
[False, False, False, False, False, False, True, True, True, True]
```

**Q:** What did the mapping do?
**A:** It replaced the list item with the value of thee function in which that list item was an input.

## Task 2.5.1e

It is not very useful with our `over_five` function, but consider this code,

```python
li = list(range(0,10))

def doubler(lx):
    return lx*2

filtered_li = list(map(doubler,li))

print(filt_li)
```

```bash
# Expected Output
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

It doubled all the values, sending every item through the function where it got transformed.

## Task 2.5.1f
You would get exactly same result by using list comprehension, replace the line

```python
filtered_li = list(map(doubler,li))
```

with

```python
filtered_li = [doubler(x) for x in li]
```

The output should be exactly same.

> ### Info
>
> Mapping can be quite powerful when you have a long list of items and you need to
> apply some sort of a transformation to each item (or perhaps, only to the items
> that match a criteria).
> For example, consider a store that buys items off a wholesaler, adds `30%`
> margin to the cost and then prints out the price tags. In a list of: broccoli,
> `£1.00`; milk `£1.20`; bananas `£0.60`, we would like to multiply all quantities by `1.3`.
>
> It is, of course, possible to do this with a loop, but Python here provides
> are more efficient and easier to read way of accomplishing the same thing.
