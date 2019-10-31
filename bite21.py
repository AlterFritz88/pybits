cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    jeeps = [value for key, value in cars.items() if key == 'Jeep']
    return ', '.join(jeeps[0])

def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [value[0] for key, value in cars.items()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    return sorted([value for sub in cars.values() for value in sub if grep.lower() in value.lower()])



def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    return {key: sorted(value) for key, value in cars.items()}


print(get_all_matching_models(cars=cars, grep='CO'))