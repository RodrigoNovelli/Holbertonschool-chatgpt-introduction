# Using ChatGPT to Debug and Solve Python Code Problems #
This repository documents various exercises where I debugged code with the help of ChatGPT. It also serves as an introduction to Python, as it's my first experience working with this language. It's a new tool that can streamline the process of solving and writing code problems more quickly. However, to make the most of it, you need to learn how to provide the correct prompts.
## Exercises ## 
### 0. Debugging - Python Factorial ###
#### Original Code ####

#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
    return result

f = factorial(int(sys.argv[1]))
print(f)

* Issues:
 The while loop in the factorial function did not update n, resulting in an infinite loop.

#### Revised Code ####

#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrease n by 1 in each iteration
    return result

f = factorial(int(sys.argv[1]))
print(f)

* Fixes *
Added n -= 1 to the while loop to ensure n is decremented each iteration, allowing the loop to terminate correctly.

### 1. Debugging - Python Arguments ###

#### Oringinal Code ####

#!/usr/bin/python3
import sys

for i in range(len(sys.argv)):
    print(sys.argv[i])

* Issue:
It should print only the arguments without the python file name.

#### Revised Code ####

#!/usr/bin/python3
import sys

# Start the loop at index 1 to skip the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])

* Fixes:
For i in "range(1, len(sys.argv)):": This starts the loop from index 1, effectively skipping the script name "(sys.argv[0])".

### 2. Debugging - HTML / Javascript ###

#### Oringinal Code ####

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Change Background Color</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
</head>
<body>

<h2>Click the button to change the background color</h2>

<button id="colorButon">Change Color</button>

<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });

    function changeBackgroundColor() {
        // Generate a random color
        var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        // Change the background color of the body
        document.body.style.backgroundColor = randomColor;
    }
</script>

</body>
</html>

* Issue: It looks like you have a small typo in your HTML and JavaScript code. Specifically, the id of the button and the JavaScript getElementById call don’t match. Here’s the corrected code:

#### Revised Code ####

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Change Background Color</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        padding-top: 50px;
    }
    button {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
</head>
<body>

<h2>Click the button to change the background color</h2>

<button id="colorButton">Change Color</button>

<script>
    document.getElementById("colorButton").addEventListener("click", function() {
        changeBackgroundColor();
    });

    function changeBackgroundColor() {
        // Generate a random color
        var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
        // Change the background color of the body
        document.body.style.backgroundColor = randomColor;
    }
</script>

</body>
</html>

* Fixes: Changed id="colorButon" to id="colorButton" to match the getElementById call in the JavaScript.
