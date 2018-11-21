import pickle

def list_gyms(filename):
    file_name_location = "gym_data_extended/" + filename
    gui_result = ""

    with open(file_name_location, "rb") as f:
        gym_store = pickle.load(f)
        for i in gym_store:
            try:
                gui_result = gui_result +  i.name + "\n" + " " + i.address + "\n" + i.time_table  + "\n\n"
            except:
                gui_result = gui_result + "INCORRENCT DATA IN .dat FILE!!!" + "\n\n"

    return gui_result