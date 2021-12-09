"""4-1-e)"""
import os
import subprocess
import sys


def check_output(expected_output_file, actual_output_file):
    """
    This function checks the output of the program.
    """
    flag = 0  # Flag to count exceptions

    try:  # Try to open the expected output file
        # Reads the expected output file and stores contents as string
        with open(file=expected_output_file, mode="r") as f:
            expected_output = f.read()

    except FileNotFoundError:  # If expected output file is not found
        flag += 1  # Increment flag

    try:  # Try to open the actual output file
        # Reads the actual output file and stores contents as string
        with open(file=actual_output_file, mode="r") as f:
            actual_output = f.read()

    except FileNotFoundError:  # If actual output file is not found
        flag += 1  # Increment flag

    if flag == 0:  # If both files are found
        # Returns whether the expected output and actual output are equal or not
        return expected_output == actual_output

    if flag == 1:  # If any one of the files is not found
        return False

    return True  # If both files are not found


def generate_output(path_to_python_program, path_to_input_file):
    """
    This function generates the output of the program.
    """
    flag = 0  # Flag to count exceptions
    inputs = ""  # Sets inputs to empty string in case input file cannot be opened

    try:  # Try to open input file
        # Reads the input file and stores it as a string
        with open(file=path_to_input_file, mode="r") as f:
            inputs = f.read()

    except FileNotFoundError:  # If input file is not found
        flag += 1  # Increment flag

    try:  # Try to run the python program
        # Runs the python program and stores the output as a string
        result = subprocess.run(
            # sys.executable is the path to the python interpreter
            [sys.executable, path_to_python_program],
            input=inputs,  # The input is the string of inputs
            text=True,  # This is needed to get the output as a string
            capture_output=True,  # This is needed to get the stdout and stderr
            timeout=5,  # This is the timeout in seconds
            check=True,  # Raises exception if the python program raises an error
        )

    # If the python program raises an error or times out after 5 seconds
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        flag += 1  # Increment flag

    if flag == 0:  # If no errors are raised
        # Creates a file with the output in the current working directory
        with open(file="actual_output.txt", mode="w") as f:
            # Do I account for print implicit newline?
            f.write(result.stdout)  # Writes the stdout to the file

    else:  # If errors are raised
        # Creates an empty output file in the current working directory
        with open(file="actual_output.txt", mode="w") as f:
            f.write("")

    # os.getcwd() returns the current working directory
    # os.path.join() joins the path components together and returns full path as a string
    return os.path.join(os.getcwd(), "actual_output.txt")


def check(path_to_python_program, path_to_input_file, path_to_expected_output):
    """Checks the program."""
    # Generates the output of the program
    path_to_actual_output = generate_output(
        path_to_python_program, path_to_input_file
    )

    # Checks the output of the program
    return check_output(path_to_expected_output, path_to_actual_output)
