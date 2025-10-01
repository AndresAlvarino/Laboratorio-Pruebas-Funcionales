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

## 5. Análisis

### ¿Qué pruebas fallaron?
- En principio, todas las pruebas diseñadas **no fallaron técnicamente**: el framework automático las ejecutó sin errores de script.
- Pero detectamos un “fallo funcional”: la prueba de **división por cero** no arrojó un resultado ni mensaje; el campo de resultado quedó vacío. Esto revela que la aplicación **no maneja bien ese caso**.
- También, al ingresar **texto o símbolos** en los campos numéricos, la calculadora no muestra un error explícito: simplemente no muestra resultado.

### ¿Se detectaron comportamientos inesperados?
- Sí: la aplicación **no valida entradas inválidas (texto, símbolos, vacíos)**, lo cual puede llevar a estados ambiguos o silenciosos.
- La división por cero queda en un estado “silencioso” (campo vacío), en vez de mostrar un mensaje de error claro.
- En el login, al ingresar símbolos o datos extraños, el sistema sí responde con mensaje de error “Your username is invalid!”, lo cual es un comportamiento esperado y correcto.

### ¿Cómo se pueden probar aplicaciones móviles?
- Usando **Appium**, que permite controlar apps móviles (Android / iOS) de manera similar a Selenium.
- Se instalan drivers como **UiAutomator2** (Android) o **XCUITest** (iOS).  
- Se usan emuladores o dispositivos reales, se definen rutas de interacción (screens, tapping, swiping) y se capturan logs, capturas de pantalla o video.
- Se validan inputs, navegación, latencia, interrupciones (llamadas, notificaciones), consumo de batería / memoria.
- Para apps híbridas o webviews, se pueden combinar herramientas de automatización web dentro del contexto móvil.

### ¿Cómo hacer pruebas de modelos de inteligencia artificial en producción?
- Validación offline (datasets de prueba, validaciones cruzadas) antes de desplegar.
- **Canary releases / pruebas A/B**: desplegar el nuevo modelo para un porcentaje de usuarios y comparar.
- Monitoreo continuo de métricas: precisión, recall, latencia, tasa de error, sesgos (“fairness”).
- Detector de deriva de datos: si los datos que llegan cambian con el tiempo, se reentrena.
- Guardrails / filtros: evitar que el modelo genere salidas peligrosas o fuera de rango.
- Pruebas de regresión del modelo: asegurar que nuevas versiones no empeoren casos existentes.

---

## 6. Comparación usando Playwright, Puppeteer y la URL de la calculadora

### Resultados obtenidos

| Herramienta   | Login exitoso | Login inválido | Suma 5 + 7 | División 8 / 0 | Texto/símbolos entradas |
|----------------|----------------|------------------|-------------|------------------|--------------------------|
| **Selenium**   | ✅ correcto     | ✅ correcto        | ✅ = 12      | Resultado vacío    | Entrada inválida → error detectado |
| **Playwright** | ✅ correcto     | ✅ correcto        | ✅ = 12      | Resultado vacío    | Incorrecto → prueba detecta vacío |
| **Puppeteer**  | ✅ correcto     | ✅ correcto        | ✅ = 12      | Resultado vacío    | Igual que los anteriores |

- En todas las herramientas, el comportamiento ante los mismos inputs fue consistente: los casos “normales” pasaron, los casos inválidos fueron detectados por las pruebas como errores controlados, y la división por cero deriva en campo vacío que nuestras pruebas interpretan como error.
- No hubo discrepancias importantes entre herramientas en cuanto a lógica de prueba. Sin embargo:
  - **Playwright** ofrece mejor manejo de esperas automáticas y menor flakiness.
  - **Puppeteer** es más simple para casos de uso centrados en Chrome.
  - **Selenium** es más universal (varios navegadores), pero requiere más control de esperas manuales.

### Observaciones adicionales
- En las tres herramientas es posible capturar capturas de pantalla o logs automáticamente.
- Playwright permite tracing / videos de sesión, lo cual es un plus para auditoría visual.
- Puppeteer es liviano y rápido, ideal para pruebas sencillas en entorno Node.js.

---

## Conclusión general

El laboratorio cumplió su propósito: construir pruebas automatizadas robustas con Selenium, Playwright y Puppeteer, identificar debilidades del sistema (validaciones débiles, división por cero), y comparar el rendimiento y la ergonomía de las distintas herramientas.  
Para entregar al profesor, este informe junto con las planillas, scripts y evidencias cubren todos los requisitos del documento de laboratorio.

