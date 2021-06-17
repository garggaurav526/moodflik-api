-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: moodflik
-- ------------------------------------------------------
-- Server version	5.7.27

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
-- Table structure for table `Post_dislikepost`
--

DROP TABLE IF EXISTS `Post_dislikepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Post_dislikepost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(130) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `gif` varchar(255) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `why_content` varchar(150) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Post_dislikepost_user_id_f6618f25_fk_User_customuser_id` (`user_id`),
  CONSTRAINT `Post_dislikepost_user_id_f6618f25_fk_User_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `User_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Post_dislikepost`
--

LOCK TABLES `Post_dislikepost` WRITE;
/*!40000 ALTER TABLE `Post_dislikepost` DISABLE KEYS */;
INSERT INTO `Post_dislikepost` VALUES (1,'this is post i dislike',NULL,NULL,NULL,NULL,'It is not of my taste.',1),(2,'Believe in yourself.',NULL,NULL,NULL,NULL,'it is disliked post content.',3),(3,'you will learn more from failures than success.',NULL,NULL,NULL,NULL,'it is disliked.',4);
/*!40000 ALTER TABLE `Post_dislikepost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Post_likepost`
--

DROP TABLE IF EXISTS `Post_likepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Post_likepost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(130) NOT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `video` varchar(255) DEFAULT NULL,
  `gif` varchar(255) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `why_content` varchar(150) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Post_likepost_user_id_00f59f11_fk_User_customuser_id` (`user_id`),
  CONSTRAINT `Post_likepost_user_id_00f59f11_fk_User_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `User_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Post_likepost`
--

LOCK TABLES `Post_likepost` WRITE;
/*!40000 ALTER TABLE `Post_likepost` DISABLE KEYS */;
INSERT INTO `Post_likepost` VALUES (1,'this is like post',NULL,NULL,NULL,NULL,'bcoz it is soothing',1),(2,'Way to get started is to quit talking and start working.',NULL,NULL,NULL,NULL,'yeah, it is motivational.',2),(3,'it\'s not whether you knocked down, it\'s whether you get up.',NULL,NULL,NULL,NULL,'yeah, it is liked one.',5),(4,'take a leap of faith.',NULL,NULL,NULL,NULL,'liked one content',2);
/*!40000 ALTER TABLE `Post_likepost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Post_reactions`
--

DROP TABLE IF EXISTS `Post_reactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Post_reactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `like` int(11) NOT NULL,
  `favorite` int(11) NOT NULL,
  `dislike` int(11) NOT NULL,
  `share` int(11) NOT NULL,
  `seen` int(11) NOT NULL,
  `comment` varchar(150) NOT NULL,
  `users_id` int(11) NOT NULL,
  `dislike_post_id` int(11) DEFAULT NULL,
  `like_post_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Post_reactions_users_id_aa42fa94_fk_User_customuser_id` (`users_id`),
  KEY `Post_reactions_dislike_post_id_0daae069_fk_Post_dislikepost_id` (`dislike_post_id`),
  KEY `Post_reactions_like_post_id_df306d93_fk_Post_likepost_id` (`like_post_id`),
  CONSTRAINT `Post_reactions_dislike_post_id_0daae069_fk_Post_dislikepost_id` FOREIGN KEY (`dislike_post_id`) REFERENCES `Post_dislikepost` (`id`),
  CONSTRAINT `Post_reactions_like_post_id_df306d93_fk_Post_likepost_id` FOREIGN KEY (`like_post_id`) REFERENCES `Post_likepost` (`id`),
  CONSTRAINT `Post_reactions_users_id_aa42fa94_fk_User_customuser_id` FOREIGN KEY (`users_id`) REFERENCES `User_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Post_reactions`
--

LOCK TABLES `Post_reactions` WRITE;
/*!40000 ALTER TABLE `Post_reactions` DISABLE KEYS */;
INSERT INTO `Post_reactions` VALUES (1,0,1,0,0,0,'0',2,NULL,1),(2,0,1,0,0,0,'0',3,NULL,1),(3,0,1,0,0,0,'0',5,NULL,1),(4,1,0,0,0,0,'0',5,NULL,1),(5,0,0,1,0,0,'0',2,1,NULL),(6,0,0,0,1,0,'0',2,1,NULL),(7,0,0,0,1,0,'0',2,1,NULL),(8,0,0,0,0,1,'0',2,1,NULL),(9,0,0,0,0,0,'1',3,1,NULL),(10,0,1,0,0,0,'0',5,NULL,2),(11,1,0,0,0,0,'0',3,NULL,1),(12,0,0,0,1,0,'0',2,2,NULL),(13,0,0,0,0,1,'0',2,2,NULL),(14,0,0,0,0,1,'0',3,2,NULL),(15,0,0,0,0,0,'1',4,1,NULL),(16,0,0,0,0,0,'1',4,2,NULL),(17,1,0,0,0,0,'0',2,NULL,1),(18,1,0,0,0,0,'0',2,NULL,2),(19,1,0,0,0,0,'0',2,NULL,3),(20,1,0,0,0,0,'0',2,NULL,4),(21,0,1,0,0,0,'0',3,NULL,2);
/*!40000 ALTER TABLE `Post_reactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_bio`
--

DROP TABLE IF EXISTS `User_bio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_bio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_number` varchar(12) NOT NULL,
  `country` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `website` varchar(255) DEFAULT NULL,
  `me` varchar(30) NOT NULL,
  `like` varchar(50) NOT NULL,
  `dislike` varchar(50) NOT NULL,
  `user_id` int(11) NOT NULL,
  `photo_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `User_bio_user_id_63796aa2_fk_User_customuser_id` (`user_id`),
  CONSTRAINT `User_bio_user_id_63796aa2_fk_User_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `User_customuser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_bio`
--

LOCK TABLES `User_bio` WRITE;
/*!40000 ALTER TABLE `User_bio` DISABLE KEYS */;
INSERT INTO `User_bio` VALUES (1,'7629083245','India','indore',NULL,'I am foody','I like cricket','I don\'t like hockey.',1,NULL),(2,'2309145638','Afghanistan','Kabul','','they are my details','I like everything','I dislike little things.',2,''),(3,'6732091678','Algeria','Algiers','','what should i talk about me','what to do','this is dissappointing',3,''),(4,'5109267430','Burundi','Gitega','','you should love yourself.','I like swimming','staying home',4,''),(5,'9027843590','Cape Verde','Praia','','go do something','ancient art','travelling',5,'');
/*!40000 ALTER TABLE `User_bio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_customuser`
--

DROP TABLE IF EXISTS `User_customuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_customuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  `terms_confirmed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_customuser`
--

LOCK TABLES `User_customuser` WRITE;
/*!40000 ALTER TABLE `User_customuser` DISABLE KEYS */;
INSERT INTO `User_customuser` VALUES (1,'pbkdf2_sha256$36000$6VYkJJ9iXYHi$Aw99wyBeR+6BToYT9zspbh9B+9oTBSMDFaaQlIzIuyA=',NULL,0,'@james123','james','fraser','james@gmail.com',0,1,'2021-04-26 09:48:12.590848','1998-07-30','M',1),(2,'pbkdf2_sha256$36000$S6FPERARkSrQ$18shlyEACxtmcGFdGr5vHnexLGafzMVSHnEUcIRbW/s=',NULL,0,'@claire123','claire','fraser','claire@gmail.com',0,1,'2021-05-25 05:32:28.351850','2013-01-01','F',1),(3,'pbkdf2_sha256$36000$dS0BSFHMJOwW$k0yxX3rcfsTElmTO4APNXtPWArEVhZsewu79Q143lMs=',NULL,0,'@devi123','devi','lex','devi@gmail.com',0,1,'2021-05-25 05:45:09.398724','2013-01-01','F',1),(4,'pbkdf2_sha256$36000$eOdiQc6NhT1V$39cpo3zEHDynntVbKNn+9oHPb9U4bbxFY2WmDgNUBxw=',NULL,0,'@adela123','adela','moh','adela@gmail.com',0,1,'2021-05-25 06:56:47.992013','2002-01-01','F',1),(5,'pbkdf2_sha256$36000$rXuiT0mZina6$vkWPaRfwQw+I1oxEvgv5l8bIz3luu0qr2KGpdEtUVmQ=',NULL,0,'@kat123','kat','hom','kat@gmail.com',0,1,'2021-05-25 07:04:16.144971','2007-01-01','F',1);
/*!40000 ALTER TABLE `User_customuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_customuser_groups`
--

DROP TABLE IF EXISTS `User_customuser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_customuser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_customuser_groups_customuser_id_group_id_21ba2504_uniq` (`customuser_id`,`group_id`),
  KEY `User_customuser_groups_group_id_b8843172_fk_auth_group_id` (`group_id`),
  CONSTRAINT `User_customuser_grou_customuser_id_c1abc90e_fk_User_cust` FOREIGN KEY (`customuser_id`) REFERENCES `User_customuser` (`id`),
  CONSTRAINT `User_customuser_groups_group_id_b8843172_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_customuser_groups`
--

LOCK TABLES `User_customuser_groups` WRITE;
/*!40000 ALTER TABLE `User_customuser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_customuser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_customuser_user_permissions`
--

DROP TABLE IF EXISTS `User_customuser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_customuser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customuser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `User_customuser_user_per_customuser_id_permission_c61a8425_uniq` (`customuser_id`,`permission_id`),
  KEY `User_customuser_user_permission_id_16b8366c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `User_customuser_user_customuser_id_b0a30bb5_fk_User_cust` FOREIGN KEY (`customuser_id`) REFERENCES `User_customuser` (`id`),
  CONSTRAINT `User_customuser_user_permission_id_16b8366c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_customuser_user_permissions`
--

LOCK TABLES `User_customuser_user_permissions` WRITE;
/*!40000 ALTER TABLE `User_customuser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `User_customuser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
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
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add content type',3,'add_contenttype'),(8,'Can change content type',3,'change_contenttype'),(9,'Can delete content type',3,'delete_contenttype'),(10,'Can add bio',4,'add_bio'),(11,'Can change bio',4,'change_bio'),(12,'Can delete bio',4,'delete_bio'),(13,'Can add user',5,'add_customuser'),(14,'Can change user',5,'change_customuser'),(15,'Can delete user',5,'delete_customuser'),(16,'Can add log entry',6,'add_logentry'),(17,'Can change log entry',6,'change_logentry'),(18,'Can delete log entry',6,'delete_logentry'),(19,'Can add session',7,'add_session'),(20,'Can change session',7,'change_session'),(21,'Can delete session',7,'delete_session'),(22,'Can add Token',8,'add_token'),(23,'Can change Token',8,'change_token'),(24,'Can delete Token',8,'delete_token'),(25,'Can add dislike post',9,'add_dislikepost'),(26,'Can change dislike post',9,'change_dislikepost'),(27,'Can delete dislike post',9,'delete_dislikepost'),(28,'Can add reactions',10,'add_reactions'),(29,'Can change reactions',10,'change_reactions'),(30,'Can delete reactions',10,'delete_reactions'),(31,'Can add like post',11,'add_likepost'),(32,'Can change like post',11,'change_likepost'),(33,'Can delete like post',11,'delete_likepost');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_User_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `User_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('3550e4d9015ceb43d9853c3f43a9b5db956070bf','2021-05-25 07:31:31.916140',4),('500f55edd5fd0123f18b0707d8e6ec9fb9d9404d','2021-05-25 07:18:27.859418',1),('6dad47db8113d90792391a08b2eea8b9c1e02c72','2021-05-25 07:32:14.399819',5),('ade0c5a01c360dabd6eefa74297dd259dc5e9e79','2021-05-25 07:21:27.893944',2),('c77e54d5414f4aebc3d5b1ce395ea051ad5d3897','2021-05-25 07:30:45.711024',3);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
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
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_User_customuser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_User_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `User_customuser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (6,'admin','logentry'),(2,'auth','group'),(1,'auth','permission'),(8,'authtoken','token'),(3,'contenttypes','contenttype'),(9,'Post','dislikepost'),(11,'Post','likepost'),(10,'Post','reactions'),(7,'sessions','session'),(4,'User','bio'),(5,'User','customuser');
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-26 09:45:09.552660'),(2,'contenttypes','0002_remove_content_type_name','2021-04-26 09:45:09.779181'),(3,'auth','0001_initial','2021-04-26 09:45:10.566396'),(4,'auth','0002_alter_permission_name_max_length','2021-04-26 09:45:10.593695'),(5,'auth','0003_alter_user_email_max_length','2021-04-26 09:45:10.607588'),(6,'auth','0004_alter_user_username_opts','2021-04-26 09:45:10.622120'),(7,'auth','0005_alter_user_last_login_null','2021-04-26 09:45:10.630192'),(8,'auth','0006_require_contenttypes_0002','2021-04-26 09:45:10.638449'),(9,'auth','0007_alter_validators_add_error_messages','2021-04-26 09:45:10.649221'),(10,'auth','0008_alter_user_username_max_length','2021-04-26 09:45:10.655284'),(11,'User','0001_initial','2021-04-26 09:45:11.904980'),(12,'admin','0001_initial','2021-04-26 13:27:22.304730'),(13,'admin','0002_logentry_remove_auto_add','2021-04-26 13:27:22.331969'),(14,'authtoken','0001_initial','2021-04-26 13:27:22.550817'),(15,'authtoken','0002_auto_20160226_1747','2021-04-26 13:27:22.769644'),(16,'sessions','0001_initial','2021-04-26 13:27:22.888296'),(17,'User','0002_auto_20210430_0650','2021-04-30 06:51:54.198389'),(18,'Post','0001_initial','2021-05-01 12:03:14.136456'),(19,'Post','0002_auto_20210525_1536','2021-05-25 15:36:45.508183');
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
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-28 20:14:41
