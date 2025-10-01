# 📋 Planillas del Laboratorio de Pruebas Funcionales Automatizadas

---

## 1. Casos de Uso de Prueba

| ID   | Actor   | Objetivo                     | Flujo Principal                                                                 | Precondiciones                  | Postcondiciones                  |
|------|---------|------------------------------|---------------------------------------------------------------------------------|---------------------------------|----------------------------------|
| CU01 | Usuario | Iniciar sesión exitosamente | Abrir login → Ingresar `tomsmith` / `SuperSecretPassword!` → Clic en Login       | App disponible                  | Usuario autenticado, mensaje OK   |
| CU02 | Usuario | Intentar login inválido     | Abrir login → Ingresar credenciales incorrectas → Clic en Login                  | App disponible                  | Mensaje de error mostrado         |
| CU03 | Usuario | Realizar suma en calculadora | Abrir BasicCalculator → Ingresar 5 y 7 → Seleccionar Add → Calcular              | App disponible                  | Resultado correcto = 12           |
| CU04 | Usuario | División por cero            | Abrir BasicCalculator → Ingresar 8 y 0 → Seleccionar Divide → Calcular           | App disponible                  | Resultado vacío o mensaje de error|
| CU05 | Usuario | Validación de texto/símbolos | Abrir BasicCalculator → Ingresar `abc` o `@#$` → Seleccionar operación → Calcular| App disponible                  | Resultado inválido controlado     |

---

## 2. Casos de Prueba

| ID   | Función a probar       | Datos de entrada                        | Resultado esperado                              | Resultado obtenido                               | Estado |
|------|------------------------|-----------------------------------------|------------------------------------------------|-------------------------------------------------|--------|
| TC01 | Login exitoso          | user=`tomsmith`, pass=`SuperSecretPassword!` | Mensaje: "You logged into a secure area!"       | Mensaje correcto, captura `login_exitoso.png`   | OK     |
| TC02 | Login inválido         | user=`wrong`, pass=`wrong`              | Mensaje: "Your username is invalid!"            | Mensaje correcto, captura `login_invalido.png`  | OK     |
| TC03 | Suma en calculadora    | 5 + 7                                   | 12                                             | 12                                              | OK     |
| TC04 | División por cero      | 8 / 0                                   | Campo vacío o mensaje de error controlado       | Resultado vacío detectado, marcado como error   | OK     |
| TC05 | Texto en campo numérico| `abc` + 7                               | Error o resultado inválido                      | "Error: resultado vacío o entrada inválida"     | OK     |
| TC06 | Símbolos en campo num. | `$#@` + 7                               | Error o resultado inválido                      | "Error: resultado vacío o entrada inválida"     | OK     |
| TC07 | Login inválido con símbolos | user=`123456`, pass=`@@@`           | Mensaje de error                                | Mensaje correcto mostrado en UI                 | OK     |

---
