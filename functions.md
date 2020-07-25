p001
    get_sum_of_multiples(num)
        Find the sum of all the multiples of 3 or 5 below a _num_

p002
    fibonacci_even_gen(num)
        Generator for even fibonacci values lesser than _num_
    
    get_sum_of_even(num)
        Sum of the even-valued fibonacci terms lesser than _num_

p003
    largest_prime_factor(num)
        Returns largest prime factor of _num_

p004
    largest_palindrome(num)
        Returns largest palindrome of _num_-digit number

p005
    prime_factors(num)
        Returns prime factors of _num_ (returns list)
    
    smallest_multiple(num)
        Returns least common multiple of 1-_num_

p006
    sum_square_diff(num)
        Returns the difference of square of sum and sum of squares of 1 to _num_

p007
    prime_generator()
        Prime number generator

    nth_prime(num)
        Returns the nth prime in _num_ sequence

p008
    greatest_adjacent()
        Returns the maximum product of thirteen adjacent digits of the given

p009
    pythagorean_triplet_generator()
        Pythagorean Triplet generator

    special_pyth_triplet(num)
        Returns the product of a,b,c of Pythagorean triplet 
        for which a + b + c = 1000.

p010
    prime_generator()
        Prime number generator
    
    sum_prime(num)
        Returns the sum of all the primes below _num_

p011
    check_left_right(matrix, row, column)
        Returns product of consecutive 4 numbers in left & right

    check_up_down(matrix, row, column)
        Returns product of consecutive 4 numbers in up & down
    

    check_right_diag(matrix, row, column)
        Returns product of consecutive 4 numbers diagonally to the right
    
    check_left_diag(matrix, row, column)
        Returns product of consecutive 4 numbers diagonally to the left

    largest_product()
        Returns the greatest product of four adjacent numbers in the same 
        direction (up, down, left, right, or diagonally) in the 20×20 grid

p012
    get_factors(n)
        Returns the factors of num

    first_n(num):
        Returns the value of the first triangle number to have over _num_ divisors

p013
    large_sum()
        Returns the first ten digits of the sum of the file input

p014
    longest_collatz(num)
        Returns the number under _num_ with the Longest Collatz sequence

p015
    def number_of_paths(num)
        Returns the max num of paths of _num_ x _num_ grid, moving only right and down

p016
    power_digit(num1, num2):
        Returns the sum of the digits of the _num1_ raised to _num2_
    
p017
    num999(n)
        with num2word()

    num2word(num)
        Converts _num_ to words (up to vigintillion)

p019
    sunday_count(date1, date2)
        Returns the number of Sundays that fell on the first of the month during the twentieth century 

p020
    factorial(num):
        Returns the factorial of _num_

    factorial_digit_sum(num)
        Returns the sum of the digits in _num_!

p025
    fiboanacci_generator()
        Fibonacci generator
    
    first_term_index(num)
        Returns the index of the first fibonacci that has _num_ length

p040
    positive_int_generator()
        Positive integer generator
   
    self_powers(num)
        Returns the product of nth digits

p048
    self_powers(num)
        Returns the last ten digits of the series, 
        1^1 + 2^2 + 3^3 + ... + _num_^_num_

***Notes***
Open a file and store line in a list
```
    with open(os.path.dirname(__file__) + '/data/file_name.txt', 'r') as f:
        data = [i.strip() for i in f.readlines()]
```

