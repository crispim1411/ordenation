class Counter:
    """Contador de trocar realizadas durante ordenação"""
    count = 0

    @classmethod
    def plus(cls):
        """Incrementa contador"""
        cls.count += 1

    @classmethod
    def __repr__(cls):
        """Retorna contador"""
        return f"count: {cls.count}"
