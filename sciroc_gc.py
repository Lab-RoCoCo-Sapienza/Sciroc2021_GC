from appJar import gui
import socket
import time
import random
import re
'''
Execution phase
Simple signs:
Caffe
Cocacola
Euro
Grazie
Limone* (Use video in “New signs” folder into Dataset)
The
Cracker
Acqua
Bicchiere
WC
Tovagliolo
Frullatore
Gomma da masticare
Birra alla spina
Patate
Bevande/bere
Cibo/mangiare
Panino

Composed signs
Buongiorno
Caffe macchiato
Succo di frutta
Acqua frizzante
Acqua da rubinetto
Vino rosso
Patate al forno
Patate fritte

Sentences
Buongiorno, desidera?* (Use video in “New signs” folder into Dataset)
Buongiorno, mi dica?
Grazie, ciao
Grazie, saluti
Latte caldo
Latte freddo
Caffe dopo
Per favore, un caffe
Sì, un euro
Mi scusi, il conto da-darmi* (Use video in “New signs” folder into Dataset)
WC uomini e a destra
Per favore, bicchiere uno
Caffe non c e mi dispiace

Interpretation phase
                   
Simple signs:
Caffe
Cappuccino
Cocacola
Euro
Grazie
Limone* (Use video in “Initial signs” folder into Dataset)
The
Cracker
Acqua
Gelato
Bicchiere
WC
Tovagliolo
Frullatore
Gomma da masticare
Birra alla spina
Patate
Bevande/bere
Cibo/mangiare
Panino
Composed signs
Buongiorno
Caffe macchiato
Succo di frutta
Acqua frizzante
Acqua da rubinetto
Vino rosso
Patate al forno
Patate fritte

Sentences:
Buongiorno, desidera? * (Use video in “Initial signs” folder into Dataset)
Buongiorno, mi dica?
Grazie, ciao
Grazie, saluti
Latte caldo
Latte freddo
Caffe dopo
Per favore, un caffe
Sì, un euro
Mi scusi, il conto da-darmi * (Use video in “Initial signs” folder into Dataset)
WC uomini e a destra
Per favore, bicchiere uno
Caffe non c e mi dispiace

'''
MY_IP = "10.68.0.128"
UDP_IP = "127.0.0.1"
UDP_PORT_WRITE = 5435
UDP_PORT_READ = 5431
MESSAGE = b"0"

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

sock_read = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP

ph = 1
tp = ""
simple_dic = []
comp_vec = []
sent_vec = []
simple_dic_ex = []
comp_vec_ex = []
sent_vec_ex = []

simple_dic.append("Caffe")
simple_dic.append("Cappuccino")
simple_dic.append("Cocacola")
simple_dic.append("Euro")
simple_dic.append("Grazie")
simple_dic.append("Limone")
simple_dic.append("The")
simple_dic.append("Cracker")
simple_dic.append("Acqua")
simple_dic.append("Gelato")
simple_dic.append("Bicchiere")
simple_dic.append("WC")
simple_dic.append("Tovagliolo")
simple_dic.append("Frullatore")
simple_dic.append("Gomma da masticare")
simple_dic.append("Birra alla spina")
simple_dic.append("Patate")
simple_dic.append("Bevande/bere")
simple_dic.append("Cibo/mangiare")
simple_dic.append("Panino")

#comp_vec.append("Composed signs")
comp_vec.append("Buongiorno")
comp_vec.append("Caffe macchiato")
comp_vec.append("Succo di frutta")
comp_vec.append("Acqua frizzante")
comp_vec.append("Acqua da rubinetto")
comp_vec.append("Vino rosso")
comp_vec.append("Patate al forno")
comp_vec.append("Patate fritte")


sent_vec.append("Buongiorno, desidera?")
sent_vec.append("Buongiorno, mi dica?")
sent_vec.append("Grazie, ciao")
sent_vec.append("Grazie, saluti")
sent_vec.append("Latte caldo")
sent_vec.append("Latte freddo")
sent_vec.append("Caffe dopo")
sent_vec.append("Per favore, un caffe")
sent_vec.append("Sì, un euro")
sent_vec.append("Mi scusi, il conto da darmi")
sent_vec.append("WC uomini e a destra")
sent_vec.append("Per favore, bicchiere uno")
sent_vec.append("Caffe non c e mi dispiace")


simple_dic_ex.append("Caffe")
simple_dic_ex.append("Cocacola")
simple_dic_ex.append("Euro")
simple_dic_ex.append("Grazie")
simple_dic_ex.append("Limone")
simple_dic_ex.append("The")
simple_dic_ex.append("Cracker")
simple_dic_ex.append("Acqua")
simple_dic_ex.append("Bicchiere")
simple_dic_ex.append("WC")
simple_dic_ex.append("Tovagliolo")
simple_dic_ex.append("Frullatore")
simple_dic_ex.append("Gomma da masticare")
simple_dic_ex.append("Birra alla spina")
simple_dic_ex.append("Patate")
simple_dic_ex.append("Bevande/bere")
simple_dic_ex.append("Cibo/mangiare")
simple_dic_ex.append("Panino")

comp_vec_ex.append("Buongiorno")
comp_vec_ex.append("Caffe macchiato")
comp_vec_ex.append("Succo di frutta")
comp_vec_ex.append("Acqua frizzante")
comp_vec_ex.append("Acqua da rubinetto")
comp_vec_ex.append("Vino rosso")
comp_vec_ex.append("Patate al forno")
comp_vec_ex.append("Patate fritte")

sent_vec_ex.append("Buongiorno, desidera?")
sent_vec_ex.append("Buongiorno, mi dica?")
sent_vec_ex.append("Grazie, ciao")
sent_vec_ex.append("Grazie, saluti")
sent_vec_ex.append("Latte caldo")
sent_vec_ex.append("Latte freddo")
sent_vec_ex.append("Caffe dopo")
sent_vec_ex.append("Per favore, un caffe")
sent_vec_ex.append("Sì, un euro")
sent_vec_ex.append("Mi scusi, il conto da darmi")
sent_vec_ex.append("WC uomini e a destra")
sent_vec_ex.append("Per favore, bicchiere uno")
sent_vec_ex.append("Caffe non c e mi dispiace")

def rob_bind():
    global UDP_IP, UDP_PORT_WRITE, UDP_PORT_READ,sock_read, sock, tp, MY_IP
    ip = pre_app.getEntry("Ip")
    aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    if(aa):
        print(ip)
        UDP_IP = ip
        try:
            sock_read.bind((MY_IP, UDP_PORT_READ))
            sock_read.settimeout(90)
        except:
            pre_app.setLabel("ip_stat", "IP Binding status:  IP connection error")
        else:
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_WRITE))
            pre_app.setLabel("ip_stat", "IP Binding status:  Successfully bound on IP"+str(ip))
            time.sleep(1)
            tp = pre_app.getRadioButton("type")
            print(tp)
            pre_app.stop()
    else:
        pre_app.setLabel("ip_stat", "IP Binding status:  IP not valid retry")
        print("ip non valido")

def reset():
    global simple_dic, comp_vec, sent_vec, ph
    s1,s2 = random.sample(simple_dic, 2)
    c = random.sample(comp_vec, 1)
    sent = random.sample(sent_vec, 1)
    app.setLabel("si1", s1)
    app.setLabel("si2", s2)
    app.setLabel("si3", c)
    app.setLabel("si4", sent)
    ph = 1
    for i in range(1,5):
        app.setLabelBg("si"+str(i), "white")
        app.setLabelBg("f"+str(i), "white")
        app.setLabel("st"+str(i), "None")
        app.setLabelBg("st" + str(i), "white")
    app.setLabelBg("si1", "orange")
    app.setLabelBg("f1", "orange")

def reset_ex():
    global simple_dic_ex, comp_vec_ex, sent_vec_ex, ph
    s1,s2 = random.sample(simple_dic_ex, 2)
    c,c2 = random.sample(comp_vec_ex, 2)
    sent = random.sample(sent_vec_ex, 1)
    app.setLabel("si1", s1)
    app.setLabel("si2", s2)
    app.setLabel("si3", c)
    app.setLabel("si4", c2)
    app.setLabel("si5", sent)
    ph = 1
    for i in range(1, 6):
        app.setLabelBg("si" + str(i), "white")
        app.setLabelBg("f" + str(i), "white")




def init():
    global MESSAGE, sock
    while(True):
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_WRITE))
        time.sleep(0.1)

def start_ex():
    global MESSAGE, UDP_IP, UDP_PORT_WRITE, sock, sock_read, comp_vec, simple_dic, sent_vec, ph
    MESSAGE = b"1"
    sign_str = "2"
    for i in range(1, 6):
        si = app.getLabel("si" + str(i))
        sign_str = sign_str + "|" + str(si)

    MESSAGE = bytes(sign_str, 'utf-8')
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_WRITE))
    for i in range(1, 6):
        app.setLabelBg("si" + str(i), "green")
        app.setLabelBg("f" + str(i), "green")

def start():
    global MESSAGE, UDP_IP, UDP_PORT_WRITE, sock, sock_read, comp_vec, simple_dic, sent_vec, ph

    #time.sleep(5)
    print(app.getLabel("si"+str(ph)))
    MESSAGE = b"1"
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT_WRITE))
    try:
        sock_read.recv(1)
        ret = sock_read.recv(1024)
        print("ret = ", ret)
    except:
        ret = ""
    if(ret != ""):
        app.setLabel("st"+str(ph), ret)
    else:
        app.setLabel("st" + str(ph), "Nothing")
    if(app.getLabel("st"+str(ph)) == app.getLabel("si"+str(ph))):
        app.setLabelBg("st"+str(ph), "green")
    else:
        app.setLabelBg("st" + str(ph), "orange")

def change_sign():
    global ph
    if(ph <= 3):
        app.setLabelBg("si"+str(ph), "green")
        app.setLabelBg("f"+str(ph), "green")
        ph += 1
        app.setLabelBg("si" + str(ph), "orange")
        app.setLabelBg("f" + str(ph), "orange")
    elif(ph == 4):
        app.setLabelBg("si" + str(ph), "green")
        app.setLabelBg("f" + str(ph), "green")


pre_app = gui()
pre_app.setSize(500,500)
pre_app.setTitle("Sciroc Gamecontroller IP Assign")
pre_app.addLabel("in", "Insert the robot IP", row=0, column=0, colspan=2)
pre_app.addLabelEntry("Ip", row=1, column=0, colspan=2)
pre_app.addLabel("sel", "Select the competition type", row=2, column=0, colspan=2)
pre_app.addRadioButton("type", "Interpretation", row=3, column=0)
pre_app.addRadioButton("type", "Execution", row=3, column=1)
pre_app.addLabel("ip_stat", "IP Binding status: ", row=4, column=0, colspan=2)
pre_app.addButton("Bind", rob_bind, row=5, column=0, colspan=2)
pre_app.go()
if(tp == "Interpretation"):
    app = gui()
    app.setSize(700,500)
    app.setFont(size=32)
    app.setTitle("Sciroc GameController")
    app.addLabel(title="titolo", text="Sciroc Challenge GameController: Interpretation phase", row = 0, column=0, colspan=3)
    #####Label fasi
    app.addLabel(title="S_info", text="Phase ", row=1, column=1)
    app.addLabel(title="f1", text="Simple sign 1", row=2, column=1)
    app.addLabel(title="f2", text="Simple sign 2", row=3, column=1)
    app.addLabel(title="f3", text="Composed sign ", row=4, column=1)
    app.addLabel(title="f4", text="Sentence ", row=5, column=1)
    ####Label segni
    app.addLabel(title="signs", text="Signs", row = 1)
    app.addLabel(title="si1", text="Sign", row=2, column=0)
    app.addLabel(title="si2", text="Sign", row=3, column=0)
    app.addLabel(title="si3", text="Sign", row=4, column=0)
    app.addLabel(title="si4", text="Sign", row=5, column=0)
    #####Label status
    app.addLabel("return", "Response", row=1, column=2)
    app.addLabel(title="st1", text="None", row=2, column=2)
    app.addLabel(title="st2", text="None", row=3, column=2)
    app.addLabel(title="st3", text="None", row=4, column=2)
    app.addLabel(title="st4", text="None", row=5, column=2)

    app.addButton(title="Send", func=start, row=6, column=0)
    app.addButton(title="Next_sign", func=change_sign, row=6, column=1)
    app.addButton(title="Reset", func=reset, row=6, column=2)
    app.setStartFunction(reset)

    app.go()
else:
    app = gui()
    app.setSize(700, 500)
    app.setFont(size=32)
    app.setTitle("Sciroc GameController")
    app.addLabel(title="titolo", text="Sciroc Challenge GameController: Execution phase", row=0, column=0,
                 colspan=2)

    #####Label fasi
    app.addLabel(title="S_info", text="Phase", row=1, column=1)
    app.addLabel(title="f1", text="Simple sign ", row=2, column=1)
    app.addLabel(title="f2", text="Simple sign ", row=3, column=1)
    app.addLabel(title="f3", text="Composed sign ", row=4, column=1)
    app.addLabel(title="f4", text="Composed sign ", row=5, column=1)
    app.addLabel(title="f5", text="Sentence ", row=6, column=1)
    ####Label segni
    app.addLabel(title="signs", text="Signs", row=1)
    app.addLabel(title="si1", text="Sign", row=2, column=0)
    app.addLabel(title="si2", text="Sign", row=3, column=0)
    app.addLabel(title="si3", text="Sign", row=4, column=0)
    app.addLabel(title="si4", text="Sign", row=5, column=0)
    app.addLabel(title="si5", text="Sign", row=6, column=0)

    app.addButton(title="Send", func=start_ex, row=7, column=0)
    app.addButton(title="Reset", func=reset_ex, row=7, column=1)
    app.setStartFunction(reset_ex)
    app.go()
