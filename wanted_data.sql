-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: wanted
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid_companies_name_1b02af` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'2024-08-13 07:13:56.183128','2024-08-13 07:13:56.183146','원티드랩'),(2,'2024-08-13 07:19:03.559116','2024-08-13 07:19:03.559202','스피링크'),(3,'2024-08-13 07:22:06.821827','2024-08-13 07:22:06.822542','주식회사 링크드코리아');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_languages`
--

DROP TABLE IF EXISTS `company_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_languages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `name` varchar(255) NOT NULL,
  `company_id` bigint NOT NULL,
  `language_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_company__companie_b4836631` (`company_id`),
  KEY `fk_company__language_dc702b72` (`language_id`),
  CONSTRAINT `fk_company__companie_b4836631` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_company__language_dc702b72` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_languages`
--

LOCK TABLES `company_languages` WRITE;
/*!40000 ALTER TABLE `company_languages` DISABLE KEYS */;
INSERT INTO `company_languages` VALUES (1,'2024-08-13 07:13:56.214031','2024-08-13 07:13:56.214047','원티드랩',1,1),(2,'2024-08-13 07:13:56.214063','2024-08-13 07:13:56.214070','Wantedlab',1,2),(3,'2024-08-13 07:13:56.214080','2024-08-13 07:13:56.214085','Wantedlab',1,3),(4,'2024-08-13 07:19:03.564812','2024-08-13 07:19:03.564822','스피링크',2,1),(5,'2024-08-13 07:19:03.564857','2024-08-13 07:19:03.564863','Speelink',2,2),(6,'2024-08-13 07:19:03.564872','2024-08-13 07:19:03.564877','Speelink',2,3),(7,'2024-08-13 07:22:06.853237','2024-08-13 07:22:06.853249','주식회사 링크드코리아',3,1),(8,'2024-08-13 07:22:06.853278','2024-08-13 07:22:06.853284','LinkedKorea',3,2);
/*!40000 ALTER TABLE `company_languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company_tags`
--

DROP TABLE IF EXISTS `company_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `company_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_company__companie_7de0ae1e` (`company_id`),
  KEY `fk_company__tags_dfab8f09` (`tag_id`),
  CONSTRAINT `fk_company__companie_7de0ae1e` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_company__tags_dfab8f09` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_tags`
--

LOCK TABLES `company_tags` WRITE;
/*!40000 ALTER TABLE `company_tags` DISABLE KEYS */;
INSERT INTO `company_tags` VALUES (1,'2024-08-13 07:13:56.249633','2024-08-13 07:13:56.249645',1,1),(2,'2024-08-13 07:19:03.567859','2024-08-13 07:19:03.567869',2,2),(3,'2024-08-13 07:19:03.577728','2024-08-13 07:19:03.577739',2,1),(4,'2024-08-13 07:22:06.860865','2024-08-13 07:22:06.860880',3,3),(5,'2024-08-13 07:22:06.868070','2024-08-13 07:22:06.868081',3,4);
/*!40000 ALTER TABLE `company_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `languages`
--

DROP TABLE IF EXISTS `languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `languages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `languages`
--

LOCK TABLES `languages` WRITE;
/*!40000 ALTER TABLE `languages` DISABLE KEYS */;
INSERT INTO `languages` VALUES (1,'2024-08-13 16:13:45.483629','2024-08-13 07:22:06.869261','ko'),(2,'2024-08-13 16:13:45.498786','2024-08-13 07:22:06.872185','en'),(3,'2024-08-13 16:13:45.499333','2024-08-13 07:19:03.601372','tw');
/*!40000 ALTER TABLE `languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag_languages`
--

DROP TABLE IF EXISTS `tag_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag_languages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `name` varchar(255) NOT NULL,
  `language_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tag_lang_language_e8cf17fa` (`language_id`),
  KEY `fk_tag_lang_tags_4cb4dbd1` (`tag_id`),
  CONSTRAINT `fk_tag_lang_language_e8cf17fa` FOREIGN KEY (`language_id`) REFERENCES `languages` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_tag_lang_tags_4cb4dbd1` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag_languages`
--

LOCK TABLES `tag_languages` WRITE;
/*!40000 ALTER TABLE `tag_languages` DISABLE KEYS */;
INSERT INTO `tag_languages` VALUES (1,'2024-08-13 07:13:56.285321','2024-08-13 07:19:03.597397','인원 급성장',1,1),(2,'2024-08-13 07:13:56.288351','2024-08-13 07:19:03.600458','rapid growthing',2,1),(3,'2024-08-13 07:13:56.290312','2024-08-13 07:19:03.602471','rapid growthing',3,1),(4,'2024-08-13 07:19:03.571711','2024-08-13 07:19:03.571724','재택근무',1,2),(5,'2024-08-13 07:19:03.573862','2024-08-13 07:19:03.573873','remote working',2,2),(6,'2024-08-13 07:19:03.575784','2024-08-13 07:19:03.575799','remote working',3,2),(7,'2024-08-13 07:22:06.863210','2024-08-13 07:22:06.863222','아기유니콘',1,3),(8,'2024-08-13 07:22:06.866800','2024-08-13 07:22:06.866812','baby unicorn',2,3),(9,'2024-08-13 07:22:06.871059','2024-08-13 07:22:06.871073','보너스',1,4),(10,'2024-08-13 07:22:06.873291','2024-08-13 07:22:06.873310','bonus',2,4);
/*!40000 ALTER TABLE `tag_languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `updated_at` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
INSERT INTO `tags` VALUES (1,'2024-08-13 07:13:56.248102','2024-08-13 07:19:03.576983','인원 급성장'),(2,'2024-08-13 07:19:03.567372','2024-08-13 07:19:03.567395','재택근무'),(3,'2024-08-13 07:22:06.854753','2024-08-13 07:22:06.855295','아기유니콘'),(4,'2024-08-13 07:22:06.867717','2024-08-13 07:22:06.867728','보너스');
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-13 16:22:59
