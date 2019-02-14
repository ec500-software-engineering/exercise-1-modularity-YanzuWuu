import threading
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

###################  input  ####################
class input_api:

    def __init__(self, user_id, age, gender, heartrate, Systolic_BP, Diastolic_BP, blood_oxygen, temperature, time):

        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.heartrate = heartrate
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.blood_oxygen = blood_oxygen
        self.temperature = temperature
        self.time = time
        self.dic = {"ID": user_id, "age": age,"gender": gender, "heartrate": heartrate,
                    "Diastolic_BP": Diastolic_BP, "Systolic_BP":Systolic_BP, "blood_oxygen": blood_oxygen,
                    "temperature": temperature, "time": time}
        # self.infodic = {self.dic['ID']:[self.dic]}
        self.infodic = {}
        self.infodic[self.dic['ID']]= [self.dic]


    def filter(data):
        wrong_flag = -1
        noise = 500
        if data > noise:
            data = wrong_flag
        return data


    def implement_filter(self):
        for key in self.dic.keys():
            if (key != "user_id" and key != "age" and key != "gender" and key != "time"):
                tmp = filter(self.dic[key])
                self.dic[key] = tmp



    def return_request(self, wire):
        alert = 1
        data_db = 2
        if (wire == alert):
            user_data_dic = {"heartrate": self.heartrate,
                    "Diastolic_BP": self.Diastolic_BP, "Systolic_BP": self.Systolic_BP, "blood_oxygen": self.blood_oxygen,
                    "temperature": self.temperature, "time": self.time}
            return user_data_dic
        if (wire == data_db):
            return self.user_id, self.dic


###################  analyzer  ####################

class Analyzer():

    def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_O2_Level, Body_temp):
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.Heart_Rate = Heart_Rate
        self.Heart_O2_Level = Heart_O2_Level
        self.Body_temp = Body_temp

    def Signal_Loss(self, Heart_Rate, Body_temp):
        # Signal loss judgement
        if (Heart_Rate < 60 and Body_temp < 36):
            return True
        return False

    def Shock_Alert(self, Heart_Rate, Body_temp):
        # Shock emergency judgement
        if (Heart_Rate < 60 and Body_temp >= 36):
            return True
        return False

    def Oxygen_Supply(self, Heart_O2_Level):
        # Oxygen supply judgement
        if (Heart_O2_Level < 70):
            return True
        return False

    def Fever(self, Body_temp):
        # Fever judgement
        if (Body_temp > 37.5):
            return True
        return False

    def Hypotension(self, Systolic_BP, Diastolic_BP):
        # Hypotension judgement
        if (Systolic_BP < 90 and Diastolic_BP < 60):
            return True
        return False

    def Hypertension(self, Systolic_BP, Diastolic_BP):
        # Hypertension judgement
        if (Systolic_BP > 140 or Diastolic_BP > 90):
            return True
        return False


####################AI module#####################


# Input: ID(from main function perhaps), infoDB(from Database function)
# output: Three predicted parameters, three Alert signals(Type:Boolean

class AI_module():
    def __init__(self, dict):
        self._dict = dict

    def Query_Data_From_Database(self,ID,infodic):
        ## connect database, query previous one day data from Database
        # Database = database_dict()
        Blood_oxygen=list()
        Heartrate = list()
        Systolic= list()
        Diastolic= list()
        # DataBaseModule.search(ID)
        # Username = input("")
        #get dictionary from database
        for key in infodic:
            if key == ID:
                a = infodic[ID]
                heartrate = a[0]['heartrate']
                oxygen = a[0]['blood_oxygen']
                Diastolic_BP = a[0]['Diastolic_BP']
                Systolic_BP = a[0]['Systolic_BP']
                Heartrate.append(heartrate)
                Blood_oxygen.append(oxygen)
                Systolic.append(Systolic_BP)
                Diastolic.append(Diastolic_BP)

        oxygen2=np.array(Blood_oxygen)
        Heartrate2 = np.array(Heartrate)
        diastolic2 = np.array(Diastolic)
        systolic2 = np.array(Systolic)
        Heartrate_predict_result = np.mean(Heartrate2)
        oxygen_predict_result=np.mean(oxygen2)
        Diastolic_predict_result = np.mean(diastolic2)
        Systolic_predict_result = np.mean(systolic2)


        return Heartrate_predict_result, oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result


    def Feedback(self,Blood_pressure_predict_result, Blood_oxygen_predict_result, Diastolic_predict_result, Systolic_predict_result):
        lower_BP= 80
        upper_BP= 120
        lower_BO = 80
        upper_BO = 120
        BP_Alert= False
        BO_Alert = False

        Pulse_Alert =False
        if(Blood_oxygen_predict_result<lower_BO or Blood_oxygen_predict_result>upper_BO):
            BO_Alert =True
        if(Blood_pressure_predict_result<lower_BP or Blood_pressure_predict_result>upper_BP):
            BP_Alert =True
        if(Systolic_predict_result< 90 or Diastolic_predict_result <60 or Systolic_predict_result > 140 or Diastolic_predict_result > 90):
            Pulse_Alert =True
        ## feedback the AI prediction result to the interface
        ## It will turn on the Alert when the statues get worse.
        return BO_Alert,BP_Alert,Pulse_Alert


####################output######################
def receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension):
 ##Recevie data from input module, then analyze it using some judge functions to generate boolean result
 ##Boolean Parameters
 ##If paramter returns True, means it should be alerted, then add it to the array
    BasicResult = {'Signal_Loss':False, 'Shock_Alert':False,'Oxygen_Supply':False,'Fever':False,'Hypotension':False,'Hypertension':False}
    if(Singal_Loss == True):
        BasicResult['Signal Loss']=True
    if(Shock_Alert == True):
        BasicResult['Shock_Alert']=True
    if(Oxygen_Supply == True):
        BasicResult['Oxygen_Supply']=True
    if(Fever == True):
        BasicResult['Fever']=True
    if(Hypotension == True):
        BasicResult['Hypotension']=True
    if(Hypertension == True):
        BasicResult['Hypertension']=True

    return BasicResult



#def send_basic_input_data(BasicResult, BasicData):
 ## Receive the result and show it on terminal or web page
 #   sentData = analyze(BasicResult)
 #   return sentData, BasicData


def display_AI_iuput_data(AI, ID, infodic):
 ## Recevie AI data from input module, then analyze it using some judge functions to generate boolean result
 ## Paramter is boolean
 ## If paramter is True, means it should be alerted, then add it to the array

    AI_module.Query_Data_From_Database(AI, ID, infodic)
    a = AI_module.Query_Data_From_Database(AI, ID, infodic)
    print('Pulse prediction:')
    print(a[0])
    print('Blood oxygen prediction:')
    print(a[1])
    print('Diastolic blood pressure prediction:')
    print(a[2])
    print('Systolic blood pressure prediction:')
    print(a[3])


def output_thread(my_data,ID):
    authenDB = {'admin':"123456"}
    Data = DataBaseModule(my_data.dic, authenDB)
    Data.auth = Data.authen('admin',"123456")
    # aa = my_data.infodic['a']
    ## database
    # Database = DataBaseModule(my_data.infodic, authenDB)
    # Data.auth = Data.authen('admin',"123456")
    # print(DataBaseModule.insert(Data,'a',{'a',70,'male', 70, 80, 90, 74, 36.5, 14}))

    # print(my_data.return_request(2))
    Diastolic = my_data.dic['Diastolic_BP']
    Systolic = my_data.dic['Systolic_BP']
    blood_oxygen = my_data.dic['blood_oxygen']
    temperature = my_data.dic['temperature']
    heartrate = my_data.dic['heartrate']

    ## analyzer
    analyzer = Analyzer(Systolic,Diastolic,heartrate, blood_oxygen,temperature)
    Singal_Loss = analyzer.Signal_Loss(heartrate,temperature)
    Shock_Alert = analyzer.Shock_Alert(heartrate,temperature)
    Oxygen_Supply = analyzer.Oxygen_Supply(blood_oxygen)
    Fever= analyzer.Fever(temperature)
    Hypotension = analyzer.Hypotension(Systolic,Diastolic)
    Hypertension = analyzer.Hypertension(Systolic,Diastolic)
    AI = AI_module
    # print(AI_module.Query_Data_From_Database(AI,'a',my_data.infodic))
    display_AI_iuput_data(AI, ID, my_data.infodic)


    ## output
    print(receive_basic_iuput_data(Singal_Loss, Shock_Alert, Oxygen_Supply, Fever, Hypotension, Hypertension))
    print(my_data.infodic)

###################  mian  ###################

def main():

    ## input
    my_data = input_api('a', 70, 'male', 80, 90, 100, 65, 38, 13)
    my_data2 = input_api('b', 80, 'male', 85, 92, 90, 70, 40, 14)
    my_data3 = input_api('c', 82, 'female', 83, 91, 95, 80, 45, 15)
    print("This is thread 1")
    t1 = threading.Thread(output_thread(my_data,'a'))
    print("#######################")
    print("This is thread 2")
    t2 = threading.Thread(output_thread(my_data2,'b'))
    print("#######################")
    print("This is thread 3")
    t3 = threading.Thread(output_thread(my_data3,'c'))
    print("#######################")


    t1.start()
    t2.start()
    t3.start()



if __name__=='__main__':
    main()
