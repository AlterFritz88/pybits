import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses =  []
        self._win = False
        self._answer = get_random_number()


    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""

        inputed = input()
        if inputed == None:
            print('Please enter a number')
            raise ValueError
        try:

            inputed = int(inputed)
        except:
            print('Should be a number')
        if inputed not in range(START, END):
            print('Number not in range')
            raise ValueError
        if inputed in self._guesses:
            print('Already guessed')
            raise ValueError
        self._guesses.append(inputed)
        return inputed

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print('{} is correct!'.format(guess))
            return True
        if guess < self._answer:
            print('{} is too low'.format(guess))
            return False
        if guess > self._answer:
            print('{} is too high'.format(guess))
            return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""

        for i in range(MAX_GUESSES):
            a = 1
            while a == 1:
                try:
                    guess = self.guess()
                    a = 0
                except ValueError:
                    pass

            if True == self._validate_guess(guess):
                print('It took you {} guesses'.format(i+1))
                self._win = True
                break
        print('Guessed {} times, answer was {}'.format(MAX_GUESSES, self._answer))


if __name__ == '__main__':
    game = Game()
    game()