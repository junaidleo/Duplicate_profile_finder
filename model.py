class Profile(object):
    def __init__(self):\
        self.profile = {}

    def add_profile(self, profileName, profileData):
        self.profile[profileName] = profileData
        return True

    def get_profile(self, profileName):
        return self.profile[profileName]