# data_processor.py

## ClassDef DataProcessor

The function of the class is to process data and check the validity of email addresses.

**Attributes**:

- None: The class does not have any attributes.

**Functions**:

- `process_data`(`data`: `list`) -> `list`
    - Parameters:
        - `data` (`list`): A list of strings that will be processed.
    - Returns:
        - `list`: A list of strings where each string is uppercase.
    
- `check_emails`(`emails`: `list`) -> `list`
    - Parameters:
        - `emails` (`list`): A list of email addresses that will be validated.
    - Returns:
        - `list`: A list indicating whether each email address is valid (True or False).

**Code Description**: The DataProcessor class provides methods for processing data and checking the validity of email addresses. The process_data method takes a list of strings as input, processes each string by converting it to uppercase, and returns the resulting list. The check_emails method takes a list of email addresses as input, validates each email address using the validate_email function from the utils module, and returns a list indicating whether each email address is valid.

**Note**: The code does not perform any error handling if invalid or null inputs are provided to the methods.

**Input Example**:

```
Input: ["hello", "world"]
Output: ["HELLO", "WORLD"]
```

## FunctionDef validate_email

The function of the function is to validate an email address using a regular expression pattern.

**Parameters**:

- `email` (`str`): The email address to be validated.
- `pattern` (`str`): A regular expression pattern used for validation.

**Returns**:

- `bool`: Indicates whether the email address matches the given pattern (True) or not (False).

**Called_functions**:

- `re.match`(): Used to match the input email against the provided pattern.

**Code Description**: The validate_email function takes an email address as input and uses a regular expression pattern to validate it. If the email address matches the pattern, the function returns True; otherwise, it returns False. The pattern is defined to allow only lowercase letters, numbers, and certain special characters in the local part and domain.

**Note**: The code does not handle exceptions raised by the re.match function in case of invalid inputs or patterns.

**Input Example**:

```
Input: "test@example.com"
Output: True
```

**Output Example**:

```
No output for this example, as it only validates an email address and returns a boolean value.
```