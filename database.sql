-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: usds
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'s12','123456'),(2,'S12345','123456'),(3,'s13','123345'),(4,'S124356','1234567'),(5,'S134223213','1234567'),(6,'s13','123456');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contractor`
--

DROP TABLE IF EXISTS `contractor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contractor` (
  `c_id` int NOT NULL AUTO_INCREMENT,
  `contractor_id` varchar(50) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`c_id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `contractor_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `vehicleowner` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contractor`
--

LOCK TABLES `contractor` WRITE;
/*!40000 ALTER TABLE `contractor` DISABLE KEYS */;
INSERT INTO `contractor` VALUES (1,'C43434','Cook','Cengal Cafe',3);
/*!40000 ALTER TABLE `contractor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `history`
--

DROP TABLE IF EXISTS `history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history` (
  `history_id` int NOT NULL AUTO_INCREMENT,
  `sticker_id` int DEFAULT NULL,
  `vehicle_name` varchar(100) DEFAULT NULL,
  `vehicle_no` varchar(45) DEFAULT NULL,
  `serial_no` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `owner_type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `sticker_id_idx` (`sticker_id`),
  CONSTRAINT `sticker_id` FOREIGN KEY (`sticker_id`) REFERENCES `sticker` (`sticker_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history`
--

LOCK TABLES `history` WRITE;
/*!40000 ALTER TABLE `history` DISABLE KEYS */;
INSERT INTO `history` VALUES (5,4,'Honda Civic','WNE3742',9901,'2022-07-13','07:10:20','valid','contractor'),(9,2,'Rolls Royce','NCG1234',249,'2022-07-13','07:50:37','valid','staff'),(10,1,'Perodua Kembara','BGC3038',1826,'2022-07-13','07:52:58','valid','student'),(11,2,'Rolls Royce','NCG1234',249,'2022-07-13','08:34:33','valid','staff'),(12,2,'Rolls Royce','NCG1234',249,'2022-07-13','08:36:49','valid','staff'),(13,2,'Rolls Royce','NCG1234',249,'2022-07-13','08:38:20','valid','staff'),(14,1,'Perodua Kembara','BGC3038',1826,'2022-07-13','09:10:51','valid','student'),(15,1,'Perodua Kembara','BGC3038',1826,'2022-07-13','09:43:50','valid','student');
/*!40000 ALTER TABLE `history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `staff` (
  `s_id` int NOT NULL AUTO_INCREMENT,
  `staff_id` varchar(50) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`s_id`),
  KEY `owner_id_idx` (`owner_id`),
  CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `vehicleowner` (`owner_id`),
  CONSTRAINT `staff_ibfk_2` FOREIGN KEY (`owner_id`) REFERENCES `vehicleowner` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES (1,'S13455','Lecturer','FC',2);
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sticker`
--

DROP TABLE IF EXISTS `sticker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sticker` (
  `sticker_id` int NOT NULL AUTO_INCREMENT,
  `expiration_date` date DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  `sticker_color` varchar(100) DEFAULT NULL,
  `serial_key` int DEFAULT NULL,
  `vehicle_id` int DEFAULT NULL,
  PRIMARY KEY (`sticker_id`),
  KEY `vehicle_id` (`vehicle_id`),
  CONSTRAINT `sticker_ibfk_1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle` (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sticker`
--

LOCK TABLES `sticker` WRITE;
/*!40000 ALTER TABLE `sticker` DISABLE KEYS */;
INSERT INTO `sticker` VALUES (1,'2022-09-01','valid','red',1826,1),(2,'2022-07-01','valid','blue',249,2),(3,'2022-05-01','invalid','blue',8757,3),(4,'2023-09-02','valid','orange',9901,4),(5,'2022-09-09','valid','blue',8745,5);
/*!40000 ALTER TABLE `sticker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `st_id` int NOT NULL AUTO_INCREMENT,
  `college` varchar(100) DEFAULT NULL,
  `matric_id` varchar(100) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `owner_id` int DEFAULT NULL,
  PRIMARY KEY (`st_id`),
  KEY `oid_idx` (`owner_id`),
  CONSTRAINT `owner_id` FOREIGN KEY (`owner_id`) REFERENCES `vehicleowner` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'KTHO','A18CS0069',4,1),(3,'KTDI','A18CS0069',4,5),(6,'KTHO','18CS0099',4,14),(7,'KTHO','A18CS0067',4,15);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `vehicle_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_color` varchar(100) DEFAULT NULL,
  `vehicle_no` varchar(100) DEFAULT NULL,
  `vehicle_name` varchar(100) DEFAULT NULL,
  `owner_id` int NOT NULL,
  PRIMARY KEY (`vehicle_id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `vehicle_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `vehicleowner` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES (1,'Grey','BGC3038','Perodua Kembara',1),(2,'White','NCG1234','Rolls Royce',4),(3,'Red','AME4567','Perodua Myvi',2),(4,'Blue','WNE3742','Honda Civic',3),(5,'Black','ABG1234','Myvi',5);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicleowner`
--

DROP TABLE IF EXISTS `vehicleowner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicleowner` (
  `owner_id` int NOT NULL AUTO_INCREMENT,
  `owner_name` varchar(50) DEFAULT NULL,
  `owner_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicleowner`
--

LOCK TABLES `vehicleowner` WRITE;
/*!40000 ALTER TABLE `vehicleowner` DISABLE KEYS */;
INSERT INTO `vehicleowner` VALUES (1,'Haiswin Raj','student'),(2,'Ali','staff'),(3,'James Bond','contractor'),(4,'Tom Cruise','staff'),(5,'Amiza','student'),(14,'Tom','student'),(15,'Rowen','student');
/*!40000 ALTER TABLE `vehicleowner` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-27  8:16:59
