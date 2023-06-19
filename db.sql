-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 19-Jun-2023 às 22:00
-- Versão do servidor: 10.4.25-MariaDB
-- versão do PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `crud`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `numerostelefone`
--

CREATE TABLE `numerostelefone` (
  `ID` int(11) NOT NULL,
  `Numero` varchar(20) DEFAULT NULL,
  `CPF_pessoa` varchar(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `numerostelefone`
--

INSERT INTO `numerostelefone` (`ID`, `Numero`, `CPF_pessoa`) VALUES
(2, '123444', '123456789'),
(3, '4444', '1313212');

-- --------------------------------------------------------

--
-- Estrutura da tabela `pessoas`
--

CREATE TABLE `pessoas` (
  `CPF` varchar(11) NOT NULL,
  `Nome` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `pessoas`
--

INSERT INTO `pessoas` (`CPF`, `Nome`) VALUES
('1234', 'Teste22'),
('123456789', 'Teste53'),
('1313212', 'jose');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `numerostelefone`
--
ALTER TABLE `numerostelefone`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CPF_pessoa` (`CPF_pessoa`);

--
-- Índices para tabela `pessoas`
--
ALTER TABLE `pessoas`
  ADD PRIMARY KEY (`CPF`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `numerostelefone`
--
ALTER TABLE `numerostelefone`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `numerostelefone`
--
ALTER TABLE `numerostelefone`
  ADD CONSTRAINT `numerostelefone_ibfk_1` FOREIGN KEY (`CPF_pessoa`) REFERENCES `pessoas` (`CPF`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
