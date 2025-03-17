'''
promptUser
Handles user input for a given prompt and multiple-choice options 
'''
def promptUser(prompt: str, options: tuple) -> str:
    choice = None
    while choice not in options:
        choice = input(f"{prompt} {options} ")
        if choice not in options:
          print(f"Unexpected input, please specify one of these options: {options}")
    return choice