-- Create the bookings table
CREATE TABLE IF NOT EXISTS `bookings` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `driverid` int DEFAULT NULL,
  `vehicleid` int DEFAULT NULL,
  `pakageid` int DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `Aadhar_number` int DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `phone_number` bigint DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  UNIQUE KEY `Aadhar_number` (`Aadhar_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create the driver table
CREATE TABLE IF NOT EXISTS `driver` (
  `Driver_id` int NOT NULL AUTO_INCREMENT,
  `Driver_name` varchar(50) DEFAULT NULL,
  `Aadhar_number` int DEFAULT NULL,
  `Address` varchar(100) DEFAULT NULL,
  `Phone` bigint DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Driver_id`),
  UNIQUE KEY `Aadhar_number` (`Aadhar_number`),
  UNIQUE KEY `Phone` (`Phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create the pakages table
CREATE TABLE IF NOT EXISTS `pakages` (
  `pakage_id` int NOT NULL AUTO_INCREMENT,
  `destinations` varchar(500) DEFAULT NULL,
  `duration` bigint DEFAULT NULL,
  `cost` bigint DEFAULT NULL,
  PRIMARY KEY (`pakage_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create the transaction table
CREATE TABLE IF NOT EXISTS `transaction` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `date_of_transaction` date NOT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Create the vehicles table
CREATE TABLE IF NOT EXISTS `vehicles` (
  `vehicle_id` int NOT NULL AUTO_INCREMENT,
  `vehicle_name` varchar(40) DEFAULT NULL,
  `rent` float DEFAULT NULL,
  `fuel_type` varchar(30) DEFAULT NULL,
  `Average` int DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
