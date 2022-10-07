# Padrão de objetos Singleton
  O padrão de projeto Singleton é um padrão criacional, cujo objetivo é criar apenas uma instância de uma classe e fornecer apenas um ponto global de acesso àquele objeto. Um exemplo comumente usado dessa classe em Java é o calendário, onde você não pode fazer uma instância daquela classe. Ele também usa seu próprio método getInstance()para obter o objeto a ser usado.
  Uma classe usando o padrão de projeto Singleton incluirá:
  - Uma variável estática privada, que contém a única instância da classe.
  - Um construtor privado, de modo a não ser possível instanciá-la de qualquer outro lugar.
  - Um método estático público, para retornar a instância única da classe.