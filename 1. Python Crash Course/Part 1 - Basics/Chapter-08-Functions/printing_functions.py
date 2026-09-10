def hello_world(country):
        print(f"Hello world of {country}.")

def make_car(manufacturer, model_name, **kwargs):
    car_dict = kwargs
    car_dict['manufacturer'] = manufacturer
    car_dict['model_name'] = model_name
    return car_dict