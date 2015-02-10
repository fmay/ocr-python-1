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