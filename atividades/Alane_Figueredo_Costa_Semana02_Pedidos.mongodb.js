/* global use, db */
// Alunof: Alane Figueredo Costa
// Turma: 2A TI
// Componente: Banco de Dados | 2ª Série Técnico
// Professor: Brian Samuel

use("LojaVirtual_DB");

db.getCollection("pedidos").insertOne({
  "_id": "PED-10045",
  "data_pedido": "2026-10-18",
  "status": "Entregue",
  "valor_total": 450.00,
  "cliente": {
    "nome": "João Silva",
    "email": "joao.silva@email.com",
    "endereco_entrega": {
      "rua": "Rua das Flores",
      "numero": "123",
      "bairro": "Centro",
      "cidade": "São Paulo"
    }
  },
  "itens": [
    {
      "produto": "Teclado mecânico",
      "quantidade": 1,
      "preco_unitario": 300.00
    },
    {
      "produto": "Mouse sem fio",
      "quantidade": 2,
      "preco_unitario": 75.00
    }
  ]
});

// Reflexão: A incorporação reúne os dados relacionados em um único documento,
// permitindo recuperar o pedido completo em uma só leitura, sem JOINs entre
// várias tabelas. Isso simplifica e pode acelerar as consultas; em contrapartida,
// os dados incorporados podem ser duplicados e exigem cuidado ao atualizá-los.
