import pickle

def open_recent(filename):
    filename = "gym_data_extended/" + filename
    #This shows how to read pickled list
    try:
        with open(filename, "rb") as f:
            gym_store = pickle.load(f)
            for i in gym_store:
                if(i.link_time_table == ""):
                    pass


    except:
        print("Sg went wrong when reading data from .dat")
