# -*- coding: utf-8 -*-
"""
Helper functions for BAIS3020: Computational Thinking
@author: Mojtaba Hosseini
"""

def safe_input(prompt, error_message = "", 
               numeric_type = float, 
               lower_value = None, upper_value = None):
    """
    This function mimics Python's builtin input function by reading a line from input, 
    then converts it to the specified numeric type, and returns that value.
    
    In addition to displaying 'prompt', it checks if the user input is valid in terms of 
    data type ('numeric_type') and is within the lower and upper values (optional).
    
    The error_message (if given) is displayed if the user enters and invalid input, 
    and the user is prompted to try again.

    Parameters
    ----------
    prompt : str
        The prompt string.
    error_message : str, optional
        Error message.
    numeric_type : function, optional
        The desired data type of the input (e.g., float or int). The default is float.
    lower_value : float, optional
        The desired lower value for valid values. The default is None.
    upper_value : float, optional
        The desired upper value for valid values. The default is None.

    Returns
    -------
    The resulting numeric value.

    """

    valid_input  = False   
    value = None
    while not valid_input:
        try:
            value = numeric_type(input(prompt))
            
            if lower_value is not None and value < lower_value:
                raise()
            
            if upper_value is not None and value > upper_value:
                raise()
                
            valid_input = True
        except:
            if error_message != "":
                print(error_message)
    return value