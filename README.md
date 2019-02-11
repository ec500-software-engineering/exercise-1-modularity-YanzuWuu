# exercise-1-modularity-YanzuWuu
exercise-1-modularity-YanzuWuu created by GitHub Classroom

We used dictionary to simulate database.
The structure is as followed:

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

And the result of the .py file is :
![pyresult](pyresult.png)

The exe file is so big that it was uploaded here:

https://drive.google.com/open?id=1KJhvdwta27qI9e2O2TDQWPmAFo7cc47U


The result is as followed.
![exeresult](exeresult.png)

All modules is connected and uploaded in the "All_modules" file, you can download and try.
In each module's file, gave the link of original forms of the modules as comments.

Known issues:

1.The input module doesn't give input parameters automatically, so we have to give the patient's medical values at the main function, which is not intelligent.

2.The databse is simulated by dictionary, so it was a little bit complecated when we transfer the data from one module to another.
