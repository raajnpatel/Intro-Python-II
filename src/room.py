# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

    def where_am_i(self):
        return f"*******************\n{self.title}\n\n{self.description}\n*******************"
