import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information, including the file name, line number, and the error message.

    Purpose:
    This function is designed to capture detailed information about an exception (error),
    such as the file in which it occurred, the line number, and the error message.
    It then formats this information into a string for logging and debugging purposes.

    :param error: The exception object that contains the error information.
                  Expected type: Exception (e.g., ValueError, KeyError, etc.)
    :param error_detail: The sys module to access traceback details, particularly the exception's traceback.
                         Expected type: sys (sys module is used to get exception details).
    :return: A string representing the detailed error message, including the file name, line number, and error message.
    """
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with the file name, line number, and the actual error message
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    
    # Log the error for better tracking and debugging
    logging.error(error_message)
    
    return error_message

class MyException(Exception):
    """
    A custom exception class to handle and log errors with detailed traceback information.

    Purpose:
    This class is used to create custom exceptions that contain not only the error message
    but also detailed information about where the error occurred, including the file and line number.

    :param error_message: A string describing the error that occurred.
                          Expected type: str (error message).
    :param error_detail: The sys module to access traceback details.
                         Expected type: sys (sys module for traceback information).
    """
    
    def __init__(self, error_message: str, error_detail: sys):
        """
        Initializes the custom exception with a detailed error message, including traceback information.

        Purpose:
        This constructor allows the creation of a custom exception object that captures both the error message
        and detailed traceback information to aid in debugging.

        :param error_message: A string message describing the error that occurred.
        :param error_detail: The sys module to extract traceback details (provides information about where the error occurred).
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the custom exception, which is the detailed error message.

        Purpose:
        This method ensures that when the exception is printed or logged, it provides
        the complete error message, including the file name and line number where the error occurred.

        :return: A string representing the formatted error message, including the file name, line number, and the error message.
        """
        return self.error_message
