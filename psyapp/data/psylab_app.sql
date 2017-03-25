-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: psylab_app
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add grant',6,'add_grant'),(17,'Can change grant',6,'change_grant'),(18,'Can delete grant',6,'delete_grant'),(19,'Can add access token',7,'add_accesstoken'),(20,'Can change access token',7,'change_accesstoken'),(21,'Can delete access token',7,'delete_accesstoken'),(22,'Can add refresh token',8,'add_refreshtoken'),(23,'Can change refresh token',8,'change_refreshtoken'),(24,'Can delete refresh token',8,'delete_refreshtoken'),(25,'Can add application',9,'add_application'),(26,'Can change application',9,'change_application'),(27,'Can delete application',9,'delete_application'),(28,'Can add cors model',10,'add_corsmodel'),(29,'Can change cors model',10,'change_corsmodel'),(30,'Can delete cors model',10,'delete_corsmodel'),(31,'Can add user',11,'add_user'),(32,'Can change user',11,'change_user'),(33,'Can delete user',11,'delete_user'),(34,'Can add ticker',12,'add_ticker'),(35,'Can change ticker',12,'change_ticker'),(36,'Can delete ticker',12,'delete_ticker'),(37,'Can add strategy',13,'add_strategy'),(38,'Can change strategy',13,'change_strategy'),(39,'Can delete strategy',13,'delete_strategy'),(40,'Can add indicators',14,'add_indicators'),(41,'Can change indicators',14,'change_indicators'),(42,'Can delete indicators',14,'delete_indicators');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2017-03-23 11:11:38.203410','1','postman',1,'[{\"added\": {}}]',9,1),(2,'2017-03-23 12:05:11.002594','ICICI','Ticker object',1,'[{\"added\": {}}]',12,1),(3,'2017-03-23 12:05:15.134398','SBIN','Ticker object',1,'[{\"added\": {}}]',12,1),(4,'2017-03-23 12:05:21.365896','RELIANCE','Ticker object',1,'[{\"added\": {}}]',12,1),(5,'2017-03-23 13:13:26.164250','8','Strategy object',3,'',13,1),(6,'2017-03-23 13:13:26.205470','7','Strategy object',3,'',13,1),(7,'2017-03-23 13:13:26.294233','6','Strategy object',3,'',13,1),(8,'2017-03-23 13:13:26.383791','5','Strategy object',3,'',13,1),(9,'2017-03-23 13:13:26.428186','4','Strategy object',3,'',13,1),(10,'2017-03-23 13:13:26.472655','3','Strategy object',3,'',13,1),(11,'2017-03-23 13:13:26.517940','2','Strategy object',3,'',13,1),(12,'2017-03-23 13:13:26.562720','1','Strategy object',3,'',13,1),(13,'2017-03-23 14:51:51.983712','14','Strategy object',3,'',13,1),(14,'2017-03-23 14:51:52.033238','13','Strategy object',3,'',13,1),(15,'2017-03-23 14:51:52.072717','12','Strategy object',3,'',13,1),(16,'2017-03-23 14:51:52.144625','11','Strategy object',3,'',13,1),(17,'2017-03-23 14:51:52.223078','9','Strategy object',3,'',13,1),(18,'2017-03-23 15:13:15.873936','15','Strategy object',3,'',13,1),(19,'2017-03-25 09:01:45.277709','20','Strategy object',2,'[{\"changed\": {\"fields\": [\"strategy\"]}}]',13,1),(20,'2017-03-25 09:02:09.975693','18','Strategy object',2,'[{\"changed\": {\"fields\": [\"name\", \"strategy\"]}}]',13,1),(21,'2017-03-25 09:02:17.861424','18','Strategy object',2,'[{\"changed\": {\"fields\": [\"is_active\"]}}]',13,1),(22,'2017-03-25 09:02:28.523418','20','Strategy object',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',13,1),(23,'2017-03-25 09:09:51.967506','1','Rp7SpbNmGW8XI93NJfw5CsMXw6vdnL',2,'[{\"changed\": {\"fields\": [\"expires\"]}}]',7,1),(24,'2017-03-25 09:25:27.614568','1','postman',2,'[{\"changed\": {\"fields\": [\"client_type\"]}}]',9,1),(25,'2017-03-25 15:13:24.626654','SBIN','SBIN',3,'',12,1),(26,'2017-03-25 15:13:24.667943','RELIANCE','RELIANCE',3,'',12,1),(27,'2017-03-25 15:13:24.756750','ICICI','ICICI',3,'',12,1),(28,'2017-03-25 16:14:04.400036','asc','asc',1,'[{\"added\": {}}]',12,1),(29,'2017-03-25 17:47:04.309700','asc','asc',3,'',12,1),(30,'2017-03-25 17:50:06.345273','S','S',3,'',12,1),(31,'2017-03-25 17:50:06.404360','3','3',3,'',12,1),(32,'2017-03-25 17:50:06.471166','2','2',3,'',12,1),(33,'2017-03-25 18:36:46.326343','5','xPduIsgW7iXAWsGfoj6kGhKYwZ8g5z',3,'',7,1),(34,'2017-03-25 18:37:13.529190','6','plNlNk0IbRDUFQacPF8uZD3mpvqyc4',2,'[{\"changed\": {\"fields\": [\"expires\"]}}]',7,1),(35,'2017-03-25 18:39:41.345351','21','Strategy object',1,'[{\"added\": {}}]',13,1),(36,'2017-03-25 19:00:24.246325','1','Indicators object',1,'[{\"added\": {}}]',14,1),(37,'2017-03-25 19:00:47.353632','2','Indicators object',1,'[{\"added\": {}}]',14,1),(38,'2017-03-25 19:01:01.542248','3','Indicators object',1,'[{\"added\": {}}]',14,1),(39,'2017-03-25 19:01:19.270167','4','Indicators object',1,'[{\"added\": {}}]',14,1),(40,'2017-03-25 19:01:57.853671','3','sma',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(41,'2017-03-25 19:02:14.852313','2','ema',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(42,'2017-03-25 19:02:23.544224','4','rsi',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(43,'2017-03-25 19:02:30.178757','3','sma',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(44,'2017-03-25 19:02:59.160330','5','macd',1,'[{\"added\": {}}]',14,1),(45,'2017-03-25 19:03:39.872091','5','macd',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(46,'2017-03-25 19:04:08.978398','6','mfi',1,'[{\"added\": {}}]',14,1),(47,'2017-03-25 19:04:28.669784','7','obv',1,'[{\"added\": {}}]',14,1),(48,'2017-03-25 19:04:42.681161','8','roc',1,'[{\"added\": {}}]',14,1),(49,'2017-03-25 19:05:22.963998','9','stochastic',1,'[{\"added\": {}}]',14,1),(50,'2017-03-25 19:06:31.395486','10','high',1,'[{\"added\": {}}]',14,1),(51,'2017-03-25 19:06:36.918872','11','low',1,'[{\"added\": {}}]',14,1),(52,'2017-03-25 19:06:42.867963','12','open',1,'[{\"added\": {}}]',14,1),(53,'2017-03-25 19:06:47.212137','13','close',1,'[{\"added\": {}}]',14,1),(54,'2017-03-25 19:07:06.116666','14','volume',1,'[{\"added\": {}}]',14,1),(55,'2017-03-25 19:07:13.475878','15','oi',1,'[{\"added\": {}}]',14,1),(56,'2017-03-25 19:07:34.101608','11','low',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(57,'2017-03-25 19:07:40.399466','10','high',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,1),(58,'2017-03-25 19:09:05.876505','16','price',1,'[{\"added\": {}}]',14,1),(59,'2017-03-25 19:10:40.632374','17','bollinger',1,'[{\"added\": {}}]',14,1),(60,'2017-03-25 19:11:14.451839','17','lowerbb',2,'[{\"changed\": {\"fields\": [\"abbreviation\", \"name\"]}}]',14,1),(61,'2017-03-25 19:11:26.728007','18','upperbb',1,'[{\"added\": {}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(10,'corsheaders','corsmodel'),(7,'oauth2_provider','accesstoken'),(9,'oauth2_provider','application'),(6,'oauth2_provider','grant'),(8,'oauth2_provider','refreshtoken'),(14,'processor','indicators'),(13,'processor','strategy'),(12,'processor','ticker'),(5,'sessions','session'),(11,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-03-23 11:08:47.916441'),(2,'contenttypes','0002_remove_content_type_name','2017-03-23 11:08:49.239632'),(3,'auth','0001_initial','2017-03-23 11:08:53.768622'),(4,'auth','0002_alter_permission_name_max_length','2017-03-23 11:08:53.882789'),(5,'auth','0003_alter_user_email_max_length','2017-03-23 11:08:53.924289'),(6,'auth','0004_alter_user_username_opts','2017-03-23 11:08:53.983617'),(7,'auth','0005_alter_user_last_login_null','2017-03-23 11:08:54.035371'),(8,'auth','0006_require_contenttypes_0002','2017-03-23 11:08:54.084018'),(9,'auth','0007_alter_validators_add_error_messages','2017-03-23 11:08:54.136983'),(10,'auth','0008_alter_user_username_max_length','2017-03-23 11:08:54.183228'),(11,'users','0001_initial','2017-03-23 11:08:59.432937'),(12,'admin','0001_initial','2017-03-23 11:09:01.475205'),(13,'admin','0002_logentry_remove_auto_add','2017-03-23 11:09:01.653977'),(14,'oauth2_provider','0001_initial','2017-03-23 11:09:12.399593'),(15,'oauth2_provider','0002_08_updates','2017-03-23 11:09:17.201637'),(16,'oauth2_provider','0003_auto_20160316_1503','2017-03-23 11:09:19.354190'),(17,'oauth2_provider','0004_auto_20160525_1623','2017-03-23 11:09:20.978757'),(18,'sessions','0001_initial','2017-03-23 11:09:21.773782'),(19,'processor','0001_initial','2017-03-23 11:56:24.431314'),(20,'processor','0002_auto_20170323_1735','2017-03-23 12:05:47.415047'),(21,'processor','0003_auto_20170323_1847','2017-03-23 13:17:13.461982'),(22,'processor','0004_auto_20170323_1858','2017-03-23 13:28:26.603174'),(23,'processor','0005_strategy_name','2017-03-23 14:51:34.581687'),(24,'processor','0006_auto_20170323_2037','2017-03-23 15:07:35.297261'),(25,'processor','0007_auto_20170323_2042','2017-03-23 15:12:04.656921'),(26,'processor','0008_auto_20170323_2103','2017-03-23 15:33:49.807069'),(27,'processor','0009_indicators','2017-03-25 14:23:43.008022'),(28,'processor','0010_ticker_uin','2017-03-25 15:28:07.039739'),(29,'processor','0011_auto_20170326_0033','2017-03-25 19:03:30.945898');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7xenwvfn14ry3rr3dry06a2uzgj91yge','ZWViMDE4YWU4MmNmNzBjNmY0NTkzYjhiNWIyOWIwYzhkNTU5ZjJkODp7Il9hdXRoX3VzZXJfaGFzaCI6IjYyOGExYTk4YmU5NDE2YmIwMzRlNTQ0MzllNTRlYTVlYjA4M2ViZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-04-08 13:09:32.436037'),('m5lebstcmrrt3wo2wv2hpoq27t5onyws','ZWViMDE4YWU4MmNmNzBjNmY0NTkzYjhiNWIyOWIwYzhkNTU5ZjJkODp7Il9hdXRoX3VzZXJfaGFzaCI6IjYyOGExYTk4YmU5NDE2YmIwMzRlNTQ0MzllNTRlYTVlYjA4M2ViZmQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-04-08 09:01:23.297923');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_accesstoken`
--

DROP TABLE IF EXISTS `oauth2_provider_accesstoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_accesstoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_accesstoken_token_8af090f8_uniq` (`token`),
  KEY `oauth2_application_id_b22886e1_fk_oauth2_provider_application_id` (`application_id`),
  KEY `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_users_user_id` (`user_id`),
  CONSTRAINT `oauth2_application_id_b22886e1_fk_oauth2_provider_application_id` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_accesstoken_user_id_6e4c9a65_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_accesstoken`
--

LOCK TABLES `oauth2_provider_accesstoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` DISABLE KEYS */;
INSERT INTO `oauth2_provider_accesstoken` VALUES (3,'zoZnxMlVHS2pFubKkwymMn3IjjnXuf','2017-03-23 22:20:44.793303','read write',1,3);
/*!40000 ALTER TABLE `oauth2_provider_accesstoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_application`
--

DROP TABLE IF EXISTS `oauth2_provider_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_application` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` varchar(100) NOT NULL,
  `redirect_uris` longtext NOT NULL,
  `client_type` varchar(32) NOT NULL,
  `authorization_grant_type` varchar(32) NOT NULL,
  `client_secret` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `skip_authorization` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `oauth2_provider_application_9d667c2b` (`client_secret`),
  KEY `oauth2_provider_application_user_id_79829054_fk_users_user_id` (`user_id`),
  CONSTRAINT `oauth2_provider_application_user_id_79829054_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_application`
--

LOCK TABLES `oauth2_provider_application` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_application` DISABLE KEYS */;
INSERT INTO `oauth2_provider_application` VALUES (1,'yItGGTFT2aUwzgUYn9bKF2YSitqQLWqop0z0CazD','','public','client-credentials','AfNITyAtMWnGXL1SGJ3tRcY6Z1L6PJNRfwVL8KCXOXsx3An3E1CzbXsKORG50Uv9C1eFSzQ01yXggizZfVQq9vgUlcCuUZaQhp89FhCf6Wa3Qbl9OOes9ssC4VOs2Ly9','postman',NULL,0);
/*!40000 ALTER TABLE `oauth2_provider_application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_grant`
--

DROP TABLE IF EXISTS `oauth2_provider_grant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_grant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(255) NOT NULL,
  `expires` datetime(6) NOT NULL,
  `redirect_uri` varchar(255) NOT NULL,
  `scope` longtext NOT NULL,
  `application_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `oauth2_provider_grant_code_49ab4ddf_uniq` (`code`),
  KEY `oauth2_application_id_81923564_fk_oauth2_provider_application_id` (`application_id`),
  KEY `oauth2_provider_grant_user_id_e8f62af8_fk_users_user_id` (`user_id`),
  CONSTRAINT `oauth2_application_id_81923564_fk_oauth2_provider_application_id` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_grant_user_id_e8f62af8_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_grant`
--

LOCK TABLES `oauth2_provider_grant` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_grant` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_grant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oauth2_provider_refreshtoken`
--

DROP TABLE IF EXISTS `oauth2_provider_refreshtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oauth2_provider_refreshtoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(255) NOT NULL,
  `access_token_id` int(11) NOT NULL,
  `application_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `access_token_id` (`access_token_id`),
  UNIQUE KEY `oauth2_provider_refreshtoken_token_d090daa4_uniq` (`token`),
  KEY `oauth2_application_id_2d1c311b_fk_oauth2_provider_application_id` (`application_id`),
  KEY `oauth2_provider_refreshtoken_user_id_da837fce_fk_users_user_id` (`user_id`),
  CONSTRAINT `oauth2_application_id_2d1c311b_fk_oauth2_provider_application_id` FOREIGN KEY (`application_id`) REFERENCES `oauth2_provider_application` (`id`),
  CONSTRAINT `oauth2_provider_refreshtoken_user_id_da837fce_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `oauth_access_token_id_775e84e8_fk_oauth2_provider_accesstoken_id` FOREIGN KEY (`access_token_id`) REFERENCES `oauth2_provider_accesstoken` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oauth2_provider_refreshtoken`
--

LOCK TABLES `oauth2_provider_refreshtoken` WRITE;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `oauth2_provider_refreshtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processor_indicators`
--

DROP TABLE IF EXISTS `processor_indicators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `processor_indicators` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `abbreviation` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `abbreviation` (`abbreviation`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processor_indicators`
--

LOCK TABLES `processor_indicators` WRITE;
/*!40000 ALTER TABLE `processor_indicators` DISABLE KEYS */;
INSERT INTO `processor_indicators` VALUES (1,'adx','average directional index'),(2,'ema','exponential moving average'),(3,'sma','moving average'),(4,'rsi','relative strength index'),(5,'macd','Moving average convergence divergence'),(6,'mfi','money flow index'),(7,'obv','on balance volume'),(8,'roc','rate of change'),(9,'stochastic','stochastic oscillator'),(10,'high','highest price'),(11,'low','lowest price'),(12,'open','open price'),(13,'close','close price'),(14,'volume','volume'),(15,'oi','open interest'),(16,'price','current price'),(17,'lowerbb','lower bollinger band'),(18,'upperbb','upper bollinger band');
/*!40000 ALTER TABLE `processor_indicators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processor_strategy`
--

DROP TABLE IF EXISTS `processor_strategy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `processor_strategy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `strategy` varchar(999) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `ticker_id` varchar(20),
  `user_id` int(11),
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `processor_strategy_user_id_52c0b004_fk_users_user_id` (`user_id`),
  KEY `processor_strategy_ticker_id_ff28c846_fk_processor_ticker_symbol` (`ticker_id`),
  CONSTRAINT `processor_strategy_ticker_id_ff28c846_fk_processor_ticker_symbol` FOREIGN KEY (`ticker_id`) REFERENCES `processor_ticker` (`symbol`),
  CONSTRAINT `processor_strategy_user_id_52c0b004_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processor_strategy`
--

LOCK TABLES `processor_strategy` WRITE;
/*!40000 ALTER TABLE `processor_strategy` DISABLE KEYS */;
INSERT INTO `processor_strategy` VALUES (21,'10 days Moving Average of 14 days rsi crosses above 14 days RSI AND today open is higher than previous day close','2017-03-25 18:39:41.344415',1,'ICICIBANK',2,'kira');
/*!40000 ALTER TABLE `processor_strategy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `processor_ticker`
--

DROP TABLE IF EXISTS `processor_ticker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `processor_ticker` (
  `symbol` varchar(20) NOT NULL,
  `exchange` varchar(6) NOT NULL,
  `uin` varchar(20) NOT NULL,
  PRIMARY KEY (`symbol`),
  UNIQUE KEY `uin` (`uin`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `processor_ticker`
--

LOCK TABLES `processor_ticker` WRITE;
/*!40000 ALTER TABLE `processor_ticker` DISABLE KEYS */;
INSERT INTO `processor_ticker` VALUES ('20MICRONS','nse','INE144J01027'),('3IINFOTECH','nse','INE748C01020'),('3MINDIA','nse','INE470A01017'),('63MOONS','nse','INE111B01023'),('8KMILES','nse','INE650K01021'),('A2ZINFRA','nse','INE619I01012'),('AARTIDRUGS','nse','INE767A01016'),('AARTIIND','nse','INE769A01020'),('AARVEEDEN','nse','INE273D01019'),('ABAN','nse','INE421A01028'),('ABB','nse','INE117A01022'),('ABBOTINDIA','nse','INE358A01014'),('ABFRL','nse','INE647O01011'),('ABIRLANUVO','nse','INE069A01017'),('ACC','nse','INE012A01025'),('ACCELYA','nse','INE793A01012'),('ACE','nse','INE731H01025'),('ADANIENT','nse','INE423A01024'),('ADANIPORTS','nse','INE742F01042'),('ADANIPOWER','nse','INE814H01011'),('ADANITRANS','nse','INE931S01010'),('ADFFOODS','nse','INE982B01019'),('ADHUNIK','nse','INE400H01019'),('ADHUNIKIND','nse','INE452L01012'),('ADLABS','nse','INE172N01012'),('ADORWELD','nse','INE045A01017'),('ADVANIHOTR','nse','INE199C01026'),('ADVENZYMES','nse','INE837H01012'),('AEGISCHEM','nse','INE208C01025'),('AFL','nse','INE020G01017'),('AGCNET','nse','INE676A01019'),('AGRITECH','nse','INE449G01018'),('AHLEAST','nse','INE926K01017'),('AHLUCONT','nse','INE758C01029'),('AHLWEST','nse','INE915K01010'),('AIAENG','nse','INE212H01026'),('AIFL','nse','INE428O01016'),('AJANTPHARM','nse','INE031B01049'),('AJMERA','nse','INE298G01027'),('AKSHOPTFBR','nse','INE523B01011'),('AKZOINDIA','nse','INE133A01011'),('ALANKIT','nse','INE914E01040'),('ALBERTDAVD','nse','INE155C01010'),('ALBK','nse','INE428A01015'),('ALCHEM','nse','INE964B01033'),('ALEMBICLTD','nse','INE426A01027'),('ALICON','nse','INE062D01024'),('ALKALI','nse','INE773I01017'),('ALKEM','nse','INE540L01014'),('ALKYLAMINE','nse','INE150B01021'),('ALLCARGO','nse','INE418H01029'),('ALLSEC','nse','INE835G01018'),('ALMONDZ','nse','INE326B01027'),('ALOKTEXT','nse','INE270A01011'),('ALPHAGEO','nse','INE137C01018'),('ALPSINDUS','nse','INE093B01015'),('AMARAJABAT','nse','INE885A01032'),('AMBIKCO','nse','INE540G01014'),('AMBUJACEM','nse','INE079A01024'),('AMDIND','nse','INE005I01014'),('AMRUTANJAN','nse','INE098F01023'),('AMTEKAUTO','nse','INE130C01021'),('AMTL','nse','INE436N01029'),('ANANDAMRUB','nse','INE618N01014'),('ANANTRAJ','nse','INE242C01024'),('ANDHRABANK','nse','INE434A01013'),('ANDHRSUGAR','nse','INE715B01013'),('ANGIND','nse','INE017D01010'),('ANKITMETAL','nse','INE106I01010'),('ANSALAPI','nse','INE436A01026'),('ANSALHSG','nse','INE880B01015'),('APARINDS','nse','INE372A01015'),('APCOTEXIND','nse','INE116A01024'),('APLAPOLLO','nse','INE702C01019'),('APLLTD','nse','INE901L01018'),('APOLLOHOSP','nse','INE437A01024'),('APOLLOTYRE','nse','INE438A01022'),('APTECHT','nse','INE266F01018'),('ARCHIDPLY','nse','INE877I01016'),('ARCHIES','nse','INE731A01020'),('ARCOTECH','nse','INE574I01027'),('ARIES','nse','INE298I01015'),('ARMANFIN','nse','INE109C01017'),('AROGRANITE','nse','INE210C01013'),('ARROWGREEN','nse','INE570D01018'),('ARROWTEX','nse','INE933J01015'),('ARSSINFRA','nse','INE267I01010'),('ARVIND','nse','INE034A01011'),('ARVSMART','nse','INE034S01021'),('ASAHIINDIA','nse','INE439A01020'),('ASAHISONG','nse','INE228I01012'),('ASAL','nse','INE900C01027'),('ASHAPURMIN','nse','INE348A01023'),('ASHIANA','nse','INE365D01021'),('ASHIMASYN','nse','INE440A01010'),('ASHOKA','nse','INE442H01029'),('ASHOKLEY','nse','INE208A01029'),('ASIANHOTNR','nse','INE363A01022'),('ASIANPAINT','nse','INE021A01026'),('ASIANTILES','nse','INE022I01019'),('ASIL','nse','INE988A01026'),('ASSAMCO','nse','INE442A01024'),('ASTEC','nse','INE563J01010'),('ASTRAL','nse','INE006I01046'),('ASTRAMICRO','nse','INE386C01029'),('ASTRAZEN','nse','INE203A01020'),('ATFL','nse','INE209A01019'),('ATLANTA','nse','INE285H01022'),('ATUL','nse','INE100A01010'),('ATULAUTO','nse','INE951D01028'),('AURIONPRO','nse','INE132H01018'),('AUROPHARMA','nse','INE406A01037'),('AUSOMENT','nse','INE218C01016'),('AUSTRAL','nse','INE455J01027'),('AUTOAXLES','nse','INE449A01011'),('AUTOIND','nse','INE718H01014'),('AUTOLITIND','nse','INE448A01013'),('AVANTIFEED','nse','INE871C01020'),('AVTNPL','nse','INE488D01021'),('AXISBANK','nse','INE238A01034'),('AXISCADES','nse','INE555B01013'),('AYMSYNTEX','nse','INE193B01039'),('BAFNAPHARM','nse','INE878I01014'),('BAGFILMS','nse','INE116D01028'),('BAJAJ-AUTO','nse','INE917I01010'),('BAJAJCORP','nse','INE933K01021'),('BAJAJELEC','nse','INE193E01025'),('BAJAJFINSV','nse','INE918I01018'),('BAJAJHIND','nse','INE306A01021'),('BAJAJHLDNG','nse','INE118A01012'),('BAJFINANCE','nse','INE296A01024'),('BALAJITELE','nse','INE794B01026'),('BALAMINES','nse','INE050E01027'),('BALKRISHNA','nse','INE875R01011'),('BALKRISIND','nse','INE787D01026'),('BALLARPUR','nse','INE294A01037'),('BALMLAWRIE','nse','INE164A01016'),('BALPHARMA','nse','INE083D01012'),('BALRAMCHIN','nse','INE119A01028'),('BANARISUG','nse','INE459A01010'),('BANCOINDIA','nse','INE213C01025'),('BANKBARODA','nse','INE028A01039'),('BANKINDIA','nse','INE084A01016'),('BANSWRAS','nse','INE629D01012'),('BARTRONICS','nse','INE855F01034'),('BASF','nse','INE373A01013'),('BASML','nse','INE186H01014'),('BATAINDIA','nse','INE176A01028'),('BAYERCROP','nse','INE462A01022'),('BBL','nse','INE464A01028'),('BBTC','nse','INE050A01025'),('BEARDSELL','nse','INE520H01014'),('BEDMUTHA','nse','INE844K01012'),('BEL','nse','INE263A01024'),('BEML','nse','INE258A01016'),('BEPL','nse','INE922A01025'),('BERGEPAINT','nse','INE463A01038'),('BFINVEST','nse','INE878K01010'),('BFUTILITIE','nse','INE243D01012'),('BGRENERGY','nse','INE661I01014'),('BHAGERIA','nse','INE354C01027'),('BHANDARI','nse','INE474E01029'),('BHARATFIN','nse','INE180K01011'),('BHARATFORG','nse','INE465A01025'),('BHARATGEAR','nse','INE561C01019'),('BHARATIDIL','nse','INE673G01013'),('BHARATRAS','nse','INE838B01013'),('BHARATWIRE','nse','INE316L01019'),('BHARTIARTL','nse','INE397D01024'),('BHEL','nse','INE257A01026'),('BHUSANSTL','nse','INE824B01021'),('BIGBLOC','nse','INE412U01017'),('BIL','nse','INE828A01016'),('BILENERGY','nse','INE607L01029'),('BILPOWER','nse','INE952D01018'),('BINANIIND','nse','INE071A01013'),('BINDALAGRO','nse','INE143A01010'),('BIOCON','nse','INE376G01013'),('BIRLACABLE','nse','INE800A01015'),('BIRLACORPN','nse','INE340A01012'),('BIRLAMONEY','nse','INE865C01022'),('BLBLIMITED','nse','INE791A01024'),('BLISSGVS','nse','INE416D01022'),('BLKASHYAP','nse','INE350H01032'),('BLS','nse','INE153T01019'),('BLUEBLENDS','nse','INE113O01014'),('BLUECOAST','nse','INE472B01011'),('BLUEDART','nse','INE233B01017'),('BLUESTARCO','nse','INE472A01039'),('BODALCHEM','nse','INE338D01028'),('BOMDYEING','nse','INE032A01023'),('BOSCHLTD','nse','INE323A01026'),('BPCL','nse','INE029A01011'),('BPL','nse','INE110A01019'),('BRFL','nse','INE589G01011'),('BRIGADE','nse','INE791I01019'),('BRITANNIA','nse','INE216A01022'),('BROOKS','nse','INE650L01011'),('BSE','nse','INE118H01025'),('BSELINFRA','nse','INE395A01016'),('BSL','nse','INE594B01012'),('BSLIMITED','nse','INE043K01029'),('BURNPUR','nse','INE817H01014'),('BUTTERFLY','nse','INE295F01017'),('BVCL','nse','INE139I01011'),('BYKE','nse','INE319B01014'),('CADILAHC','nse','INE010B01027'),('CAIRN','nse','INE910H01017'),('CALSOFT','nse','INE526B01014'),('CAMLINFINE','nse','INE052I01032'),('CANBK','nse','INE476A01014'),('CANFINHOME','nse','INE477A01012'),('CANTABIL','nse','INE068L01016'),('CAPF','nse','INE688I01017'),('CAPLIPOINT','nse','INE475E01026'),('CAPTRUST','nse','INE707C01018'),('CARBORUNIV','nse','INE120A01034'),('CAREERP','nse','INE521J01018'),('CARERATING','nse','INE752H01013'),('CASTEXTECH','nse','INE068D01021'),('CASTROLIND','nse','INE172A01027'),('CCCL','nse','INE429I01024'),('CCHHL','nse','INE652F01027'),('CCL','nse','INE421D01022'),('CEATLTD','nse','INE482A01020'),('CEBBCO','nse','INE209L01016'),('CELEBRITY','nse','INE185H01016'),('CELESTIAL','nse','INE221I01017'),('CENTENKA','nse','INE485A01015'),('CENTEXT','nse','INE281A01026'),('CENTRALBK','nse','INE483A01010'),('CENTUM','nse','INE320B01020'),('CENTURYPLY','nse','INE348B01021'),('CENTURYTEX','nse','INE055A01016'),('CERA','nse','INE739E01017'),('CEREBRAINT','nse','INE345B01019'),('CESC','nse','INE486A01013'),('CGCL','nse','INE180C01026'),('CGPOWER','nse','INE067A01029'),('CHAMBLFERT','nse','INE085A01013'),('CHEMFALKAL','nse','INE479E01028'),('CHENNPETRO','nse','INE178A01016'),('CHOLAFIN','nse','INE121A01016'),('CHROMATIC','nse','INE662C01015'),('CIGNITITEC','nse','INE675C01017'),('CIMMCO','nse','INE184C01028'),('CINELINE','nse','INE704H01022'),('CIPLA','nse','INE059A01026'),('CLNINDIA','nse','INE492A01029'),('CMICABLES','nse','INE981B01011'),('CNOVAPETRO','nse','INE672K01025'),('COALINDIA','nse','INE522F01014'),('COFFEEDAY','nse','INE335K01011'),('COLPAL','nse','INE259A01022'),('COMPINFO','nse','INE070C01037'),('COMPUSOFT','nse','INE453B01029'),('CONCOR','nse','INE111A01017'),('CONSOFINVT','nse','INE025A01027'),('CONTROLPR','nse','INE663B01015'),('CORDSCABLE','nse','INE792I01017'),('COROMANDEL','nse','INE169A01031'),('CORPBANK','nse','INE112A01023'),('COSMOFILMS','nse','INE757A01017'),('COUNCODOS','nse','INE695B01025'),('COX&KINGS','nse','INE008I01026'),('CREATIVEYE','nse','INE230B01021'),('CREST','nse','INE559D01011'),('CRISIL','nse','INE007A01025'),('CROMPTON','nse','INE299U01018'),('CTE','nse','INE627H01017'),('CUB','nse','INE491A01021'),('CUMMINSIND','nse','INE298A01020'),('CUPID','nse','INE509F01011'),('CURATECH','nse','INE117B01012'),('CYBERMEDIA','nse','INE278G01037'),('CYBERTECH','nse','INE214A01019'),('CYIENT','nse','INE136B01020'),('DAAWAT','nse','INE818H01020'),('DABUR','nse','INE016A01026'),('DALMIABHA','nse','INE439L01019'),('DALMIASUG','nse','INE495A01022'),('DAMODARIND','nse','INE497D01014'),('DATAMATICS','nse','INE365B01017'),('DBCORP','nse','INE950I01011'),('DBL','nse','INE917M01012'),('DBREALTY','nse','INE879I01012'),('DBSTOCKBRO','nse','INE921B01025'),('DCBBANK','nse','INE503A01015'),('DCM','nse','INE498A01018'),('DCMSHRIRAM','nse','INE499A01024'),('DCW','nse','INE500A01029'),('DECCANCE','nse','INE583C01013'),('DEEPAKFERT','nse','INE501A01019'),('DEEPAKNTR','nse','INE288B01029'),('DEEPIND','nse','INE677H01012'),('DELTACORP','nse','INE124G01033'),('DELTAMAGNT','nse','INE393A01011'),('DEN','nse','INE947J01015'),('DENABANK','nse','INE077A01010'),('DENORA','nse','INE244A01016'),('DFMFOODS','nse','INE456C01012'),('DHAMPURSUG','nse','INE041A01016'),('DHANBANK','nse','INE680A01011'),('DHANUKA','nse','INE435G01025'),('DHARSUGAR','nse','INE988C01014'),('DHFL','nse','INE202B01012'),('DHUNINV','nse','INE320L01011'),('DIAPOWER','nse','INE989C01012'),('DICIND','nse','INE303A01010'),('DIGJAMLTD','nse','INE731U01010'),('DISHMAN','nse','INE353G01020'),('DISHTV','nse','INE836F01026'),('DIVISLAB','nse','INE361B01024'),('DLF','nse','INE271C01023'),('DLINKINDIA','nse','INE250K01012'),('DMART','nse','INE192R01011'),('DOLPHINOFF','nse','INE920A01011'),('DONEAR','nse','INE668D01028'),('DPL','nse','INE477B01010'),('DPSCLTD','nse','INE360C01024'),('DQE','nse','INE656K01010'),('DREDGECORP','nse','INE506A01018'),('DRREDDY','nse','INE089A01023'),('DSKULKARNI','nse','INE891A01014'),('DSSL','nse','INE417B01040'),('DTIL','nse','INE341R01014'),('DUCON','nse','INE741L01018'),('DWARKESH','nse','INE366A01033'),('DYNAMATECH','nse','INE221B01012'),('EASTSILK','nse','INE962C01027'),('ECEIND','nse','INE588B01014'),('ECLERX','nse','INE738I01010'),('EDELWEISS','nse','INE532F01054'),('EDL','nse','INE180G01019'),('EDUCOMP','nse','INE216H01027'),('EICHERMOT','nse','INE066A01013'),('EIDPARRY','nse','INE126A01031'),('EIHAHOTELS','nse','INE276C01014'),('EIHOTEL','nse','INE230A01023'),('EKC','nse','INE184H01027'),('ELAND','nse','INE311H01018'),('ELECON','nse','INE205B01023'),('ELECTCAST','nse','INE086A01029'),('ELECTHERM','nse','INE822G01016'),('ELGIEQUIP','nse','INE285A01027'),('ELGIRUBCO','nse','INE819L01012'),('EMAMIINFRA','nse','INE778K01012'),('EMAMILTD','nse','INE548C01032'),('EMCO','nse','INE078A01026'),('EMKAY','nse','INE296H01011'),('EMMBI','nse','INE753K01015'),('ENDURANCE','nse','INE913H01037'),('ENERGYDEV','nse','INE306C01019'),('ENGINERSIN','nse','INE510A01028'),('ENIL','nse','INE265F01028'),('EON','nse','INE076H01025'),('EQUITAS','nse','INE988K01017'),('EROSMEDIA','nse','INE416L01017'),('ESABINDIA','nse','INE284A01012'),('ESCORTS','nse','INE042A01014'),('ESL','nse','INE481K01013'),('ESSARSHPNG','nse','INE122M01019'),('ESSDEE','nse','INE825H01017'),('ESSELPACK','nse','INE255A01020'),('ESTER','nse','INE778B01029'),('EUROCERA','nse','INE649H01011'),('EUROTEXIND','nse','INE022C01012'),('EVEREADY','nse','INE128A01029'),('EVERESTIND','nse','INE295A01018'),('EXCEL','nse','INE688J01015'),('EXCELCROP','nse','INE223G01017'),('EXCELINDUS','nse','INE369A01029'),('EXIDEIND','nse','INE302A01020'),('FACT','nse','INE188A01015'),('FAGBEARING','nse','INE513A01014'),('FAIRCHEM','nse','INE959A01019'),('FCL','nse','INE045J01026'),('FCONSUMER','nse','INE220J01025'),('FDC','nse','INE258B01022'),('FEDDERLOYD','nse','INE249C01011'),('FEDERALBNK','nse','INE171A01029'),('FEL','nse','INE623B01027'),('FELDVR','nse','IN9623B01058'),('FIEMIND','nse','INE737H01014'),('FILATEX','nse','INE816B01019'),('FINCABLES','nse','INE235A01022'),('FINPIPE','nse','INE183A01016'),('FLEXITUFF','nse','INE060J01017'),('FLFL','nse','INE452O01016'),('FMGOETZE','nse','INE529A01010'),('FMNL','nse','INE360L01017'),('FORTIS','nse','INE061F01013'),('FOSECOIND','nse','INE519A01011'),('FRETAIL','nse','INE752P01024'),('FSL','nse','INE684F01012'),('GABRIEL','nse','INE524A01029'),('GAEL','nse','INE036B01022'),('GAIL','nse','INE129A01019'),('GAL','nse','INE482J01021'),('GALLANTT','nse','INE297H01019'),('GALLISPAT','nse','INE528K01011'),('GAMMNINFRA','nse','INE181G01025'),('GAMMONIND','nse','INE259B01020'),('GANDHITUBE','nse','INE524B01027'),('GANECOS','nse','INE845D01014'),('GANESHHOUC','nse','INE460C01014'),('GANGOTRI','nse','INE670B01028'),('GARDENSILK','nse','INE526A01016'),('GARWALLROP','nse','INE276A01018'),('GATI','nse','INE152B01027'),('GAYAPROJ','nse','INE336H01023'),('GDL','nse','INE852F01015'),('GEECEE','nse','INE916G01016'),('GEMINI','nse','INE878C01033'),('GENESYS','nse','INE727B01026'),('GENUSPAPER','nse','INE949P01018'),('GENUSPOWER','nse','INE955D01029'),('GEOJITFSL','nse','INE007B01023'),('GEPIL','nse','INE878A01011'),('GESHIP','nse','INE017A01032'),('GET&D','nse','INE200A01026'),('GHCL','nse','INE539A01019'),('GICHSGFIN','nse','INE289B01019'),('GILLANDERS','nse','INE047B01011'),('GILLETTE','nse','INE322A01010'),('GINNIFILA','nse','INE424C01010'),('GIPCL','nse','INE162A01010'),('GITANJALI','nse','INE346H01014'),('GKWLIMITED','nse','INE528A01020'),('GLAXO','nse','INE159A01016'),('GLENMARK','nse','INE935A01035'),('GLOBALVECT','nse','INE792H01019'),('GLOBOFFS','nse','INE446C01013'),('GLOBUSSPR','nse','INE615I01010'),('GMBREW','nse','INE075D01018'),('GMDCLTD','nse','INE131A01031'),('GMRINFRA','nse','INE776C01039'),('GNA','nse','INE934S01014'),('GNFC','nse','INE113A01013'),('GOACARBON','nse','INE426D01013'),('GOCLCORP','nse','INE077F01035'),('GODFRYPHLP','nse','INE260B01028'),('GODREJCP','nse','INE102D01028'),('GODREJIND','nse','INE233A01035'),('GODREJPROP','nse','INE484J01027'),('GOKEX','nse','INE887G01027'),('GOKUL','nse','INE020J01029'),('GOKULAGRO','nse','INE314T01025'),('GOLDENTOBC','nse','INE973A01010'),('GOLDIAM','nse','INE025B01017'),('GOODLUCK','nse','INE127I01024'),('GPIL','nse','INE177H01013'),('GPPL','nse','INE517F01014'),('GPTINFRA','nse','INE390G01014'),('GRANULES','nse','INE101D01020'),('GRAPHITE','nse','INE371A01025'),('GRASIM','nse','INE047A01021'),('GRAVITA','nse','INE024L01027'),('GREAVESCOT','nse','INE224A01026'),('GREENLAM','nse','INE544R01013'),('GREENPLY','nse','INE461C01038'),('GREENPOWER','nse','INE999K01014'),('GRINDWELL','nse','INE536A01023'),('GROBTEA','nse','INE646C01018'),('GRPLTD','nse','INE137I01015'),('GRUH','nse','INE580B01029'),('GSCLCEMENT','nse','INE542A01039'),('GSFC','nse','INE026A01025'),('GSKCONS','nse','INE264A01014'),('GSPL','nse','INE246F01010'),('GSS','nse','INE871H01011'),('GTL','nse','INE043A01012'),('GTLINFRA','nse','INE221H01019'),('GTNIND','nse','INE537A01013'),('GTNTEX','nse','INE302H01017'),('GTOFFSHORE','nse','INE892H01017'),('GUFICBIO','nse','INE742B01025'),('GUJALKALI','nse','INE186A01019'),('GUJAPOLLO','nse','INE826C01016'),('GUJFLUORO','nse','INE538A01037'),('GUJGASLTD','nse','INE844O01022'),('GUJNRECOKE','nse','INE110D01013'),('GUJNREDVR','nse','IN9110D01011'),('GULFOILLUB','nse','INE635Q01029'),('GULFPETRO','nse','INE586G01017'),('GULPOLY','nse','INE255D01024'),('GVKPIL','nse','INE251H01024'),('HANUNG','nse','INE648H01013'),('HARITASEAT','nse','INE939D01015'),('HARRMALAYA','nse','INE544A01019'),('HATHWAY','nse','INE982F01036'),('HATSUN','nse','INE473B01035'),('HAVELLS','nse','INE176B01034'),('HBLPOWER','nse','INE292B01021'),('HBSTOCK','nse','INE550B01014'),('HCC','nse','INE549A01026'),('HCG','nse','INE075I01017'),('HCL-INSYS','nse','INE236A01020'),('HCLTECH','nse','INE860A01027'),('HDFC','nse','INE001A01036'),('HDFCBANK','nse','INE040A01026'),('HDIL','nse','INE191I01012'),('HEG','nse','INE545A01016'),('HEIDELBERG','nse','INE578A01017'),('HERCULES','nse','INE688E01024'),('HERITGFOOD','nse','INE978A01019'),('HEROMOTOCO','nse','INE158A01026'),('HESTERBIO','nse','INE782E01017'),('HEXATRADEX','nse','INE750M01017'),('HEXAWARE','nse','INE093A01033'),('HFCL','nse','INE548A01028'),('HGS','nse','INE170I01016'),('HIGHGROUND','nse','INE361M01021'),('HIKAL','nse','INE475B01022'),('HIL','nse','INE557A01011'),('HILTON','nse','INE788H01017'),('HIMATSEIDE','nse','INE049A01027'),('HINDALCO','nse','INE038A01020'),('HINDCOMPOS','nse','INE310C01011'),('HINDCOPPER','nse','INE531E01026'),('HINDDORROL','nse','INE551A01022'),('HINDMOTORS','nse','INE253A01025'),('HINDNATGLS','nse','INE952A01022'),('HINDOILEXP','nse','INE345A01011'),('HINDPETRO','nse','INE094A01015'),('HINDSYNTEX','nse','INE155B01012'),('HINDUJAFO','nse','INE291F01016'),('HINDUJAVEN','nse','INE353A01023'),('HINDUNILVR','nse','INE030A01027'),('HINDZINC','nse','INE267A01025'),('HIRECT','nse','INE835D01023'),('HISARMETAL','nse','INE598C01011'),('HITECHGEAR','nse','INE127B01011'),('HITECHPLAS','nse','INE120D01012'),('HMVL','nse','INE871K01015'),('HOCL','nse','INE048A01011'),('HONAUT','nse','INE671A01010'),('HONDAPOWER','nse','INE634A01018'),('HOTELEELA','nse','INE102A01024'),('HOTELRUGBY','nse','INE275F01019'),('HOVS','nse','INE596H01014'),('HPL','nse','INE495S01016'),('HSCL','nse','INE019C01026'),('HSIL','nse','INE415A01038'),('HTMEDIA','nse','INE501G01024'),('HUBTOWN','nse','INE703H01016'),('IBREALEST','nse','INE069I01010'),('IBULHSGFIN','nse','INE148I01020'),('IBVENTURES','nse','INE274G01010'),('IBWSL','nse','INE126M01010'),('ICICIBANK','nse','INE090A01021'),('ICICIPRULI','nse','INE726G01019'),('ICIL','nse','INE483B01026'),('ICRA','nse','INE725G01011'),('ICSA','nse','INE306B01029'),('IDBI','nse','INE008A01015'),('IDEA','nse','INE669E01016'),('IDFC','nse','INE043D01016'),('IDFCBANK','nse','INE092T01019'),('IFBAGRO','nse','INE076C01018'),('IFBIND','nse','INE559A01017'),('IFCI','nse','INE039A01010'),('IFGLREFRAC','nse','INE023B01012'),('IGARASHI','nse','INE188B01013'),('IGL','nse','INE203G01019'),('IGPL','nse','INE204A01010'),('IIFL','nse','INE530B01024'),('IITL','nse','INE886A01014'),('IL&FSENGG','nse','INE369I01014'),('IL&FSTRANS','nse','INE975G01012'),('IMFA','nse','INE919H01018'),('IMPAL','nse','INE547E01014'),('IMPEXFERRO','nse','INE691G01015'),('INDBANK','nse','INE841B01017'),('INDHOTEL','nse','INE053A01029'),('INDIACEM','nse','INE383A01012'),('INDIAGLYCO','nse','INE560A01015'),('INDIANB','nse','INE562A01011'),('INDIANCARD','nse','INE061A01014'),('INDIANHUME','nse','INE323C01030'),('INDIGO','nse','INE646L01027'),('INDLMETER','nse','INE065B01013'),('INDNIPPON','nse','INE092B01017'),('INDOCO','nse','INE873D01024'),('INDORAMA','nse','INE156A01020'),('INDOSOLAR','nse','INE866K01015'),('INDOTECH','nse','INE332H01014'),('INDOTHAI','nse','INE337M01013'),('INDRAMEDCO','nse','INE681B01017'),('INDSWFTLAB','nse','INE915B01019'),('INDSWFTLTD','nse','INE788B01028'),('INDTERRAIN','nse','INE611L01021'),('INDUSINDBK','nse','INE095A01012'),('INEOSSTYRO','nse','INE189B01011'),('INFIBEAM','nse','INE483S01012'),('INFINITE','nse','INE486J01014'),('INFRATEL','nse','INE121J01017'),('INFY','nse','INE009A01021'),('INGERRAND','nse','INE177A01018'),('INOXLEISUR','nse','INE312H01016'),('INOXWIND','nse','INE066P01011'),('INSECTICID','nse','INE070I01018'),('INTEGRA','nse','INE418N01027'),('INTELLECT','nse','INE306R01017'),('INTENTECH','nse','INE781A01025'),('INVENTURE','nse','INE878H01016'),('IOB','nse','INE565A01014'),('IOC','nse','INE242A01010'),('IOLCP','nse','INE485C01011'),('IPAPPM','nse','INE435A01028'),('IPCALAB','nse','INE571A01020'),('IRB','nse','INE821I01014'),('ISFT','nse','INE566K01011'),('ISMTLTD','nse','INE732F01019'),('ITC','nse','INE154A01025'),('ITDC','nse','INE353K01014'),('ITDCEM','nse','INE686A01026'),('ITI','nse','INE248A01017'),('IVC','nse','INE050B01023'),('IVP','nse','INE043C01018'),('IVRCLINFRA','nse','INE875A01025'),('IZMO','nse','INE848A01014'),('J&KBANK','nse','INE168A01041'),('JAGRAN','nse','INE199G01027'),('JAGSNPHARM','nse','INE048B01027'),('JAIBALAJI','nse','INE091G01018'),('JAICORPLTD','nse','INE070D01027'),('JAIHINDPRO','nse','INE343D01010'),('JAMNAAUTO','nse','INE039C01024'),('JAYAGROGN','nse','INE785A01026'),('JAYBARMARU','nse','INE571B01028'),('JAYNECOIND','nse','INE854B01010'),('JAYSREETEA','nse','INE364A01020'),('JBCHEPHARM','nse','INE572A01028'),('JBFIND','nse','INE187A01017'),('JBMA','nse','INE927D01028'),('JCHAC','nse','INE782A01015'),('JENSONICOL','nse','INE819B01021'),('JETAIRWAYS','nse','INE802G01018'),('JHS','nse','INE544H01014'),('JIKIND','nse','INE026B01049'),('JINDALPHOT','nse','INE796G01012'),('JINDALPOLY','nse','INE197D01010'),('JINDALSAW','nse','INE324A01024'),('JINDALSTEL','nse','INE749A01030'),('JINDCOT','nse','INE904J01016'),('JINDRILL','nse','INE742C01031'),('JINDWORLD','nse','INE247D01013'),('JISLDVREQS','nse','IN9175A01010'),('JISLJALEQS','nse','INE175A01038'),('JKCEMENT','nse','INE823G01014'),('JKIL','nse','INE576I01022'),('JKLAKSHMI','nse','INE786A01032'),('JKPAPER','nse','INE789E01012'),('JKTYRE','nse','INE573A01042'),('JMA','nse','INE412C01015'),('JMCPROJECT','nse','INE890A01016'),('JMFINANCIL','nse','INE780C01023'),('JMTAUTOLTD','nse','INE988E01036'),('JOCIL','nse','INE839G01010'),('JPASSOCIAT','nse','INE455F01025'),('JPINFRATEC','nse','INE099J01015'),('JPOLYINVST','nse','INE147P01019'),('JPPOWER','nse','INE351F01018'),('JSL','nse','INE220G01021'),('JSLHISAR','nse','INE455T01018'),('JSWENERGY','nse','INE121E01018'),('JSWHL','nse','INE824G01012'),('JSWSTEEL','nse','INE019A01038'),('JUBILANT','nse','INE700A01033'),('JUBLFOOD','nse','INE797F01012'),('JUBLINDS','nse','INE645L01011'),('JUSTDIAL','nse','INE599M01018'),('JVLAGRO','nse','INE430G01026'),('JYOTHYLAB','nse','INE668F01031'),('JYOTISTRUC','nse','INE197A01024'),('KABRAEXTRU','nse','INE900B01029'),('KAJARIACER','nse','INE217B01036'),('KAKATCEM','nse','INE437B01014'),('KALPATPOWR','nse','INE220B01022'),('KAMATHOTEL','nse','INE967C01018'),('KAMDHENU','nse','INE390H01012'),('KANANIIND','nse','INE879E01037'),('KANORICHEM','nse','INE138C01024'),('KANSAINER','nse','INE531A01024'),('KARMAENG','nse','INE725L01011'),('KARURVYSYA','nse','INE036D01028'),('KAUSHALYA','nse','INE234I01010'),('KAVVERITEL','nse','INE641C01019'),('KAYA','nse','INE587G01015'),('KCP','nse','INE805C01028'),('KCPSUGIND','nse','INE790B01024'),('KDDL','nse','INE291D01011'),('KEC','nse','INE389H01022'),('KECL','nse','INE134B01017'),('KEI','nse','INE878B01027'),('KELLTONTEC','nse','INE164B01022'),('KESARENT','nse','INE133B01019'),('KESORAMIND','nse','INE087A01019'),('KEYCORPSER','nse','INE681C01015'),('KGL','nse','INE299C01024'),('KHANDSE','nse','INE060B01014'),('KICL','nse','INE029L01018'),('KILITCH','nse','INE729D01010'),('KINGFA','nse','INE473D01015'),('KIOCL','nse','INE880L01014'),('KIRIINDUS','nse','INE415I01015'),('KIRLOSBROS','nse','INE732A01036'),('KIRLOSENG','nse','INE146L01010'),('KIRLOSIND','nse','INE250A01039'),('KITEX','nse','INE602G01020'),('KKCL','nse','INE401H01017'),('KMSUGAR','nse','INE157H01023'),('KNRCON','nse','INE634I01029'),('KOHINOOR','nse','INE080B01012'),('KOKUYOCMLN','nse','INE760A01029'),('KOLTEPATIL','nse','INE094I01018'),('KOPRAN','nse','INE082A01010'),('KOTAKBANK','nse','INE237A01028'),('KOTARISUG','nse','INE419A01022'),('KOTHARIPET','nse','INE720A01015'),('KOTHARIPRO','nse','INE823A01017'),('KPIT','nse','INE836A01035'),('KPRMILL','nse','INE930H01023'),('KRBL','nse','INE001B01026'),('KRIDHANINF','nse','INE524L01026'),('KSBPUMPS','nse','INE999A01015'),('KSCL','nse','INE455I01029'),('KSERASERA','nse','INE216D01026'),('KSK','nse','INE143H01015'),('KSL','nse','INE907A01026'),('KTIL','nse','INE096L01025'),('KTKBANK','nse','INE614B01018'),('KWALITY','nse','INE775B01025'),('L&TFH','nse','INE498L01015'),('LAKPRE','nse','INE651C01018'),('LAKSHMIEFL','nse','INE992B01026'),('LAKSHVILAS','nse','INE694C01018'),('LALPATHLAB','nse','INE600L01024'),('LAMBODHARA','nse','INE112F01022'),('LAOPALA','nse','INE059D01020'),('LAURUSLABS','nse','INE947Q01010'),('LAXMIMACH','nse','INE269B01029'),('LGBBROSLTD','nse','INE337A01034'),('LGBFORGE','nse','INE201J01017'),('LIBERTSHOE','nse','INE557B01019'),('LICHSGFIN','nse','INE115A01026'),('LINCOLN','nse','INE405C01035'),('LINCPEN','nse','INE802B01019'),('LINDEINDIA','nse','INE473A01011'),('LITL','nse','INE785C01048'),('LLOYDELENG','nse','INE245C01019'),('LML','nse','INE862A01015'),('LOKESHMACH','nse','INE397H01017'),('LOTUSEYE','nse','INE947I01017'),('LOVABLE','nse','INE597L01014'),('LPDC','nse','INE197J01017'),('LSIL','nse','INE093R01011'),('LT','nse','INE018A01030'),('LTI','nse','INE214T01019'),('LTTS','nse','INE010V01017'),('LUMAXIND','nse','INE162B01018'),('LUMAXTECH','nse','INE872H01019'),('LUPIN','nse','INE326A01037'),('LUXIND','nse','INE150G01020'),('LYKALABS','nse','INE933A01014'),('LYPSAGEMS','nse','INE142K01011'),('M&M','nse','INE101A01026'),('M&MFIN','nse','INE774D01024'),('MAANALU','nse','INE215I01019'),('MADHAV','nse','INE925C01016'),('MADHUCON','nse','INE378D01032'),('MADRASFERT','nse','INE414A01015'),('MAGMA','nse','INE511C01022'),('MAGNUM','nse','INE387I01016'),('MAHABANK','nse','INE457A01014'),('MAHASTEEL','nse','INE451L01014'),('MAHINDCIE','nse','INE536H01010'),('MAHLIFE','nse','INE813A01018'),('MAHSCOOTER','nse','INE288A01013'),('MAHSEAMLES','nse','INE271B01025'),('MAITHANALL','nse','INE683C01011'),('MAJESCO','nse','INE898S01029'),('MALUPAPER','nse','INE383H01017'),('MANAKCOAT','nse','INE830Q01018'),('MANAKINDST','nse','INE831Q01016'),('MANAKSIA','nse','INE015D01022'),('MANAKSTEEL','nse','INE824Q01011'),('MANALIPETC','nse','INE201A01024'),('MANAPPURAM','nse','INE522D01027'),('MANGALAM','nse','INE584F01014'),('MANGCHEFER','nse','INE558B01017'),('MANGLMCEM','nse','INE347A01017'),('MANGTIMBER','nse','INE805B01012'),('MANINDS','nse','INE993A01026'),('MANINFRA','nse','INE949H01023'),('MANPASAND','nse','INE122R01018'),('MANUGRAPH','nse','INE867A01022'),('MARALOVER','nse','INE882A01013'),('MARATHON','nse','INE182D01012'),('MARICO','nse','INE196A01026'),('MARKSANS','nse','INE750C01026'),('MARUTI','nse','INE585B01010'),('MASTEK','nse','INE759A01021'),('MAWANASUG','nse','INE636A01039'),('MAXINDIA','nse','INE153U01017'),('MAXVIL','nse','INE154U01015'),('MAYURUNIQ','nse','INE040D01038'),('MAZDA','nse','INE885E01034'),('MBECL','nse','INE748A01016'),('MBLINFRA','nse','INE912H01013'),('MCDHOLDING','nse','INE836H01014'),('MCDOWELL-N','nse','INE854D01016'),('MCLEODRUSS','nse','INE942G01012'),('MCX','nse','INE745G01035'),('MEGASOFT','nse','INE933B01012'),('MEGH','nse','INE974H01013'),('MELSTAR','nse','INE817A01019'),('MENONBE','nse','INE071D01033'),('MEP','nse','INE776I01010'),('MERCATOR','nse','INE934B01028'),('MERCK','nse','INE199A01012'),('METALFORGE','nse','INE425A01011'),('MFSL','nse','INE180A01020'),('MGL','nse','INE002S01010'),('MHRIL','nse','INE998I01010'),('MIC','nse','INE287C01029'),('MINDACORP','nse','INE842C01021'),('MINDAIND','nse','INE405E01023'),('MINDTECK','nse','INE110B01017'),('MINDTREE','nse','INE018I01017'),('MIRCELECTR','nse','INE831A01028'),('MIRZAINT','nse','INE771A01026'),('MMFL','nse','INE227C01017'),('MMTC','nse','INE123F01029'),('MOHITIND','nse','INE954E01012'),('MOIL','nse','INE490G01020'),('MOLDTECH','nse','INE835B01035'),('MOLDTKPAC','nse','INE893J01029'),('MONNETISPA','nse','INE743C01013'),('MONSANTO','nse','INE274B01011'),('MONTECARLO','nse','INE950M01013'),('MORARJEE','nse','INE161G01027'),('MOREPENLAB','nse','INE083A01026'),('MOSERBAER','nse','INE739A01015'),('MOTHERSUMI','nse','INE775A01035'),('MOTILALOFS','nse','INE338I01027'),('MPHASIS','nse','INE356A01018'),('MPSLTD','nse','INE943D01017'),('MRF','nse','INE883A01011'),('MRO-TEK','nse','INE398B01018'),('MRPL','nse','INE103A01014'),('MSPL','nse','INE752G01015'),('MTEDUCARE','nse','INE472M01018'),('MTNL','nse','INE153A01019'),('MUKANDENGG','nse','INE022B01014'),('MUKANDLTD','nse','INE304A01026'),('MUKTAARTS','nse','INE374B01019'),('MUNJALAU','nse','INE672B01032'),('MUNJALSHOW','nse','INE577A01027'),('MURUDCERA','nse','INE692B01014'),('MUTHOOTCAP','nse','INE296G01013'),('MUTHOOTFIN','nse','INE414G01012'),('MVL','nse','INE744I01034'),('NAGAFERT','nse','INE454M01024'),('NAGAROIL','nse','INE453M01018'),('NAGREEKCAP','nse','INE245I01016'),('NAGREEKEXP','nse','INE123B01028'),('NAHARCAP','nse','INE049I01012'),('NAHARINDUS','nse','INE289A01011'),('NAHARPOLY','nse','INE308A01027'),('NAHARSPING','nse','INE290A01027'),('NAKODA','nse','INE559B01023'),('NATCOPHARM','nse','INE987B01026'),('NATHBIOGEN','nse','INE448G01010'),('NATIONALUM','nse','INE139A01034'),('NAUKRI','nse','INE663F01024'),('NAVINFLUOR','nse','INE048G01018'),('NAVKARCORP','nse','INE278M01019'),('NAVNETEDUL','nse','INE060A01024'),('NBCC','nse','INE095N01023'),('NBVENTURES','nse','INE725A01022'),('NCC','nse','INE868B01028'),('NCLIND','nse','INE732C01016'),('NDGL','nse','INE756C01015'),('NDL','nse','INE875G01030'),('NDTV','nse','INE155G01029'),('NECCLTD','nse','INE553C01016'),('NECLIFE','nse','INE023H01027'),('NELCAST','nse','INE189I01024'),('NELCO','nse','INE045B01015'),('NESCO','nse','INE317F01027'),('NESTLEIND','nse','INE239A01016'),('NET4','nse','INE553E01012'),('NETWORK18','nse','INE870H01013'),('NEULANDLAB','nse','INE794A01010'),('NFL','nse','INE870D01012'),('NH','nse','INE410P01011'),('NHPC','nse','INE848E01016'),('NIBL','nse','INE047O01014'),('NIITLTD','nse','INE161A01038'),('NIITTECH','nse','INE591G01017'),('NILAINFRA','nse','INE937C01029'),('NILKAMAL','nse','INE310A01015'),('NIPPOBATRY','nse','INE567A01010'),('NITCO','nse','INE858F01012'),('NITESHEST','nse','INE639K01016'),('NITINFIRE','nse','INE489H01020'),('NITINSPIN','nse','INE229H01012'),('NKIND','nse','INE542C01019'),('NLCINDIA','nse','INE589A01014'),('NMDC','nse','INE584A01023'),('NOCIL','nse','INE163A01018'),('NOESISIND','nse','INE141B01020'),('NOIDATOLL','nse','INE781B01015'),('NORBTEAEXP','nse','INE369C01017'),('NRBBEARING','nse','INE349A01021'),('NSIL','nse','INE023A01030'),('NTL','nse','INE333I01036'),('NTPC','nse','INE733E01010'),('NUCLEUS','nse','INE096B01018'),('NUTEK','nse','INE318J01027'),('OBEROIRLTY','nse','INE093I01010'),('OCCL','nse','INE321D01016'),('OCL','nse','INE290B01025'),('OFSS','nse','INE881D01027'),('OIL','nse','INE274J01014'),('OILCOUNTUB','nse','INE591A01010'),('OISL','nse','INE196J01019'),('OMAXAUTO','nse','INE090B01011'),('OMAXE','nse','INE800H01010'),('OMKARCHEM','nse','INE474L01016'),('OMMETALS','nse','INE239D01028'),('ONELIFECAP','nse','INE912L01015'),('ONGC','nse','INE213A01029'),('ONMOBILE','nse','INE809I01019'),('ONWARDTEC','nse','INE229A01017'),('OPTOCIRCUI','nse','INE808B01016'),('ORBTEXP','nse','INE231G01010'),('ORCHIDPHAR','nse','INE191A01019'),('ORICONENT','nse','INE730A01022'),('ORIENTABRA','nse','INE569C01020'),('ORIENTBANK','nse','INE141A01014'),('ORIENTBELL','nse','INE607D01018'),('ORIENTCEM','nse','INE876N01018'),('ORIENTHOT','nse','INE750A01020'),('ORIENTLTD','nse','INE609C01024'),('ORIENTPPR','nse','INE592A01026'),('ORIENTREF','nse','INE743M01012'),('ORISSAMINE','nse','INE725E01024'),('ORTEL','nse','INE849L01019'),('ORTINLABSS','nse','INE749B01012'),('PAGEIND','nse','INE761H01022'),('PANACEABIO','nse','INE922B01023'),('PANAMAPET','nse','INE305C01029'),('PANORAMUNI','nse','INE194B01029'),('PAPERPROD','nse','INE275B01026'),('PARABDRUGS','nse','INE618H01016'),('PARAGMILK','nse','INE883N01014'),('PARRYSUGAR','nse','INE353B01021'),('PARSVNATH','nse','INE561H01026'),('PATELENG','nse','INE244B01030'),('PATINTLOG','nse','INE529D01014'),('PATSPINLTD','nse','INE790C01014'),('PBAINFRA','nse','INE160H01019'),('PCJEWELLER','nse','INE785M01013'),('PDMJEPAPER','nse','INE865T01018'),('PDPL','nse','INE904D01019'),('PDSMFL','nse','INE111Q01013'),('PDUMJEIND','nse','INE105C01023'),('PDUMJEPULP','nse','INE606A01024'),('PEL','nse','INE140A01024'),('PENIND','nse','INE932A01024'),('PENINLAND','nse','INE138A01028'),('PENPEBS','nse','INE455O01019'),('PERSISTENT','nse','INE262H01013'),('PETRONENGG','nse','INE742A01019'),('PETRONET','nse','INE347G01014'),('PFC','nse','INE134E01011'),('PFIZER','nse','INE182A01018'),('PFOCUS','nse','INE367G01038'),('PFS','nse','INE560K01014'),('PGEL','nse','INE457L01011'),('PGHH','nse','INE179A01014'),('PGIL','nse','INE940H01014'),('PHILIPCARB','nse','INE602A01015'),('PHOENIXLL','nse','INE455B01016'),('PHOENIXLTD','nse','INE211B01039'),('PIDILITIND','nse','INE318A01026'),('PIIND','nse','INE603J01030'),('PINCON','nse','INE675G01018'),('PIONDIST','nse','INE889E01010'),('PIONEEREMB','nse','INE156C01018'),('PIRPHYTO','nse','INE122J01015'),('PITTILAM','nse','INE450D01021'),('PKTEA','nse','INE431F01018'),('PLASTIBLEN','nse','INE083C01022'),('PNB','nse','INE160A01022'),('PNBGILTS','nse','INE859A01011'),('PNBHOUSING','nse','INE572E01012'),('PNC','nse','INE392B01011'),('PNCINFRA','nse','INE195J01029'),('PNEUMATIC','nse','INE096T01010'),('POCHIRAJU','nse','INE332G01032'),('PODDARMENT','nse','INE371C01013'),('POKARNA','nse','INE637C01017'),('POLARIS','nse','INE763A01023'),('POLYMED','nse','INE205C01021'),('POLYPLEX','nse','INE633B01018'),('PONNIERODE','nse','INE838E01017'),('POWERGRID','nse','INE752E01010'),('POWERMECH','nse','INE211R01019'),('PPAP','nse','INE095I01015'),('PRABHAT','nse','INE302M01033'),('PRAENG','nse','INE505C01016'),('PRAJIND','nse','INE074A01025'),('PRAKASH','nse','INE603A01013'),('PRAKASHCON','nse','INE023M01027'),('PRAKASHSTL','nse','INE696K01024'),('PRATIBHA','nse','INE308H01022'),('PRECAM','nse','INE484I01029'),('PRECOT','nse','INE283A01014'),('PRECWIRE','nse','INE372C01029'),('PREMEXPLN','nse','INE863B01011'),('PREMIER','nse','INE342A01018'),('PREMIERPOL','nse','INE309M01012'),('PRESSMN','nse','INE980A01023'),('PRESTIGE','nse','INE811K01011'),('PRICOLLTD','nse','INE726V01018'),('PRIMESECU','nse','INE032B01021'),('PRISMCEM','nse','INE010A01011'),('PROVOGE','nse','INE968G01033'),('PROZONINTU','nse','INE195N01013'),('PSB','nse','INE608A01012'),('PSL','nse','INE474B01017'),('PTC','nse','INE877F01012'),('PTL','nse','INE034D01031'),('PUNJABCHEM','nse','INE277B01014'),('PUNJLLOYD','nse','INE701B01021'),('PURVA','nse','INE323I01011'),('PVP','nse','INE362A01016'),('PVR','nse','INE191H01014'),('QUESS','nse','INE615P01015'),('QUICKHEAL','nse','INE306L01010'),('QUINTEGRA','nse','INE033B01011'),('RADAAN','nse','INE874F01027'),('RADICO','nse','INE944F01028'),('RADIOCITY','nse','INE919I01016'),('RAIN','nse','INE855B01025'),('RAINBOWPAP','nse','INE028D01025'),('RAIREKMOH','nse','INE313D01013'),('RAJESHEXPO','nse','INE343B01030'),('RAJOIL','nse','INE294G01018'),('RAJRAYON','nse','INE533D01024'),('RAJSREESUG','nse','INE562B01019'),('RAJTV','nse','INE952H01027'),('RAJVIR','nse','INE011H01014'),('RALLIS','nse','INE613A01020'),('RAMANEWS','nse','INE278B01020'),('RAMASTEEL','nse','INE230R01027'),('RAMCOCEM','nse','INE331A01037'),('RAMCOIND','nse','INE614A01028'),('RAMCOSYS','nse','INE246B01019'),('RAMKY','nse','INE874I01013'),('RANASUG','nse','INE625B01014'),('RANEENGINE','nse','INE222J01013'),('RANEHOLDIN','nse','INE384A01010'),('RATNAMANI','nse','INE703B01027'),('RAYMOND','nse','INE301A01014'),('RBL','nse','INE244J01017'),('RBLBANK','nse','INE976G01028'),('RCF','nse','INE027A01015'),('RCOM','nse','INE330H01018'),('RDEL','nse','INE542F01012'),('RECLTD','nse','INE020B01018'),('REDINGTON','nse','INE891D01026'),('REFEX','nse','INE056I01017'),('REIAGROLTD','nse','INE385B01031'),('RELAXO','nse','INE131B01039'),('RELCAPITAL','nse','INE013A01015'),('RELIANCE','nse','INE002A01018'),('RELIGARE','nse','INE621H01010'),('RELINFRA','nse','INE036A01016'),('REMSONSIND','nse','INE474C01015'),('RENUKA','nse','INE087H01022'),('REPCOHOME','nse','INE612J01015'),('REPRO','nse','INE461B01014'),('RESPONIND','nse','INE688D01026'),('REVATHI','nse','INE617A01013'),('RICOAUTO','nse','INE209B01025'),('RIIL','nse','INE046A01015'),('RJL','nse','INE722H01016'),('RKDL','nse','INE722J01012'),('RKFORGE','nse','INE399G01015'),('RML','nse','INE050H01012'),('ROHITFERRO','nse','INE248H01012'),('ROHLTD','nse','INE283H01019'),('ROLLT','nse','INE927A01040'),('ROLTA','nse','INE293A01013'),('ROSSELLIND','nse','INE847C01020'),('RPGLIFE','nse','INE105J01010'),('RPOWER','nse','INE614G01033'),('RPPINFRA','nse','INE324L01013'),('RSSOFTWARE','nse','INE165B01029'),('RSWM','nse','INE611A01016'),('RSYSTEMS','nse','INE411H01032'),('RTNINFRA','nse','INE834M01019'),('RTNPOWER','nse','INE399K01017'),('RUBYMILLS','nse','INE301D01026'),('RUCHIRA','nse','INE803H01014'),('RUCHISOYA','nse','INE619A01027'),('RUPA','nse','INE895B01021'),('RUSHIL','nse','INE573K01017'),('SABEVENTS','nse','INE860T01019'),('SABTN','nse','INE416A01036'),('SADBHAV','nse','INE226H01026'),('SADBHIN','nse','INE764L01010'),('SAGCEM','nse','INE229C01013'),('SAIL','nse','INE114A01011'),('SAKHTISUG','nse','INE623A01011'),('SAKSOFT','nse','INE667G01015'),('SAKUMA','nse','INE190H01016'),('SALORAINTL','nse','INE924A01013'),('SALZERELEC','nse','INE457F01013'),('SAMBHAAV','nse','INE699B01027'),('SAMTEL','nse','INE381A01016'),('SANDESH','nse','INE583B01015'),('SANGAMIND','nse','INE495C01010'),('SANGHIIND','nse','INE999B01013'),('SANGHVIFOR','nse','INE263L01013'),('SANGHVIMOV','nse','INE989A01024'),('SANOFI','nse','INE058A01010'),('SANWARIA','nse','INE890C01046'),('SARDAEN','nse','INE385C01013'),('SAREGAMA','nse','INE979A01017'),('SARLAPOLY','nse','INE453D01025'),('SASKEN','nse','INE231F01020'),('SASTASUNDR','nse','INE019J01013'),('SATHAISPAT','nse','INE176C01016'),('SATIN','nse','INE836B01017'),('SBIN','nse','INE062A01020'),('SCHNEIDER','nse','INE839M01018'),('SCI','nse','INE109A01011'),('SDBL','nse','INE480C01012'),('SEAMECLTD','nse','INE497B01018'),('SEINV','nse','INE420C01042'),('SELAN','nse','INE818A01017'),('SELMCL','nse','INE105I01012'),('SEPOWER','nse','INE735M01018'),('SEQUENT','nse','INE807F01027'),('SERVALL','nse','INE431L01016'),('SESHAPAPER','nse','INE630A01016'),('SETCO','nse','INE878E01021'),('SEZAL','nse','INE955I01036'),('SFCL','nse','INE935O01010'),('SFL','nse','INE916U01025'),('SGL','nse','INE353H01010'),('SHAHALLOYS','nse','INE640C01011'),('SHAKTIPUMP','nse','INE908D01010'),('SHALPAINTS','nse','INE849C01026'),('SHANTIGEAR','nse','INE631A01022'),('SHARDACROP','nse','INE221J01015'),('SHARDAMOTR','nse','INE597I01010'),('SHARONBIO','nse','INE028B01029'),('SHEMAROO','nse','INE363M01019'),('SHILPAMED','nse','INE790G01031'),('SHILPI','nse','INE510K01019'),('SHIRPUR-G','nse','INE196B01016'),('SHIVAMAUTO','nse','INE637H01024'),('SHIVTEX','nse','INE705C01012'),('SHK','nse','INE500L01026'),('SHOPERSTOP','nse','INE498B01024'),('SHREECEM','nse','INE070A01015'),('SHREEPUSHK','nse','INE712K01011'),('SHREERAMA','nse','INE879A01019'),('SHREYANIND','nse','INE231C01019'),('SHREYAS','nse','INE757B01015'),('SHRIRAMCIT','nse','INE722A01011'),('SHRIRAMEPC','nse','INE964H01014'),('SHYAMCENT','nse','INE979R01011'),('SHYAMTEL','nse','INE635A01023'),('SICAGEN','nse','INE176J01011'),('SICAL','nse','INE075B01012'),('SIEMENS','nse','INE003A01024'),('SIGNET','nse','INE529F01027'),('SILINV','nse','INE923A01015'),('SIMBHALS','nse','INE748T01016'),('SIMPLEXINF','nse','INE059B01024'),('SINTEX','nse','INE429C01035'),('SITASHREE','nse','INE686I01011'),('SITINET','nse','INE965H01011'),('SIYSIL','nse','INE076B01010'),('SJVN','nse','INE002L01015'),('SKFINDIA','nse','INE640A01023'),('SKIL','nse','INE429F01012'),('SKIPPER','nse','INE439E01022'),('SKMEGGPROD','nse','INE411D01015'),('SMARTLINK','nse','INE178C01020'),('SMLISUZU','nse','INE294B01019'),('SMPL','nse','INE215G01021'),('SMSPHARMA','nse','INE812G01025'),('SNOWMAN','nse','INE734N01019'),('SOBHA','nse','INE671H01015'),('SOFTTECHGR','nse','INE863A01013'),('SOLARINDS','nse','INE343H01029'),('SOMANYCERA','nse','INE355A01028'),('SOMICONVEY','nse','INE323J01019'),('SONASTEER','nse','INE643A01035'),('SONATSOFTW','nse','INE269A01021'),('SORILINFRA','nse','INE034H01016'),('SOTL','nse','INE035D01012'),('SOUTHBANK','nse','INE683A01023'),('SPAL','nse','INE212I01016'),('SPARC','nse','INE232I01014'),('SPCENET','nse','INE970N01027'),('SPECIALITY','nse','INE247M01014'),('SPENTEX','nse','INE376C01020'),('SPHEREGSL','nse','INE737B01033'),('SPIC','nse','INE147A01011'),('SPICEMOBI','nse','INE927C01020'),('SPLIL','nse','INE978G01016'),('SPMLINFRA','nse','INE937A01023'),('SPYL','nse','INE268L01020'),('SQSBFSI','nse','INE201K01015'),('SREEL','nse','INE099F01013'),('SREINFRA','nse','INE872A01014'),('SRF','nse','INE647A01010'),('SRHHYPOLTD','nse','INE917H01012'),('SRIPIPES','nse','INE943C01027'),('SRSLTD','nse','INE219H01039'),('SRTRANSFIN','nse','INE721A01013'),('SSWL','nse','INE802C01017'),('STAMPEDE','nse','INE224E01028'),('STAR','nse','INE939A01011'),('STARPAPER','nse','INE733A01018'),('STCINDIA','nse','INE655A01013'),('STEL','nse','INE577L01016'),('STERLINBIO','nse','INE324C01038'),('STERTOOLS','nse','INE334A01023'),('STINDIA','nse','INE090C01019'),('STRTECH','nse','INE089C01029'),('SUBEX','nse','INE754A01014'),('SUBROS','nse','INE287B01021'),('SUDARSCHEM','nse','INE659A01023'),('SUJANAUNI','nse','INE216G01011'),('SUMEETINDS','nse','INE235C01010'),('SUMMITSEC','nse','INE519C01017'),('SUNCLAYLTD','nse','INE105A01035'),('SUNDARAM','nse','INE108E01023'),('SUNDARMFIN','nse','INE660A01013'),('SUNDRMBRAK','nse','INE073D01013'),('SUNDRMFAST','nse','INE387A01021'),('SUNFLAG','nse','INE947A01014'),('SUNILHITEC','nse','INE305H01028'),('SUNPHARMA','nse','INE044A01036'),('SUNTECK','nse','INE805D01026'),('SUNTV','nse','INE424H01027'),('SUPERHOUSE','nse','INE712B01010'),('SUPERSPIN','nse','INE662A01027'),('SUPPETRO','nse','INE663A01017'),('SUPRAJIT','nse','INE399C01030'),('SUPREMEIND','nse','INE195A01028'),('SUPREMEINF','nse','INE550H01011'),('SUPREMETEX','nse','INE651G01027'),('SURANACORP','nse','INE357D01010'),('SURANASOL','nse','INE272L01022'),('SURANAT&P','nse','INE130B01031'),('SURYALAXMI','nse','INE713B01026'),('SURYAROSNI','nse','INE335A01012'),('SUTLEJTEX','nse','INE645H01019'),('SUVEN','nse','INE495B01038'),('SUZLON','nse','INE040H01021'),('SWANENERGY','nse','INE665A01038'),('SWARAJENG','nse','INE277A01016'),('SWELECTES','nse','INE409B01013'),('SYMPHONY','nse','INE225D01027'),('SYNCOM','nse','INE602K01014'),('SYNDIBANK','nse','INE667A01018'),('SYNGENE','nse','INE398R01022'),('TAINWALCHM','nse','INE123C01018'),('TAJGVK','nse','INE586B01026'),('TAKE','nse','INE142I01023'),('TALBROAUTO','nse','INE187D01011'),('TALWALKARS','nse','INE502K01016'),('TANLA','nse','INE483C01032'),('TARAJEWELS','nse','INE799L01016'),('TARMAT','nse','INE924H01018'),('TASTYBITE','nse','INE488B01017'),('TATACHEM','nse','INE092A01019'),('TATACOFFEE','nse','INE493A01027'),('TATACOMM','nse','INE151A01013'),('TATAELXSI','nse','INE670A01012'),('TATAGLOBAL','nse','INE192A01025'),('TATAINVEST','nse','INE672A01018'),('TATAMETALI','nse','INE056C01010'),('TATAMOTORS','nse','INE155A01022'),('TATAMTRDVR','nse','IN9155A01020'),('TATAPOWER','nse','INE245A01021'),('TATASPONGE','nse','INE674A01014'),('TATASTEEL','nse','INE081A01012'),('TBZ','nse','INE760L01018'),('TCI','nse','INE688A01022'),('TCIDEVELOP','nse','INE662L01016'),('TCIEXP','nse','INE586V01016'),('TCIFINANCE','nse','INE911B01018'),('TCS','nse','INE467B01029'),('TDPOWERSYS','nse','INE419M01019'),('TEAMLEASE','nse','INE985S01024'),('TECHIN','nse','INE778A01021'),('TECHM','nse','INE669C01036'),('TECHNO','nse','INE286K01024'),('TECHNOFAB','nse','INE509K01011'),('TERASOFT','nse','INE482B01010'),('TEXINFRA','nse','INE435C01024'),('TEXMOPIPES','nse','INE141K01013'),('TEXRAIL','nse','INE621L01012'),('TFCILTD','nse','INE305A01015'),('TFL','nse','INE804H01012'),('TGBHOTELS','nse','INE797H01018'),('THANGAMAYL','nse','INE085J01014'),('THEMISMED','nse','INE083B01016'),('THERMAX','nse','INE152A01029'),('THIRUSUGAR','nse','INE409A01015'),('THOMASCOOK','nse','INE332A01027'),('THYROCARE','nse','INE594H01019'),('TI','nse','INE133E01013'),('TIDEWATER','nse','INE484C01022'),('TIIL','nse','INE545H01011'),('TIJARIA','nse','INE440L01017'),('TIL','nse','INE806C01018'),('TIMETECHNO','nse','INE508G01029'),('TIMKEN','nse','INE325A01013'),('TINPLATE','nse','INE422C01014'),('TIPSINDLTD','nse','INE716B01011'),('TIRUMALCHM','nse','INE338A01016'),('TITAN','nse','INE280A01028'),('TMRVL','nse','INE759V01019'),('TNPETRO','nse','INE148A01019'),('TNPL','nse','INE107A01015'),('TOKYOPLAST','nse','INE932C01012'),('TORNTPHARM','nse','INE685A01028'),('TORNTPOWER','nse','INE813H01021'),('TPLPLASTEH','nse','INE413G01014'),('TREEHOUSE','nse','INE040M01013'),('TRENT','nse','INE849A01020'),('TRF','nse','INE391D01019'),('TRIDENT','nse','INE064C01014'),('TRIGYN','nse','INE948A01012'),('TRIL','nse','INE763I01018'),('TRITURBINE','nse','INE152M01016'),('TRIVENI','nse','INE256C01024'),('TTKHLTCARE','nse','INE910C01018'),('TTKPRESTIG','nse','INE690A01010'),('TTL','nse','INE592B01016'),('TTML','nse','INE517B01013'),('TUBEINVEST','nse','INE149A01025'),('TULSI','nse','INE474I01012'),('TV18BRDCST','nse','INE886H01027'),('TVSELECT','nse','INE236G01019'),('TVSMOTOR','nse','INE494B01023'),('TVSSRICHAK','nse','INE421C01016'),('TVTODAY','nse','INE038F01029'),('TVVISION','nse','INE871L01013'),('TWL','nse','INE615H01020'),('UBHOLDINGS','nse','INE696A01025'),('UBL','nse','INE686F01025'),('UCALFUEL','nse','INE139B01016'),('UCOBANK','nse','INE691A01018'),('UFLEX','nse','INE516A01017'),('UFO','nse','INE527H01019'),('UGARSUGAR','nse','INE071E01023'),('UJAAS','nse','INE899L01022'),('UJJIVAN','nse','INE334L01012'),('ULTRACEMCO','nse','INE481G01011'),('UMANGDAIRY','nse','INE864B01027'),('UMESLTD','nse','INE240C01028'),('UNICHEMLAB','nse','INE351A01035'),('UNIENTER','nse','INE037A01022'),('UNIONBANK','nse','INE692A01016'),('UNITECH','nse','INE694A01020'),('UNITEDBNK','nse','INE695A01019'),('UNITEDTEA','nse','INE458F01011'),('UNITY','nse','INE466H01028'),('UNIVCABLES','nse','INE279A01012'),('UPL','nse','INE628A01036'),('USHAMART','nse','INE228A01035'),('UTTAMSTL','nse','INE699A01011'),('UTTAMSUGAR','nse','INE786F01031'),('V2RETAIL','nse','INE945H01013'),('VADILALIND','nse','INE694D01016'),('VAKRANGEE','nse','INE051B01021'),('VALUEIND','nse','INE352A01017'),('VARDHACRLC','nse','INE116G01013'),('VARDMNPOLY','nse','INE835A01011'),('VASCONEQ','nse','INE893I01013'),('VASWANI','nse','INE590L01019'),('VBL','nse','INE200M01013'),('VEDL','nse','INE205A01025'),('VENKEYS','nse','INE398A01010'),('VENUSREM','nse','INE411B01019'),('VESUVIUS','nse','INE386A01015'),('VETO','nse','INE918N01018'),('VGUARD','nse','INE951I01027'),('VHL','nse','INE701A01023'),('VICEROY','nse','INE048C01017'),('VIDEOIND','nse','INE703A01011'),('VIDHIING','nse','INE632C01026'),('VIJAYABANK','nse','INE705A01016'),('VIJIFIN','nse','INE159N01027'),('VIJSHAN','nse','INE806F01011'),('VIKASECO','nse','INE806A01020'),('VIMALOIL','nse','INE067D01015'),('VIMTALABS','nse','INE579C01029'),('VINATIORGA','nse','INE410B01029'),('VINDHYATEL','nse','INE707A01012'),('VINYLINDIA','nse','INE250B01029'),('VIPCLOTHNG','nse','INE450G01024'),('VIPIND','nse','INE054A01027'),('VIPULLTD','nse','INE946H01037'),('VISAKAIND','nse','INE392A01013'),('VISASTEEL','nse','INE286H01012'),('VISESHINFO','nse','INE861A01058'),('VISHNU','nse','INE270I01014'),('VISUINTL','nse','INE965A01016'),('VIVIDHA','nse','INE370E01029'),('VIVIMEDLAB','nse','INE526G01021'),('VLSFINANCE','nse','INE709A01018'),('VMART','nse','INE665J01013'),('VOLTAMP','nse','INE540H01012'),('VOLTAS','nse','INE226A01021'),('VRLLOG','nse','INE366I01010'),('VSSL','nse','INE050M01012'),('VSTIND','nse','INE710A01016'),('VSTTILLERS','nse','INE764D01017'),('VTL','nse','INE825A01012'),('WABAG','nse','INE956G01038'),('WABCOINDIA','nse','INE342J01019'),('WALCHANNAG','nse','INE711A01022'),('WEBELSOLAR','nse','INE855C01015'),('WEIZFOREX','nse','INE726L01019'),('WEIZMANIND','nse','INE080A01014'),('WELCORP','nse','INE191B01025'),('WELENT','nse','INE625G01013'),('WELINV','nse','INE389K01018'),('WELSPUNIND','nse','INE192B01031'),('WENDT','nse','INE274C01019'),('WHEELS','nse','INE715A01015'),('WHIRLPOOL','nse','INE716A01013'),('WILLAMAGOR','nse','INE210A01017'),('WINDMACHIN','nse','INE052A01021'),('WINSOME','nse','INE784B01035'),('WIPRO','nse','INE075A01022'),('WOCKPHARMA','nse','INE049B01025'),('WONDERLA','nse','INE066O01014'),('WSI','nse','INE100D01014'),('WSTCSTPAPR','nse','INE976A01021'),('XCHANGING','nse','INE692G01013'),('XLENERGY','nse','INE183H01011'),('XPROINDIA','nse','INE445C01015'),('YESBANK','nse','INE528G01019'),('ZANDUREALT','nse','INE719A01017'),('ZEEL','nse','INE256A01028'),('ZEELEARN','nse','INE565L01011'),('ZEEMEDIA','nse','INE966H01019'),('ZENITHBIR','nse','INE318D01020'),('ZENITHEXPO','nse','INE058B01018'),('ZENSARTECH','nse','INE520A01019'),('ZENTEC','nse','INE251B01027'),('ZICOM','nse','INE871B01014'),('ZODIACLOTH','nse','INE206B01013'),('ZODJRDMKJ','nse','INE077B01018'),('ZUARI','nse','INE840M01016'),('ZUARIGLOB','nse','INE217A01012'),('ZYDUSWELL','nse','INE768C01010'),('ZYLOG','nse','INE225I01026');
/*!40000 ALTER TABLE `processor_ticker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `avatar` varchar(100) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$30000$1S036SIAxfQ2$AfUtpFOSii+2Gt+XdEctewkDu9qCi/a2Z0GuBLQ6+eU=',1,'admin@psylab.io','','','2017-03-23 11:10:28.672906','2017-03-25 13:09:32.345929','',1,1),(2,'pbkdf2_sha256$30000$NYT5lGQiqW08$BMRGtCA2+eIMkGwwNv1rdBqQfXfvD36czqJAqYTT12Q=',0,'rajdeep@gmail.com','','','2017-03-23 11:11:56.122058',NULL,'',1,0),(3,'pbkdf2_sha256$30000$0cGr7yNtMNbX$Pa84kubpLgtFv27iMADtVsk+YIpx4yzkXlYzL6Ov9dU=',0,'shubham@gmail.com','','','2017-03-23 11:12:01.337348',NULL,'',1,0);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_per_permission_id_0b93982e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `users_user_user_per_permission_id_0b93982e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-03-26  4:08:01
