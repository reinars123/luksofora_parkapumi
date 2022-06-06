# Python projekts, kas izmanto yolo4 un opencv, lai uzskaitītu mašīnas, kas pārbrauc pār sarkano luksofora gaismu.
<b> Autori: </b> Oskars Zandersons, Raivo Rogošs Edvarts Počs, Reinārs Brokāns.
## Apraksts
### <b> Aizmugursistēma: </b> 
1. yolo4 - bibliotēka priekš objekta atklāšanas
2. opencv - bibliotēka ir priekš objektu izskekošanas
### <b> Frontend: </b>

### <b> programmas darbība </b>

object_detection.py tiek atklāj objektus ar neironu tīklu.
![image](https://user-images.githubusercontent.com/106994489/172222787-248e3c40-36b4-4a5f-98c3-b39d9a4d5418.png)

Trafficproject.py tiek izvēlēts video. 
![image](https://user-images.githubusercontent.com/106994489/172234510-77478fe0-75b2-4ee4-80b2-8e8c30e8781a.png)

duplikātu pārbaude
![image](https://user-images.githubusercontent.com/106994489/172234580-4070f3b5-c574-490f-a422-4562bce02c56.png)

saglabā bildi, kad izsauc komandu

def drawLine un drawPoint kods, lai lietotājs var iezīmēt manuāli video pārkāpuma  līniju
![image](https://user-images.githubusercontent.com/106994489/172235015-0c90cdce-f1af-42fb-900c-760cfbc288f7.png)
![image](https://user-images.githubusercontent.com/106994489/172235254-41fc74b4-119a-4957-9f38-4bc415de77c9.png)
![image](https://user-images.githubusercontent.com/106994489/172235287-b193d5fb-8092-4a84-b4a7-21dc073a7fdf.png)

image = frame video rāmis

for box in boxes uzzīmē taisnstūrus ap objektiem un ieliek centrētu punktu

piešķir identifikāciju obketiekm un starp kadriem nosaka vai tas objekts vēl ir ekrānā un ja nav tad izdzēš

for object_id skaita un saglabā pārkāpumus
