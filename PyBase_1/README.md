# your first script

We will begin with the bases of python, step by step we will be able to create a first script, this one is not very useful for network engineer, but don't worry, next ones will be.

On ll the next sections, if you use an IDE you should have a "play" icon on the top right of the screen, if you want to execute in CLI:
on windows:
python3.exe 1_HelloWorld.py
on Mac or Linux:
python3 1_HelloWorld.py

## 1. Hello World

first of all, what's a script without displaying a "Hello World»? The first function is "print()" which will display the value inside the () try to write the following code in a file in the file "1_HelloWorld.py" and execute the script:

```python3
print('hello world')
```

the function "print()" can support several type of variables, Integer, Float, String, Boolean etc... and is pretty useful for troubleshoot phases when your script is not working.

let's jump to the next section

## 2. Variables and types

A variable is easily defined in python, using the "=" sign. in the second file "2_Variable_types.py" try the following script:

```python3
my_var1 = 'Hello World'

print(my_var1)
print(type(my_var1))

```

In the example above, the first output will be the value of the variable, and the function type() will display the type of the variable. the type displayed is "string" type but it exists several, the table below will list the default types in python scripts

Family types | value in python
---------|----------
 Text | str
 Numeric | int, float, complex
 Boolean | bool
 Sequence | list, tuple, range
 Mapping | dict
 Binary | memoryview, bytes, bytarray

In general, the following types are used: "str", "int", "bool", "list", "dict" and "float".

let's try with the following test below:

```python3
my_var1 = 'Hello World'
my_var2 = 42
my_var3 = True
my_var4 = [1,2,3,4]
my_var5 = {"Company”: "Cisco", "Location": "ILM"}
my_var6 = 3.14

print(my_var1)
print(type(my_var1))
print('')
print(my_var2)
print(type(my_var2))
print('')
print(my_var3)
print(type(my_var3))
print('')
print(my_var4)
print(type(my_var4))
print('')
print(my_var5)
print(type(my_var5))
print('')
print(my_var6)
print(type(my_var6))
print('')
```

## 3. input value

The idea of a script is to take some input and display a result.
The input can be a file or ask the user to type a value on their keyboard, let's try the second solution.

The function "input()" can be used, its argument is a string with the question to be sent to the user, the input will be only string type and can set a variable to be used later on. Let's try this example below in the file "3_input.py”:

```python3
# notice that ' is a special character and special character can be protected with ==> \
my_var1 = input('what\'s your age: ')

print(my_var1)
print(type(my_var1))
```

Good! but the script is asking an age which should be an integer, and we retrieve a string, for that the function "int()" changing a string value to integer, but be careful if the string cannot be translate it will raise an error. with the same logic you can use the functions:

* int() to translate to an integer type
* float() to translate to a float type
* str() to translate to a string

Try the code below:

```python3
# notice that ' is a special character and special character can be protected with ==> \
my_var1 = input('what\'s your age: ')

print(my_var1)
print(type(my_var1))

my_var2 = int(my_var1)
my_var3 = float(my_var2)
print(my_var2)
print(type(my_var2))
print(my_var3)
print(type(my_var3))
```

## 4. Operators and concatenation

There is several operators available in python, for the numeric variable type, the table will display them:

Operator | Description
---------|----------
 \+ | Addition
 \- | Subtraction
 \* | Multiplication
 / | Division
 \*\* | Exponentiation
 // | Floor division
 % | Modulus

below an example with numeric variables:

```python3
print('three way to calculate the same operation: ')
print('-------------------------------------------')
#simple addition
print('15+1 ==>')
print(15+1)

#use two variables to do the same
var1 = 15
var2 = 1
print('var1+var2 ==>')
print(var1+var2)

#now using += to add the value (on the right) in the variable (on the left)
result = 15 
var3 = 1

result += var3 
print('result += var3 ==>')
print(result)

# * will take precedence over + 
print('-------------------------------------------')
print('* will take precedence over + you need to use () to order the calculation')
print('5+2*10=')
print(5+2*10)
print('')
print('(5+2)*10=')
print((5+2)*10)
print('')
```

Combined with the input() function, you will be able to manipulate numeric variable and send a result.

String variables can use as well two operators : "+" and "*" for concatenations.
"+" can concatenate only strings if you try to concatenate another type of variable it will raise an error.
"*" will repeat the same string as many time you mentioned with an integer.

it will be more understandable with an example :

```python3
var4 = 'Hello '
var5 = 'World'

# "+" operator
## simple concatenation
print('var4 + var5 = '+var4+var5)

## you can as well merge the variables
var4 += var5
print('now var4 = '+var4)

# "*" operator
## with 3 iterations of the var 4
print('var4 * 3 = '+var4*3)

```

Now you if you understand all of this, you can jump to folder 'assignment_PyBase_1'.
