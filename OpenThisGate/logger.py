import datetime

def log(log_text):
    today = datetime.datetime.now().strftime('%Y%m%d')
    filepath = 'log/log_' + today
    log = open(filepath, 'a')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.write('\n' + now + ' ' + log_text)
    log.close()