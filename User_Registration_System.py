'''
*********************************************************
User Registration System
*********************************************************

Purpose: Creates a simple user registration module that utilizes: 
    - Validation Functions
    - Exception Handling
    - Duplicate Checking 
    - Basic in-memory Storage

Inputs: name (str), email (str), password

Returns: Appends user information into a registered user simulated database after checking for duplicate entries
         Otherwise appends user information to a failed registrations simulated database
'''



#***********************************************
# Simulated Database
#***********************************************

registered_users = []
failed_registrations = []

#***********************************************
# Validation Functions 
#***********************************************

def validate_name(name: str) -> bool: 
    '''
    Validate that the name input contains at least 3 characters

    Arugments: 
        name(str): The input for user's name
    
    Returns: 
        bool: True if valid, False if not 
     ''' 
    return len(name) >= 3

def validate_email(email: str) -> bool: 
    '''
    Validate that the email input contains both '@' and '.'

    Arguments: 
        email(str): The input for the user's email 

    Returns: 
        bool: True if valid, False if not 
    '''
    return '@' in email and '.' in email 

def validate_password(password: str) -> bool: 
    '''
    Validate that the password input is valid. 

    Rules: 
        - Contains at least 8 characters
        - Contains at least one uppercase letter 
        - Contains at least one digit 
    
    Arguments: 
        password(str): The input for the user's password 

    Returns: 
        bool: True if valid, False if not
    '''
    if len(password)<8: 
        return False
    #generator expression
    has_uppercase= any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_uppercase and has_digit 

#***********************************************
# Orchestrator Validation Function 
#***********************************************

def validate_user_data(name: str, email: str, password: str) -> bool: 
    '''
    Validate user inputs (name, email, password)

    Arguments: 
        name(str): The input for user's name
        email(str): The input for the user's email 
        password(str): The input for the user's password

    Returns: 
        bool: True if all validation checks pass

    Raises: 
        ValueError: If any validation check fails
    ''' 

    if not validate_name(name): 
        raise ValueError('Name must contain at least 3 characters.')
    
    if not validate_email(email):
        raise ValueError("Email must contain '@' and '.' ")
    
    if not validate_password(password):
        raise ValueError(
            'Password must be at least 8 characters long and contain one uppercase letter and one digit')
    
    return True 

#***********************************************
# Registration Function 
#***********************************************

def create_user_account(name: str, email: str, password: str): 
    '''
    Create a user account after validation checks pass

    Arguments: 
        name(str): The input for user's name
        email(str): The input for the user's email 
        password(str): The input for the user's password

    Returns: 
        dict: User dictionary if registration succeeds. 
        None: if registration fails (appended as error to failed_registrations)        

    Raises: 
        ValueError: Interanally raised during validation or duplicate checks
    '''

    try: 
        validate_user_data(name, email, password)

        if any(user['email'] == email for user in registered_users): 
            raise ValueError('An account with this email already exists.')

        user_record = {
            'name': name, 
            'email': email, 
            'password': password, 
            'status':'active', 
        }

        registered_users.append(user_record)
        return user_record
    
    except ValueError as error: 
        failed_registrations.append(
            {'email':email, 'error': str(error)}
        )
        return None

#***********************************************
# Test Script
#***********************************************
def run_tests():
    '''
    Executes sample registration cases

    Returns: 
        None
    '''

    test_cases = [
        ('Jane', 'jane@email.com', 'Thisisagoodpassword1'), 
        ('Joan', 'jane@email.com', 'Thisisagoodpassword1'), 
        ('Jo', 'jo@email.com', 'Thisisagoodpassword1'), 
        ('Alan', 'Alan@email.com', 'badpass'), 
    ]

    for index, (name, email, password) in enumerate(test_cases, start = 1): 
        print(f'\nTest {index}')
        result = create_user_account(name, email, password)

        if result: 
            print('Registration Sucessful:', result) 
        else: 
            print('Registration failed.')

    print('\nFinal Registered Users:')
    print(registered_users)

    print('\nFailed Registrations:')
    print(failed_registrations)


run_tests()