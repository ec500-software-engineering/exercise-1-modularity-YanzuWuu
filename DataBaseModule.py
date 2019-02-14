#https://github.com/leonshen95/EC500-Modular-design-2.4/blob/master/Database_Module.py

###################  database  ###################
"""
data format of infodic:
{
    'XXXXXX(user_id)': [{
        'time': '2019-02-06 17:11',
        'gender': 'male',
        'heartrate': 100,
        'blood_pressure': 125,
        'blood_oxygen': 0.7
        },
        {
            ...
        }
    ]
}
"""
# authenDB = {'username':username, }
class DataBaseModule:

    def __init__(self, infodic, authenDB):
        self.infodic = infodic
        self.authDB = authenDB
        self.auth = False


    def authen(self, username, password):
        """
        user log in, must call this function before using delete\insert\search
        :param username: user id
        :param password: user password
        :return void
        """
        if self.authDB[username] == password:
            print("Authentication Succeed!")
            self.auth = True
            return self.auth
        else:
            print("Try username and password again")


    def delete(self, ID):
        """
        delete patient's data based on user id
        :param ID: user id
        :return void
        """
        if self.auth:
            self.infodic.popitem(ID)
        else:
            print ("Authentation Failed")

    def insert(self, ID, info):
        """
        insert patient's data, it will be stored by user id
        :param ID: user id
        :param info: patient's data, type: dict, format example:
        {
        'time': '2019-02-06 17:11',
        'gender': 'male',
        'heartrate': 100,
        'blood_pressure': 125,
        'blood_oxygen': 0.7
        }
        :return void
        """
        if self.auth:
            self.infodic[ID] = info
            return self.infodic
        else:
            print("Authentation Failed")



    def search(self, ID):
        """
        search all patient's historical data based on user id
        :param ID: user id
        :return type: dict, format example:
        {
        'time': '2019-02-06 17:11',
        'gender': 'male',
        'heartrate': 100,
        'blood_pressure': 125,
        'blood_oxygen': 0.7
        }
        """
        if self.auth:
            return self.infodic[ID]
        else:
            print("Authentation Failed")
