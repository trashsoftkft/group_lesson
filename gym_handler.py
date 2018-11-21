class Gym:
    def __init__(self, details):
        self.name = details[0]
        self.address = details[1]
        self.link = details[2]
        self.link_time_table = ""
        self.time_table_selector = ""
        self.tableHTML = ""
        self.link_correct = True
        self.correct_link = ""