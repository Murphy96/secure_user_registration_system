# Welcome!

This project creates a simple secure user registration system using Python. 

## Project Requirements 

### 1) Simulate a Database 
      This step creates two global lists to simulate a connection to a database. 

### 2) Validation Functions 
      This section contains 3 functions: 
      
      **validate_name(name)** validates the name has at least 3 characters, returns True if valid, otherwise False

      **validate_email(email)** validates the email contains '@' and '.', returns True if valid, otherwise False 

      **validate_password(password)** validates the password is at least 8 characters, contains an uppercase letter and a digit, returns True if valid, otherwise False. 

### 3) Main Validation Function 

    This is an orchestrator function named **validate_user_date(name, email, password)**

    This function calls the three validation functions, raises a ValueError if any validation fails, and returns True if all validation pass successfully. 


### 4) Registration Function 

    This is a function called **create_user_account(name,email,password)**

    This function calls **validate_user_date()** to validate inputs. Checks if the email already exists, and if it doest, raises a Value Error. 
    If validation passes, the function creates a dictionary containing name, email, password, and a status flag set to active. It appends the dictonary to the "database" and returns the created user dictionary. 
    If any error occurs during validation or duplicate checking, the function catches the ValueError, stores a dictionary inside the simulated database with the email and error message, and returns None. 

### 5) Testing Section 

    This section contains test cases to ensure the system performs as expected in both successful and fail-case scenarios. 
      
