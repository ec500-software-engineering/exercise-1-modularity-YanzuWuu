#https://github.com/leonshen95/EC500-Modular-design-2.4/blob/master/AI%20module.py
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
