CREATE TABLE `products` (
  `product_id` INT AUTO_INCREMENT,
  `product_name` VARCHAR(100) NOT NULL UNIQUE,
  `platform_id` INT NOT NULL,
  `ages_id` INT NOT NULL,
  `brand_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `line_id` INT NOT NULL,
  `price` INT NOT NULL,
  `info_get_date` DATETIME NOT NULL,
  `status` ENUM("S","A","B","C","D"),
  PRIMARY KEY (`product_id`),
  FOREIGN KEY (`platform_id`) REFERENCES platforms(`platform_id`),
  FOREIGN KEY (`ages_id`) REFERENCES ages(`ages_id`),
  FOREIGN KEY (`brand_id`) REFERENCES brands(`brand_id`),
  FOREIGN KEY (`item_id`) REFERENCES items(`item_id`),
  FOREIGN KEY (`line_id`) REFERENCES line(`line_id`)
);
