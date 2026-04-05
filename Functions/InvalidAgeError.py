class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 18 or age > 60:
        return True
    else:
        raise InvalidAgeError('Please enter the age between 18 and 60')
try:
    result = validate_age(15)
    print(result)
except InvalidAgeError as e:
    print('Error : ',e)