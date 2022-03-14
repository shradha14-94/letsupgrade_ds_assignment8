#assignment8.1  try & except
# The code below takes the list of country (country) & searches to see if it is in the dictionary gold which
# shows the some countries who can gold during  the olympics.
# country _gold with either the number of golds won or the string"did not get gold"



gold = {"US":46, "FiJi":1, "Great Britain":27, "cuba":5, "Thailand":2, "China":26, "France":10}
country= ["FiJi","Chile","Mexico","France","Norway","US"]
country_gold=[]

for x in country:
    try:
        country_gold.append(gold[x])
        print(country_gold)
           
    except KeyError:
        country_gold.append("did not get gold")
        print(country_gold)
        


	
