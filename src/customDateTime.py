import datetime

def returnDateTime():
    currentDateTime = datetime.datetime.now()
    return currentDateTime

if __name__ == '__main__':
    print("This program will print the current dataTime")
    currentDateTime = returnDateTime()
    print('The current date Time is: {0}'.format(currentDateTime))
