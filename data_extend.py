import pickle
import datetime
from get_grouplesson_link import get_time_table_link as get_table
from data_save import save_data

folder = "gym_data/"
folder_extend = "gym_data_extended/"

filename_date = folder + str(datetime.datetime.now().strftime("%Y_%m_%d")) + ".dat"

def collect_details():
    gui_result = ""
    #This shows how to read pickled list
    try:
        with open(filename_date, "rb") as f:
            gym_store = pickle.load(f)
            for i in gym_store:
                try:
                    i.time_table = get_table(i)
                    gui_result = gui_result + i.name + "\n" + " "+ i.address + "\n" + " "+ i.link + "\n" + " "+ \
                    i.time_table  + "\n\n"
                except:
                    print("Problem with gym data")
                break
            save_data(gym_store,folder_extend)

    except:
        print("No data for today! Run 'page_reader.py' before!")

    return gui_result

#collect_details()