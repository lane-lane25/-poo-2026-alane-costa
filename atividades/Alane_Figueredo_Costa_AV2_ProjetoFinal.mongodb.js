/* global use, db */
// ============================================================================
// PROJETO FINAL AV2 — MONGODB / NOSQL
// Aluna: Alane Figueredo Costa | Turma: 2A TI
// Disciplina: Banco de Dados | Professor: Brian Samuel
// Cenário Escolhido: Opção C — E-Commerce de Tecnologia e Hardware
//
// JUSTIFICATIVA ARQUITETURAL (README):
// O modelo NoSQL orientado a documentos (MongoDB) é ideal para um E-Commerce de
// Tecnologia devido à sua flexibilidade de esquema (schema-less). Produtos de
// hardware possuem especificações técnicas totalmente distintas (um monitor
// tem polegadas e Hz; um teclado tem tipo de switch e layout; um SSD tem
// velocidade de leitura). Em um banco relacional (SQL), isso exigiria dezenas
// de tabelas auxiliares ou colunas nulas. Além disso, os documentos incorporados
// permitem salvar o pedido completo (cliente + endereço + array de itens) em
// um único registro, eliminando JOINs complexos e garantindo escalabilidade
// horizontal para alto volume de acessos.
// ============================================================================

// Seleciona/cria o banco exclusivo no cluster da turma
use("Alane_EcommerceTech_DB");

// Limpa as coleções antes de rodar (garante que o script rode do início ao fim sem erro de ID duplicado)
db.pedidos.drop();
db.produtos.drop();

// ============================================================================
// ETAPA 1: ARQUITETURA, MODELAGEM E POVOAMENTO (insertOne e insertMany)
// Requisito: 2 coleções, mínimo 8 documentos, objetos aninhados {}, arrays []
// e demonstração de schema-less.
// ============================================================================

// 1.1 Inserindo 1 pedido com insertOne() (Documento incorporado + Array de itens)
db.pedidos.insertOne({
  "_id": "PED-10045",
  "data_pedido": "2026-11-10",
  "status": "Concluido",
  "valor_total": 450.00,
  "cliente": {
    "nome": "João Silva",
    "email": "joao.silva@email.com",
    "cidade": "São Paulo",
    "endereco_entrega": {
      "rua": "Rua das Flores",
      "numero": "123",
      "bairro": "Centro"
    }
  },
  "itens": [
    { "produto": "Teclado Mecânico", "quantidade": 1, "preco_unitario": 300.00 },
    { "produto": "Mouse Sem Fio", "quantidade": 2, "preco_unitario": 75.00 }
  ]
});

// 1.2 Inserindo mais 3 pedidos com insertMany()
db.pedidos.insertMany([
  {
    "_id": "PED-10046",
    "data_pedido": "2026-11-12",
    "status": "Concluido",
    "valor_total": 1850.00,
    "cliente": {
      "nome": "Mariana Costa",
      "email": "mari.costa@email.com",
      "cidade": "Campinas",
      "endereco_entrega": { "rua": "Av. Brasil", "numero": "500", "bairro": "Guanabara" }
    },
    "itens": [
      { "produto": "Monitor Gamer 27", "quantidade": 1, "preco_unitario": 1850.00 }
    ]
  },
  {
    "_id": "PED-10047",
    "data_pedido": "2026-11-15",
    "status": "Concluido",
    "valor_total": 620.00,
    "cliente": {
      "nome": "Carlos Mendes",
      "email": "carlos.m@email.com",
      "cidade": "São Paulo",
      "endereco_entrega": { "rua": "Rua Augusta", "numero": "900", "bairro": "Consolação" }
    },
    "itens": [
      { "produto": "SSD NVMe 1TB", "quantidade": 1, "preco_unitario": 420.00 },
      { "produto": "Headset Gamer", "quantidade": 1, "preco_unitario": 200.00 }
    ]
  },
  {
    "_id": "PED-10048",
    "data_pedido": "2026-11-18",
    "status": "Cancelado",
    "valor_total": 300.00,
    "cliente": {
      "nome": "Fernanda Lima",
      "email": "fer.lima@email.com",
      "cidade": "Artur Nogueira",
      "endereco_entrega": { "rua": "Rua 7 de Setembro", "numero": "45", "bairro": "Centro" }
    },
    "itens": [
      { "produto": "Teclado Mecânico", "quantidade": 1, "preco_unitario": 300.00 }
    ]
  }
]);

// 1.3 Inserindo 5 produtos com insertMany() demonstrando SCHEMA-LESS (atributos variados)
db.produtos.insertMany([
  {
    "_id": "PROD-001",
    "nome": "Teclado Mecânico RGB",
    "categoria": "Periféricos",
    "preco": 300.00,
    "estoque": 12,
    "tags": ["gamer", "rgb", "usb"],
    "especificacoes": { "switch": "Blue", "layout": "ABNT2" } // Atributos de teclado
  },
  {
    "_id": "PROD-002",
    "nome": "Monitor Gamer 27'",
    "categoria": "Monitores",
    "preco": 1850.00,
    "estoque": 8,
    "tags": ["144hz", "ips", "full-hd"],
    "especificacoes": { "polegadas": 27, "taxa_atualizacao": "144Hz", "painel": "IPS" } // Atributos de monitor
  },
  {
    "_id": "PROD-003",
    "nome": "SSD NVMe 1TB",
    "categoria": "Armazenamento",
    "preco": 420.00,
    "estoque": 20,
    "tags": ["rapido", "pcie", "upgrade"],
    "especificacoes": { "capacidade": "1TB", "leitura_mb": 3500 } // Atributos de armazenamento
  },
  {
    "_id": "PROD-004",
    "nome": "Mouse Sem Fio Ergonômico",
    "categoria": "Periféricos",
    "preco": 75.00,
    "estoque": 3,
    "tags": ["wireless", "escritorio"]
  },
  {
    "_id": "PROD-TESTE-001",
    "nome": "Cabo VGA Obsoleto",
    "categoria": "Cabos",
    "preco": 15.00,
    "estoque": 0,
    "tags": ["descontinuado"]
  }
]);

// ============================================================================
// ETAPA 2: CONSULTAS DE LEITURA E FILTROS AVANÇADOS (find + operadores)
// ============================================================================

// 2.1 Comparação numérica ($gt): Produtos com preço maior que R$ 350,00
print("--- Consulta 2.1: Produtos acima de R$ 350 ---");
printjson(db.produtos.find({ "preco": { $gt: 350.00 } }).toArray());

// 2.2 Operador de lista ($in): Produtos das categorias Periféricos ou Monitores
print("--- Consulta 2.2: Periféricos e Monitores ---");
printjson(db.produtos.find({ "categoria": { $in: ["Periféricos", "Monitores"] } }).toArray());

// 2.3 Projeção no find(): Exibir apenas nome, categoria e preço, ocultando o _id
print("--- Consulta 2.3: Catálogo resumido (sem _id) ---");
printjson(db.produtos.find({}, { "_id": 0, "nome": 1, "categoria": 1, "preco": 1 }).toArray());

// ============================================================================
// ETAPA 3: MANIPULAÇÃO E MANUTENÇÃO DE DADOS (update e delete)
// ============================================================================

// 3.1 updateOne() com $set: Atualiza o preço do Teclado Mecânico para promoção
db.produtos.updateOne(
  { "_id": "PROD-001" },
  { $set: { "preco": 249.90 } }
);

// 3.2 updateMany() com $set: Ativa selo de promoção para produtos com estoque > 5
db.produtos.updateMany(
  { "estoque": { $gt: 5 } },
  { $set: { "status_promocao": "ativo" } }
);

// 3.3 updateOne() com $push: Adiciona a tag "liquidacao" no array tags do PROD-001
db.produtos.updateOne(
  { "_id": "PROD-001" },
  { $push: { "tags": "liquidacao" } }
);

// 3.4 deleteOne() com filtro seguro: Remove o produto obsoleto de teste
db.produtos.deleteOne({ "_id": "PROD-TESTE-001" });

// ============================================================================
// ETAPA 4: INTELIGÊNCIA ANALÍTICA COM AGGREGATION PIPELINE (aggregate)
// ============================================================================

// 4.1 Pipeline 1: Faturamento total e ticket médio por cidade (apenas pedidos Concluídos)
print("--- Pipeline 1: Faturamento por Cidade ---");
printjson(db.pedidos.aggregate([
  { $match: { "status": "Concluido" } }, // Filtra apenas vendas efetivadas
  {
    $group: {
      "_id": "$cliente.cidade",
      "total_faturado": { $sum: "$valor_total" },
      "media_pedido": { $avg: "$valor_total" },
      "qtd_pedidos": { $sum: 1 }
    }
  },
  { $sort: { "total_faturado": -1 } } // Ordena da cidade que mais faturou para a menor
]).toArray());

// 4.2 Pipeline 2: Relatório gerencial formatado de estoque por categoria
print("--- Pipeline 2: Relatório Formatado de Estoque ---");
printjson(db.produtos.aggregate([
  { $match: { "estoque": { $gt: 0 } } }, // Considera apenas itens disponíveis em estoque
  {
    $group: {
      "_id": "$categoria",
      "total_itens_estoque": { $sum: "$estoque" },
      "preco_medio": { $avg: "$preco" }
    }
  },
  {
    $project: {
      "_id": 0, // Oculta o _id técnico
      "Categoria": "$_id", // Renomeia de forma amigável
      "Unidades_Disponiveis": "$total_itens_estoque",
      "Preco_Medio_Categoria": { $round: ["$preco_medio", 2] }
    }
  },
  { $sort: { "Unidades_Disponiveis": -1 } }
]).toArray());