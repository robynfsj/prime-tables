# Findmypast coding exercise—prime tables


## 1. Task

Write an application that takes numeric input (N) from a user and outputs a 
multiplication table of (N) prime numbers.
* Please write an algorithm to solve the prime number generation. Do not use a 
library method to generate your primes.
* You should input a whole number N, where is N is at least 1.
* The application should output an N+1 x N+1 grid of numbers.

Expected primes multiplication table when N is 3:  
```
|  | 2 | 3 | 5 |
| 2 | 4 | 6 | 10 |
| 3 | 6 | 9 | 15 |
| 5 | 10 | 15 | 25 |
```


## 2. How to run

Run:  
`python3 prime_tables/main.py`

Run tests:  
`python3 -m unittest discover tests "test_*.py`  


## 3. What I'm pleased with

* The good alignment of the table values through the use of the padding 
function.
* The simple, clear structure and names of the directories and files, which 
allow for easy extension (I have commented in the files how I could extend).
* Clear documentation, function/variable names and commenting.
* Improvement in the time efficiency of the find primes algorithm from my first 
attempt (reduced time to calculate 10,000 primes from ~34.65s to ~0.18s)


## 4. What I would do with more time

* Improve the print_table function. Although I like the way the output looks in 
the console, the function is long and not very efficient, calculating each value 
one at a time and containing multiple loops and if statements. By its nature, a 
multiplication table contains duplicate values so there must be a way to 
generate it without repeated calculations. I would also explore other data 
structures and libraries to see if there is a better/easier way of creating a 
table.
* Once the efficiency of print_table was improved, I would look at improving the 
efficiency of finding primes by using a sieve algorithm such as the Sieve of 
Erathosthenes.
* Increase unit test coverage by mocking.
* Refactor into OOP to improve extensibility.
* Explore other output formats as it gets very difficult to view a large table in 
the console, and it does not display nicely with line wrapping on.
