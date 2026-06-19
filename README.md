# Numberbot by YOLO

Integrantes:
Abraham Marentes Ramirez     23310382 as DarkDemon19
Manuel Emiliano Osorio Muñoz 23310359 as T-55AM1

## Caso de estudio: Numberbot by YOLO 

### 1. Descripción general

**Numberbot by YOLO** es un modelo de visión artificial desarrollado para detectar números dentro de imágenes. Su aplicación práctica propuesta consiste en integrarlo en un sistema de escaneo y digitalización de documentos que contienen información numérica, como ejercicios de matemáticas, exámenes, hojas de trabajo, tablas, formularios, registros de laboratorio y documentos técnicos.

La finalidad del sistema sería transformar documentos físicos en información digital organizada. A diferencia de un escáner convencional, que solamente produce una imagen o un archivo PDF, Numberbot analizaría el contenido visual del documento, identificaría la ubicación de cada número y permitiría convertirlos en datos que puedan almacenarse, buscarse, editarse o procesarse posteriormente.

Este sistema podría utilizarse principalmente en escuelas, bibliotecas, oficinas, laboratorios y áreas administrativas donde existe una gran cantidad de documentos con valores numéricos que deben capturarse manualmente.

----------------------------------------------------------

### 2. Problema que se busca resolver

En muchas instituciones todavía existen documentos físicos que contienen información importante escrita o impresa en forma de números. Algunos ejemplos son:

* Ejercicios y evaluaciones de matemáticas.
* Tablas de resultados.
* Calificaciones de estudiantes.
* Registros de mediciones.
* Hojas de prácticas de laboratorio.
* Formularios con fechas, cantidades o identificadores.
* Inventarios y números de serie.
* Documentos técnicos con dimensiones y valores.
* Lecturas de instrumentos o medidores.
* Libros antiguos de matemáticas que no cuentan con una versión digital editable.

La digitalización de estos documentos normalmente se realiza mediante captura manual. Una persona observa cada hoja y escribe los números en una computadora. Este procedimiento puede ser lento, repetitivo y propenso a errores, especialmente cuando se trabaja con una gran cantidad de documentos.

Por ejemplo, si una escuela necesita digitalizar cientos de hojas de ejercicios matemáticos, una persona tendría que capturar manualmente cada cantidad. Además del tiempo requerido, existe la posibilidad de confundir números similares, omitir información o colocar los datos en un orden incorrecto.

Numberbot permitiría automatizar una parte importante de este proceso. El modelo localizaría cada número en la imagen y proporcionaría su clase, posición y nivel de confianza. Posteriormente, un programa complementario ordenaría las detecciones para reconstruir números completos y relacionarlos con el área del documento donde aparecen.

----------------------------------------------------------------------------

### 3. Propuesta de aplicación

La propuesta consiste en desarrollar una estación de digitalización de documentos basada en una cámara, un sistema de iluminación y una computadora que ejecute el modelo Numberbot.

El usuario colocaría una hoja sobre una superficie de escaneo. La cámara capturaría una imagen del documento y la enviaría al sistema. Numberbot analizaría la imagen y marcaría cada número mediante un cuadro delimitador.

Después de la detección, el programa utilizaría la posición de los cuadros para organizar los dígitos de izquierda a derecha y de arriba hacia abajo. De esta manera, varios dígitos cercanos podrían agruparse para formar cantidades completas.

Por ejemplo, si el modelo detecta los dígitos:

1   2   5

y los tres se encuentran cercanos y sobre la misma línea, el sistema podría interpretarlos como:

125

El resultado podría mostrarse en una interfaz para que el usuario verifique las detecciones antes de guardar el documento. Finalmente, la información podría exportarse en formatos como `.txt`, `.csv`, `.xlsx`, `.json` o PDF digitalizado.

------------------------------------------------------------------

### 4. Aplicaciones del escaneo de números

Una aplicación directa de Numberbot sería la digitalización de hojas de ejercicios de matemáticas. El sistema podría detectar los números presentes en operaciones, problemas, tablas y respuestas de los estudiantes.

Por ejemplo, en una hoja con las siguientes operaciones:

25 + 13 = 38
42 - 17 = 25
8 × 6 = 48

Numberbot detectaría los dígitos presentes en cada línea. Posteriormente, un módulo adicional podría organizar las detecciones de acuerdo con su posición. Para reconocer signos como suma, resta, multiplicación o igualdad, sería necesario agregar nuevas clases al modelo o utilizar un módulo complementario de reconocimiento óptico de caracteres.

Otra aplicación sería el procesamiento de tablas numéricas. En documentos con registros de temperaturas, velocidades, voltajes, calificaciones o cantidades, el sistema podría localizar los números y asociarlos con cada fila y columna. Esto permitiría convertir una tabla impresa en un archivo digital que pueda analizarse mediante Excel u otro programa.

En laboratorios y talleres, Numberbot podría emplearse para capturar resultados escritos en hojas de prácticas. Mediciones como voltaje, corriente, temperatura, distancia, tiempo o velocidad podrían digitalizarse para evitar su transcripción manual.

También podría utilizarse en bibliotecas o archivos escolares para digitalizar libros antiguos de matemáticas. El sistema permitiría localizar todos los números de una página, generar un índice de contenido numérico o preparar los documentos para su procesamiento mediante otras herramientas de reconocimiento.

En una versión más avanzada, Numberbot podría analizar fotografías tomadas con un teléfono celular. De esta manera, el usuario no necesitaría un escáner especializado: solamente tendría que fotografiar el documento y cargar la imagen en la aplicación.

---

### 5. Hardware propuesto

Para implementar el sistema se propone utilizar el siguiente hardware:

#### Cámara o escáner

Se podría emplear una cámara web de alta resolución, una cámara para Raspberry Pi, una cámara industrial o incluso la cámara de un teléfono celular. La cámara debería colocarse de manera perpendicular al documento para evitar deformaciones en la imagen.

Una resolución adecuada permitiría que los números pequeños sean visibles y puedan ser analizados correctamente por el modelo.

#### Base para documentos

Se utilizaría una superficie plana donde el usuario colocaría las hojas. La base podría incluir marcas que indiquen la posición correcta del documento, evitando que quede inclinado o fuera del área de captura.

#### Sistema de iluminación

Se colocarían lámparas LED a los lados de la cámara para proporcionar una iluminación uniforme. Esto ayudaría a disminuir sombras, reflejos y zonas oscuras que podrían afectar la detección.

#### Unidad de procesamiento

El modelo podría ejecutarse en diferentes equipos, dependiendo de la velocidad requerida:

* Computadora portátil o de escritorio.
* Raspberry Pi con acelerador de inteligencia artificial.
* NVIDIA Jetson Nano, Orin Nano o equipo similar.
* Servidor local.
* Servicio de procesamiento en la nube.

Para una versión escolar o de demostración, una computadora con Python y Google Colab sería suficiente. Para una instalación permanente, sería conveniente utilizar un equipo local que pueda procesar las imágenes sin depender de una conexión a internet.

#### Pantalla o interfaz de usuario

El sistema podría incluir una pantalla donde se mostraría la imagen original junto con los números detectados. El usuario tendría la posibilidad de corregir alguna detección antes de guardar los resultados.

----------------------------------------------------------------------------------

### 6. Software propuesto

El sistema estaría compuesto por varios módulos de software:

* **Modelo Numberbot by YOLO:** detectaría los números presentes en la imagen.
* **Python:** controlaría el flujo general de la aplicación.
* **Ultralytics:** permitiría cargar y ejecutar el modelo YOLO.
* **OpenCV:** se utilizaría para capturar, recortar y mejorar las imágenes.
* **Módulo de organización:** ordenaría los dígitos según sus coordenadas.
* **Interfaz gráfica:** permitiría revisar y corregir las detecciones.
* **Base de datos:** almacenaría los documentos y los resultados.
* **Módulo de exportación:** generaría archivos de texto, tablas o documentos digitales.

El archivo `best.pt`, generado después del entrenamiento, sería el encargado de realizar las detecciones. Cada resultado incluiría la clase detectada, las coordenadas del número y la confianza de la predicción.

------------------------------------------------------------------------

### 7. Flujo de funcionamiento

El funcionamiento del sistema se realizaría de la siguiente manera:

1. **Colocación del documento:** el usuario coloca la hoja sobre la base de digitalización.

2. **Captura de la imagen:** la cámara toma una fotografía del documento completo.

3. **Preprocesamiento:** el programa corrige la inclinación, mejora el contraste, ajusta el tamaño y reduce posibles sombras.

4. **Detección con Numberbot:** la imagen se envía al modelo YOLO, que identifica cada número y dibuja un cuadro alrededor de él.

5. **Organización de las detecciones:** el sistema utiliza las coordenadas de los cuadros para ordenar los números por línea, columna o sección.

6. **Agrupación de dígitos:** los dígitos cercanos se combinan para formar números completos. Por ejemplo, las detecciones `2`, `0`, `2` y `6` podrían agruparse como `2026`.

7. **Validación:** la interfaz muestra los resultados al usuario. Las detecciones con poca confianza se resaltan para que puedan revisarse manualmente.

8. **Almacenamiento:** los resultados se guardan junto con la imagen original, la fecha de digitalización y el nombre del documento.

9. **Exportación:** la información puede convertirse en texto, tabla de Excel, archivo CSV, JSON o PDF digital.

El flujo general sería el siguiente:

Documento físico
       ↓
Captura de imagen
       ↓
Mejora y corrección de la imagen
       ↓
Detección de números con Numberbot
       ↓
Ordenamiento y agrupación de los dígitos
       ↓
Revisión del usuario
       ↓
Almacenamiento y exportación digital

-----------------------------------------------------------------------------

### 8. Ejemplo de uso en una institución educativa

Un docente necesita digitalizar las respuestas numéricas de varias hojas de ejercicios. En lugar de capturar manualmente cada respuesta, coloca las hojas una por una debajo de la cámara.

El sistema fotografía cada documento y Numberbot identifica los números escritos o impresos. Las detecciones se organizan de acuerdo con la posición de cada ejercicio. Posteriormente, el docente observa los resultados en pantalla y corrige solamente aquellos valores que el modelo haya marcado con baja confianza.

Después de la revisión, el sistema genera una tabla como la siguiente:

Alumno | Ejercicio 1 | Ejercicio 2 | Ejercicio 3
A01    |      25     |      48     |      120
A02    |      24     |      46     |      115
A03    |      25     |      48     |      120

Esta información podría utilizarse para almacenar respuestas, comparar resultados o realizar análisis estadísticos. Para que el sistema califique automáticamente, sería necesario agregar una etapa que compare las respuestas detectadas con una plantilla de respuestas correctas.

-----------------------------------------------------------------

### 9. Beneficios de la propuesta

La implementación de Numberbot en un sistema de digitalización permitiría reducir el tiempo necesario para capturar información numérica. También disminuiría los errores provocados por la transcripción manual y facilitaría la conservación de documentos físicos.

Otro beneficio sería la posibilidad de localizar información dentro de documentos digitalizados. Por ejemplo, el usuario podría buscar una cantidad, fecha, matrícula o número específico sin revisar todas las páginas manualmente.

El sistema también podría adaptarse a diferentes áreas. Aunque la propuesta inicial está enfocada en documentos matemáticos, el mismo principio podría aplicarse a inventarios, formularios, registros de mantenimiento, hojas de producción, mediciones industriales y documentos administrativos.

-----------------------------------------------------------------------

### 10. Limitaciones y posibles mejoras

El funcionamiento del sistema dependerá de la calidad y variedad de las imágenes utilizadas durante el entrenamiento. Numberbot fue entrenado con imagenes digitales de la web y escritura de numeros a mano

También debe considerarse que el modelo detecta dígitos individuales, pero no comprende automáticamente el significado completo de una operación matemática. Para interpretar ecuaciones sería necesario entrenar nuevas clases, como:

+
-
×
÷
=
.
,
%
Tambien se consideraria simbolos de la matematica avanzada.

Otra mejora consistiría en ampliar el dataset con diferentes tipos de letra, tamaños, colores, fondos, niveles de iluminación y estilos de escritura. Esto permitiría que el modelo funcione en una mayor variedad de documentos reales.

Asimismo, podría incorporarse un módulo de corrección manual. Cuando una detección tenga una confianza baja, el sistema solicitaría al usuario que confirme el número. Las correcciones realizadas podrían guardarse y utilizarse posteriormente para mejorar el modelo mediante nuevos entrenamientos.

------------------------------------------------------------------

### 11. Factibilidad del proyecto

La propuesta es técnicamente factible porque puede implementarse utilizando una cámara convencional, una computadora y herramientas de software disponibles para Python. En una primera etapa, el sistema puede funcionar en Google Colab, cargando una carpeta con imágenes y ejecutando el modelo sobre ellas.

En una segunda etapa, el modelo podría integrarse en una aplicación con una interfaz más sencilla. El usuario solamente tendría que seleccionar o capturar el documento, esperar el procesamiento y revisar los resultados.

Numberbot by YOLO no se limitaría a demostrar que un modelo puede colocar cuadros alrededor de números. Su utilidad real estaría en convertir documentos físicos en información digital aprovechable. Con una ampliación adecuada del conjunto de datos y la integración de módulos de organización, validación y exportación, el proyecto podría convertirse en una herramienta funcional para instituciones educativas, oficinas, laboratorios y entornos donde se procesan grandes cantidades de información numérica.


////////////////Instalación de Dependencias//////////////////////////////////////////////////////

-----codigo-------------------------------------------

# Instalar ultralytics (que incluye YOLOv8) y otras dependencias comunes
!pip install ultralytics opencv-python matplotlib

# Verificar la instalación de ultralytics
from ultralytics import YOLO
print("YOLOv8 instalado y listo para usar.")

------------------------------------------------------

/////////////////Carga del Modelo Preentrenado YOLOv8/////////////////////////////////////////////

-----codigo-------------------------------------------

# Cargar un modelo YOLOv8 preentrenado (por ejemplo, 'yolov8n.pt' para la versión nano)
model = YOLO('yolov8n.pt')

print("Modelo YOLOv8 cargado exitosamente.")

---------------------------------------------------------

////////////////////Detección de Objetos con YOLOv8////////////////////////////////////////////////

Una vez que el modelo está cargado, podemos usarlo para detectar objetos 
en imágenes o videos. El modelo identificará objetos dentro de las imágenes y 
dibujará cuadros delimitadores alrededor de ellos, junto con sus etiquetas de clase y un 
puntaje de confianza.

/////////////////////Descargar una imagen de ejemplo//////////////////////////////////////////////////

-----codigo-------------------------------------------

# Descargar una imagen de ejemplo para la detección
!wget -nc https://ultralytics.com/images/bus.jpg -O bus.jpg

print("Imagen de ejemplo 'bus.jpg' descargada.")

----------------------------------------------------------

////////////////////Realizar la detección/////////////////////////////////////////////////////////////

-----codigo-------------------------------------------

from PIL import Image

# Realizar la detección de objetos en la imagen de ejemplo
results = model('bus.jpg')

# Mostrar los resultados (esto guardará las imágenes con las detecciones en una carpeta 'runs/detect/expX')
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    display(im) # Muestra la imagen con las detecciones

print("Detección de objetos completada. Las imágenes resultantes se muestran arriba y se guardan en el directorio 'runs'.")

-----------------------------------------------------------

//////////////////////////Fine-tuning un Modelo YOLOv8/////////////////////////////////////////////////////////

El fine-tuning es el proceso de tomar un modelo preentrenado (como YOLOv8n) y entrenarlo 
aún más en un conjunto de datos específico de su dominio. Esto permite que el modelo se adapte 
mejor a sus necesidades, detectando objetos que podrían no estar presentes en los datos originales 
o mejorando la precisión en objetos ya conocidos.

Para realizar el fine-tuning, necesitará un conjunto de datos personalizado que incluya imágenes y 
anotaciones (etiquetas de bounding boxes) para los objetos que desea detectar. Las anotaciones 
deben estar en un formato que YOLOv8 pueda entender, generalmente el formato YOLO (archivos .txt 
por cada imagen, especificando la clase del objeto y sus coordenadas normalizadas).

/////////////////////////////////Preparación del Conjunto de Datos///////////////////////////////////////

Para el fine-tuning, su conjunto de datos debe estar estructurado de una manera específica. 
Típicamente, tendrá directorios separados para las imágenes de entrenamiento (train/images), validación 
(val/images) y opcionalmente prueba (test/images), con sus respectivas anotaciones en formatos 
YOLO (train/labels, val/labels, test/labels).

También necesitará un archivo data.yaml que describa la estructura de su dataset, las 
clases de objetos y las rutas a las imágenes. Aquí hay un ejemplo de cómo se vería un archivo 
data.yaml:

-----codigo-------------------------------------------

%%writefile data.yaml
train: ../datasets/my_custom_dataset/train/images
val: ../datasets/my_custom_dataset/val/images

nc: 2  # número de clases
names: ['object1', 'object2']  # nombres de las clases

-------------------------------------------------------

En un escenario real, reemplazaría ../datasets/my_custom_dataset/ con la ruta a su dataset y 
object1, object2 con los nombres reales de sus clases. Aquí se asume que ha subido su dataset a 
Colab o lo tiene montado desde Google Drive.

///////////////////////////////Entrenamiento del Modelo////////////////////////////////////

-----codigo-------------------------------------------

# Para este ejemplo, simularemos el entrenamiento.
# En un caso real, necesitarías tener tus archivos de imágenes y etiquetas.
# Para una demostración, usaremos un dataset pequeño y predefinido de ultralytics
# o simplemente mostraremos la sintaxis.

# Asumiendo que ya tienes un dataset configurado y el archivo data.yaml
# (para ejecutar esto, necesitarías un dataset real en la ruta especificada)

# Cargar el modelo preentrenado (por ejemplo, yolov8n)
model_for_finetuning = YOLO('yolov8n.pt')

# Entrenar el modelo en tu dataset personalizado
# Aquí usamos el dataset 'coco128' que viene con ultralytics para demostración
# En tu caso, usarías 'data.yaml' como en la sección anterior.

# Descomenta y ajusta esta línea para tu propio dataset:
results_finetune = model_for_finetuning.train(data='data.yaml', epochs=50, imgsz=640)

# Para demostración sin un dataset cargado, mostraremos la sintaxis para un dataset de ejemplo:
print("Para iniciar el fine-tuning en un dataset real, usarías:")
print("results_finetune = model_for_finetuning.train(data='data.yaml', epochs=50, imgsz=640)")
print("Donde 'data.yaml' apunta a tu configuración de dataset, 'epochs' es el número de épocas y 'imgsz' es el tamaño de la imagen.")

# Si quieres ejecutar un entrenamiento de demostración (descarga el dataset coco128)
# try:
#     results_finetune = model_for_finetuning.train(data='coco128.yaml', epochs=3, imgsz=640) # Reducir epochs para el ejemplo
# except Exception as e:
#     print(f"Error durante el entrenamiento de demostración: {e}. Asegúrate de que coco128.yaml sea accesible.")

-----------------------------------------------------------

//////////////////////#### Usar el Modelo Fine-tuned para Inferencia/////////////////////////////////////////////////////////

-----codigo-------------------------------------------

from PIL import Image

# Cargar el modelo fine-tuned (reemplaza 'path/to/best.pt' con la ruta real)
# Para este ejemplo, cargaremos el modelo yolov8n.pt original ya que no hemos hecho un fine-tuning real.
# En un escenario real, cargarías: fine_tuned_model = YOLO('runs/detect/trainX/weights/best.pt')

fine_tuned_model = YOLO('yolov8n.pt') # Cargamos el modelo original para demostración

# Realizar inferencia con el modelo fine-tuned en una nueva imagen
# Usaremos la misma imagen 'bus.jpg' para ilustrar, pero usarías nuevas imágenes
results_finetuned_inference = fine_tuned_model('bus.jpg')

for r in results_finetuned_inference:
    im_array_finetuned = r.plot()
    im_finetuned = Image.fromarray(im_array_finetuned[..., ::-1])
    display(im_finetuned)

print("Inferencia con el modelo (simulado) fine-tuned completada.")

-------------------------------------------------------