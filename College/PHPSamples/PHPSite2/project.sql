-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 28, 2023 at 09:54 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

CREATE TABLE `authors` (
  `auth_name` varchar(255) NOT NULL,
  `auth_id` int(255) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`auth_name`, `auth_id`) VALUES
('James Dashner', 1),
('Harper Lee', 2),
('Rick Riordan', 3),
('J.K. Rowling', 4),
('Veronica Roth', 5);

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_name` varchar(255) NOT NULL,
  `book_id` int(255) NOT NULL,
  `auth_id` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_name`, `book_id`, `auth_id`) VALUES
('To Kill A Mockingbird', 1, 2),
('The Maze Runner', 2, 1),
('Divergent', 3, 5),
('The Scorch Trials', 4, 1),
('The Death Cure', 5, 1),
('The Fever Code', 6, 1),
('Four', 7, 5),
('Insurgent', 8, 5),
('Allegiant', 9, 5),
('Harry Potter and The Chamber of Secrets', 10, 4),
('Percy Jackson and The Olympians', 11, 3);

-- --------------------------------------------------------

--
-- Table structure for table `my_accounts`
--

CREATE TABLE `my_accounts` (
  `id` int(7) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `my_accounts`
--

INSERT INTO `my_accounts` (`id`, `username`, `password`) VALUES
(1, 'test', '$2y$10$SFkWxwL2j4wiiuWTswKqyuKNT/u5vKDpv1XRQHPU7xtLEgqk.ZtJa'),
(2, 'testa', '$2y$10$7OzXEtrLcfSXAc1CftRzjOieudtNFdWNoamgK99gz33QnKJGdGvqK'),
(3, 'tta', '$2y$10$R4L3Qyb0.Xas1EZox6XBleJR6L7KRzQgLQmTWHOI/vIxZHvM4FH1O'),
(4, 'tttt', '$2y$10$tDLyTGTbQ2YkFLq8uS0Dy.0ikyb7GvzRw4/HenU6hsOlLzDL4c1p.'),
(5, 'ttttt', '$2y$10$r8prepIFy/weqjVHeUdOS.3WWQDX8VX4/uZb.J5aTMK.AdBQScypO'),
(6, 'testb', '$2y$10$g7yIMZxu14H14En3ypRT9uIyp.tG.x9o2fD37RpGF6S58A/Dbsdr.'),
(7, 'testba', '$2y$10$8j3AqcJkx5IYeHF/KIizLex/T62QDbngjXVRsRn56BF94GoUmaEem'),
(8, 'a', '$2y$10$ZbZ4ajKZ77ptDQkQspajFebMG0IvdAszJcgygDdVb167QKmwGtsvy'),
(9, 'aa', '$2y$10$jdAtn4sGGY6pAT6sBrWbtecdxnFr82isBmV5.GFRE7AHoB9Be3xtu'),
(10, 'aaa', '$2y$10$jsTiea1aKHqDhtHVvCdliejmCnzSjZMMpkex0ufOzE6BrFhnH1vP2'),
(13, 'aaaaa', '$2y$10$x3AFapWUW8xzaux5N0QVMuKwdSpFSv3Hhxjfap80emEoifVSxNJMa'),
(16, 'b', '$2y$10$4yiV8Tid3dLJgXi/yb20uuPpSY16LBGRXw3X.PzC8J1snrtQLES6O');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`auth_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `my_accounts`
--
ALTER TABLE `my_accounts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authors`
--
ALTER TABLE `authors`
  MODIFY `auth_id` int(255) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `my_accounts`
--
ALTER TABLE `my_accounts`
  MODIFY `id` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
