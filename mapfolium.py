import folium
import pandas

#pandas.read_excel()
path=r"D:\map\\"
data = pandas.read_excel(path+"iit_data.xlsx")

iit_ranking = list(data["IIT Ranking"])
college_name = list(data["IIT College"])
Nirf_score = list(data["NIRF Score"])
lat = list(data["Latitude"])
lon = list(data["Longitude"])
pic = list(data["Image"])
fg = folium.FeatureGroup("m")
fg.add_child(folium.GeoJson(data =(open(path+"india_states.json","r",encoding="utf-8-sig").read())))
for rank , name , score , lati , longi , ima in zip(iit_ranking,college_name,Nirf_score,lat,lon,pic):
    print(lati,longi)
    fg.add_child(folium.Marker(location=[lati , longi] , popup="<b>college Name : </b>"+str(name)+
    "<br> <b>Rank among IIT in Indian : </b>"+ str(rank)+
    "<br> <b>NIRF Score : </b>"+ str(score)+
    "<br> <img scr"+ima+
    "height =145 , width = 300>",icon = folium.Icon(color="red")))
m = folium.Map(location =[20.0000,75.0000],zoom_start = 4)
m.add_child(fg)
m.save(path+"final.html")
