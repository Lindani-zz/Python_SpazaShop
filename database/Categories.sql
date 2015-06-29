DROP TABLE IF EXISTS `Categories`;

CREATE TABLE `Categories`
(
	`Id` int NOT NULL auto_increment primary key,
	`Name` char (100) not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `Categories` WRITE;
INSERT INTO `Categories`(Diary, Bakery, CanFood, Beverages, Starch, Toiletries, Fruits, Candy, Extras)
VALUES('Milk 1l', 'Imasi'),('Bread'),('Chakalaka Can','Gold Dish Vegetable Curry Can'),('Fanta 500ml','Coke 500ml','Cream Soda 500ml'),('Iwisa Pap 5kg'),('Top Class Soy Mince'),('Shampoo 1 litre','Soap Bar'),('Bananas - loose','Apples - loose'),('Mixed Sweets 5s','Heart Chocolates');('Rose (plastic)','Valentine Cards');
UNLOCK TABLES;
