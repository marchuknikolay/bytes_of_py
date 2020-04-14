"""
Bite 21. Query a nested data structure

Given the provided cars dictionary:

1. Get all Jeeps
2. Get the first car of every manufacturer.
3. Get all vehicles containing the string Trail in their names (should work for other grep too)
4. Sort the models (values) alphabetically

See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better to pass the cars dict into each function to make its
scope local.
"""


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    pass


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    pass


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    pass


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    pass
