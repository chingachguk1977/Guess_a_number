# Проекты
* [Project 0. Game: Guess a Number] https://github.com/chingachguk1977/Guess_a_number

Роман Быков (SF, DST-100)


## Contents
[1. Description] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Description)
[2. The Problem Being Solved] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#The-Problem-Being-Solved)
[3. The Data Lay-out] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#The-Data-Lay-out)
[4. The Project Stages] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#The-Project-Stages)
[5. The Results] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#The-Results)
[6. Summary] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Summary)

### Description
The computer generates a sequence of random numbers and tries to guess a number within this sequence. 

:arrow-up: [Back to the Contents] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Contents)


### The Problem Being Solved
The goal is to guess the given number within the minimal number of tries. 

:arrow-up: [Back to the Contents] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Contents)


### The Data Lay-out
Right now it implements the binary search algorithm. The cycle repeats 1000 times, each time the number of attempts it took to guess the number is added to the list, in the end we get the average number of attempts.
Presumably, this number must not exceed log2 of the length of the array of numbers that we search in.

:arrow-up: [Back to the Contents] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Contents)


### The Project Stages
***

:arrow-up: [Back to the Contents] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Contents)


### The Results
From what I've found, the binary search algorithm does work best for this type of task and for 1000 iterations, the average number of attempts does not exceed the log2 of 1000, i.e. between 7 and 8.

:arrow-up: [Back to the Contents] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Contents)


### Summary
***

:arrow-up: [Back to the Contents] (https://github.com/chingachguk1977/Guess_a_number/blob/main/README.md#Contents)