#from requests_html import HTMLSession
from rake_nltk import Rake
import nltk
nltk.download('stopwords')
nltk.download('punkt')


#text = "Subsequently, urban development was marked by the increase in population due to immigration from other parts of Spain, which led to various urban projects such as the Regional Plan of 1953 or the General Metropolitan Plan of 1976. Likewise, the adaptation of the urban space of the city has been favored between the 19th and 21st centuries by various events held in the city, such as the Universal Exposition of 1888, the International Exposition of 1929, the XXXV International Eucharistic Congress of 1952, the Olympic Games of 1992 and the Universal Forum of Cultures of 2004."

text = "Posteriormente, el desarrollo urbanístico estuvo marcado por el aumento de la población debido a la inmigración desde otras partes de España, lo que conllevó diversos proyectos urbanísticos como el Plan Comarcal de 1953 o el Plan General Metropolitano de 1976. Igualmente, la adecuación del espacio urbano de la ciudad se ha visto favorecida entre los siglos XIX y XXI por diversos eventos celebrados en la ciudad, como la Exposición Universal de 1888, la Internacional de 1929, el XXXV Congreso Eucarístico Internacional de 1952, los Juegos Olímpicos de 1992 y el Fórum Universal de las Culturas de 2004."

noticia1= ''' 
Militant, photojournalist and ex-combatant of the FARC. He was 47 years old. He was the son of the Justice of the Peace from Trevelin, Chubut.
Facundo Molares Schoenfeld, 47, died this Thursday afternoon after suffering a cardiac arrest at the Buenos Aires Obelisk, in the framework of a left-wing demonstration. The militant, photojournalist and former FARC combatant had spent a year in prison in Bolivia and eight months in Ezeiza Federal Penitentiary Unit No. 6. Resuscitation maneuvers were performed on him for more than half an hour until his death was confirmed at the Ramos Mejía Hospital.

“The causes of death are related to cardiac arrest resulting from risk factors. The body was transferred to the judicial morgue for the corresponding autopsy”, detailed sources from the Buenos Aires government.

Molares Schoenfeld grew up and lived in the Buenos Aires town of José C. Paz, until in his adolescence his family decided to settle in Trevelin, in the province of Chubut, where he finished secondary school. According to his father, Hugo Molares, Justice of the Peace of Trevelin, said that he wanted to be like Ernesto Che Guevara. He began to be a member of the Communist Youth, and his activity led him to tour Ecuador, Cuba, Paraguay, Brazil, Peru, Chile and Bolivia, until he reached Colombia. There he joined the ranks of the FARC, where his companions nicknamed him "Camilo el Argentino."
In November 2019, when the coup against then-President Evo Morales was unleashed in Bolivia, Facundo Molares was tempted by some photographer colleagues "to cover" the events. During the coverage, he was shot three times, lost 80% of the vision in his right eye and remained hospitalized and in a coma for 23 days.
“There were coincidences that hurt me. Those days Evo Morales was in Buenos Aries and had said that in the face of the constitutional disobedience of the armed forces a popular militia should be formed. I fell like a glove ”, he explained in a report to Télam, on July 30, about the year that he was detained and with preventive detention in the maximum security prison of Chonchocoro, during the de facto government of Jeanine Áñez .

One month after Áñez's departure, and after the plea in her favor made by the Argentine consul Roberto Dupuy, the photojournalist was released in Bolivia on December 2, 2020.

Molares returned to the country and settled in his father's house, in the town of Trevelin, where he was trying to rebuild his life until November 7, 2021, when he was arrested by the Federal Police based on an Interpol order, based on an arrest warrant from the Colombian Judiciary.

The former FARC was accused of the kidnapping of councilman Armando Acuña, committed on March 25, 2009 in the municipality of Garzón, and he spent almost eight months in prison in Ezeiza Federal Penitentiary Unit No. 6 awaiting the verdict of the trial for his extradition. to the coffee country.
The request issued by the Colombian authorities from the 162 Specialized Prosecutor's Office DECOD Florencia included the qualifications of aggravated kidnapping for extortion, manufacturing, trafficking and carrying of restricted-use weapons and ammunition, private use of armed forces and illegal use of uniforms and insignia.
"The facts for which I was accused had to do with the armed conflict and that can only be investigated by the Special Jurisdiction for Peace (the Colombian judicial body that mediated in the Peace Accords)," Molares recalled in dialogue with Télam.

On Friday, July 8, 2021, the lawyers for Molares, Gustavo Franquet and Eduardo Soares, who are members of La Gremial de Abogados, were notified by the JEP of their rejection of the extradition request, which caused the judge to federal of Esquel, Guido Otranto, will finally order his release.

"I want to thank everyone who has helped," said Molares upon regaining his freedom after months of detention in Ezeiza.
After learning the news of the death of the photojournalist, from the Center for Legal and Social Studies (CELS) they repudiated the circumstances through their social networks.

“The militant and photojournalist Facundo Molares died as a result of the repression of the City police against a demonstration at the Obelisk. The troops advanced on those who were demonstrating on the esplanade of the Plaza de la República and began to beat them. They then pinned them to the ground. At that moment, molars broke down. The death of Facundo, whom we knew, is irreparable. We accompany his family and colleagues at this painful moment, ”they wrote.
'''

noticia2= ''' 
The head of the Buenos Aires Government, Horacio Rodríguez Larreta, lamented the death of Facundo Molares after the repression of the City Police in the Obelisk, praised the actions of that security force and affirmed that "violence is the limit."

"Today in the framework of a demonstration with incidents, Facundo Molares died after a decompensation. I regret his death and extend my condolences to his family," Larreta said from his social networks, through a statement titled "An Argentina in peace and without fear."

The Buenos Aires mayor gave his support "completely" to the "action of the City Police" and said that the CABA police force that carried out the operation "acted professionally, containing the acts of violence."

Larreta also praised SAME for his intervention in the episode, noting that he "gave an answer, as usual, always taking care of the residents of the City."

In addition, he stated that "Argentines need to live in peace" and considered "political speculation like the one we are seeing" unacceptable.

"As I have been arguing for a long time, we have to leave behind the violence, the aggressions and the confrontation," he added.

Finally, he announced that he "will lead" together with "millions of Argentines that process of an Argentina in peace, where we can live calmly and without fear."

repression and death

Molares, 47, died a few meters from the Obelisk after the repression by the City Police of a protest carried out by left-wing groups and social organizations called "against the electoral farce and for the democracy of the people."

The agents who acted in front of the demonstration belong to the Urban Containment Operations Division (DOUC) and were under the command of police station 1-B of the Buenos Aires Police, as could be established from the National Criminal Correctional Prosecutor's Office 30, through charge of the prosecutor Marcela Sánchez.

Prosecutor Sánchez, who is leading the investigation, ordered the identification of the troops who participated in the operation and commissioned the judicial intervention division of the Federal Police (PFA) to carry out the evidence.'''


cap1= ''' 
Who was Facundo Molares Schoenfeld, the man killed in the repression at the Obelisk
In 2019 he traveled to Bolivia to cover the coup against President Evo Morales. He was shot three times in Montero, during a repression. He spent 23 days in an induced coma. He was left with sequelae: heart problems and almost complete loss of vision in his right eye.


Facundo Molares Schoenfeld was born in 1975, the son of a union activist at Hospital Ciudadela. He grew up in José C. Paz and in the early 90s he settled in Patagonia. In those years he began his militancy against the policies of Menemism.

Back in Buenos Aires, received as a forester, he settled in the villa 1-11-14. He mobilized on December 19 and 10, 2001. A little later, he set out to tour Latin America, inspired by the figure of Che Guevara. He passed through Paraguay, Bolivia, Peru and Ecuador before arriving in Colombia.

There, in 2003, he joined the Revolutionary Armed Forces of Colombia (FARC), joining the Teófilo Forero Column in the town of Los Pozos. By then he took the name of Camilo Fierro. Critical of the peace agreement, he left in 2018.'''

cap2 = ''' 
Who was Facundo Molares, the man who died after the incidents at the Obelisk
Militant, photojournalist and ex-combatant of the FARC. He was 47 years old. He was the son of the Justice of the Peace from Trevelin, Chubut

Facundo Molares Schoenfeld, 47, died this Thursday afternoon after suffering a cardiac arrest at the Buenos Aires Obelisk, in the framework of a left-wing demonstration. The militant, photojournalist and former FARC combatant had spent a year in prison in Bolivia and eight months in Ezeiza Federal Penitentiary Unit No. 6. Resuscitation maneuvers were performed on him for more than half an hour until his death was confirmed at the Ramos Mejía Hospital.

“The causes of death are related to cardiac arrest resulting from risk factors. The body was transferred to the judicial morgue for the corresponding autopsy”, detailed sources from the Buenos Aires government.

Molares Schoenfeld grew up and lived in the Buenos Aires town of José C. Paz, until in his adolescence his family decided to settle in Trevelin, in the province of Chubut, where he finished secondary school. According to his father, Hugo Molares, Justice of the Peace of Trevelin, said that he wanted to be like Ernesto Che Guevara. He began to be a member of the Communist Youth, and his activity led him to tour Ecuador, Cuba, Paraguay, Brazil, Peru, Chile and Bolivia, until he reached Colombia. There he joined the ranks of the FARC, where his companions nicknamed him "Camilo el Argentino."'''

r = Rake()
r.extract_keywords_from_text(cap1)
for rating, keyword in r.get_ranked_phrases_with_scores():
    if rating > 5:
        print(rating, keyword)

print("/////////////")

r = Rake()
r.extract_keywords_from_text(cap2)
for rating, keyword in r.get_ranked_phrases_with_scores():
    if rating > 5:
        print(rating, keyword)