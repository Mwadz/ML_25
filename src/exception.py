# importing module that allows us to manipulate different pparts of the py runtime environment. 
# Any exception that is not handled will be caught by this module. If not there, include it in the requirements.txt file.
import sys
from src.logger import logging # logging is imported to log the error message when the exception is raised

def error_message_detail(error, error_detail:sys):
    """
        function that takes an error and its details as input and returns a formatted string with the error message and its details.
    """
    _, _, exc_tb = error_detail.exc_info() # gives us the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename # gives us the file name where the error occurred
    line_number = exc_tb.tb_lineno # gives us the line number where the error occurred
    error_message = f"Error occurred in pyscript: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]" # you can use f-string to format the string or use .format() method
    return error_message

"""
        class that inherits from the built-in Exception class.
        It takes an error message and its details as input and returns a formatted string with the error message and its details.
        The __init__ method initializes the error message and error details.
        The __str__ method returns the error message when the exception is raised.
"""

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys=sys):
        super().__init__(str(error_message)) # calls the parent class's __init__ method with the error message
        self.error_message = error_message_detail(error_message, error_detail)


    def __str__(self): 

        return self.error_message 
 # if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero") # this will log the error message
#         raise CustomException(e, sys) # this will raise the custom exception with the error message and its details    
    
"""
once you see the error message, you can remove the if __name__ == "__main__": block and use the CustomException class in your code.
It's work was to test whether the CustomException class is working or not.
use {python -m src.exception} to run exception.py file and see the error message in the logs. it forces python to treat src as a package and run the exception.py file as a module. 
"""