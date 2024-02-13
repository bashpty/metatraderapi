class EnableOptions:
    def __init__(self, single=None, trailing=None, expert=None, all=None):
        self.single: bool = single
        self.trailing: bool = trailing
        self.expert: bool = expert
        self.all: bool = all

    single: bool
    trailing: bool
    expert: bool
    all: bool
