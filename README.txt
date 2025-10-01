# Proyecto de Pruebas Automatizadas

Este proyecto está listo para abrirse en Visual Studio Code.

## Pasos de instalación

### 1. Crear entorno virtual (Python)
```
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows
```

### 2. Instalar dependencias de Python
```
pip install -r requirements.txt
python -m playwright install

```

### 3. Instalar dependencias de Node.js (Puppeteer)
```
npm install
```

### 4. Ejecutar pruebas
#### Selenium
```
python tests/test_login_selenium.py
python tests/test_calculator_selenium.py
```

#### Playwright
```
python tests/test_playwright.py
```

#### Puppeteer
```
npm start
```

## Notas
- Carpeta `/evidencias` para capturas y logs.
- Configuración básica de VS Code en `.vscode/settings.json`.
