import pymysql
import pymysql.cursors
import random

GREETING_INPUTS = ("bonjour", "salut", "yo", "salutations", "sup","hey",)
GREETING_RESPONSES = ["Bonjour", "Yo", "Salut!", "Salutations", "hey"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

dico={"nom": ['toblome ', 'coste', 'vavrille', 'oroudjian', 'kettab', 'dentand', 'ros', 'flaus', 'champredon', 'scheurer', 'guseynov', 'arethens', 'tin', 'fulleringer', 'merel', 'mai'],
      "prenom":['kodjo ', 'christine', 'nory', 'haikouhi', 'bachir', 'arthur', 'hugo', 'théo', 'marina', 'timothée', 'rustam', 'emmanuel', 'william', 'adrien', 'caroline', 'dao'],
      "date_naissance":['date','Date','naissance','birthday', 'anniversaire','né','date','née'],
      "lat":['lieu','vacance','lat','lattitude','paradis'],
      "lon":['lieu','vacance','longitude','Longitude','paradis'],
      "pygame_id":['jeu','pygame'],
      "astro":['astrologique','astro','signe'],
      "telephone":['phone','phonetel','06','07','tel','telephone','téléphone','ordiphone','cellulaire','smartphone','keitai','denwa','num','numéro'],
      "email":['mail','mèl','mél','mel','adresse de messagerie','messagerie électronique','@','email']
      }

def ditSImotRECONNU(motaCHERCHER):

    for cles, valeurs in dico.items():
        for mots in valeurs:
            if motaCHERCHER == mots:
                return True

def donnelemotCLEF(motaCHERCHER):

    for cles, valeurs in dico.items():
        for mots in valeurs:
            if motaCHERCHER == mots:
                return cles


def makeListe(s):
    l = s.split()
    return l

def selectRequest(data, dataTable, whereCol = "NULL", whereVal = "NULL" ):

    connection = pymysql.connect(host='localhost',
                                 user='pypromo',
                                 password='123',
                                 db='chatbot',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:

        with connection.cursor() as cursor:
            if whereCol == "NULL":
                sql = """SELECT `%s` FROM `%s`""" % (data, dataTable)
            else:
                sql = """SELECT `%s` FROM `%s` WHERE `%s` = '%s'""" % (data, dataTable, whereCol, whereVal)
            cursor.execute(sql)
            dataList = cursor.fetchall()
            list = []
            for elt in dataList:
                list.append(elt[data])
            return list


    finally:
        connection.close()



def bobot(questi):
    #print("Bonjour!")

    while 1:

        requetesur = ""
        question = questi
        question = question.lower()
        ListeMots = makeListe(question)
        ListeInfosDemand = []
        ListeTypeInfosDemand = []
        CompteurdINFOS = 0
        nomintero=""
        if(greeting(questi)!=None):
            return greeting(questi)
        if question != "q":
            for mot in ListeMots:
                if ditSImotRECONNU(mot) == True:
                    paramrequet = donnelemotCLEF(mot)
                    if paramrequet == "prenom":
                        nomintero= mot.capitalize()

                        #print(nomintero)

            for mot in ListeMots:
                if ditSImotRECONNU(mot) == True:
                    paramrequet = donnelemotCLEF(mot)
                    if paramrequet != "prenom" and nomintero != "":
                        CompteurdINFOS = CompteurdINFOS + 1
                        ListeTypeInfosDemand.append(paramrequet)
                        infosurNOM = selectRequest(paramrequet, "Students", "prenom", nomintero)
                        for i in infosurNOM:
                            ListeInfosDemand.append(i)

            #print(ListeInfosDemand)
            #print(ListeTypeInfosDemand)
            #print(CompteurdINFOS)
            ListeRepBOT = []
            for i in range(0, CompteurdINFOS):
                RepBOT="{}: {}".format(ListeTypeInfosDemand[i],ListeInfosDemand[i])
                ListeRepBOT.append(RepBOT)
                #print(ListeRepBOT)
            StringRepBot = ", ".join(ListeRepBOT)
            #print(StringRepBot)
            if CompteurdINFOS == 1:
                return "Tu as demandé {} info sur {}, la voici : ".format(CompteurdINFOS, nomintero) + StringRepBot
            elif CompteurdINFOS > 1:
                return "Tu as demandé {} infos sur {}, les voici : ".format(CompteurdINFOS, nomintero) + StringRepBot
            else:
                return "En quoi puis-je t'aider ? "

        else:
            return "Ciao"