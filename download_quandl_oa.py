import datetime as dt
import quandl 
import sys
from enum import Enum
sys.path.insert(0,'..')
import auth_keep_local

# class Call(Enum):
#     LAST_1_DAY = 1
#     LAST_7_DAYS = 7
#     LAST_31_DAYS = 31
#     LAST_365_DAYS = 365
#     ALL = 0

def prepare():
    time_window = int(sys.argv[1])
    # Now
    now = dt.date.today()
    global now_str
    now_str = str(now)
    print(now_str)
    # Start
    then = now - dt.timedelta(days=time_window)
    print(then)
    global then_str
    then_str = str(then)

def call():
    response = quandl.get('QOA/AUB', start_date=then_str, end_date=now_str)
    response.to_csv('rename_this.csv',sep=',')

if __name__ == "__main__":
    '''
    python call_api.py <DAYS_OF_WINDOW>
    '''
    prepare()
    call()