from graphics import *
import mysql.connector
import winsound as W

class TC:
    def __init__(self, File, Name,win):
        self.File = File
        self.Name = Name
        self.win = win

    def Draw(self,x,y):
        self.x = x
        self.y = y
        self.Image = Image(Point(x,y), self.File)
        self.Image.draw(self.win)

    def Undraw(self):
        self.Image.undraw()

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getName(self):
        return self.Name

def SQLSTART(db,cur):
    
    SQLSIF = "INSERT Into SEES (id, character_name , arcana, persona, ultimate_persona,  higher_order_persona,  Alias , Team, IFILE ,BIO ,PFILE) "
    cur.execute("CREATE TABLE SEES (id SMALLINT UNSIGNED,  character_name VARCHAR(20), arcana CHAR(20), persona VARCHAR(30),  ultimate_persona VARCHAR(20),  higher_order_persona VARCHAR(30), Alias VARCHAR(20), Team VARCHAR(20), IFILE VARCHAR(30), BIO VARCHAR(1000), PFILE VARCHAR (30), constraint m_id primary key (id));")
    cur.execute("CREATE TABLE IT (id SMALLINT UNSIGNED,  character_name VARCHAR(20), arcana CHAR(20), persona VARCHAR(30),  ultimate_persona VARCHAR(20),  higher_order_persona VARCHAR(30),  Alias VARCHAR(20), Team VARCHAR(20), IFILE VARCHAR(30), BIO VARCHAR(1000),  PFILE VARCHAR(30) , CONSTRAINT m_id PRIMARY KEY (id) );")
    cur.execute("CREATE TABLE PT (id SMALLINT UNSIGNED,  character_name VARCHAR(20), arcana CHAR(20), persona VARCHAR(30),  ultimate_persona VARCHAR(20),  higher_order_persona VARCHAR(30), Alias VARCHAR(20), Team VARCHAR(20), IFILE VARCHAR(30), BIO VARCHAR(1000), PFILE VARCHAR (30), constraint m_id primary key (id));")

    cur.execute(SQLSIF + ' Values(1,"Makoto Yuki", "Fool", "Orpheus","Messiah",Null,null,"S.E.E.S.", "Char/SEES/MY.png", "A young man who had the power of the wildcard and was the acting leader of S.E.E.S during adventures into Dark Hour. He sacrificed himself and became the seal of Nyx who would have destroyed the world we live in. There may still be a chance to save him.", "Char/SEES/M.png");')
    cur.execute(SQLSIF + ' Values(2,"Yukari Takeba", "Lovers", "Io", "Isis",Null,null,"S.E.E.S.","Char/SEES/YT.png","The daughter of a Kirjo scientist working on shadows. She joined S.E.E.S. and helped rid the world of the dark hour. She is now Featherman Pink in an acting carrer.", "Char/SEES/I.png");')
    cur.execute(SQLSIF + ' Values(3,"Ken Amada","Justice","Nemesis","Kala-Nemi",Null,null,"S.E.E.S.","Char/SEES/KA.png","A young boy who started fighting shadows while in elementary school. He is extremly skilled and is contining his schoolling.","Char/SEES/Kala.png");')
    cur.execute(SQLSIF + ' Values(4,"Akihiko Sanada","Star","Polydeuces","Caesar",Null,null,"S.E.E.S.","Char/SEES/AS.png","Deadly in the ring, Akihiko is an amazing boxer and has been training across the world. His reflexes make him superhuman, and wants to become a police officer. He has an addiction to protein though.", "Char/SEES/C.png");')
    cur.execute(SQLSIF + ' Values(5,"Fuuka Yamagishi","High Pristess","Lucia","Juno",Null,null,"S.E.E.S.","Char/SEES/FY.png","Fuuka is a valuable support asset and can use her persona in the real world. She is advanced in working with electronics, has gotten better with food.", "Char/SEES/J.png");')
    cur.execute(SQLSIF + ' Values(6,"Mitsuru Kirijo","Empress","Penthesilea","Artemisia",Null,null,"S.E.E.S.","Char/SEES/MK.png","The heir to the Kirjo group and the leader of the Shadow Operatives. The Queen of Executions will not give mercy to her enemies.", "Char/SEES/Artemisia.png");')
    cur.execute(SQLSIF + ' Values(7,"Junpei Iori","Magician","Hermes","Trismegistus",Null,null,"S.E.E.S.","Char/SEES/JI.png","One who has rose from the dead and is deadly with a bat. You would not want to get burned by the ace defective.", "Char/SEES/T.png");')
    cur.execute(SQLSIF + ' Values(8,"Aigis","Aeon & Fool","Palladion","Athena",Null,null,"S.E.E.S.","Char/SEES/A.png","The Anti-Shadow Suppression Weapon Aigis is a robot made to have a personality and thus have a persona. Her personality has devloped to the point where she is more human than some humans. She posses the wildcard as well.","Char/SEES/Athena.png");')
    cur.execute(SQLSIF + ' Values(28,"Shinjiro Aragaki","Moon","Castor",Null,Null,null,"S.E.E.S.","Char/SEES/SA.png","Shinjiro was a friend of Akihiko that was murdered by a group called Strega.","Char/SEES/Castor.png");')
    cur.execute(SQLSIF + ' Values(27,"Koromaru", "Strength", "Cerberus", Null,Null,null,"S.E.E.S.","Char/SEES/K.png","Koromaru is a dog who had the ability to summon a persona to protect the shrine of his deceased owner. Now he follows Ken Amada.", "Char/SEES/Cerberus.png")')

    SQLIIF = "INSERT Into IT (id, character_name , arcana, persona, ultimate_persona,  higher_order_persona,  Alias , Team, IFILE ,BIO,PFILE ) "
    cur.execute(SQLIIF + ' Values(9,"Yu Narukami","Fool","Izanagi","Izanagi-no-Okami",Null,null,"Investigation Team","Char/IT/Yu.png","Yu Narukami came to Inaba for a year and the gained the ability to enter the T.V. He has the power of the wildcard and returned home after removing the fog from his world and the T.V. world and stopped a string of murders with the help of the Investigation Team. Whatever you do do not mess with Nanoko though.","Char/IT/INO.png");')
    cur.execute(SQLIIF + ' Values(10,"Yosuke Hanamura","Magician","Jiraiya","Susano-o","Takehaya Susano-o",null,"Investigation Team","Char/IT/Y.png","The partner of Yu and who has the will to fight through the troubles that come his way. The son of the manager of Junes in Inaba. Currently the caretaker of another member, Teddie.","Char/IT/S.png");')
    cur.execute(SQLIIF + ' Values(11,"Chie Satonaka","Chariot","Tomoe","Suzuka Gongen","Haraedo-no-Okami",Null,"Investigation Team","Char/IT/C.png","The Kung-Fu warrior of the group. She the only weapon she needs are her legs and you do not want to be her prey. She does want to become a police officer however.","Char/IT/H.png");')
    cur.execute(SQLIIF + ' Values(12,"Yukiko Amagi","High Priestess","Konohana Sakuya","Amaterasu","Sumeo-Okami",null,"Investigation Team","Char/IT/Yukiko.png","The owner of the Amagi Inn. She is a charcater but she will burn you if rubbed the wrong way. Do not make her laugh, she will not be effective in combat until she stops.","Char/IT/Sumeo-Okami.png");')
    cur.execute(SQLIIF + ' Values(13,"Kanji Tatsumi","Emperor","Take-Mikazuchi","Rokuten Maou","Takeji Zaiten",null,"Investigation Team","Char/IT/K.png","The manliest of all men. He may seem like a brute but is soft at heart. He works at his mothers shop making small objects. Do not let his inner self decieve you his looks represent his power.","Char/IT/TZ.png");')
    cur.execute(SQLIIF + ' Values(14,"Rise Kujikawa","Lovers","Himiko","Kanzeon","Kouzeon","Risette","Investigation Team","Char/IT/R.png","The famed idol went to Inaba on a break from show business. Her persona is unique to the group in the way that it aids in both combat and support. Do not touch her or Yu, unless you want to face her wrath. ","Char/IT/Kouzeon.png");')
    cur.execute(SQLIIF + ' Values(15,"Teddie","Star","Kintoki-Douji","Kamui","Kamui-Moshiri",null,"Investigation Team","Char/IT/T.png","This individual is a shadow at heart being native to the T.V. World. However, once coming to our world he grew a human body. He thinks he is beary funny.","Char/IT/KM.png");')
    cur.execute(SQLIIF + ' Values(16,"Naoto Shirogane","Fortune","Sukuna-Hikona","Yamato Takeru","Yamato Sumeragi",null,"Investigation Team","Char/IT/N.png","The detective prince from the Shirogane family She is deadly with her firearms, and extremly intelligent. Deciet will not be effective with her.","Char/IT/YS.png");')

    SQLIIF = "INSERT Into PT (id, character_name , arcana, persona, ultimate_persona,  higher_order_persona,  Alias , Team, IFILE ,BIO,PFILE ) "
    cur.execute(SQLIIF + ' Values(17,"Ren Amamiya","Fool","Arsene","Satanael", Null,"Joker","Phantom Thieves","Char/PT/Joker.png","After being framed for assualt, he was forced to move away for a year and eventually formed the Phantom Thieves to steal hearts and reform society. His story is still being written...","Char/PT/S.png");')
    cur.execute(SQLIIF + ' Values(23,"Futaba Sakura","Hermit","Necronomicon","Prometheus","Al Azif","Oracle","Phantom Thieves","Char/PT/Futaba.png","The hacker and support of the group. She does not really go out much but she is growing out of it","Char/PT/P.png");')
    cur.execute(SQLIIF + ' Values(20,"Morgana","Magician","Zorro","Mercurius","Diego","Mona","Phantom Thieves","Char/PT/Mona.png","This indivdual was made in the Velvet room to aid Joker in his quest. He can turn into a car, does not like being called a cat, and can poteitally turn human...","Char/PT/D.png");')
    cur.execute(SQLIIF + ' Values(18,"Ryuji Sakamoto","Chariot","Captian Kidd","Seiten Taisei","William","Skull","Phantom Thieves","Char/PT/Skull.png","After being dragged to the Meta-Verse, Ryuji became one of the founding members of the Phantom Thieves and helps to reform society.","Char/PT/W.png");')
    cur.execute(SQLIIF + ' Values(19,"Ann Takamaki","Lovers","Carmen","Hecate","Celestine","Panther","Phantom Thieves","Char/PT/Panther.png","Once hurt by teacher, she now works with the Phantom Thieves to bring justice to those who use their power to harm others.","Char/PT/C.png");')
    cur.execute(SQLIIF + ' Values(21,"Yusuke Kitagawa","Emperor","Goemon","Kamu Susanoo","Gorokichi","Fox","Phantom Thieves","Char/PT/Yuske.png","A starving artist taken adavantged of by his master, after learning the truth to the death of his mother, he aids the Phantom Thieves while creating art.","Char/PT/G.png");')
    cur.execute(SQLIIF + ' Values(22,"Makoto Niijima","High Pristess","Johanna","Anat","Agnes","Queen","Phantom Thieves","Char/PT/Queen.png","The student council president took to helping the Phantom Thieves after getting into trouble herself, she has a new view on justice and will previal.","Char/PT/A.png");')
    cur.execute(SQLIIF + ' Values(24,"Haru Okumura","Empress","Milady","Astarte","Lucy","Noir","Phantom Thieves","Char/PT/Noir.png","She is the daughter of a the owner of a massive burger chain. After learning of her fathers corruption, she choose to work with the Phantom Thieves and may get more screen time in the royal treatment.","Char/PT/L.png");')
    cur.execute(SQLIIF + ' Values(25,"Goro Akechi","Justice","Robin Hood","Loki",Null,"Crow","Phantom Thieves","Char/PT/Crow.png","The new Prince Detetctive who turns out to be a fruad and has somehow come back from the dead.","Char/PT/Loki.png");')
    cur.execute(SQLIIF + ' Values(26,"Kasumi Yoshizawa","Faith","Cendrillon",Null,Null,Null,"Phantom Thieves","Char/PT/Kasumi.png","She is a gymnast, but not much is known about her.","Char/PT/Cen.png");')
  
def DROPTABLE(cur):
    cur.execute("Drop Table SEES")
    cur.execute("Drop Table IT")
    cur.execute("Drop Table PT")

def Teams(win):
    SEESL= Image(Point(30+200,30+100), 'Pics/SEES.png')
    ITL= Image(Point((1280-30-200),30+100), 'Pics/IT.png')
    PTL= Image(Point(640,360), 'Pics/PT.png')
    WC = Image(Point(230,590),"Pics/WC.png")
    A = Image(Point(1280-30-200,590), "Pics/A.png") 
    SEESL.draw(win)
    ITL.draw(win)
    PTL.draw(win)
    WC.draw(win)
    A.draw(win)
    click = win.getMouse()
    x = click.getX()
    y = click.getY()

    while(True):
        if (30<=x<=(30+400) and 30<=y<=30+200):
            SEESL.undraw()
            ITL.undraw()
            PTL.undraw()
            WC.undraw()
            A.undraw()
            return 'S','Pics/SB.png',"Music/MD.wav"

        elif (640-200<=x<=(640+200) and 260<=y<=460):
            SEESL.undraw()
            ITL.undraw()
            PTL.undraw()
            WC.undraw()
            A.undraw()
            return 'P', 'Pics/PB.png',"Music/WU.wav"

        elif(1280-400-30<=x<=(1280-30) and 30<=y<=30+200):
            SEESL.undraw()
            ITL.undraw()
            PTL.undraw()
            WC.undraw()
            A.undraw()
            return 'I','Pics/IB.png',"Music/SW.wav"

        elif(30<=x<=(30+400) and 720-30-200<=y<=720-30):
            SEESL.undraw()
            ITL.undraw()
            PTL.undraw()
            WC.undraw()
            A.undraw()
            return 'W','Pics/WB.png',"Music/PFES.wav"

        elif(1280-400-30<=x<=(1280-30) and 720-30-200<=y<=720-30):
            SEESL.undraw()
            ITL.undraw()
            PTL.undraw()
            WC.undraw()
            A.undraw()
            return 'A','Pics/AB.png',"Music/PFES.wav"

def Info(win,INFO):
    Images = []
    Images.append(Image(Point(30+(242/2),200), INFO[8]))
    Images.append(Image(Point(1129,200), INFO[10]))
    
    y = 50
    
    temp = Text(Point(640, y),("Name: " + INFO[1]))
    temp.setTextColor("White")
    temp.setSize(15)

    Images.append(temp)
    
    y= y +50
    temp = Text(Point(640,y),("Arcana: " + INFO[2]))
    temp.setTextColor("White")
    temp.setSize(15)

    Images.append(temp)
    y= y +50
    temp = Text(Point(640,y),("Persona: " + INFO[3]))
    temp.setTextColor("White")
    temp.setSize(15)

    Images.append(temp)
    y= y +50
    w = INFO[4]

    if type(INFO[4]) == type(None):
        w = 'N/A'

    temp = Text(Point(640,y),("Ultimate Persona: " + w))
    temp.setTextColor("White")
    temp.setSize(15)
    y= y +50
    Images.append(temp)
    
    w = INFO[5]

    if type(INFO[5]) == type(None):
        w = 'N/A'

    temp = Text(Point(640,y),("High Order Persona: " + w))
    temp.setTextColor("White")
    temp.setSize(15)
    y= y +50
    Images.append(temp)

    w = INFO[6]

    if type(INFO[6]) == type(None):
        w = 'N/A'

    temp = Text(Point(640,y),("Alias: " + w))
    temp.setTextColor("White")
    temp.setSize(15)
    y= y +50
    Images.append(temp)

    temp = Text(Point(640,y),("Team: " + INFO[7]))
    temp.setTextColor("White")
    temp.setSize(15)
    y= y +50
    Images.append(temp)

    biolen = len(INFO[9])

    ts = 25

    if  biolen <=75:
        temp = Text(Point(640,680),("Info: " + INFO[9]))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

    elif  150 >= biolen >75:
        d = INFO[9]
        d = d[:75]
        temp = Text(Point(640,500),("Info: " + d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
        d=INFO[9]
        d = d[75:149]
        temp = Text(Point(640,550),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
    
    elif  225 >= biolen >150:
        d = INFO[9]
        d = d[:75]
  
        temp = Text(Point(640,500),("Info: " + d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
        d =INFO[9] 
        d=d[75:150]

        temp = Text(Point(640,550),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

        d =INFO[9] 
        d=d[150:225]

        temp = Text(Point(640,600),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
    
    elif  300 >= biolen >225:
        d = INFO[9]
        d = d[:75]

        temp = Text(Point(640,500),("Info: " + d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
        d =INFO[9] 
        d=d[75:150]

        temp = Text(Point(640,550),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

        d =INFO[9] 
        d=d[150:225]

        temp = Text(Point(640,600),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

        d =INFO[9] 
        d=d[225:300]

        temp = Text(Point(640,650),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
    
    elif  375 >= biolen >300:
        d = INFO[9]
        d = d[:75]

        temp = Text(Point(640,500),("Info: " + d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)
        d =INFO[9] 
        d=d[75:150]

        temp = Text(Point(640,550),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

        d =INFO[9] 
        d=d[150:225]

        temp = Text(Point(640,600),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

        d =INFO[9] 
        d=d[225:300]

        temp = Text(Point(640,650),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

        d =INFO[9] 
        d=d[300:]

        temp = Text(Point(640,700),(d))
        temp.setTextColor("White")
        temp.setSize(ts)
        Images.append(temp)

    for i in Images:
        i.draw(win)

    win.getMouse()

    for i in Images:
        i.undraw()

def Memeber(win, cur,team,background,Song):
    background = Image(Point(640,360), background)
    background.draw(win)
    W.PlaySound(Song , W.SND_ASYNC)
    if team != 'WC':
        #This is for any general team
        cur.execute('select * from '+ team +' ;')
        ALLROWS = cur.fetchall()

    elif team == 'WC':
        #This takes all the heros that have a speical ability and displays them
        ALLROWS = []

        cur.execute('select * from SEES;')

        for i in cur.fetchall():
            if i[2] == 'Fool' or i[2]== 'Aeon & Fool':
                ALLROWS.append(i)

        cur.execute('select * from IT;')
        for i in cur.fetchall():
            if i[2] == 'Fool' or i[2]== 'Aeon & Fool':
                ALLROWS.append(i)

        cur.execute("select * from PT;")

        for i in cur.fetchall():
            if i[2] == 'Fool' or i[2]== 'Aeon & Fool':
                ALLROWS.append(i)

    x=15
    y=160
    count = 0
    images = []

    for i in ALLROWS:
        count= count + 1
        images.append(Image(Point(x+(242/2),y), i[8]))
        x=x+10+242
        if count == 5:
            x=15
            y=720-160
    
    for i in images:
        i.draw(win)
    
    z=0
    
    #print(clickx)
   # print(clicky)

    while(z==0):

        click = win.getMouse()
        clickx=click.getX()
        clicky = click.getY()
        x = 15
        y=10
        w=0
        ym = 300
        
        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 1

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 2

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 3

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 4

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 5

        x=15
        ym = 720-10
        y = ym - 300

        if (x<=clickx <= x+242) and (y<=clicky<=ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 6

        if (x<=clickx <= x+242) and (y<=clicky<=ym):
  
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 7

        if (x<=clickx <= x+242) and (y<=clicky<=ym):

            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 8


        if (x<=clickx <= x+242) and (y<=clicky<=ym):

            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 9


        if (x<=clickx <= x+242) and (y<=clicky<=ym):

            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 10


    for i in images:
        i.undraw()

    Info(win,z)

def ArcanaPerson(win,cur,a):
    ALLROWS = []
    cur.execute('select * from SEES;')
    for i in cur.fetchall():
        if a == 'Fool' or a == 'Aeon':
            if i[2] == a or i[2]== 'Aeon & Fool': 
                ALLROWS.append(i)
        else:
            if i[2] == a:
                ALLROWS.append(i)

    cur.execute('select * from IT;')
    for i in cur.fetchall():
        if a == 'Fool' or a == 'Aeon':
            if i[2] == a or i[2]== 'Aeon & Fool': 
                ALLROWS.append(i)
        else:
            if i[2] == a:
                ALLROWS.append(i)

    cur.execute('select * from PT;')
    for i in cur.fetchall():
        if a == 'Fool' or a == 'Aeon':
            if i[2] == a or i[2]== 'Aeon & Fool': 
                ALLROWS.append(i)
        else:
            if i[2] == a:
                ALLROWS.append(i)
    

    x=15
    y=160
    count = 0
    images = []

    for i in ALLROWS:
        count= count + 1
        images.append(Image(Point(x+(242/2),y), i[8]))
        x=x+10+242
        if count == 5:
            x=15
            y=720-160
    
    for i in images:
        i.draw(win)
    
    z=0
    
    while(z==0):

        click = win.getMouse()
        clickx=click.getX()
        clicky = click.getY()
        x = 15
        y=10
        w=0
        ym = 300
        
        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 1

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 2

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 3

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 4

        if (x<=clickx <= x+242) and (y<=clicky<=y+ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        w = 5

        x=15
        ym = 720-10
        y = ym - 300

        if (x<=clickx <= x+242) and (y<=clicky<=ym):
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 6

        if (x<=clickx <= x+242) and (y<=clicky<=ym):
  
            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 7

        if (x<=clickx <= x+242) and (y<=clicky<=ym):

            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 8


        if (x<=clickx <= x+242) and (y<=clicky<=ym):

            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 9


        if (x<=clickx <= x+242) and (y<=clicky<=ym):

            z=ALLROWS[w]
                
            break
        
        x = x+ 242+ 10
        
        w = 10


    for i in images:
        i.undraw()

    Info(win,z)

def Arcana(win,cur,background,Song):
    background = Image(Point(640,360), background)
    background.draw(win)
    W.PlaySound(Song , W.SND_ASYNC)
    Cards = []
    Cards.append(TC("Cards/A.png","Aeon", win))
    Cards.append(TC("Cards/C.png","Chariot", win))
    Cards.append(TC("Cards/Em.png","Emperor", win))
    Cards.append(TC("Cards/E.png","Empress", win))
    Cards.append(TC("Cards/F.png","Faith", win))
    Cards.append(TC("Cards/Fool.png","Fool", win))
    Cards.append(TC("Cards/Fortune.png","Fortune", win))
    Cards.append(TC("Cards/H.png","Hermit", win))
    Cards.append(TC("Cards/HP.png","High Pristess", win))
    Cards.append(TC("Cards/J.png","Justice", win))
    Cards.append(TC("Cards/L.png","Lovers", win))
    Cards.append(TC("Cards/M.png","Magician", win))
    Cards.append(TC("Cards/Moon.png","Moon", win))
    Cards.append(TC("Cards/S.png","Strength", win))
    Cards.append(TC("Cards/Star.png","Star", win))
    
    x = 5+ (150/2)
    y = 160
    w = 1
    for i in Cards:
        if w == 9:
            x= 5+ (150/2)
            y = 720-160 
        
        i.Draw(x,y)
        x = x + 5 + 150
        w = w + 1
        
    
    click = win.getMouse()
    clickx = click.getX()
    clicky = click.getY()

    for i in Cards:
        if (i.getX()-150/2) <= clickx <= (i.getX() + 150/2) and (i.getY()-300/2) <= clicky <= (i.getY() + 300/2):
            for w in Cards:
                w.Undraw()
            ArcanaPerson(win,cur,i.getName())
            return

def main():
    db = mysql.connector.connect(host='127.0.0.1',user='root',password='*********',database = 'persona')
    cur = db.cursor()

    DROPTABLE(cur)
    SQLSTART(db,cur)

    win = GraphWin("********", 1280, 720)
    titleScreen = Image(Point(640, 360), 'Pics/StartPage.png')
    titleScreen.draw(win)
    win.getMouse()
    homeScreen= Image(Point(640,360),'Pics/MB.png')
    homeScreen.draw(win)
    titleScreen.undraw()
    Team, background, Song = Teams(win)

    if Team != "A":
        if Team == 'S':
            team = 'SEES'
        
        elif Team == 'P':
            team = 'PT'
        
        elif Team == 'I':
            team = 'IT'

        elif Team == 'W':
            team = 'WC'
        
        Memeber(win,cur, team,background,Song)
        homeScreen.undraw()

    else:
        Arcana(win,cur,background,Song)

main()