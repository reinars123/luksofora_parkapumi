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

def drawLine un drawPoint kods, lai lietotājs var iezīmēt manuāli video pārkāpuma  līniju un punktu luksofora gaismas izsekošanai.
![image](https://user-images.githubusercontent.com/106994489/172235015-0c90cdce-f1af-42fb-900c-760cfbc288f7.png)
![image](https://user-images.githubusercontent.com/106994489/172235254-41fc74b4-119a-4957-9f38-4bc415de77c9.png)
![image](https://user-images.githubusercontent.com/106994489/172235287-b193d5fb-8092-4a84-b4a7-21dc073a7fdf.png)

video rāmis

![image](https://user-images.githubusercontent.com/106994489/172236683-28e8a3cc-70ae-42d9-a72b-e6438a2bd9d9.png)

for box in boxes uzzīmē taisnstūrus ap objektiem un ieliek centrētu punktu

![image](https://user-images.githubusercontent.com/106994489/172236771-33fcfd5f-2d13-4d02-8077-c7666cd99e0b.png)

pārbauda luksofora krāsu

![image](https://user-images.githubusercontent.com/106994489/172238903-4f812e92-564c-4da8-a6e8-4deb9c88cb67.png)


piešķir identifikāciju objektiekm un starp kadriem nosaka vai tas objekts vēl ir ekrānā un ja nav tad izdzēš

skaita un saglabā pārkāpumus

![image](https://user-images.githubusercontent.com/106994489/172237912-e70def69-45fc-4a65-80fa-1bcb2e0e5b40.png)
