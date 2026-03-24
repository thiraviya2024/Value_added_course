import time
import sys
h=12
s=55
m=40
while(True):
    sys.stdout.write(f"\r{h}:{m}:{s}")
    sys.stdout.flush()
    time.sleep(1)
    s+=1
    if(s==60):
        s=0
        m+=1
        if(m==60):
            m=0
            h+=1
            if(h==13):
                h=1