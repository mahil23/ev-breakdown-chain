/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - breakdowndb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`breakdowndb` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `breakdowndb`;

/*Table structure for table `assign` */

DROP TABLE IF EXISTS `assign`;

CREATE TABLE `assign` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `m_unit_id` int(11) DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/* Data for the table `assign` */

INSERT INTO `assign` (`id`, `m_unit_id`, `request_id`, `date`, `status`) VALUES
(1, 6, 1, '2023-02-23', 'working'),
(2, 12, 3, '2023-02-23', 'finished'),
(3, 12, 5, '2023-02-23', 'rtty'),
(4, 5, 6, '2023-02-25', 'no location'),
(5, 12, 8, '2023-03-09', 'completed'),
(6, 13, 8, '2023-03-09', 'completed'),
(7, 19, 4, '2023-03-09', 'Assigned'),
(8, 21, 10, '2023-03-09', 'Assigned'),
(9, 19, 9, '2025-03-10', 'Assigned'),
(10, 28, 2, '2025-03-25', 'finished'),
(11, 30, 7, '2025-03-25', 'Assigned'),
(12, 28, 6, '2025-03-26', 'no location'),
(13, 28, 2, '2025-03-26', 'Assigned'),
(14, 28, 1, '2025-03-26', 'Assigned');


/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `bid` int(20) NOT NULL AUTO_INCREMENT,
  `uid` int(20) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `slotid` int(20) DEFAULT NULL,
  `booking_time` varchar(40) DEFAULT NULL,
  `booking_date` varchar(40) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */
INSERT INTO `booking` (`bid`, `uid`, `station_id`, `slotid`, `booking_time`, `booking_date`, `status`) VALUES 
(1, 10, 3, 2, '8-9', '11/2/22', 'Accepted'),
(2, 10, 3, 2, '8-9', '23/4/2009', 'pending'),
(3, 10, 3, 5, '8-9', '34/6/89', 'Accepted'),
(4, 14, 3, 4, '8-9', '12/32/34', 'pending'),
(5, 15, 3, 3, '8-9', '25/2/2023', 'Accepted'),
(6, 10, 3, 4, '8-9', 'rfffee', 'Reject'),
(7, 10, 3, 3, '10-11', 'entho h', 'pending'),
(8, 10, 3, 3, '8-9', 're', 'pending'),
(9, 10, 3, 4, '8-9', 'uiiudkejsjhjj', 'pending'),
(10, 10, 3, 5, '8-9', 'udjjsjjs', 'pending'),
(11, 10, 3, 2, '8-9', '9-3-2023', 'pending'),
(12, 10, 3, 5, '12-13', '14-3-2023', 'Accepted'),
(13, 27, 3, 6, '5-6', '23/3/24', 'Accepted'),
(14, 27, 3, 5, '5-6', '23/3/24', 'pending'),
(15, 15, 3, 2, '8-9', '24-4-25', 'pending'),
(16, 27, 3, 3, '6-7', '3/5/24', 'Accepted'),
(17, 10, 3, 2, '4-5', '23/4/25', 'pending'),
(18, 10, 3, 2, '3-4', '23/4/23', 'Reject');


/*Table structure for table `charging_station` */

DROP TABLE IF EXISTS `charging_station`;

CREATE TABLE `charging_station` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `latitude` varchar(200) DEFAULT NULL,
  `longitude` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `charging_station` */

insert  into `charging_station`(`id`,`lid`,`name`,`place`,`phone`,`email`,`latitude`,`longitude`) values 
(1,3,'electro','kozhikode',9048596789,'nava321@gmail.com','525252','878759'),
(2,9,'current','eranjhipalame',9856234855,'current123@gmail.com','56.8925','578942'),
(3,17,'hindusthan petroleum','kozhikode',9685987589,'hp21@gmail.com','568974','297859');

/*Table structure for table `delivery agent` */

DROP TABLE IF EXISTS `delivery agent`;

CREATE TABLE `delivery agent` (
  `id` int(11) NOT NULL,
  `lid` int(11) DEFAULT NULL,
  `name` varchar(10) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `latitude` bigint(30) DEFAULT NULL,
  `longitude` bigint(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `delivery agent` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `type` varchar(255) DEFAULT 'MECHANIC',
  `date` varchar(10) DEFAULT NULL,
  
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

INSERT INTO `feedback` ( `id`,`lid`, `uid`, `feedback`, `date`, `type`) VALUES
(1, 13, 27, 'nice service', '2025-03-26', 'ev'),
(2, 14, 27, 'nice work guys', '2025-03-26', 'ev'),
(3, 16, 10, 'nice hjob', '2025-03-26', 'mechanic'),
(4, 16, 27, 'new here', '2025-03-26', 'ev'),
(5, 2, 27, 'nice and good', '2025-03-26', 'mechanic'),
(6, 3, 27, 'very late response', '2025-03-26', 'ev');


/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(20) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`location_id`,`lid`,`latitude`,`longitude`) values 
(1,10,11.2577,75.7846),
(2,6,11.2578,75.7846),
(3,12,11.2578,75.7845),
(4,14,11.2575,75.7845),
(5,2,11.2577,75.7846),
(6,13,11.2577,75.7847),
(7,15,11.2578,75.7846),
(8,21,11.2578,75.7845);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','scrypt:32768:8:1$Bf2pSZbbaSYfy5g6$bb8aedfa362b8e8c935e1387758f06709771dcb340cc0b0c39c68a943a55a5cbd2a146e4c516668cb3f896a2da2e915bea3721a22f141e11b8121c3b4f748de0','admin'),
(2,'nava','scrypt:32768:8:1$5vK368WEhjuVbINv$373c18d8884d11cf0130171e4d72cff0732de636347b2820d2db24f27c89744f96ccbdb6e6d8ccdc1904e2e39530fd07606a6289ee8d3dfbc9af12ba7435765e','mechanic'),
(3,'electro','scrypt:32768:8:1$OXBIzqI4rYUcAE20$fef44ec2c8ab7f77a2cfd58661453f9d72a40349bb9773b6a03156412998a066d7d7649a2e199104454ebf30d229f745656da5157ef3ad6e323aaaa1c1a795b8','station'),
(5,'joseph','scrypt:32768:8:1$tv83A6kNRpX7XEm4$d5523c4cf4cf2bd0963499945f36c3c3a13f0e8146245be27f71705c919d958c5626d64e5e2f5b73b6379054a506fcb37365ba0a68c0919560d02cf833a180ff','m_unit'),
(6,'manu','scrypt:32768:8:1$i1mZVDkQfuEj7kZS$fde502504e889c788238f09d10c8229639bfd531bdcb2cdbe3f4a31f6a1144d5caeb8e69ab58cb0c3b070498f85791148d5a5afee25007b7b42c329605be5244','m_unit'),
(7,'james','scrypt:32768:8:1$ATeqhYfmPCF8a1Lp$f5b26e69b53fb98b8486ebfd565bfa5f38ced91e8fffe31267b6ce3ea361d8c40b47ecf79b562972235c52977ddfe841b84d70ceabde750129c4844099e16aac','m_unit'),
(8,'rahul','scrypt:32768:8:1$Ko4kpUhoAmfm9ST9$e02b6496a1c73d20d6b3fd88fcb8ca083756e6b748f596032f6925faad5951b4cfee0221a05752a00ae738ea26652055f89b8c3cdaca6d26dbb6fdcf0f579fbb','mechanic'),
(9,'current','scrypt:32768:8:1$l3l3REJII19MWisj$84d9b92db2fa6e427322ef350f044e3669c3f4234808939e1eeb7d856e36a39fa5d3e947691db4d2e89b4bf09cbe871b54a6b425f10e56e05edd3642a505a10d','station'),
(10,'amith','scrypt:32768:8:1$0F9x6r6lotFh1SG7$7dd67f3c9541aef9e56cbbdbf83e36434585f1c7e468191d51f7bdb4a95461d3a902be51dff0841098dcb4e1c495874d130e8ada42bedab9d1289ead0352feb3','user'),
(11,'afnan','scrypt:32768:8:1$xpt04apMk17yuRfG$b9e2074344523ac4a0d99ba9e1f13b590b2fb80af05c6619f8a09f3a4c21ae91cec4b6b10d6b6200763afc02887e34bda85fffcda6872315aac440963e3fb282','mechanic'),
(12,'mohan','scrypt:32768:8:1$VqC4PhE34mzrfuc5$7936abc52ea050a25e9e70157b707f63e020dca6e3152b2f31fa1799c454d76a5a1ea6f72006433a66cb8bd8113cd71ea5c2929a8b5e3753aa4764ecb0cd085d','m_unit'),
(13,'jack','scrypt:32768:8:1$wFDbgHFwScU9doYs$1a6126b8c2803b5cb3e29aab4889e8d2114e497aec4059c40a5697c6daaeb49c3d744a4ad3059f649acf1b6c7cc8a7e9dc54fb90814b7056938c3d8e9a6849b4','m_unit'),
(14,'Navaneeth','scrypt:32768:8:1$oDB3TM27bZFi8B8a$a6df67770750fd7a6ba11fbbc4417fbb164bc6c569f9bccbd8a6b6ce6271ce9287e9586b028ecf510a6abe9db9f932d9496a769e0c2572dd03dad78119fc9d03','user'),
(15,'user','scrypt:32768:8:1$DFGEtX8x1M9KZr1u$6a1555439a769756ed61a7fdf4e2a21c29acd42e387ff8dec4a90ce8577ef5caeaebb3a1df2a6a505248e5c404bfde1ca763bc0d1cb9b86aef08d17a2577e8ec','user'),
(16,'today','scrypt:32768:8:1$0QxAynZeMEG8wAh3$b37a336a1e9376f9000b2b72067e7a94e27be17b6889f4fbeede2bacd141822091388219378c64992f4587593652e3ba4885fb7319a3e8afeaca372e24647589','mechanic'),
(17,'hp123','scrypt:32768:8:1$UtIErUtOEudoTRFe$a6e9f9bb3b1a7db2388c016c156252d4061ef16c0f98f64252e60e0d274892f42ae713e7f7d621c9cb940115370f9705d351053b0df68e73458be1488520d094','pending'),
(18,'mech','scrypt:32768:8:1$Owstjr7qwxVRQSx1$617239c4317f40180366732f87f93e8f8cb2870363447f0391b43469a4371992873a7442d70b0c8a2c09313386da33573b110e4509894a4e10f7533638e33f1e','pending'),
(19,'uiui','scrypt:32768:8:1$yiMR71KCSqj8QlHN$72042d72d75d48c66666bf8f182d2cc46eb573d01258ec917a66258d2325dacd84857da1f9eff86cad0005a8208f93db92a3860c9d38c90de6d7c70d1dde697d','m_unit'),
(20,'janas','scrypt:32768:8:1$1BaQijapnJMZKwjt$4495367f999f5b421e93ce393f5a7d5efa4edf31b0e0ede4cb2e5d6f98dcb46fa1696263e2414a5c8950dcd590409fad16ff1546dd8966061767a7af38c39e6b','user'),
(21,'manoj','scrypt:32768:8:1$TPO3r6uYKAAPxPuC$c34fe2a137867b25264c4f5833868afd384fca5129f071428bbc65eee84a8761959c672eba4ef57821ffc456179eca65c3b2fbe95facd87094564f6f2c4e127e','m_unit');

/*Table structure for table `mechanic` */

DROP TABLE IF EXISTS `mechanic`;

CREATE TABLE `mechanic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(10) DEFAULT NULL,
  `lname` varchar(10) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `m_latitude` varchar(50) DEFAULT NULL,
  `m_longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `mechanic` */

insert  into `mechanic`(`id`,`lid`,`fname`,`lname`,`phone`,`email`,`m_latitude`,`m_longitude`) values 
(1,2,'navan','nava',9056568925,'navaneeth4322@gmail.','565656','525252'),
(2,8,'rahul','r',8956234795,'rahul123@gmail.com','565628','789568'),
(3,11,'afnan','afnan',9865748523,'afnan123@gmail.com','589856','569852'),
(4,16,'today','today',9048992459,'navaneeth4322@gmail.','525252','789568'),
(5,18,'mech','mech',9265895986,'navaneeth4322@gmail.','589785','848844');

/*Table structure for table `mobile_unit` */

DROP TABLE IF EXISTS `mobile_unit`;

CREATE TABLE `mobile_unit` (
  `uid` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `driver` varchar(20) DEFAULT NULL,
  `vehicle_num` varchar(100) DEFAULT NULL,
  `station_id` int(20) DEFAULT NULL,
  `capacity` int(100) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `mobile_unit` */

insert  into `mobile_unit`(`uid`,`lid`,`driver`,`vehicle_num`,`station_id`,`capacity`) values 
(2,5,'joseph','kl 69665',3,18),
(3,6,'manu','kl 5986',3,56),
(4,7,'james','kl 5987',3,45),
(5,12,'mohan','kl 2564',9,45),
(6,13,'jack','kl 5897',9,67),
(7,19,'ravi','kl 354647',9,55),
(8,21,'manoj','kl 45453',9,45);

/*Table structure for table `mobilunitrequest` */

DROP TABLE IF EXISTS `mobilunitrequest`;

CREATE TABLE `mobilunitrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `m_unitid` int(11) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `status` varchar(40) DEFAULT NULL,
  `latitude` varchar(202) DEFAULT NULL,
  `longitude` varchar(220) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `mobilunitrequest` */

insert  into `mobilunitrequest`(`id`,`uid`,`m_unitid`,`date`,`status`,`latitude`,`longitude`) values 
(1,10,6,'2023-02-23','working ','11.25701984','75.78453681'),
(2,10,5,'2023-02-23','pending','11.25777155','75.7845838'),
(3,10,12,'2023-02-23','rtty','11.25776651','75.78458788'),
(4,14,13,'2023-02-23','pending','11.25730752','75.78451307'),
(5,14,12,'2023-02-23','done','11.25738817','75.78446263'),
(6,15,5,'2023-02-25','dobe','',''),
(7,10,6,'2023-03-09','pending','',''),
(8,10,12,'2023-03-09','god','11.257736666666665','75.78448833333333'),
(9,10,13,'2023-03-09','pending','11.25773','75.78453833333333'),
(10,15,21,'2023-03-09','ready aayo','11.257773333333335','75.78459833333334');

/*Table structure for table `request mechanic` */

DROP TABLE IF EXISTS `request mechanic`;

CREATE TABLE `request mechanic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `mid` int(11) DEFAULT NULL,
  `request` varchar(50) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `latitude` bigint(30) DEFAULT NULL,
  `longitude` bigint(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

/*Data for the table `request mechanic` */

insert  into `request mechanic`(`id`,`uid`,`mid`,`request`,`date`,`status`,`latitude`,`longitude`) values 
(1,10,2,'tyre poi','2023-02-23','Accepted',11,76),
(2,10,2,'glass potti','2023-02-23','Accepted',0,0),
(3,10,2,'demo','2023-02-23','reject',11,76),
(4,10,2,'ll','2023-02-23','Accepted',11,76),
(5,10,2,'petrol leak','2023-02-23','pending',11,76),
(6,14,11,'car washing ','2023-02-23','reject',11,76),
(7,14,11,'car washing ','2023-02-23','reject',11,76),
(8,14,11,'car washing ','2023-02-23','pending',11,76),
(9,14,2,'demo','2023-02-23','pending',11,76),
(10,15,11,'user tyre noncat','2023-02-25','pending',0,0),
(11,15,2,'testtoday','2023-02-25','pending',0,0),
(12,15,11,'eda','2023-02-25','pending',0,0),
(13,15,8,'da demo','2023-02-25','pending',0,0),
(14,15,2,'navademo','2023-02-25','pending',0,0),
(15,15,11,'demo','2023-02-25','pending',11,76),
(16,15,16,'work aavane','2023-02-25','pending',11,76),
(17,15,16,'ith work aavum','2023-02-25','pending',0,0),
(18,15,16,'god','2023-02-25','pending',0,0),
(19,15,16,'dey','2023-02-25','pending',0,0),
(20,15,2,'beeyum','2023-02-25','pending',0,0),
(21,10,8,'glass brok','2023-02-25','pending',0,0),
(22,10,16,'oil change','2023-02-25','pending',0,0),
(23,10,16,'26 test','2023-02-26','pending',0,0),
(24,10,11,'ghh','2023-03-09','pending',0,0),
(25,10,11,'dudidi','2023-03-09','pending',0,0),
(26,10,16,'test ','2023-03-09','pending',0,0),
(27,10,16,'test 2','2023-03-09','pending',0,0),
(28,10,16,'test 3','2023-03-09','pending',0,0),
(29,10,16,'puthiyath','2023-03-09','pending',11,76),
(30,10,16,'hi','2023-03-09','pending',11,76),
(31,10,8,'panchar','2023-03-09','pending',11,76),
(32,10,8,'panchar','2023-03-09','pending',11,76);

/*Table structure for table `slot` */

DROP TABLE IF EXISTS `slot`;

CREATE TABLE `slot` (
  `slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_id` int(20) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `slot_number` varchar(100) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `slot` */

insert  into `slot`(`slot_id`,`station_id`,`type`,`slot_number`,`details`) values 
(2,3,'slow','23','ev'),
(3,3,'fast','88','elec'),
(4,9,'slow','58','22w'),
(5,9,'fast','22','55w'),
(6,9,'fast','s4','sdsefs');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(500) DEFAULT NULL,
  `lname` varchar(500) DEFAULT NULL,
  `place` varchar(500) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `post` varchar(500) DEFAULT NULL,
  `email` varchar(500) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`lid`,`fname`,`lname`,`place`,`pin`,`post`,`email`,`phone`) values 
(1,10,'amith','k','Calicut ',673612,'calicut','amithk@gmail.com',9087986754),
(2,14,'Navaneeth','b','8/2',673616,'chelannur','Navaneeth4322@gmail.com',9876768976),
(3,15,'user','user','user',786576,'useresh','user123@gmail.com',9087654567),
(4,20,'janas','janas','chelannur',673616,'jsjskoshiku','jhsjsj@gmail.com',9087907667);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
