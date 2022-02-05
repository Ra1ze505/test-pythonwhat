from pythonwhat.signatures import sig_from_params
from pythonwhat.test_exercise import prep_context

_, ctxt = prep_context()
globals().update(ctxt)

# ex_code - Что видит студент в начале -------------------------------------------------------------
'''
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    

    # Change the value of team in global: team
    
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
# '''

# sol_code - Код который верный --------------------------------------------------------------------
sol_code = '''
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
'''

# stu_code - Код который тестиреум -----------------------------------------------------------------
stu_code = '''
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league 1"

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)
'''


# Tests --------------------------------------------------------------------------------------------
from pythonwhat.test_exercise import setup_state
setup_state(stu_code=stu_code, sol_code=sol_code)

def test_good():
    Ex().check_function('change_team')
    Ex().has_code('global team')
    Ex().check_function('print', index=0)\
        .check_args('value')\
        .has_equal_value(pre_code='team="teen titans"')
    Ex().check_function('print', index=1)
    # Ex().check_object('team')
    # print('*'*40)
    # print(Ex().check_object('team').__dict__)
