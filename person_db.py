import pymysql

host = "mysql.stud.iie.ntnu.no"
user = "" # Skriv inn brukernavnet ditt her
password = "" # Skriv inn passordet ditt her

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
    
def delete_person(id):
    db = pymysql.connect(host, user, password, user)
    db.autocommit(True)
    cursor = db.cursor()
    
    cursor.execute("DELETE FROM person WHERE id=%s", (id))
            
    db.close()
    
    # Vi logger resultatet til konsollet
    print("delete_person count: " + str(cursor.rowcount))   
    
def update_person(id, name, address):
    db = pymysql.connect(host, user, password, user)
    db.autocommit(True)
    cursor = db.cursor()
    
    cursor.execute("UPDATE person SET navn=%s, adresse=%s WHERE id=%s", (name, address, id))
            
    db.close()
    
    # Vi logger resultatet til konsollet
    print("update_person count: " + str(cursor.rowcount))

def create_person(name, address):
    db = pymysql.connect(host, user, password, user)
    db.autocommit(True)
    cursor = db.cursor()
    
    cursor.execute("INSERT INTO person (navn,adresse) VALUES(%s,%s)", (name, address))
            
    db.close()
    
    # Vi logger resultatet til konsollet
    print("create_person count: " + str(cursor.rowcount))
    