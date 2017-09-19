# simple-python-gui-app

Dette er en enkel Python-applikasjon som bruker
* *tkinter* for å lage et enkelt gui
* *pymysql* for å kontakte en enkel database
* *matplotlib* for å lage et enkelt histogram

Applikasjonen er ikke objektorientert

Databasen kan opprettes med følgende skript:

```sql
CREATE TABLE IF NOT EXISTS `person` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `navn` varchar(256) NOT NULL,
    `adresse` varchar(256) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4;

INSERT INTO `person` (`id`, `navn`, `adresse`) VALUES
    (1, 'Nils Tesdal', 'Byen'),
    (2, 'Hei Sveisen', 'Byen'),
    (3, 'Bjørn Bjørnsen', 'Skogen');
```
