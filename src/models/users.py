class User:
    def __init__(self, username, full_name=None):
        self.username = username
        self.full_name = full_name or username
        # more profile info if needed
        # full name will be assigned to none automatically if no value is assigned
