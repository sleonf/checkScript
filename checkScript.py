#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  checkScriptSsh.py
#  
#  Copyright 2022 salvatore <salvatore@Linux>
#
from pickletools import markobject
import subprocess,os,time

#nv = str(input("quale nv?\n"))
#cmd = str(input("quale comando vuoi dare?"))
#os.system(f'ssh {nv} {cmd}')

while True:

    print("\n0)exit\n\n1)httpd \n2)mariadb \n3)asterisk\n4)nginx\n5)audio caller\n6)ws\n7)porte\n8)controlla la coda del PD\n\n")
    service = int(input("inserisci il numero corrispondente del servizio vuoi controllare?\n"))

    if service == 1:
        nv = str(input("su quale vuoi nv collegarti?\n\n"))
        
        print("\n1)status-info \n2)se è attivo\n3)restart\n")
        opzione = int(input("inserisci il numero corrispondente dell'azione che vuoi controllare di apache?\n"))
        if opzione == 1:
            print("Questo è lo stato del servizio Apache:\n")
            os.system(f'ssh nv{nv} systemctl status httpd')
        elif opzione == 2:
            #os.system(f'ssh nv{nv} systemctl is-active httpd')
            action = subprocess.Popen([os.system(f'ssh nv{nv} systemctl is-active httpd')], stdout=subprocess.PIPE, shell=True)
            (out, err) = action.communicate()
            print("program output:", out) 

            #output = str(os.system(f'ssh nv{nv} systemctl is-active httpd'))
            #print(f"il servizio Apache è: {output}")
        else:
            print("sto riavviando il servizio Apache\n")
            os.system(f'ssh nv{nv} systemctl restart httpd')
    elif service == 2:
        nv = str(input("su quale vuoi nv collegarti?\n"))
        
        print("\n1)status-info \n2)se è attivo\n3)restart\n")
        opzione = int(input("inserisci il numero corrispondente dell'azione vuoi controllare di mariadb?\n"))
        if opzione == 1:
            print("Questo è lo stato del servizio mariadb:\n")
            os.system(f'ssh nv{nv} systemctl status mariadb')
        elif opzione == 2:
            os.system(f'ssh nv{nv} systemctl is-active mariadb')
            #output = str(os.system(f'ssh nv{nv} systemctl is-active mariadb'))
            #print(f"il servizio mariadb è: {output}")
        else:
            print("sto riavviando il servizio mariadb\n")
            os.system(f'ssh nv{nv} systemctl restart mariadb')
    elif service == 3:
        nv = str(input("su quale vuoi nv collegarti?\n"))
        
        print("\n1)status-info \n2)se è attivo\n3)restart\n")
        opzione = int(input("inserisci il numero corrispondente dell'azione vuoi controllare di asterisk?\n"))
        if opzione == 1:
            print("Questo è lo stato del servizio asterisk:\n")
            os.system(f'ssh nv{nv} systemctl status asterisk')
        elif opzione == 2:
            os.system(f'ssh nv{nv} systemctl is-active asterisk')
            #output = str(os.system(f'ssh nv{nv} systemctl is-active asterisk'))
            #print(f"il servizio asterisk è: {output}")
        else:
            print("sto riavviando il servizio asterisk\n")
            os.system(f'ssh nv{nv} systemctl restart asterisk')
    elif service == 4:
        nv = str(input("su quale vuoi nv collegarti?\n"))
        
        print("\n1)status-info \n2)se è attivo\n3)restart\n")
        opzione = int(input("inserisci il numero corrispondente dell'azione vuoi controllare di nginx?\n"))
        if opzione == 1:
            print("Questo è lo stato del servizio nginx:\n")
            os.system(f'ssh nv{nv} systemctl status nginx')
        elif opzione == 2:
            os.system(f'ssh nv{nv} systemctl is-active nginx')
            #output = str(os.system(f'ssh nv{nv} systemctl is-active nginx'))
            #print(f"il servizio nginx è: {output}")
        else:
            print("sto riavviando il servizio nginx\n")
            os.system(f'ssh nv{nv} systemctl restart nginx')
    elif service == 6:
        nv = str(input("in quale server vuoi controllare le ws?\n"))
        os.system(f'ssh nv{nv} ps aux | grep webrtc2sip')
        ws = input("Vuoi killare tutte le ws?\n")
        if ws == 'si' or ws == 'Si' or ws == 'SI':
            print("sto chiudendo tutte le ws")
            os.system(f'ssh nv{nv} killall -9 webrtc2sip')
        else:
            print("\ns\nu\nc\na\n")
    elif service == 7:
        nv = str(input("su quale server vuoi controllare se le porte sono aperte?\n"))
        caller = input("di quale caller vuoi controllare le porte?\n")
        os.system(f'ssh nv{nv} netstat -lnp | grep {caller}')
        chiusura = input("ci sono porte rimaste aperte che vuoi chiudere?\n")
        if chiusura == 'si' or chiusura == 'Si' or chiusura == 'SI':
            #porta = os.sys('ssh mv{nv} netstat -lnp | grep {caller} | awk {print $7} | sed s/\/webrtc2sip$//')
            #os.sys(f'ssh nv{nv} netstat -lnp | grep {caller} | awk {print $7} |  sed s/\/webrtc2sip$//')
            porta = input("quale porta vuoi chiudere?\n")
            os.system(f'ssh nv{nv} kill -9 {porta}')
        else:
            print("\ns\nu\nc\na\n")
    elif service == 8:
        nv = str(input("in quale server vuoi controllare la coda del PD?\n"))
        os.system(f'ssh -t nv{nv} watch -n 0 ls -alht /var/spool/asterisk/outgoing/')

    elif service == 0:
        print("addio!")
        break
    else:               #service == 5
        nv = str(input("su quale vuoi nv collegarti?\n"))
        opzione = str(input("i caller stanno riscontrando problemi audio?\n"))
        if opzione == 'si' or opzione == 'Si' or opzione == 'SI':
            print("fai slogare tutti caller o verranno buttati fuori tra 30 secondi ;)")
            startTime = time.time()
            for i in range(1,31):
                print(i)
                #making delay 1 sec
                time.sleep(1)
            print("sto chiudemdo le ws e riavviando asterisk")
            os.system(f'ssh nv{nv} killall -9 webrtc2sip')
            os.system(f'ssh nv{nv} systemctl restart asterisk')
        elif opzione == 'no' or opzione == 'No' or opzione == 'NO':
            print("non rompere i coglioni")
        else:
            print("Si o No rincoglionit*")

