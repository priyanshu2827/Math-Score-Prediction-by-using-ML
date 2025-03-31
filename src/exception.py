# sys module in python provides various functions and variables that can be used to manipulate different parts of the Python runtime environment.
import sys
import logging  # Importing the logging module to enable logging functionality

def error_message_detail(error, error_detail:sys):
    """
    This function takes an error and its details as input and returns a string containing the error message and its details.
    """
    _, _, exc_tb = error_detail.exc_info()  # Extracting the traceback information from the error detail(whwere the error has occur at what location etc)
    file_name = exc_tb.tb_frame.f_code.co_filename  # Getting the file name where the error occurred
    line_number = exc_tb.tb_lineno  # Getting the line number where the error occurred
    error_message = f"Error occurred in file: {file_name} at line number: {line_number} with message: {str(error)}"
    return error_message  # Returning the formatted error message

class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It overrides the constructor to provide a custom error message.
    """
    def __init__(self, error_message, error_detail:sys):
        """
       def__init__ Constructor for the CustomException class.
        It takes an error message and its details as input and initializes the exception with a formatted error message.
        """
        super().__init__(error_message)  # Calling the constructor of the parent class (Exception)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)  # Formatting the error message using the helper function

    def __str__(self):
        """
        This method returns the string representation of the CustomException object.
        """
        return self.error_message
    
    if __name__== "__main__":
        logging.info("Logging has started")  # This line logs an info message indicating that the logging process has started.