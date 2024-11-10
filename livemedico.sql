-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: livemedico
-- ------------------------------------------------------
-- Server version	8.0.38

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
  `admin_username` varchar(45) NOT NULL,
  `admin_password` varchar(90) NOT NULL,
  PRIMARY KEY (`admin_username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('admin','$2a$10$SZodLcS7YFa4vcvcmFoeOubJI9GOos/nlYdQY29X0UC4ubr6D1WWK');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int NOT NULL,
  `doctor_id` int NOT NULL,
  `patient_name` varchar(45) NOT NULL,
  `patient_age` int NOT NULL,
  `appointment_date` date NOT NULL,
  `appointment_time` varchar(45) NOT NULL,
  `appointment_mode` varchar(45) NOT NULL,
  `appointment_payment` varchar(45) NOT NULL,
  `doctor_name` varchar(45) NOT NULL,
  PRIMARY KEY (`appointment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
INSERT INTO `appointment` VALUES (1,1,1,'navi',22,'2024-11-23','10:00 AM - 12:30 PM','offline','upi','arun'),(2,1,2,'aswin',33,'2024-11-15','2:00 PM - 5:00 PM','online','upi','nevin'),(3,1,2,'sajin',22,'2024-11-15','10:00 AM - 12:30 PM','offline','upi','nevin'),(4,1,2,'sajin',20,'2024-11-11','2:00 PM - 5:00 PM','offline','upi','nevin'),(5,1,3,'sajin',21,'2024-11-29','10:00 AM - 12:30 PM','online','upi','Dr. Anjali Suresh');
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `doctor_name` varchar(45) NOT NULL,
  `doctor_speciality` varchar(45) NOT NULL,
  `doctor_experience` int NOT NULL,
  `doctor_username` varchar(45) NOT NULL,
  `doctor_password` varchar(100) NOT NULL,
  `doctor_city` varchar(45) NOT NULL,
  PRIMARY KEY (`doctor_id`),
  UNIQUE KEY `doctor_username_UNIQUE` (`doctor_username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (3,'Dr. Anjali Suresh','Pediatrics',6,'anjalisuresh100','$2b$12$yHVtOaPbm5or1SYUmBzj7WrIS1mr3TXxxgy0zm43eNEoSP3v0Iu1S','Kottayam'),(4,'Dr. Vinu Prakash','Cardiology',12,'vinuprakash150','$2b$12$XlAi8Rmk4mOcbTx0nO5YrJkRuoe6g0yyP2x5TISzHlXEV2Vgxa4p6','Thrissur'),(5,'Dr. Neena Raj','Neurology',10,'neenraj1000','$2b$12$4CzI6rFtoU65BxnTP6Rj.kEKbpGH3XzMjwEL7IMJgG5RoaIsBwObK','Ernakulam'),(6,'Dr. Vishnu Das','Orthopedics',14,'vishnudas400','$2b$12$WbWxjTSktwEhrl7vKl1Q2oSdrQDx7sdx7t2mn9n7Ucd/2QLXyXlV8','Pathanamthitta'),(7,'Dr. Sreelatha Nair','Dermatology',8,'sreelathanair250','$2b$12$k5AYhvjwMJhzxCKo5.AoLUtnUrHO3Pau0LRJ76YypEZWcx71FzV0C','Palakkad'),(8,'Dr. Ravi Kumar','General Surgery',20,'ravikumar500','$2b$12$5f8t7y2nBOuIGuSzADHR8TtUSwPR0A3XIz3wPzskVtCvGF67YvcB0','Kannur'),(9,'Dr. Shruti Varma','Obstetrics',4,'shrutivarma22','$2b$12$CgZ6eZmQSbi8kKYElpaRBiSk9EHW1NeHlR4AqwhP2HeI9eZnxxZf.','Kozhikode'),(11,'Dr. Priya Kumar','Anesthesiology',13,'priyakumar789','$2b$12$nbZQycuQWlCpAq2U6tT5Xz5Wf.JwX7wp5JZ9/qSIV3zD0P.TZ6hPi','Alappuzha'),(12,'Dr. Manu Jacob','Gastroenterology',11,'manujacob312','$2b$12$ti2DNhMczjs5LxRl/TpywWrk4Gj7cxyx/2wggYk6O4rwpTwABYhOa','Trivandrum');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `patient_name` varchar(45) NOT NULL,
  `patients_username` varchar(45) NOT NULL,
  `patient_email` varchar(45) NOT NULL,
  `patient_password` varchar(100) NOT NULL,
  `patient_dob` date NOT NULL,
  `patient_cn` varchar(45) NOT NULL,
  `patient_city` varchar(45) NOT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `patients_username_UNIQUE` (`patients_username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'navaneeth','navi','navi@gmail.com','$2b$12$dbxhfC6t1CQDVRAADOzBz.qx6t6jSkEqTwyzDgXoZquPlfojnf/m2','2024-11-01','88888','kottayam');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-10 22:45:20
