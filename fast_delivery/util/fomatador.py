def formatar_moeda(valor: float) -> str:
    """Formata um valor float para Real (BRL)"""
    return f"R$ {valor:.2f}".replace(".", ",")