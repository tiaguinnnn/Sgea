CREATE TABLE Usuario (
id_usuario INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
nome_usuario VARCHAR(100) NOT NULL,
senha CHAR(64) NOT NULL
);

CREATE TABLE Estoque (
id_estoque INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
qtd_produto INT NOT NULL,
id_produto INT NOT NULL,
FOREIGN KEY (id_produto) REFERENCES Produto (id_produto)
);

CREATE TABLE Produto (
id_produto INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
nome_produto VARCHAR(100) NOT NULL,
data_validade DATE NOT NULL,
categoria VARCHAR(50) NOT NULL,
localidade VARCHAR(30) NOT NULL,
preco DECIMAL NOT NULL
);

SELECT  nome_produto, categoria, preco, localidade, qtd_produto FROM Produto as P
INNER JOIN Estoque AS E ON P.id_produto = E.id_produto
;







