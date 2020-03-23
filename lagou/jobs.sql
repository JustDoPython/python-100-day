CREATE TABLE `jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `positionName` varchar(45) DEFAULT NULL,
  `workYear` varchar(45) DEFAULT NULL,
  `salary` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `education` varchar(100) DEFAULT NULL,
  `positionAdvantage` varchar(100) DEFAULT NULL,
  `companyLabelList` varchar(100) DEFAULT NULL,
  `financeStage` varchar(45) DEFAULT NULL,
  `companySize` varchar(45) DEFAULT NULL,
  `industryField` varchar(100) DEFAULT NULL,
  `firstType` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) 
