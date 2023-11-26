# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 05:00:17 2023

@author: schla
"""


code = input('zu untersuchender Code: ')
print ('Dörte Binder')
print ('OSMI Master')
print ('Moderne Softwareentwicklung')
print ('Wintersemester 2023/24')
print ('Übung Metriken')
print ()
print ('Dies ist ein Programm zur Erstellung einfacher Metriken')
print ()

print ('Einfache Ermittlung der Codebestandteile')
print()

datei = open('text.txt','w')    #Umwandlung .java in .txt
datei.write(code)
datei.close() 

datei = open('text.txt', 'r')   #Auslesen der Datei zeilenweise
lines = datei.read()
Zeilen = code.count('\n') + 1

i = 0                           #Definition der notwendigen Variablen
Zahl_if = 0
Zahl_for = 0
Zahl_while = 0
Zahl_switch = 0
Zahl_Kanten = 0
Zahl_Knoten = 0
Zahl_Ausgang = 0
Liste_if = []
Liste_switch = []
Liste_for = []
Liste_while = []
Liste_case = []
Liste_class = []
Liste_methode = []
Liste_comment = []
Liste_default = []
Liste_else = []

while i < Zeilen:       #Ermitteln der Vorkommen der einzelnen Schlüsselwörter
    line = lines.split('\n')[i]
    if 'if' in line:
        Liste_if.append(i)
        Zahl_Kanten = Zahl_Kanten + 3
        Zahl_Knoten = Zahl_Knoten + 3
        Zahl_Ausgang = Zahl_Ausgang + 1
    if 'else' in line:
        Liste_else.append(i)
        Zahl_Kanten = Zahl_Kanten + 3
        Zahl_Knoten = Zahl_Knoten + 2
    if 'switch' in line:
        Liste_switch.append(i)
        Zahl_Knoten = Zahl_Knoten + 2
        Zahl_Ausgang = Zahl_Ausgang + 1
    if 'for' in line:
        Liste_for.append(i)
        Zahl_Kanten = Zahl_Kanten + 4
        Zahl_Knoten = Zahl_Knoten + 3
        Zahl_Ausgang = Zahl_Ausgang + 1
    if 'case' in line:
        Liste_case.append(i)
        Zahl_Kanten = Zahl_Kanten + 2
        Zahl_Knoten = Zahl_Knoten + 1
    if 'default' in line:
        Liste_default.append(i)
        Zahl_Kanten = Zahl_Kanten + 2
        Zahl_Knoten = Zahl_Knoten + 1
    if 'class' in line:
        Liste_class.append(i)
    if 'public' in line:
        if '(' in line:
            Liste_methode.append(i)
    if '//' in line:
        Liste_comment.append(i)
    if 'while' in line:
        Liste_while.append(i)
        i = i + 1    
        Zahl_Kanten = Zahl_Kanten + 4
        Zahl_Knoten = Zahl_Knoten + 3
        Zahl_Ausgang = Zahl_Ausgang + 1            
    else:
        i = i + 1

a = 0                       # Ermitteln der End-Zeilen der if-Funktionen
Liste_ifEnde = []
while a < len(Liste_if):
    j = Liste_if[a] + 1
    öffnen = 1
    schließen = 0
    while öffnen > schließen:
        line = lines.split('\n')[j]
        if '}' in line: 
            schließen = schließen + 1
        if '{' in line:
            öffnen = öffnen + 1
        if 'if' in line:
            Zahl_Kanten = Zahl_Kanten -1
            Zahl_Knoten = Zahl_Knoten -1
            Zahl_Ausgang = Zahl_Ausgang -1
        j = j + 1
    Liste_ifEnde.append(j)
    a = a + 1
    
print ('Der Code hat insgesamt' , Zeilen , 'Zeilen (inklusive Leerzeilen).')
print ('Der Code enthält insgesamt' , len(Liste_class) , 'Klasse(n) und' , len(Liste_methode) , 'Funktionen und Methoden.')
print ('Es werden' , len(Liste_comment) , 'Kommentare verwendet.')  
print()
print ('Der Code enthält' , Zahl_Kanten , 'Kanten,' , Zahl_Knoten , 'Knoten und' , Zahl_Ausgang, 'Ausgänge')
M = Zahl_Kanten - Zahl_Knoten + Zahl_Ausgang
print ('Damit ergibt sich eine McCabe-Metrik von M = ' , M)
if (M) < 11: 
    print('Diese Metrik spricht für ein einfaches Programm mit geringen Risiken.')
if 10 < M < 21:
    print('Diese Metrik spricht für ein Programm mit moderater Komplexität und moderaten Risiken.')
if 20 < M < 51:
    print('Diese Metrik spricht für ein Programm mit hoher Komplexität und hohem Risiko.')
if (M) > 50: 
    print('Diese Metrik spricht für Programm, das nicht testbar ist.')
print()

print ('ACD-Metrik')
print()

print ('Es gibt in dem Code', len(Liste_if), 'if-Verzweigung(en)', len(Liste_else), 'else-Verzweigung(en),', len(Liste_switch), 'switch-Verzweigung(en)mit', len(Liste_case) + len(Liste_default), 'case / default und', len(Liste_for) + len(Liste_while), 'Schleifen.')
print()

Liste_ACD_Namen = []
Liste_ACD_Beginn = []
Liste_ACD_Ende = []

Liste_elseEnde = []
if len(Liste_else) > 0:
    a = 0      
    while a < len(Liste_else):    
        j = Liste_else[a] + 1  
        öffnen = 1
        schließen = 0
        while öffnen > schließen:
            line = lines.split('\n')[j]
            if '}' in line: 
                schließen = schließen + 1
            if '{' in line:
                öffnen = öffnen + 1            
            j = j + 1
        Liste_elseEnde.append(j)
        a = a + 1

Liste_switchEnde = []
if len(Liste_switch) > 0:
    a = 0    
    while a < len(Liste_switch):   
        j = Liste_switch[a]+1
        öffnen = 1
        schließen = 0
        while öffnen > schließen:
            line = lines.split('\n')[j]
            if '}' in line: 
                schließen = schließen + 1
            if '{' in line:
                öffnen = öffnen + 1            
            j = j + 1
        Liste_switchEnde.append(j)
        a = a + 1
    
Liste_caseEnde = []
if len(Liste_case) > 0:
    a = 0
    while a < len(Liste_case):
        j = Liste_case[a] + 1
        öffnen = 1
        schließen = 0
        while öffnen > schließen:
            line = lines.split('\n')[j]
            if '}' in line: 
                schließen = schließen + 1
            if '{' in line:
                öffnen = öffnen + 1            
            j = j + 1
        Liste_caseEnde.append(j)
        a = a + 1
    
Liste_defaultEnde = []
if len(Liste_default) > 0:
    a = 0
    while a < len(Liste_default):        
        j = Liste_default[a] + 1
        öffnen = 1
        schließen = 0
        while öffnen > schließen:
            line = lines.split('\n')[j]
            if '}' in line: 
                schließen = schließen + 1
            if '{' in line:
                öffnen = öffnen + 1            
            j = j + 1
        Liste_defaultEnde.append(j)
        a = a + 1

Liste_forEnde = []
if len(Liste_for) > 0:
    a = 0
    while a < len(Liste_for):        
        j = Liste_for[a] + 1
        öffnen = 1
        schließen = 0
        while öffnen > schließen:
            line = lines.split('\n')[j]
            if '}' in line: 
                schließen = schließen + 1
            if '{' in line:
                öffnen = öffnen + 1                            
            j = j + 1
        Liste_forEnde.append(j)
        a = a + 1

Liste_whileEnde = []
if len(Liste_while) > 0:
    a = 0
    while a < len(Liste_if):        
        j = Liste_while[a] + 1
        öffnen = 1
        schließen = 0
        while öffnen > schließen:
            line = lines.split('\n')[j]
            if '}' in line: 
                schließen = schließen + 1
            if '{' in line:
                öffnen = öffnen + 1            
            j = j + 1
        Liste_whileEnde.append(j)
        a = a + 1

Liste_1 = []
Liste_1Beginn = []
Liste_1Ende = []
a = 0
b = 1
c = 1
d = 1 
e = 1 
f = 1 
g = 1 
h = 1
while a < Zeilen: 
    line = lines.split('\n')[a]
    if len(Liste_if) > 0 and 'if' in line:
        Liste_1.append('if' + str(b))
        Liste_1Beginn.append(Liste_if[b-1])
        Liste_1Ende.append(Liste_ifEnde[b-1])
        b = b + 1
    if len(Liste_else) > 0 and 'else' in line:
        Liste_1.append('else' + str(c))
        Liste_1Beginn.append(Liste_else[c-1])
        Liste_1Ende.append(Liste_elseEnde[c-1])
        c = c + 1
    if len(Liste_switch) > 0 and 'switch' in line:
        Liste_1.append('switch' + str(d))
        Liste_1Beginn.append(Liste_switch[d-1])
        Liste_1Ende.append(Liste_switchEnde[d-1])
        d = d + 1
    if len(Liste_case) > 0 and 'case' in line:
        Liste_1.append('case' + str(e))
        Liste_1Beginn.append(Liste_case[e-1])
        Liste_1Ende.append(Liste_caseEnde[e-1])
        e = e + 1
    if len(Liste_default) > 0 and 'default' in line:
        Liste_1.append('default' + str(f))
        Liste_1Beginn.append(Liste_default[f-1])
        Liste_1Ende.append(Liste_defaultEnde[f-1])
        f = f + 1
    if len(Liste_for) > 0 and 'for' in line:
        Liste_1.append('for' + str(g))
        Liste_1Beginn.append(Liste_for[g-1])
        #Liste_1Ende.append(Liste_forEnde[g-1])
        g = g + 1
    if len(Liste_while) > 0 and 'while' in line:
        Liste_1.append('while' + str(h))
        Liste_1Beginn.append(Liste_while[h-1])
        Liste_1Ende.append(Liste_whileEnde[h-1])
        h = h + 1 
    a = a + 1
    
a = 0 
Liste_Verzweigung1 = [Liste_1[a]] 
while a < len(Liste_1) and a < len(Liste_1Beginn) and a < len(Liste_1Ende):
    if Liste_1Beginn[a] < Liste_1Ende[a-1]:
        Liste_Verzweigung1.append(Liste_1[a + 1])
        print (Liste_Verzweigung1)
    a = a + 1
        