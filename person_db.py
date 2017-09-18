import pymysql

host = "mysql.stud.iie.ntnu.no"
user = "nilstesd"
password = "cMzqlqqW"

def search(name, adress):
    db = pymysql.connect(host, user, password, user)
    cursor = db.cursor()
    
    print("Søker på navn: " + name + ", adresse: " + adress)

    cursor.execute("SELECT * FROM person WHERE navn LIKE %s AND adresse LIKE %s", ("%"+name+"%", "%"+adress+"%"))
    
    result = []
    for row in cursor:
        person = []
        person.append(row[0])
        person.append(row[1])
        person.append(row[2])
        result.append(person)
        
    db.close()
    
    # Vi logger resultatet til konsollet
    print("Resultat: " + str(result))
    
    return result

def get_adress_counts():
    db = pymysql.connect(host, user, password, user)
    cursor = db.cursor()
    
    cursor.execute("SELECT adresse, count(navn) FROM person GROUP BY adresse")
    
    adresses = []
    counts = []
    for row in cursor:
        adresses.append(row[0])
        counts.append(row[1])
         
    db.close()
    
    # Vi logger resultatet til konsollet
    print("Adresses: " + str(adresses))
    print("Counts: " + str(counts))
    
    return counts, adresses
    