# ATiA

**A**pp **Ti**me **A**nalytics no es realmente una app, es solo código Python que lee los registros de las aplicaciones que usas y te da un informe de cuánto tiempo dedicas a cada una.

Por ahora, es solo eso. Pero quizás algún día incluya algunos análisis basados en estos datos.

## Instalación

Hay dos formas de instalarlo:

### 1. Instalación para desarrollo

```bash
# Clona el repositorio
git clone https://github.com/lhansa/atia.git
cd atia

# Instala en modo desarrollo
pip install -e .
```

Después de esto, el comando `atia` estará disponible en tu terminal.

## Cómo usar

ATiA ahora es más fácil de usar. Solo necesitas estos comandos:

1. Para iniciar el monitor:
```bash
atia start -d 120  # Monitoriza durante 2 minutos
# o
atia start  # Monitoriza hasta que presiones Ctrl+C
```

2. Para ver el informe:
```bash
atia report
```

Ten en cuenta que el informe no es nada sofisticado. Es solo una lista de las apps que usaste y el tiempo que dedicaste a cada una.

### Ejemplo de resultados

```
Informe de uso de aplicaciones:
app
Code              0:07:37
Google-chrome     0:00:17
Xfce4-terminal    0:00:00
```

## Detalles técnicos

La app rastrea 2 cosas:

1. La aplicación que estás usando
2. Si es Google Chrome, el dominio que estás navegando

## Ejemplos de uso

En la carpeta `examples/` encontrarás ejemplos de cómo usar ATiA programáticamente:

- `basic_monitor_test.py`: Ejemplo básico de monitorización y lectura de resultados

## Desarrollo

Si quieres contribuir o modificar ATiA:

1. Instala en modo desarrollo como se indicó arriba
2. Los tests se ejecutan con: `python -m pytest`
3. Los ejemplos están en la carpeta `examples/`

## Por hacer

- [ ] Añadir análisis más sofisticados
- [ ] Mejorar la presentación del informe