import os

def get_newest_data():
    gym_data = os.listdir("gym_data")
    newest_gym_data = gym_data[-1]

    return newest_gym_data

def get_newest_extended_data():
    gym_data_extended = os.listdir("gym_data_extended")
    newest_gym_data_extended = gym_data_extended[-1]

    return newest_gym_data_extended
