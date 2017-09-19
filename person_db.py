import pymysql

host = "mysql.stud.iie.ntnu.no"
user = "" # Skriv inn brukernavnet ditt her
password = "" # Skriv inn passordet ditt her

# Søk på personer, gitt navn og adresse
def search(name, adress):
    db = pymysql.connect(host, user, password, user)
    cursor = db.cursor()
    
    # Logger inputdata til konsollet
    print("search: name=" + name + ", adresse=" + adress)

    # PS! Vi henter IKKE bildet nå da det er for stort til å ha i en liste
    cursor.execute("SELECT id,navn,adresse,alder FROM person WHERE navn LIKE %s AND adresse LIKE %s", ("%"+name+"%", "%"+adress+"%"))
    
    result = []
    for row in cursor:
        person = []
        person.append(row[0]) # id
        person.append(row[1]) # navn
        person.append(row[2]) # adresse
        person.append(row[3]) # alder
        result.append(person)
        
    db.close()
    
    # Logger antall rader funnet til konsollet
    print("search: rowcount=" + str(len(result)))
    
    return result

# Hent alle adresser og antall som bor på hver av dem som to lister
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

    # Logger antall rader funnet til konsollet
    print("get_adress_counts: rowcount=" + str(len(adresses)))   

    return counts, adresses
 
# Hent alle aldre
def get_ages():
    db = pymysql.connect(host, user, password, user)
    cursor = db.cursor()    
    cursor.execute("SELECT alder FROM person")
    
    ages = []
    for row in cursor:
        ages.append(row[0])
         
    db.close()

    # Logger antall rader funnet til konsollet
    print("get_ages: rowcount=" + str(len(ages)))   

    return ages
  
# Slett person med gitt id
def delete_person(id):
    db = pymysql.connect(host, user, password, user)
    db.autocommit(True)
    cursor = db.cursor()    
    cursor.execute("DELETE FROM person WHERE id=%s", (id))            
    db.close()
    
    # Logger resultatet til konsollet
    print("delete_person: rowcount=" + str(cursor.rowcount))   
   
# Hent kun bilde for en person, kodet som en base64-streng
def get_image_base64(id):
    db = pymysql.connect(host, user, password, user)
    cursor = db.cursor()   
    cursor.execute("SELECT bilde_base64 FROM person WHERE id=%s", (id))    
    image_base64 = cursor.fetchone()[0]        
    db.close()
    
    # Logger resultatet til konsollet
    if image_base64:
        print("get_image_base64: image size=" + str(len(image_base64)))
    else:
        print("get_image_base64: no image found")
            
    return image_base64
    
# Oppdater en personsom allerede eksisterer i databasen
def update_person(id, name, address, age, image_base64):
    db = pymysql.connect(host, user, password, user)
    db.autocommit(True)
    cursor = db.cursor()    
    cursor.execute("UPDATE person SET navn=%s, adresse=%s, alder=%s, bilde_base64=%s WHERE id=%s", (name, address, age, image_base64, id))            
    db.close()
    
    # Logger resultatet til konsollet
    print("update_person: rowcount=" + str(cursor.rowcount))

# Lagre en person som ikke finnes i database fra før
def create_person(name, address, age, image_base64):
    db = pymysql.connect(host, user, password, user)
    db.autocommit(True)
    cursor = db.cursor()    
    cursor.execute("INSERT INTO person (navn,adresse,alder,bilde_base64) VALUES(%s,%s,%s,%s)", (name, address, age, image_base64))            
    db.close()
    
    # Logger resultatet til konsollet
    print("create_person: rowcount=" + str(cursor.rowcount))
    