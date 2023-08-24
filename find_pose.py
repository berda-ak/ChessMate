import cv2
import statistics as st


def square_color(buyuk_kare):
    
    y=len(buyuk_kare)
    x=len(buyuk_kare[0])

    bas_bosluk = int( 0.1 * x) -1
    alt_bosluk = int( 0.1 * y) - 1

    yatay= int((x - 2* bas_bosluk )/3)
    dikey= int((y - 2* alt_bosluk )/3)


    kareler=[]

    for k in range(0,9): #hangi karede
        toplam_r=0
        toplam_g=0
        toplam_b=0
        for i in range(bas_bosluk+(k%3)*yatay,bas_bosluk+((k%3)+1)*yatay ):
            for j in range(alt_bosluk+int((k/3))*dikey,alt_bosluk+int((k/3))*dikey+dikey):
                toplam_r= toplam_r+ buyuk_kare[j][i][0]
                toplam_g= toplam_g+ buyuk_kare[j][i][1]
                toplam_b= toplam_b+ buyuk_kare[j][i][2]
        kareler.append([int(toplam_r/(yatay*dikey)),int(toplam_g/(yatay*dikey)),int(toplam_b/(yatay*dikey))] )

    return kareler  



def find(buyuk_kare, kare_rengi):

   # kare rengi ==>> sarı için 1 , kahve için 0
   # return ==>> boş için -1, siyah taş için 0 , beyaz taş için 1 
   y=len(buyuk_kare)
   x=len(buyuk_kare[0])

   bas_bosluk = int( 0.1 * x) -1
   alt_bosluk = int( 0.1 * y) - 1

   list_1 = [buyuk_kare[k][i][0] for k in range(alt_bosluk,len(buyuk_kare)-alt_bosluk) for i in range(bas_bosluk,len(buyuk_kare[0])-bas_bosluk)]
   list_2 = [buyuk_kare[k][i][1] for k in range(alt_bosluk,len(buyuk_kare)-alt_bosluk) for i in range(bas_bosluk,len(buyuk_kare[0])-bas_bosluk)]
   list_3 = [buyuk_kare[k][i][2] for k in range(alt_bosluk,len(buyuk_kare)-alt_bosluk) for i in range(bas_bosluk,len(buyuk_kare[0])-bas_bosluk)]

   derivations = [st.stdev(float(x) for x in list_1),st.stdev(float(x) for x in list_2),st.stdev(float(x) for x in list_3)]

   '''print( st.stdev(float(x) for x in list_1))
   print( st.stdev(float(x) for x in list_2))
   print( st.stdev(float(x) for x in list_3))'''

   if derivations[0]<=9 and derivations[1]<=9 and derivations[2]<=9:
      return -1 #bos
   
   elif derivations[0]>=20 and derivations[1]>=20 and derivations[2]>=20:
      if kare_rengi==1:
         return 0 #siyah
      else:
         return 1 #beyaz
      

   elif square_color(buyuk_kare)[4][0]<= 90 and  square_color(buyuk_kare)[4][1]<= 90 and square_color(buyuk_kare)[4][2]<= 90:
      return 0 #siyah
   
   else:
      return 1 #beyaz



kare = cv2.imread("32.png") 
# kare rengi ==>> sarı için 1 , kahve için 0
# return ==>> boş için -1, siyah taş için 0 , beyaz taş için 1 

x = find(kare,1)
if x == 0:
   print("siyah tas")
elif x == 1:
   print("beyaz tas")
else:
   print("bos")







            
            


   













