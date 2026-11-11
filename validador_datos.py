class ValidadorDatos:
    @staticmethod
    def validar_no_vacio(*campos):
        for campo in campos:
            if not str(campo).strip():
                return False
        return True

    @staticmethod
    def validar_numero(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False

    @staticmethod
    def validar_placa(placa):
        return len(str(placa).strip()) >= 5