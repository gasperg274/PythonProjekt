import pandas as pd
import matplotlib.pyplot as plt
#Ker so nizi v excelu shranjeni kot object zeljene stolpce spremenimo v int oz. float
excel = pd.read_excel('Podatki_o_filmih.xlsx')
excel['Leto izdaje'] = excel['Leto izdaje'].str.replace('I','')#Ce je v istem letu izdanih vec filmov z istim naslovom imajo dodano I
excel = excel.astype({'Leto izdaje': int})
excel['Glasovi'] = excel['Glasovi'].str.replace(',','')
excel = excel.astype({'Glasovi': int})
excel['Zasluzek'] = excel['Zasluzek'].str.replace('$','')
excel['Zasluzek'] = excel['Zasluzek'].str.replace('M','')
excel = excel.astype({'Zasluzek': float})


def podrobnosti(stolpec):
    '''Funkcija vrne nekatere informacije (stevilo podatkov, aritmeticna sredina, min, max, povprecje,...)
    o stolpcih s stevilskimi vrednostmi. Rezultati so v milijonih.'''
    return (excel.describe()[stolpec])

def osnovne_info(ver = True):
    '''Funkcija vrne nekaj splosnih informacij o stolpcih v excel tabeli in vrstah podatkov v njih.
    Za ver = False vrnemo skrajsano verzijo teh podatkov.
    '''
    return(excel.info(verbose=ver))


def st_Filmov(ime_zanra):
    ''' Vrne stevilo filmov zanra ime_zanra'''
    dolzina=len(excel.Zanr)
    st=0
    for i in range(0,dolzina):
        if ime_zanra in str(excel.Zanr[i]) :
            st+=1

    return st

def ocena(ocena_filma):
    ''' Vrne seznam filmov, ki imajo oceno vec ali enako oceni ocena_filma''' 
    dolzina=len(excel)
    tab=[]
    for i in range(0,dolzina):
        if excel['Ocena'][i] >= ocena_filma:
            tab.append(excel['Ime filma'][i] )
    return tab

def graf_x_y(x_os, y_os):
    '''Funkcija vrne graf, ki ima na x-osi podatke x_os in na y-osi podatke y_os
       Graf tudi shrani v pdf obliki. 
    '''
    plt.figure(figsize = (15, 7))
    plt.plot(excel[x_os], excel[y_os])#Izberemo podatke, iz katerih bomo izdelali diagram
    plt.ylabel(y_os, fontsize = 18)#Izberemo imena osi in velikost pisave
    plt.xlabel(x_os, fontsize = 15)
    plt.savefig(y_os + ' od ' + x_os +' graph.pdf')#Shranimo v pdf s smiselnim imenom
    return plt.show()


zanri = ['Drama', 'Action', 'Crime', 'Adventure', 'Sci-Fi',
         'Romance', 'Mystery', 'Western', 'War', 'Thriller',
         'Biography', 'Comedy', 'Fantasy', 'History',
         'Animation', 'Family', 'Horror', 'Music', 'Sport']
rezultat = []#Ustvarimo tabelo kjer shranimo koliko filmov je dolocenega zanra. To potrebujemo za izdelavo stolpicnega diagrama
for el in zanri:
    rezultat.append(st_Filmov(el))

def graf_zanri():
    '''Funkcija vrne stolpicni diagram, v katerem so na x-osi zanri na y-osi pa stevilo filmov tega zanra.
    Graf tudi shrani v pdf obliko z imenom Stolpicni diagram zanrov.pdf'''
    ax = plt.figure(figsize = (18,7))#Smiselno dolocimo velikost, da bo graf pregleden
    ax.set_facecolor('white')
    plt.bar(zanri, rezultat)#Izberemo podatke, iz katerih bomo izdelali diagram
    plt.xlabel('Zanri')#Izberemo imena osi
    plt.ylabel('St_Filmov')
    plt.savefig('Stolpicni diagram zanrov.pdf', transparent = True)
    return plt.show()
    
    






