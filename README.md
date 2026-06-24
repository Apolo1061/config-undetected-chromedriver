<div align="center">

# undetected-chromedriver config

![Version](https://img.shields.io/badge/version-1.0-green.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![Discord](https://img.shields.io/discord/Xw2eaWvNsz?logo=discord&style=for-the-badge)](https://discord.gg/p4nxegVB8W)

</div>
Este Script aplica tecnicas de anti-deteccion de bot para tu undetected-chromedriver

---
 
## Estructura del código
 
| Función | Descripción |
|---|---|
| `se()` | Crea o devuelve el directorio del perfil de Chrome |
| `opts()` | Configura las opciones de Chromiun  |
| `paolizador(drv)` | Inyecta los scripts JS para ocultar señales de webdriver |
| `human(drv)` | Simula scroll en la pagina |
| `checkerpro()` | Verifica que `google-chrome` este instalado en el sistema |
| `start2()` | Funcion principal hace todo XD |
 
---
 
## Requisitos
 
- Python 3.11+
- Google Chrome instalado
 
---

 ## Installation

**1. Clone the repository**
```bash
git clone https://github.com/Apolo1061/config-undetected-chromedriver.git
cd config-undetected-chromedriver
```

**2. Install dependencies**
```bash
pip install undetected-chromedriver
```


**3. Execution permissions**
```bash
chmod 777 main.py
```

## Uso
 
```bash
python3 main.py
```
 
Al finalizar se genera un archivo `test.png` con el screenshot de la pagina visitada.
 
---
 
## Perfil de Chrome
 
el script guarda el perfil del navegador en `./paolonodes_profile/` para mantener sesion entre ejecuciones.
 
---
 ** codigo del 19 de noviembre del 2025 **
