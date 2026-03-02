import pytest
from student_score import evaluar_estudiante

# ==================================================
# 1️. PRUEBAS NORMALES
# ==================================================

def test_aprobado_normal():
    assert evaluar_estudiante(70, 1) == "APROBADO"

def test_reprobado_normal():
    assert evaluar_estudiante(40, 0) == "REPROBADO"

def test_excelente_normal():
    assert evaluar_estudiante(87, 1) == "EXCELENTE"

def test_sobresaliente_normal():
    assert evaluar_estudiante(95, 0) == "SOBRESALIENTE"


# ==================================================
# 2️. PRUEBAS DE BORDE
# ==================================================

def test_borde_aprobado():
    assert evaluar_estudiante(60, 0) == "APROBADO"

def test_borde_excelente():
    assert evaluar_estudiante(85, 0) == "EXCELENTE"

def test_borde_sobresaliente():
    assert evaluar_estudiante(90, 0) == "SOBRESALIENTE"

def test_borde_faltas_3():
    assert evaluar_estudiante(80, 3) == "APROBADO"


# ==================================================
# 3️. PRUEBAS DE ERROR
# ==================================================

def test_error_nota_string():
    with pytest.raises(TypeError):
        evaluar_estudiante("90", 2)

def test_error_faltas_string():
    with pytest.raises(TypeError):
        evaluar_estudiante(90, "2")

def test_error_nota_fuera_rango():
    with pytest.raises(ValueError):
        evaluar_estudiante(150, 2)

def test_error_faltas_negativas():
    with pytest.raises(ValueError):
        evaluar_estudiante(80, -1)


# ==================================================
# 4️. PRUEBAS DE VALORES EXTREMOS
# ==================================================

def test_nota_minima():
    assert evaluar_estudiante(0, 0) == "REPROBADO"

def test_nota_maxima():
    assert evaluar_estudiante(100, 0) == "SOBRESALIENTE"

def test_faltas_criticas():
    assert evaluar_estudiante(100, 11) == "REPROBADO"


# ==================================================
# 5️. PRUEBAS DE REGLAS DE NEGOCIO
# ==================================================

def test_descuento_por_faltas():
    # 84 - 5 = 79 → APROBADO
    assert evaluar_estudiante(84, 4) == "APROBADO"

def test_descuento_reprobado():
    # 62 - 5 = 57 → REPROBADO
    assert evaluar_estudiante(62, 5) == "REPROBADO"

def test_reprobado_por_faltas_mayores_10():
    assert evaluar_estudiante(90, 15) == "REPROBADO"


# ==================================================
# 6️. PRUEBAS DE VALIDACIÓN DE DATOS
# ==================================================

def test_nota_negativa():
    with pytest.raises(ValueError):
        evaluar_estudiante(-5, 2)

def test_faltas_no_entero():
    with pytest.raises(TypeError):
        evaluar_estudiante(80, 2.5)

def test_tipo_invalido_nota():
    with pytest.raises(TypeError):
        evaluar_estudiante("90", 1)

def test_tipo_invalido_faltas():
    with pytest.raises(TypeError):
        evaluar_estudiante(90, "dos")