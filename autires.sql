-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-04-2023 a las 06:51:29
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `viodatcadb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autires`
--

CREATE TABLE `autires` (
  `id` int(11) NOT NULL,
  `autor` varchar(60) NOT NULL,
  `cita` varchar(250) NOT NULL,
  `palabras` int(11) NOT NULL,
  `tiempo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `autires`
--

INSERT INTO `autires` (`id`, `autor`, `cita`, `palabras`, `tiempo`) VALUES
(1, 'Mario Benedetti', '“Pero, en definitiva, ¿qué es Lo Nuestro? Por ahora, al menos, es una especie de complicidad frente a otros, un secreto compartido, un pacto unilateral. Naturalmente, esto no es una aventura, ni un programa ni -menos que menos- un noviazgo. Sin embar', 76, 33),
(2, 'Marilyn Monroe', '\"Soy egoísta, impaciente y un poco insegura. Cometo errores, estoy fuera de control y a veces soy difícil de manejar. Pero si no puedes manejarme en mi peor momento, entonces seguro que no me mereces en los mejores.\"', 38, 17),
(3, 'Sigmund Freud', '\"Es imposible escapar a la impresión de que las personas se focalizan en conseguir cosas superfluas, buscan poder, éxito y riqueza para sí mismos, además lo admiran en otros pero subestiman lo que tiene verdadero valor en la vida.\"', 39, 17),
(4, 'George S. Patton', '\"La guerra es la lucha más magnífica que un ser humano puede disfrutar. Saca lo mejor de si mismo; elimina lo que es superficial. Todos los hombres tienen miedo en la guerra. El cobarde es el que deja que su miedo supere su sentido del deber. El debe', 54, 23),
(5, 'Douglas MacArthur', '\"Constrúyeme un hijo, oh Señor, que sea lo suficientemente fuerte para saber cuándo es débil y lo suficientemente valiente para enfrentarse a sí mismo cuando tiene miedo, alguien que se sentirá orgulloso e inflexible en la derrota, y humilde y amable', 55, 24),
(6, 'Ken Follett ', '\"Era un día soleado de principios de verano, y se oía el canto de los pájaros. En un huerto cercano que hasta entonces se había librado de los bombardeos, los manzanos florecían de forma espectacular. El hombre era el único animal que acababa con la ', 113, 50),
(7, 'Stephen Hawking.', '\"Para sobrevivir como especie, a la larga debemos viajar hacia las estrellas, y hoy nos comprometemos con el próximo gran avance del hombre en el cosmos\"', 26, 12),
(8, 'Octavio Paz', '\"Así como del fondo de la música\r\nbrota una nota\r\nque mientras vibra crece y se adelgaza\r\nhasta que en otra música enmudece,\r\nbrota del fondo del silencio\r\notro silencio, aguda torre, espada,\r\ny sube y crece y nos suspende\r\ny mientras sube caen\r\nrecu', 71, 32),
(9, 'Charles Bukowski', '\"Hay cosas peores que\r\nestar solo\r\npero a menudo toma décadas\r\ndarse cuenta de ello\r\ny más a menudo\r\ncuando esto ocurre\r\nes demasiado tarde\r\ny no hay nada peor\r\nque\r\nun demasiado tarde\"', 34, 16),
(10, 'Mac miller', '\"Cuando te sientes triste, está bien. No es el fin del mundo. Todo el mundo tiene esos días en los que dudas de ti mismo y cuando sientes que todo lo que haces apesta, pero luego están esos días en los que te sientes como Superman. Es solo el equilib', 57, 26),
(11, 'Michael jackson', '\"Nación por Nación, todo el mundo debe unirse para hacer frente a los problemas que veamos. Quizás entonces podamos resolverlos de alguna manera. Le pedí un favor a mi vecina. Me dijo \"más tarde\" ¿Que le ha pasado a la gente? ¿Hemos perdido el amor, ', 89, 39),
(12, 'Michael Jackson', '\"Hay un lugar en tu corazón y yo sé que es amor, y este lugar puede ser mucho más brillante mañana. Y si realmente lo intentas encontrarás que no hay necesidad de llorar en este lugar, sentirás que no hay dolor ni penas\"', 43, 20),
(13, 'Michael Jackson', '\"Yo creo que los humanos también tienen capacidad de volar; el problema es que no sabemos concebir los pensamientos adecuados que nos permitirán levitar\"', 24, 11),
(14, 'Michael Jackson', '\"Si no tienes ese recuerdo de amor de la infancia estás condenado a buscar por todo el mundo algo para llenar ese vacío. Pero no importa cuánto dinero ganes o lo famoso que te vuelvas, siempre seguirás sintiéndote vacío\"', 39, 18),
(15, 'Michael Jackson', '\"Cuando los niños escuchan música, no solo escuchan. Se funden en la melodía y fluyen con el ritmo. Algo en el interior comienza a desplegar sus alas, pronto el niño y la música son uno\"', 35, 17);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
