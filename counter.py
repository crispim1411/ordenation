class Counter:
    """Contador de trocar realizadas durante ordenação"""
    count_set = 0
    count_comp = 0

    @classmethod
    def assignment(cls):
        """Incrementa contador de atribuição de valores"""
        cls.count_set += 1

    @classmethod
    def comparation(cls):
        """Incrementa contador de comparação de valores"""
        cls.count_comp += 1

    @classmethod
    def __repr__(cls):
        """Retorna contador"""
        return f"atribuições: {cls.count_set}\ncomparações: {cls.count_comp}"
