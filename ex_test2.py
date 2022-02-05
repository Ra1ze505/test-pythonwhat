from pythonwhat.signatures import sig_from_params
from pythonwhat.test_exercise import prep_context

_, ctxt = prep_context()
globals().update(ctxt)

# ex_code - Что видит студент в начале -------------------------------------------------------------
"""
# Определите функцию shout
def ____():
    '''Объединяет строку с тремя восклицательными знаками'''
    # Объедините строки в переменной: shout_word

    # Напечатайте shout_word
    print(____)


# Вызовите shout
"""

# sol_code - Код который верный --------------------------------------------------------------------
sol_code = """
# Определите функцию shout
def shout():
    '''Выведите строку с тремя восклицательными знаками'''
    # Объедините строки: shout_word
    shout_word = 'congratulations' + '!!!'

    # Напечатайте shout_word
    print(shout_word)


# Вызовите shout
shout()
"""

# stu_code - Код который тестиреум -----------------------------------------------------------------
stu_code = """
# Определите функцию shout
def shout():
    '''Print a string with three exclamation marks'''
    # Concatenate the strings: shout_word
    shout_word = 'any string' + '!!!'
    # Print shout_word
    print(shout_word)


# Call shout
shout()
"""

# Tests --------------------------------------------------------------------------------------------
from pythonwhat.test_exercise import setup_state
setup_state(stu_code=stu_code, sol_code=sol_code)

Ex().check_function_def('shout').check_body().multi(
        has_equal_value(name='shout_word', func=lambda x, y: x[-3:] == y[-3:]),
        has_code('.*\+.*!!!.*'),
        has_code('print(.*shout_word.*)')
)
Ex().check_function('shout')

