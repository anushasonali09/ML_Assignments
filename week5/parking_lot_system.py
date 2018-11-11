

class parklot:
    vtype=[]
    vid=[]
    pid=[]
    
    def __init__(self):
        for i in range(20):
            self.vtype.append('*')
            self.vid.append('*')
            self.pid.append("P"+ str(i+1))
            
    def park(self,ID,typ):
        
        pkd=-1
        if typ =='b':
            r=0
            v='Bike'
        if typ =='B':
            r=17
            v='Bus'
        if typ == 'c':
            r=11
            v='Car'
        for i in range(r,20):
            if self.vid[i]=='*':
                pkd=i
                self.vtype[i]=v
                self.vid[i]=ID
                break
            
        return pkd


def park(p):
    
    while True:
        vtype=input('b for Bike\nc for Car\nB for Bus\nEnter a Vehicle Type : ')
        if vtype in ['B','c','b']:
            break
        else:
            print('Please Enter the correct Type')
    vid=input('Enter the Vehicle ID : ')
    return p.park(vid,vtype)

def bill(p):
    ch=park(p)
    print('\n\n\n')
    if ch==-1:
        print('BILL'.center(20,'*'))
        print((' '*18).center(20,'*'))
        print((' '*18).center(20,'*'))
        print((' '*18).center(20,'*'))
        print('*'+'Sorry The Parking'.center(18,' ')+'*')
        print('*'+'is full'.center(18,' ')+'*')
        print((' '*18).center(20,'*'))
        print((' '*18).center(20,'*'))
        print((' '*18).center(20,'*'))
        print(''.center(20,'*'))
    else:
        print('BILL'.center(26,'*'))
        
        print('*'+('PID : '+p.pid[int(ch)]).center(24,' ')+'*')
        print((' '*24).center(26,'*'))
        print('*'+('Type : '+p.vtype[int(ch)]).center(24,' ')+'*')
        print((' '*24).center(26,'*'))
        print('*'+('Vehicle ID : '+p.vid[int(ch)]).center(24,' ')+'*')
        print(''.center(26,'*'))


def show(p):
    print(''.center(23,'*'))
    print('PID\tTYPE\tNo.')
    print(''.center(23,'*'))
    for i in range(20):
        print(p.pid[i]+'\t'+p.vtype[i]+'\t'+p.vid[i])
    print(''.center(23,'*'))


def main():
    p=parklot()
    print('\n\n\n')
    while True:
        t=input('Type :-\nS to Show The parked Vehicle\nP to park Vehicle\nEND to Stop\n:')
        
        if t in ['S','P','END']:
            if t=='END':
                print('\n\nThank you\n\n')
                break
            if t=='P':
                print('\n\n\n')
                bill(p)
                print('\n\n')
            if t=='S':
                show(p)
        else:
            print('Please Check the type...\n\n\n')
    
    
        
main()


