import datetime
import pandas as pd

dt_now = str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

df = pd.DataFrame([[dt_now, "yoshiayu", "Hello cron"]],
                  columns=['datetime', 'name', 'greet'])

df.to_csv('/Users/yoshi/python-cron/test_'+dt_now+'.csv')
print(dt_now, 'Hellow world from cron')

# /opt/anaconda3/bin:/opt/anaconda3/condabin:/opt/homebrew/bin:/opt/homebrew/bin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
