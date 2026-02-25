def evaluar_estudiante(nota, faltas):
    """
    nota: int (0-100)
    faltas: int (>=0)
    """

    if not isinstance(nota, int):
        raise TypeError("La nota debe ser entera")

    if not isinstance(faltas, int):
        raise TypeError("Las faltas deben ser enteras")

    if nota < 0 or nota > 100:
        raise ValueError("Nota fuera de rango")

    if faltas < 0:
        raise ValueError("Faltas inválidas")

    # ===== Regla crítica =====
    if faltas > 10:
        return "REPROBADO"

    # regla de negocio
    if faltas > 3:
        nota = nota - 5

    # ===== Clasificación =====
    if nota < 60:
        return "REPROBADO"
    elif nota < 85:
        return "APROBADO"
    elif nota < 90:
        return "EXCELENTE"
    else:
        return "SOBRESALIENTE"