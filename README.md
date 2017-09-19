# simple-python-gui-app

Dette er en enkel Python-applikasjon som bruker bibliotekene
* *tkinter* for å lage et enkelt gui
* *pymysql* for å kontakte en enkel database
* *matplotlib* for å lage et enkelt histogram

Applikasjonen er ikke objektorientert

Databasen kan opprettes med følgende skript:

```sql
CREATE TABLE IF NOT EXISTS `person` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `navn` varchar(256) NOT NULL,
    `alder` int(3) NULL,
    `adresse` varchar(256) NOT NULL,
    `bilde_base64` longtext NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4;

INSERT INTO `person` (`navn`, `adresse`, `alder`) VALUES
    ('Super Supersen', 'Byen', 50),
    ('Hei Sveisen', 'Byen', 43),
    ('Bjørn Bjørnsen', 'Skogen', 21);
```
Brukernavn og passord til databasen må settes øverst i *person_db.py*.

Kjør *person_main.py* for å starte applikasjonen.
