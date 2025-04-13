# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # Create a list of student names
    students = ['Alice', 'Bob', 'Charlie', 'David']

    # Assign the second student's name to first_student
    first_student = students[1]

    # Assign the last student's name to last_student
    last_student = students[-1]

    # Return the results as a dictionary
    return {
        'first_student': first_student,
        'last_student': last_student
    }
# Call the function and print the result
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # Create a tuple of food names
    foods = ('Pizza', 'Burger', 'Pasta', 'Salad')

    # Initialize an empty string for meal
    meal = ''

    # Use a for loop to concatenate food names into meal
    for food in foods:
        meal += food + ' '

    # Return the concatenated meal string
    return meal.strip()  # Remove trailing space

# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # Create a tuple of food names
    foods = ('Pizza', 'Burger', 'Pasta', 'Salad')

    # Slice the tuple to get the last two food items
    last_two_foods = foods[-2:]

    # Return the sliced tuple
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())


# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # Create a dictionary with hometown information
    home_town = {
        'city': 'Springfield',
        'state': 'Illinois',
        'population': 116250
    }

    # Create a formatted string using the dictionary values
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"

    # Return the formatted message
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())


# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # Create a dictionary with hometown information
    home_town = {
        'city': 'Springfield',
        'state': 'Illinois',
        'population': 116250
    }

    # Initialize an empty list to store items
    home_town_items = []

    # Iterate over the dictionary items and format them
    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")

    # Return the list of formatted strings
    return home_town_items

# Call the function and print the result
print('Exercise 5:', list_home_town_items())


# Exercise 6: Celebrate Students
#
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings.
# For example: ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]

def create_awesome_students():
    # Create a list of student names
    students = ['Alice', 'Bob', 'Charlie', 'David']

    # Use a list comprehension to create awesome_students
    awesome_students = [f"{student} is awesome!" for student in students]

    # Return the list of awesome students
    return awesome_students

# Call the function and print the result
print('Exercise 6:', create_awesome_students())


# Exercise 7: Filter Foods
#
# Assign to a variable named foods_with_an_a the result of list comprehension that filters the foods tuple to only include food strings that contain the letter 'a'.
# For example, if foods is a tuple of ('Taco', 'Burrito', 'Sandwich'), foods_with_an_a would be a list equal to ['Taco', 'Sandwich']

def filter_foods_with_a():
    # Create a tuple of food names
    foods = ('Taco', 'Burrito', 'Sandwich')

    # Use a list comprehension to filter foods containing 'a'
    foods_with_an_a = [food for food in foods if 'a' in food.lower()]

    # Return the filtered list
    return foods_with_an_a

# Call the function and print the result
print('Exercise 7:', filter_foods_with_a())
