import pickle
import datetime

filename_date = str(datetime.datetime.now().strftime("%Y_%m_%d")) + ".dat"

def save_data(gym_store):
    with open(filename_date, "wb") as f:
        pickle.dump(gym_store, f)

    #This shows how to read pickled list
    with open(filename_date, "rb") as f:
        for i in pickle.load(f):
            print("Gym ")
            print(i.name)
            print(i.address)
            print(i.link)
            print("*******************************")