USE robometrics_prod;

CREATE TABLE cargos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE permissoes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE cargos_permissoes (
  id_cargo INT NOT NULL,
  id_permissao INT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_cargo, id_permissao),
  FOREIGN KEY (id_cargo) REFERENCES cargos(id),
  FOREIGN KEY (id_permissao) REFERENCES permissoes(id)
);


CREATE TABLE equipes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  equipe VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE usuarios (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  senha VARCHAR(255) NOT NULL,
  id_cargo INT NOT NULL,
  id_equipe INT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (id_cargo) REFERENCES cargos(id),
  FOREIGN KEY (id_equipe) REFERENCES equipes(id)
);


CREATE TABLE robos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_equipe INT NOT NULL,
  tipo VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (id_equipe) REFERENCES equipes(id)
);


CREATE TABLE sensores (
  id INT PRIMARY KEY AUTO_INCREMENT,
  sensores VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE robos_sensores (
  id_robo INT NOT NULL,
  id_sensores INT NOT NULL,
  periodo_ativacao DATE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id_robo, id_sensores),
  FOREIGN KEY (id_robo) REFERENCES robos(id),
  FOREIGN KEY (id_sensores) REFERENCES sensores(id)
);


CREATE TABLE pistas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  pista VARCHAR(255) NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


CREATE TABLE corridas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  id_pista INT NOT NULL,
  id_robos INT NOT NULL,
  log_corrida VARCHAR(255),
  P FLOAT,
  I FLOAT,
  D FLOAT,
  tempo FLOAT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (id_pista) REFERENCES pistas(id),
  FOREIGN KEY (id_robos) REFERENCES robos(id)
);


INSERT INTO cargos (nome) VALUES ('Engenheiro'), ('Programador'), ('Analista');


INSERT INTO permissoes (nome) VALUES ('Admin'), ('Editor'), ('Viewer');


INSERT INTO cargos_permissoes (id_cargo, id_permissao) VALUES
  (1, 1), (1, 2), (2, 2), (3, 3);


INSERT INTO equipes (equipe) VALUES ('Equipe A'), ('Equipe B'), ('Equipe C');


INSERT INTO usuarios (nome, email, senha, id_cargo, id_equipe) VALUES
  ('Carlos Souza', 'carlossouza@teste.com', '123456', 1, 1),
  ('Fernanda Lima', 'fernandalima@teste.com', '123456', 2, 2),
  ('Paulo Mendes', 'paulomendes@teste.com', '123456', 3, 3);


INSERT INTO robos (id_equipe, tipo) VALUES
  (1, 'Robo Tipo A'), 
  (2, 'Robo Tipo B'), 
  (3, 'Robo Tipo C');


INSERT INTO sensores (sensores) VALUES ('Sensor A'), ('Sensor B'), ('Sensor C');


INSERT INTO robos_sensores (id_robo, id_sensores, periodo_ativacao) VALUES
  (1, 1, '2024-05-01'), 
  (2, 2, '2024-05-02'), 
  (3, 3, '2024-05-03');


INSERT INTO pistas (pista) VALUES ('Pista A'), ('Pista B'), ('Pista C');


INSERT INTO corridas (id_pista, id_robos, log_corrida, P, I, D, tempo) VALUES
  (1, 1, 'Log 1', 1.1, 1.2, 1.3, 30.5),
  (2, 2, 'Log 2', 2.1, 2.2, 2.3, 25.0),
  (3, 3, 'Log 3', 3.1, 3.2, 3.3, 20.8);




SELECT 
  usuarios.nome AS Usuario, 
  equipes.equipe AS Equipe
FROM usuarios
INNER JOIN equipes ON usuarios.id_equipe = equipes.id;


SELECT 
  robos.tipo AS Robo, 
  equipes.equipe AS Equipe
FROM robos
INNER JOIN equipes ON robos.id_equipe = equipes.id;


SELECT 
  usuarios.nome AS Usuario, 
  cargos.nome AS Cargo
FROM usuarios
INNER JOIN cargos ON usuarios.id_cargo = cargos.id;


SELECT 
  robos.tipo AS Robo, 
  sensores.sensores AS Sensor, 
  robos_sensores.periodo_ativacao AS Periodo_Ativacao
FROM robos
INNER JOIN robos_sensores ON robos.id = robos_sensores.id_robo
INNER JOIN sensores ON robos_sensores.id_sensores = sensores.id;


SELECT 
  usuarios.nome AS Usuario, 
  cargos.nome AS Cargo, 
  permissoes.nome AS Permissao
FROM usuarios
INNER JOIN cargos ON usuarios.id_cargo = cargos.id
INNER JOIN cargos_permissoes ON cargos.id = cargos_permissoes.id_cargo
INNER JOIN permissoes ON cargos_permissoes.id_permissao = permissoes.id;


SELECT 
  corridas.id AS CorridaID,
  pistas.pista AS Pista,
  robos.tipo AS Robo,
  corridas.tempo AS Tempo
FROM corridas
INNER JOIN pistas ON corridas.id_pista = pistas.id
INNER JOIN robos ON corridas.id_robos = robos.id;
