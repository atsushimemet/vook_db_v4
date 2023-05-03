CREATE TABLE `line` (
  `line_id` int NOT NULL AUTO_INCREMENT,
  `line_name` varchar(100) NOT NULL,
  `brand_id` int NOT NULL,
  `item_id` int NOT NULL,
  PRIMARY KEY (`line_id`),
  FOREIGN KEY (`brand_id`) REFERENCES brands(`brand_id`),
  FOREIGN KEY (`item_id`) REFERENCES items(`item_id`)
);
