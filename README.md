# Sobre o projeto
Este projeto foi realizado para o processo seletivo da entidade **Mileage** do **Insper**.

---

## Tecnologias e linguagens utilizadas
- Python
- Flask
- HTML
- CSS
- SCSS
- jQuery
- Chart.Js

---

## Como acessar
- A aplicação está hospedada no Heroku. [clique aqui para acessar!](https://mileage-case.herokuapp.com/) ou utilize este link https://mileage-case.herokuapp.com/

---

## Rotas da API

- /api/info 
  - Retorna a listagem de todos os carros **caso nenhum filtro tenha sido aplicado**.
- /api/motor
  - Permite filtrar os carros a partir do valor do motor. Nessa requisição um parâmetro deve ser passado:
    - Motor
- /api/add
  - Permite adicionar um carro novo à lista. Nessa requisição quatro parâmetros devem ser passados:
    - Modelo;
    - Velocidade máxima;
    - Motor;
    - Marca
- /api/change
  - Permite alterar o valor do motor de um determinado modelo. Dois parâmetros são exigidos:
    - Modelo;
    - Motor
- /api/delete
  - Permite deletar modelo específico. Exige um parâmetro:
    - Modelo;

**Neste modelo não foi implementado um sistema de autenticação para chamadas na API. Esse modelo NÃO FOI FEITO PARA SER USADO EM PRODUÇÃO.**



