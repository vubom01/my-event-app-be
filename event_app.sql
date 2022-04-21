-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: my_event_app
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

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
-- Table structure for table `event_images`
--

DROP TABLE IF EXISTS `event_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `event_images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_id` int NOT NULL,
  `image` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_image_event_idx` (`event_id`),
  CONSTRAINT `fk_image_event` FOREIGN KEY (`event_id`) REFERENCES `events` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event_images`
--

LOCK TABLES `event_images` WRITE;
/*!40000 ALTER TABLE `event_images` DISABLE KEYS */;
INSERT INTO `event_images` VALUES (1,2,'string','2022-03-28 14:51:44','2022-03-28 14:51:44'),(2,3,'string','2022-03-28 14:51:46','2022-03-28 14:51:46'),(3,4,'string','2022-03-28 14:51:47','2022-03-28 14:51:47'),(4,5,'string','2022-03-28 14:51:48','2022-03-28 14:51:48'),(5,6,'string','2022-03-28 14:52:03','2022-03-28 14:52:03'),(6,7,'string','2022-04-21 21:41:58','2022-04-21 21:41:58'),(7,8,'string','2022-04-21 21:42:21','2022-04-21 21:42:21');
/*!40000 ALTER TABLE `event_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `host_id` varchar(255) NOT NULL,
  `topic` longtext NOT NULL,
  `event_name` varchar(255) NOT NULL,
  `start_at` datetime NOT NULL,
  `end_at` datetime DEFAULT NULL,
  `description` longtext,
  `status` int NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `lat` float DEFAULT NULL,
  `long` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_host_event_idx` (`host_id`),
  CONSTRAINT `fk_host_event` FOREIGN KEY (`host_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'RHYF3WCZAWCTT','string','string','2022-03-28 14:51:15','2022-03-28 14:51:15','string',0,'2022-03-28 14:51:18','2022-03-28 14:51:18',0,0),(2,'RHYF3WCZAWCTT','string','string','2022-03-28 14:51:15','2022-03-28 14:51:15','string',0,'2022-03-28 14:51:44','2022-04-22 04:39:32',0,0),(3,'RHYF3WCZAWCTT','string','string','2022-03-28 14:51:15','2022-03-28 14:51:15','string',1,'2022-03-28 14:51:46','2022-04-22 00:18:52',0,0),(4,'RHYF3WCZAWCTT','string','string','2022-03-28 14:51:15','2022-03-28 14:51:15','string',0,'2022-03-28 14:51:47','2022-03-28 14:51:47',0,0),(5,'RHYF3WCZAWCTT','string','string','2022-03-28 14:51:15','2022-03-28 14:51:15','string',0,'2022-03-28 14:51:48','2022-03-28 14:51:48',0,0),(6,'RHYF3WCZAWCTT','string','string','2022-03-28 14:51:15','2022-03-28 14:51:15','string',0,'2022-03-28 14:52:03','2022-03-28 14:52:03',0,0),(7,'BZCREAQZ95SM5','string','string','2022-04-21 21:12:07','2022-04-21 21:12:07','string',0,'2022-04-21 21:41:58','2022-04-21 21:41:58',0,0),(8,'RHYF3WCZAWCTT','string','string','2022-04-21 21:42:19','2022-04-21 21:42:19','string',0,'2022-04-21 21:42:21','2022-04-21 21:42:21',0,0);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `friends` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) NOT NULL,
  `friend_id` varchar(255) NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_user_friend_idx` (`user_id`),
  CONSTRAINT `fk_user_friend` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
INSERT INTO `friends` VALUES (7,'RHYF3WCZAWCTT','UPLYFFHSRB3IZ',1,'2022-03-28 15:24:25','2022-04-04 15:04:32'),(9,'RHYF3WCZAWCTT','BZCREAQZ95SM5',1,'2022-04-04 15:10:16','2022-04-04 15:28:14'),(11,'UPLYFFHSRB3IZ','RHYF3WCZAWCTT',1,'2022-04-04 15:17:31','2022-04-04 15:17:31'),(12,'BZCREAQZ95SM5','RHYF3WCZAWCTT',1,'2022-04-04 15:28:14','2022-04-04 15:28:14');
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `like_events`
--

DROP TABLE IF EXISTS `like_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_id` int NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_events`
--

LOCK TABLES `like_events` WRITE;
/*!40000 ALTER TABLE `like_events` DISABLE KEYS */;
INSERT INTO `like_events` VALUES (8,6,'RHYF3WCZAWCTT','2022-04-21 16:48:29','2022-04-21 23:48:29'),(10,3,'BZCREAQZ95SM5','2022-04-21 17:44:04','2022-04-22 00:44:04');
/*!40000 ALTER TABLE `like_events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_event_status`
--

DROP TABLE IF EXISTS `user_event_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_event_status` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event_id` int NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `status` int NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_event_status`
--

LOCK TABLES `user_event_status` WRITE;
/*!40000 ALTER TABLE `user_event_status` DISABLE KEYS */;
INSERT INTO `user_event_status` VALUES (9,2,'BZCREAQZ95SM5',1,'2022-04-21 17:58:47','2022-04-22 01:10:15'),(16,3,'BZCREAQZ95SM5',1,'2022-04-21 21:36:24','2022-04-22 04:36:24');
/*!40000 ALTER TABLE `user_event_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `avatar` varchar(255) DEFAULT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('BZCREAQZ95SM5','string2','$2b$12$thwvWjF2mfWv7LapTIaaJ.D6G4luIaIUPk33QsOt6xFc55va1K7wy','string','string','string2','string','2022-04-04 08:06:54','2022-04-04 15:06:54','string','string','2022-04-04'),('RHYF3WCZAWCTT','string','$2b$12$pa7tOOdMuuQ/ub/litfMQ.D1ivf1.EkeFHbBWrtxgfIfKvKA4AEUW','string1','string','string','string','2022-03-28 07:49:25','2022-03-28 14:50:37','asd','string','2022-03-28'),('UPLYFFHSRB3IZ','string1','$2b$12$TzBEbEiB4uHDZPBKMgPdCu2pYY/vXygeWK6j/rnk5EFOZUsfcWh9O','string','string','asd','string','2022-03-28 08:19:53','2022-03-28 15:19:53','string','string','2022-03-28');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-22  4:55:26
