# 📊 Informe del Laboratorio de Pruebas Funcionales Automatizadas

---

## 1. Resultados de ejecución

- **Login exitoso:** Funcionó correctamente, se mostró el mensaje esperado.
- **Login inválido:** El sistema mostró el mensaje "Your username is invalid!" como se esperaba.
- **Suma en calculadora:** Resultado correcto `12`.
- **División por cero:** La aplicación no devuelve un mensaje claro, el campo queda vacío. La prueba detecta el error como comportamiento inválido controlado.
- **Texto y símbolos en calculadora:** El sistema no genera resultado, queda vacío. Nuestras pruebas lo marcan como error válido.
- **Login con símbolos/números:** El sistema rechaza la entrada y muestra mensaje de error.

---

## 2. Observaciones

- El sistema **no maneja bien entradas inválidas** (texto, símbolos, división por cero).  
- Las pruebas automatizadas **permiten documentar estas fallas** y garantizan que la app no se rompa ante inputs inesperados.  
- La **validación de datos de entrada** es un área de mejora para los desarrolladores de la aplicación.

---

## 3. Comparación de herramientas

### Selenium
- ✅ Multi-lenguaje (Python, Java, C#).  
- ✅ Gran comunidad y soporte.  
- ❌ Flakiness por tiempos de carga (resuelto con WebDriverWait).  
- Ideal para aplicaciones web tradicionales.

### Playwright
- ✅ Esperas automáticas más estables.  
- ✅ Soporte moderno para trazas, screenshots y videos.  
- ❌ Menor comunidad que Selenium (pero creciendo rápido).  
- Ideal para pruebas confiables y modernas.

### Puppeteer
- ✅ Muy rápido y simple en Node.js.  
- ✅ Excelente para Chrome/Chromium.  
- ❌ Soporte limitado para otros navegadores.  
- Ideal para proyectos ligeros o pruebas rápidas.

---

## 4. Cómo se probarían aplicaciones móviles

- Usando **Appium** con drivers para Android (UiAutomator2) o iOS (XCUITest).  
- Integración con emuladores y dispositivos reales.  
- Validar inputs, gestos, rendimiento y consumo de recursos.

---

## 5. Cómo se prueban modelos de IA en producción

- **Validación offline:** conjuntos de prueba separados (holdout).  
- **Canary releases / A-B testing:** comparar versiones de modelos en producción.  
- **Monitoreo en tiempo real:** métricas de precisión, latencia, fairness, costos.  
- **Guardrails:** restricciones de salida para evitar errores graves.  
- **Reentrenamiento continuo:** detectar deriva de datos.

---

## 6. Conclusión

El laboratorio permitió:
- Diseñar y ejecutar pruebas automatizadas con Selenium, Playwright y Puppeteer.  
- Detectar limitaciones en la aplicación (ej. división por cero y entradas inválidas).  
- Comparar distintas herramientas de automatización.  
- Reflexionar sobre pruebas en entornos más avanzados (móviles, IA).  

**Entregables listos:** planillas, scripts, evidencias y este informe cumplen con lo solicitado por la guía.

---
