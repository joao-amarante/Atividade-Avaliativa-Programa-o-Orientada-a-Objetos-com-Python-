def validar_campo_vazio(texto: str) -> bool:
    """Retorna False se o campo estiver vazio"""
    return len(texto.strip()) > 0