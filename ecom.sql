-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 14, 2021 at 01:28 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecom`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(50) NOT NULL,
  `product_name` varchar(200) NOT NULL,
  `product_desc` varchar(500) NOT NULL,
  `product_cost` int(11) NOT NULL,
  `product_discount` varchar(50) NOT NULL,
  `product_category` varchar(50) NOT NULL,
  `product_brand` varchar(50) NOT NULL,
  `image_url` varchar(500) NOT NULL,
  `color` text NOT NULL,
  `top_brand` text NOT NULL DEFAULT 'No',
  `top_deal` text NOT NULL DEFAULT 'No',
  `date_added` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `product_name`, `product_desc`, `product_cost`, `product_discount`, `product_category`, `product_brand`, `image_url`, `color`, `top_brand`, `top_deal`, `date_added`) VALUES
(1, 'Nike Shoe', 'Nike Air Jordan. Mens Type', 6000, '10%', 'Men', 'Nike', 'nike1.png', 'White', 'Yes', 'No', '2021-10-14 06:03:21'),
(2, 'Air Jordans', 'Classic Air Jordan\'s suited for female', 6500, '5%', 'Female Wear', 'Jordans', 'nike2.png', 'Pink', 'No', 'yes', '2021-10-14 06:03:21'),
(3, 'Mc Clarens', 'Cool Mclarens Wear', 5500, '6%', 'Athletic', 'Mc claren', 'nike3.png', 'Black', 'yes', 'No', '2021-10-14 06:11:00'),
(4, 'Air Max', 'An athletic Air max shoes', 7000, '10%', 'Men Trainer', 'Air Max', 'airmax2.png', 'Black', 'No', 'yes', '2021-10-14 06:11:00'),
(5, 'Canon Camera', 'Canon Camera with a high picture pixel', 30000, '5%', 'electronic', 'Canon', 'camera.jpg', 'Black', 'yes', 'No', '2021-10-14 06:24:17'),
(6, 'Manchester United Jersey', 'New Latest Away Manchester United Jersey', 2000, '5%', 'Jersey', 'Clothing', 'jersey.jpeg', 'Blue', 'No', 'yes', '2021-10-14 06:24:17');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
