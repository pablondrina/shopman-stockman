# shopman-stockman

Gestão de estoque físico para Django. Controle de quantidades por lote e posição, movimentações rastreáveis, reservas temporárias (holds), alertas automáticos e planejamento de reposição.

Part of the [Django Shopman](https://github.com/pablondrina/django-shopman) commerce framework.

## Domínio

- **Quant** — quantidade em estoque de um SKU em uma posição específica. Nunca negativo.
- **Move** — movimentação rastreável (entrada, saída, transferência, ajuste). Audit trail imutável.
- **Hold** — reserva temporária de estoque para um pedido. TTL configurável, fulfillment idempotente.
- **Batch** — lote de produção com validade, fornecedor, custo. Rastreabilidade FIFO/FEFO.
- **Position** — local físico no estoque (prateleira, câmara fria, vitrine).
- **StockAlert** — alerta automático quando estoque atinge mínimo configurado.

## StockService

API única para todas as operações de estoque:

| Método | O que faz |
|--------|-----------|
| `receive(sku, qty, ...)` | Entrada de mercadoria |
| `hold(sku, qty, ref)` | Reserva temporária para pedido |
| `fulfill_hold(hold_id)` | Confirma a reserva (desconta do físico) |
| `release_hold(hold_id)` | Libera reserva (devolve ao disponível) |
| `transfer(sku, from_pos, to_pos, qty)` | Transferência entre posições |
| `adjust(sku, qty, reason)` | Ajuste manual (inventário, quebra) |
| `check_availability(sku)` | Disponibilidade real (físico - holds) |
| `get_alternatives(sku, limit)` | Produtos alternativos quando indisponível |

## Contribs

- `stockman.contrib.alerts` — Alertas automáticos de estoque mínimo. Configurável por SKU.
- `stockman.contrib.admin_unfold` — Admin com Unfold theme.

## Instalação

```bash
pip install shopman-stockman
```

```python
INSTALLED_APPS = [
    "shopman.stockman",
    "shopman.stockman.contrib.alerts",        # opcional
    "shopman.stockman.contrib.admin_unfold",   # opcional
]
```

## Development

```bash
git clone https://github.com/pablondrina/django-shopman.git
cd django-shopman && pip install -e packages/stockman
make test-stockman  # ~188 testes
```

## License

MIT — Pablo Valentini
