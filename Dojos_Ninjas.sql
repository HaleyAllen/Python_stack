-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojos_ninjas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojos_ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojos_ninjas` DEFAULT CHARACTER SET utf8 ;
USE `dojos_ninjas` ;

-- -----------------------------------------------------
-- Table `dojos_ninjas`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas`.`dojos` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojos_ninjas`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojos_ninjas`.`ninjas` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL DEFAULT now(),
  `updated_at` DATETIME NULL DEFAULT now() on update now(),
  `dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ninjas_dojo_idx` (`dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_ninjas_dojo`
    FOREIGN KEY (`dojo_id`)
    REFERENCES `dojos_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SELECT * FROM dojos;

INSERT INTO `dojos_ninjas`.`dojos` (`id`, `name`) VALUES ('1', 'coding_dojo');
INSERT INTO `dojos_ninjas`.`dojos` (`id`, `name`) VALUES ('2', 'fun_dojo');
INSERT INTO `dojos_ninjas`.`dojos` (`id`, `name`) VALUES ('3', 'dojo');

DELETE FROM `dojos_ninjas`.`dojos` WHERE (`id` = '1');
DELETE FROM `dojos_ninjas`.`dojos` WHERE (`id` = '2');
DELETE FROM `dojos_ninjas`.`dojos` WHERE (`id` = '3');

INSERT INTO `dojos_ninjas`.`dojos` (`id`, `name`) VALUES ('4', 'Dojo_One');
INSERT INTO `dojos_ninjas`.`dojos` (`id`, `name`) VALUES ('5', 'Dojo_Two');
INSERT INTO `dojos_ninjas`.`dojos` (`id`, `name`) VALUES ('6', 'Dojo_Three');

INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('1', 'Patch', 'Allen', '10','4');
INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('2', 'Pumpkin', 'Allen', '2','4');
INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('3', 'Max', 'Allen', '1','4');

INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('4', 'Shanda', 'Hamilton', '31','5');
INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('5', 'Larissa', 'Roberts', '30','5');
INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('6', 'Ellen', 'Roberts', '25','5');

INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('7', 'Christian', 'Allen', '25','6');
INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('8', 'Fred', 'Roberts', '56','6');
INSERT INTO `dojos_ninjas`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `dojo_id`) VALUES ('9', 'Lila', 'Roberts', '52','6');

SELECT * FROM `ninjas` WHERE dojo_id = 4;
SELECT * FROM `ninjas` WHERE dojo_id = 6;
SELECT id=4 FROM `dojos`;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
