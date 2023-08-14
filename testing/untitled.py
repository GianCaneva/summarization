#instalar !pip3 install sentencepiece

from transformers import pipeline
summarizer = pipeline("summarization", model="ELiRF/mt5-base-dacsa-es")

ARTICLE = """
Fue una decisión de la plana mayor de Unión por la Patria para resaltar la figura del precandidato presidencial. La Vicepresidenta viajará a El Calafate el jueves y se quedará allá para votar
Finalmente, ni Alberto Fernández ni Cristina Kirchner estarán en el cierre de campaña de Unión por la Patria. Luego de que ayer se confirmara que el acto sería en el Teatro Argentino de La Plata, había dudas sobre la presencia del Presidente y la Vicepresidenta. Sin embargo, según pudo confirmar Infobae, en una decisión conjunta entre la plana mayor del oficialismo, se definió que ninguno estuviera para resaltar la figura del precandidato a presidente del espacio.

“La idea de campaña ahora es presidencialismo, elección centralizada en Sergio, mas que en la fuerza política”, resumieron en el búnker de UP. Además, según explicaron, la intención es mostrar recambio generacional. Por eso, sí estarán Eduardo de Pedro, Máximo Kirchner y Leandro Santoro, entre otros. Por su parte, Fernández de Kirchner viajará el jueves a El Calafate y permanecerá allí hasta el día de la votación.

Como adelantó este medio, Massa presentará las propuestas que tiene para gobernar la Argentina. “Será un formato diferente para lo que son habitualmente los cierres de campaña. Massa tendrá un conversatorio con ciudadanos que representan sectores y problemáticas distintas”, indicaron en el comando de campaña peronista, por donde pasan con asiduidad Eduardo “Wado” de Pedro y Máximo Kirchner, para supervisar cada detalle.
Pocos meses atrás la vicepresidenta, Cristina Kirchner, encabezó un acto en el mismo teatro donde el ministro de Economía cerrará la campaña el próximo jueves. Es un lugar de mucha importancia para el kirchnerismo, que ha cerrado otras campañas ahí en lo que ellos mismos definen como la época dorada, cuando el matrimonio estuvo al frente de tres gestiones.

Este martes Massa recibió el respaldo de la CGT en la localidad bonaerense de Malvinas Argentinas, en un acto promovido por la alianza sindical que maneja la CGT, integrada por “los Gordos” (Héctor Daer y Armando Cavalieri, de Comercio) y los independientes (Andrés Rodríguez, de UPCN; Gerardo Martínez, de UOCRA, y José Luis Lingeri, de Obras Sanitarias).

Se trata de la misma dirigencia sindical que fue una firme aliada de Alberto Fernández desde que asumió, en diciembre de 2019, pero comenzó a tomar distancia de él cuando comenzó la gestión de Massa en Economía, hace un año, cuando la mayor parte del sindicalismo interpretó que podía domesticar la inflación y darle expectativas de un triunfo electoral al Frente de Todos.

Durante su alocución, Massa cuestionó a los candidatos que llaman a “abrir la economía y que venga todo importado, sin importarles el trabajo de nuestra gente. A nosotros nos importa una economía argentina que ocupe lugar en el mundo, que venda, que exporte. No una economía argentina que transforme a las fábricas en cementerios”.

“El domingo se empieza a discutir a que Argentina vamos. Están ellos planteando la eliminación de la indemnización por despido, de las vacaciones pagas, de la ultractividad de los convenios colectivos de trabajo, ellos que hablan del trabajo como un costo y no como el elemento de dignidad más importante que tenemos como sociedad”, dijo.

Massa centró su discurso en la recuperación del salario, la reivindicación de las paritarias y advirtió de que si Juntos por el Cambio gana las elecciones se precarizarán las relaciones laborales. “El domingo cuando vayamos a votar va a ser en defensa de los jubilados, frente a los que quieren hacer recortes”, resaltó y agregó: “El domingo, cueste lo que cueste, tenemos que ganar”.
"""

print(summarizer(ARTICLE, max_length=300, min_length=200, do_sample=False))
