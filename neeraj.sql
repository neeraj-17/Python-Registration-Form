-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 20, 2019 at 06:07 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `neeraj`
--

-- --------------------------------------------------------

--
-- Table structure for table `nnn`
--

CREATE TABLE `nnn` (
  `First_name` varchar(10) NOT NULL,
  `Last_name` varchar(10) NOT NULL,
  `Student_ID` varchar(10) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Contact` int(15) NOT NULL,
  `Email` varchar(25) NOT NULL,
  `Roll_no` int(10) NOT NULL,
  `Address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `nnn`
--

INSERT INTO `nnn` (`First_name`, `Last_name`, `Student_ID`, `Gender`, `DOB`, `Contact`, `Email`, `Roll_no`, `Address`) VALUES
('', '', '', 'Select Gen', '0000-00-00', 1234567890, 'nnn@fas.com', 0, '\n'),
('neeraj', 'dumbare', '123456', '   MALE   ', '0000-00-00', 1234567890, 'neeraj@dumbare.com', 9, 'new panvel..\n'),
('neeraj', 'dumbare', '123456', '   MALE   ', '2001-12-01', 1234567890, 'neeraj@dumbare.com', 9, 'new panvel..\n'),
('NNN', 'DDD', '1234567890', '   MALE   ', '2012-12-01', 1234567890, 'neeee@fffff.com', 11, 'E-1\n'),
('', '', '', 'Select Gen', '0000-00-00', 1234567890, 'dsds@sdsd.dff', 0, '\n'),
('jksjhkj', '', '', 'Select Gen', '0000-00-00', 1234567890, 'asjjhxdajh@jajd', 0, '\n'),
('', '', '', 'Select Gen', '0000-00-00', 1243765890, 'zjhcjhadjh@jwsjhj', 0, '\n'),
('Neraj', 'dumbare', '234567', '   MALE   ', '0000-00-00', 1234567890, 'fasfd@fasdf.com', 3, 'rajuri\n');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
