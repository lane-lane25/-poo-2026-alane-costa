/* global use, db */
// Alunof: Alane Figueredo Costa
// Turma: 2A TI
// Componente: Banco de Dados | 2ª Série Técnico
// Professor: Brian Samuel

use("AlaneFCosta_DB");

// PARTE 1: Atualizações com updateOne e updateMany
// Ajuste o _id do exemplo para o identificador de um produto existente.
db.getCollection("produtos").updateOne(
  { "_id": "PROD-001" },
  { $set: { "preco": 199.90 } }
);

db.getCollection("produtos").updateMany(
  { "estoque": { $gt: 5 } },
  { $set: { "status_promocao": "ativo" } }
);

// PARTE 2: Operadores de Modificação e Comparação
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

// PARTE 3: Exclusão e Pergunta de Aprofundamento
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
