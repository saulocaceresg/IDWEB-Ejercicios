USE universidades_licenciadas;

SELECT nombre, periodo_licenciamiento, departamento_local, denominacion_programa
FROM universidades
ORDER BY RAND()
LIMIT 15;