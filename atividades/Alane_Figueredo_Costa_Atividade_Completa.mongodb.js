/* global use, db */
// Alunof: Alane Figueredo Costa
// Turma: 2A TI
// Componente: Banco de Dados | 2ª Série Técnico
// Professor: Brian Samuel

use("LojaVirtual_DB");

// ETAPA 1 — SEMANA 2: Modelagem NoSQL e documentos incorporados
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

// ETAPA 2 — SEMANA 4: Atualizações com updateOne e updateMany
// Ajuste o _id do exemplo para o identificador de um produto existente.
db.getCollection("produtos").updateOne(
  { "_id": "PROD-001" },
  { $set: { "preco": 199.90 } }
);

db.getCollection("produtos").updateMany(
  { "estoque": { $gt: 5 } },
  { $set: { "status_promocao": "ativo" } }
);

// Operadores de modificação e comparação
// O $push acrescenta uma tag sem remover as que já existem.
db.getCollection("produtos").updateOne(
  { "_id": "PROD-001" },
  { $push: { "tags": "liquidacao" } }
);

db.getCollection("produtos").find({
  "preco": { $lt: 150.00 }
});

db.getCollection("produtos").find({
  "categoria": { $in: ["Periféricos", "Monitores"] }
});

// Exclusão
// ID reservado como exemplo de produto de teste; ajuste-o se necessário.
db.getCollection("produtos").deleteOne({
  "_id": "PROD-TESTE-001"
});

// Atenção: remove todos os produtos cujo estoque seja exatamente zero.
db.getCollection("produtos").deleteMany({
  "estoque": 0
});

// Aprofundamento: replaceOne substitui o documento inteiro. Campos omitidos,
// inclusive dados importantes adicionados por outros processos, podem ser
// apagados. Já updateOne com $set altera somente os campos indicados e mantém
// os demais. No updateOne, use operadores de atualização como $set.
