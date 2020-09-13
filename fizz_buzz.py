#time pass problems

#ask number and check for Fizz or Buzz
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


print(fizz_buzz(15)) #try for yourself

#prints all Fizz and buzz in a given limit
def show_fizzBuzz(limit):
    show = 0
    for i in range(limit):
        show += 1
        if show % 3 == 0 and show % 5 == 0:
            print('FizzBuzz')
        elif show % 3 == 0:
            print('Fizz')
        elif show % 5 == 0:
            print('Buzz')
        else:
            print(show)

show_fizzBuzz(25) #try for yourself
