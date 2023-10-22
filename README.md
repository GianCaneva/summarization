# Unchained News 🟩
> Aplicación para la optimización de lectura de noticias digitales y libre de sesgos.
---
## Descripción
El presente código forma parte de una constelación de servicios que, en conjunto, trabajan para conseguir el objetivo deseado.
En particular, la presente aplicación, se encarga de todo el procesamiento de datos que involucre análisis de texto y uso de Inteligencia Artificial de tipo NLP. Se divide en tres módulos fundamentales:
* Keywords: dado un texto, utiliza la técnica de POS, para detectar las palabras más relevantes de ese texto.
* Resumidor: de artículos o títulos para recrear y acortar su longitud en base a ciertos paramétros.
* Removedor de sesgo: dado un texto, analiza aquellas palabras que expresen una tendencia y las elimina. También se emplea la técnica POS.

Esta aplicación fue concebida pera ser ejecutada internamente dentro de un flujo de procesamiento por otros servicios de la constelación. Por lo tanto, su uso aislado carece de sentido. Aunque, se exponenen endpoints pudiendo ser llamada externamente.


## Pre-requisitos

Este programa fue diseñado para ser utilizado con las siguientes especificaciones:
* [Python 3.9.6](https://www.python.org/downloads/release/python-396/)
* [pip 23.2.1](https://pip.pypa.io/en/stable/news/#v23-2-1)

Si bien la utilización otras versiones pueden permitir la ejecución del programa, no se puede asegurar su correcto funcionamiento.

## Instalación

Use la librería pip para asegurarse para instalar las dependencias necesarias mediante el comando a continuación.

```
pip3 install -r requirements.txt
```
Eso instalará todas las dependencias que se encuentren definidas en el documento requirements.txt

## Ejecución

En una terminal, ejecute el método principal en main.py mediante el siguiente comando (asegúrese de estar en la carpeta raíz del proyecto).

```
python3 main.py
```

## Uso

* Como se mencionó previamente, el uso de esta aplicacíon por si sola no representa alguna funcionalidad al usuario final y la misma no va a ser pública/visible para que puedan interactuar con la misma.
* El uso de está aplicación se realiza a través de otros servicios, invocandola con parametros consistentes.
* Sin embargo se exponen 4 endpoints relevantes:
  * `/api/keywords` [POST]: endpoint responsable de recibir un texto y devolver las palabras más relevantes del mismo.
  * `/api/summarize/article` [POST]: mediante la ingesta de un artículo, y parámetros de entrada que determinen su longitud, resume el texto en base a los parámetros.
  * `/api/summarize/title` [POST]: mediante la ingesta de un texto, resume el mismo en un tamaño fijo y en formato de título de noticia.
  * `/api/bias` [POST]: dado un texto, detecta palabras tendenciosas y las elimina.


## Autores
Caneva, Gianfranco

## Contacto

Por cualquier sugerencia, problema o inconveniente comunicarse con `gfocaneva@gmail.com`