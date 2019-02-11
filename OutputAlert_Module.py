#https://github.com/leonshen95/EC500-Modular-design-2.4/blob/master/OutputAlert%20module.py
from AI_module import AI_module
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

