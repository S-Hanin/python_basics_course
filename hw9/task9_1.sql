create database if not exists artezio_hw9;
use artezio_hw9;

CREATE TABLE IF NOT EXISTS `staff` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `salary` decimal(10,2) unsigned NOT NULL,
  `position` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO staff (first_name, last_name, salary, position) VALUES ("Артем", "Дзюба", 25000, "менеджер по продажам");
INSERT INTO staff (first_name, last_name, salary, position) VALUES ("Игорь", "Акинфеев", 25000, "менеджер по продажам");
INSERT INTO staff (first_name, last_name, salary, position) VALUES ("Павел", "Крашенинников", 30000, "менеджер по продажам");
INSERT INTO staff (first_name, last_name, salary, position) VALUES ("Антон", "Михайленко", 50000, "руководитель отдела продаж");
INSERT INTO staff (first_name, last_name, salary, position) VALUES ("Мария", "Васина", 20000, "офисменеджер");



SELECT * FROM staff WHERE salary < 30000;
SELECT * FROM staff WHERE position = "менеджер по продажам" AND salary < 30000;


CREATE TABLE `staff_rel` (
  `chief_id` int(10) unsigned NOT NULL,
  `employee_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`chief_id`,`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO staff_rel (chief_id, employee_id) VALUES (4, 1), (4, 2), (4, 3);


SELECT s.first_name, s.last_name, s.salary, s.position FROM staff s
INNER JOIN staff_rel sr ON s.id=sr.employee_id
WHERE sr.chief_id = (SELECT id FROM staff WHERE position="руководитель отдела продаж");