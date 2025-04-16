import json
import pickle
import numpy as np

__locations=None
__model=None
__data_columns=None

def get_estimated_price(location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __locations
    global __data_columns

    with open("./columns.json", 'r') as f:
        __data_columns=json.load(f)['data_columns']
        __locations=__data_columns[3:]

    global __model
    with open("./house_price_model.pickle", 'rb') as f:
        __model=pickle.load(f)

    print("loading saved artifacts...done")
    
if __name__=='__main__':
    load_saved_artifacts()
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_location_names())