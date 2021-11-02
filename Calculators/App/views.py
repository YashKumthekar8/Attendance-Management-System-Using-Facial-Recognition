import math
from django.shortcuts import render



def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)


def convert2(val,u1,num):
  if val=="volt":
    if u1=='V':
      return float(num),""
    elif u1=="mV":
      return float(num/1000),"/1000"
    elif u1=="kV":
      return float(num*1000),"*1000"
    elif u1=="MV":
      return float(num*1000000),"* 10"+add_tags("sup",6)
    else:
      return num,""       
  
  elif val=="res":
    if u1=="Ω":
     return float(num),""
    elif u1=="mΩ":
      return float(num/1000),"/1000"
    elif u1=="kΩ":
      return float(num*1000),"*1000"
    elif u1=="MΩ":
      return float(num*1000000),"* 10 "+add_tags("sup",6)  
    else:
      return 1,"";  

  elif val=="curr":
    if u1=='A':
     return float(num),""
    elif u1=="mA":
      return float(num/1000),"/1000"
    elif u1=="µA":
      return float(num/1000000),"/( 10"+add_tags("sup",6)+")"    
    else:
      return 1,"";  

  elif val=="mass":
    if u1=='g':
        return num,"/1000"
    elif u1=='kg':
        return num*1000,"" 
    elif u1=='mg':
        return num/1000,"/1000000"      
    elif u1=='µg':
        return num/(10**6),"/( 10 "+add_tags("sup",9)+")"
    elif u1=='dg':
        return num/10,"/10000"
    elif u1=='t':
        return num*(10**6),"*1000"
    elif u1=='oz':
        return num*28.34,"*0.02834"
    elif u1=='lb':
        return num*453.3,"*0.4533"
    elif u1=='me':
      return num*9.10938356*(10**-28),"* 9.109 * 10" + add_tags("sup",-31)
    elif u1=='mp':
      return num*1.672621898*(10**-24),"* 1.67 * 10" + add_tags("sup",-27)
    elif u1=='mn':
      return num*1.672621898*(10**-24),"* 1.67 * 10" + add_tags("sup",-27)
    elif u1=='u':
      return num*1.67*(10**-24),"* 1.67 * 10" + add_tags("sup",-27)
    elif u1=='e':
      return num*9.1094e-28,"* 9.1 * 10" + add_tags("sup",-31)
    else:
      return num,"" 
  
  
  elif val=="len":
    if u1=='m':
        return num,""
    elif u1=='nm':
        return num/(10**9),"* 10 " + add_tags("sup",-9) 
    elif u1=='pm':
        return num/(10**12),"* 10 " + add_tags("sup",-12)      
    elif u1=='µm':
        return num/(10**6),"* 10 " + add_tags("sup",-6)
    elif u1=='mm':
        return num/1000,"* 10" + add_tags("sup",-3)
    elif u1=='ft':
        return num*0.304,"* 0.304"
    elif u1=='in':
        return num*0.025,"* 0.025 "
    elif u1=='km':
       return num*1000 ,"* 1000"   
    elif u1=='cm':
       return num/100 ,"/100"   
    else:
      return num,""

  elif val=="charge":

    if u1=='C':
     return float(num),""
    elif u1=="mC":
      return float(num/1000),"/1000"
    elif u1=="μC":
      return float(num/1000000),"* 10" + add_tags("sup",-6)  
    elif u1=="nC":
      return float(num/(10**9)),"* 10" + add_tags("sup",-9)
    elif u1=="PC":
      return float(num/(10**12)),"* 10" + add_tags("sup",-12)
    elif u1=='e':
      return num*1.60218e-19,"* 1.602 "+ add_tags("sup",-19)    
    else:
      return num*2,""    

  elif val=="force":
    if u1=='N':
        return num,""
    elif u1=='kN':
        return num*1000,"* 1000"
    elif u1=='mN':
        return num/1000,"* 10" + add_tags("sup",-3)      
    elif u1=='μN':
        return num/(10**6),"* 10" + add_tags("sup",-6)
    elif u1=='d':
        return num/(10**5),"* 10" + add_tags("sup",-5)
    else:
      return num,""    
  
  elif val=="cap":
    if u1=='F':
        return num,""
    elif u1=='mF':
        return float(num/1000),"* 10 " + add_tags("sup",-3) 
    elif u1=='nF':
        return float(num/(10**9)),"* 10 " + add_tags("sup",-9)      
    elif u1=='µF':
        return float(num/(10**6)),"* 10 " + add_tags("sup",-6)
    else:
      return 1,""    

  elif val=="ind":
    if u1=='H':
        return num,""
    elif u1=='mH':
        return float(num/1000),"* 10 "+ add_tags("sup",-3) 
    elif u1=='nH':
        return float(num/(10**9)),"* 10 " + add_tags("sup",-9)      
    elif u1=='µH':
        return float(num/(10**6)),"* 10 " + add_tags("sup",-6)
    else:
      return 100,""       

  elif val=="freq":
    if u1=='Hz':
        return num,""
    elif u1=='mHz':
        return float(num/1000),"* 10 " + add_tags("sup",-3) 
    elif u1=='MHz':
        return float(num*(10**6)),"* 10 " + add_tags("sup",6)      
    elif u1=='kHz':
        return float(num*1000),"* 10 * " + add_tags("sup",3)
    else:
      return 1,""    

 
  elif val=="vel":
    if u1=='m/s':
        return num,""
    elif u1=='km/hr':
        return float(num*0.27)," * 0.27" 
    elif u1=='ft/s':
        return float(num*0.34),"* 0.34"      
    elif u1=='mph':
        return float(num*0.45)," * 0.45"
    else:
      return num,""              

  elif val=="temp":
    if u1=='°C':
        return num,""
    elif u1=='K':
        return num-273.15," -273.15"
    elif u1=='°F':
        return 5/9*(num-32),""      
    else:
      return 1,""              
    

  elif val=="time":
    if u1=="s":
      return num,""
    elif u1=="ms":
      return num/1000,"/1000"
    elif u1=="ns":
      return num/(10**9),"* 10 " + add_tags("sup",-9)
    elif u1=="ps":
      return num/(10**12),"* 10 " + add_tags("sup",-12)  
    elif u1=="min":
      return num*60,"*60"
    elif u1=="hr":
      return num*3600,"*3600"
    elif u1=="day":
      return num*86400,"*86400"
    elif u1=="week":
      return num*86400*7,"*86400*7"
    elif u1=="month":
      return num*2.628e+6,"* 2.628 * 10"+add_tags("sup",6) 
    elif u1=="year":
      return num*3.154e+7,"*3.154 * 10"+add_tags("sup",7)          
    else:
      return 1,""    
  
  elif val=="flow":
    if u1=="m/s":
      return num,""
    elif u1=="l/s":
      return num*0.01,"*0.01"
    elif u1=="cm/s":
      return num*(10**-6),"* 10" + add_tags("sup",-6)
    elif u1=="m/min":
      return num/60,"/ 60 "
    elif u1=="l/min":
      return num*0.01/60,"*0.01/60"
    elif u1=="cm/min":
      return num*(10**-6)/60,"* 10 "+ add_tags("sup",-6)+"/60"    
    else:
      return 1,""

  elif val=="energy":
    if u1=='J':
      return num,""
    elif u1=='kJ':
      return num*1000,"*1000"
    elif u1=='MJ':
      return num*(10**6),"*1000000"
    elif u1=="wh":
      return num*3600,"*3600"  
    elif u1=="kwh":
      return num*3.6e6,"*36000000"  
  
  elif val=="frequency":
    if u1=="per/second":
      return num,""
    elif u1=="per/min":
      return num/60,"/60"
    elif u1=="per/hour":
       return num/3600,"/3600"
    elif u1=="per/day":
       return num/86400,"/86400"   
    elif u1=="per/week":
      return num/(86400*7),"/( 86400*7 )"
    elif u1=="per/month":
      return num/2.628e+6,"/( 2.628 * 10"+add_tags("sup",6)+")" 
    elif u1=="per/year":
      return num/3.154e+7,"/ ( 3.154 * 10"+add_tags("sup",7)+")"          
    

    
#FUCNTUON FOR CALCULATING THE MATERIAL FOR THE 
def materialValueCalculator(val):
   if val=="ABS":
     return 130
   elif val=="Aluminum":
     return 140  
   elif val=="Asbestos Cement":
     return 140  
   elif val=="Asphalt Lining":
     return 135
   elif val=="Brass":
     return 135
   elif val=="Brick sewer":
     return 95
   elif val=="Cast-Iron - new unlined (CIP)":
     return 130
   elif val=="Cement lining":
     return 135
   elif val=="Concrete":
     return 120
   elif val=="Concrete lined, steel forms":
     return 140
   elif val=="Concrete lined, wooden forms":
     return 120
   elif val=="Copper":
     return 135
   elif val=="Corrugated Metal":
     return 60
   elif val=="Ductile Iron Pipe (DIP)":
     return 120
   elif val=="Fiber":
     return 140
   elif val=="Fiber Glass Pipe - FRP":
     return 150
   elif val=="Galvanized iron":
     return 120
   elif val=="Glass":
     return 130
   elif val=="Lead":
     return 135
   elif val=="Metal Pipes - Very to extremely smooth":
     return 135
   elif val=="Plastic":
     return 140
   elif val=="Polyvinyl chloride, PVC, CPVC":
     return 150
   elif val=="Tin":
      return 130
   elif val=="Wood Stave":
      return 115         
       
     
#DICTIONARY FOR THE SPECIFIC HEAT OF A SUBSTANCE
specificHeat={
'Aluminium':897,
'Asphalt'	:915,
'Bone' :  440,
'Boron' :1106,
'Brass':920,
'Brick':841,
'Cast Iron':554,
'Clay':878,
'Coal':	1262,
'Cobalt':420,
'Concrete':	879,	
'Copper':385,
'Glass':792,
'Gold':130,
'Granite':774,
'Gypsum':1090,
'Helium':5192,
'Hydrogen':14300,
'Ice':2090,
'Iron':462,
'Lead':130,
'Limestone':806,
'Lithium':3580,	
'Magnesium':1024,	
'Marble':832,	
'Mercury':126,
'Nitrogen':	1040,
'Oak Wood':	2380,
'Oxygen':919,
'Platinum':150,	
'Plutonium':140,
'Quartzite':1100,
'Rubber':2005,
'Salt':881,	
'Sand':780,
'Sandstone':740,
'Silicon':710,
'Silver':236,
'Soil':1810,
'Stainless Steel': 316,
'Steam':2094,
'Sulfur':706,
'Thorium':118,
'Tin':226,	
'Titanium':521,
'Tungsten':133,	
'Uranium':115,	
'Vandium':490,	
'Water':4187,
'Zinc':	389,
}
  

#FUNCTION FOR THE ROUNDING OFF THE NUMBER
def Roundoff(n):
  base=""
  power=""
  n='%.2E' % n
  s=str(n)
  base=""
  power=""
  f=False
  for i in range(0,len(s)):
    if s[i]=='E':
        f=True
        continue
    if f:
        power+=s[i]
    else:
        base+=s[i]           
   
  return base,power
  
      


def ohmslawcalculator(request):

  if request.method=='POST':
     given_data=request.POST.get('given_data')
     
      #VALUE FOR THE Current
     if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
      inp=str(request.POST.get('Ia'))
      if inp.isdigit():
          Ia=int(request.POST.get('Ia'))
      else:
          Ia=float(request.POST.get('Ia'))
     else:
        Ia=None

    #VALUE FOR THE resistance
     if request.POST.get('Ib')!=None and request.POST.get('Ib')!='':
      inp=str(request.POST.get('Ib'))
      if inp.isdigit():
          Ib=int(request.POST.get('Ib'))
      else:
          Ib=float(request.POST.get('Ib'))
     else:
      Ib=None

    #VALUE FOR THE  VOLTAGE
     if request.POST.get('F')!=None and request.POST.get('F')!='':
      inp=str(request.POST.get('F'))
      if inp.isdigit():
          F=int(request.POST.get('F'))
      else:
          F=float(request.POST.get('F'))
     else:
      F=None


     if given_data=="form1" and Ia and Ib:
       
       #Copy of the values
       Ia1=Ia
       Ib1=Ib
       
       #Units
       Ia_op=request.POST.get('Ia_op')
       Ib_op=request.POST.get('Ib_op')

       #Copying of the units
       Ia1_op=Ia_op
       Ib1_op=Ib_op

       #Converting Units
       Ia,Ia_c=convert2("curr",Ia_op,Ia)
       Ib,Ib_c=convert2("res",Ib_op,Ib)

       F=Ia*Ib
       #Power 
       p=F*Ia
  

       if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
       else:
        Ia=round(Ia,5)
       
       if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
       else:
         Ib=round(Ib,5) 

       if not  ((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
         base1,power1=Roundoff(p)
         p=f"{base1} X 10"+add_tags('sup',power1)
       else:
         p=round(p,5) 
       
       if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
       else:
         F=round(F,5) 


       context={
         'F':F,
         'Ia':Ia,
         'Ib':Ib,
         'Ia1':Ia1,
         'Ib1':Ib1,
         'Ia_op':Ia_op,
         'Ib_op':Ib_op,
         'Ia1_op':Ia1_op,
         'Ib1_op':Ib1_op,
         'p':p,
         'given_data':given_data,
         'id':1,
         'Ia_c':Ia_c,
         'Ib_c':Ib_c
       }

       return render(request,'ohmslawcalculator.html',context)
     
     
     elif given_data=="form2" and F and Ib:
       
       
       #Copy of the values
       
       Ib1=Ib
       F1=F

       #Units
       F_op=request.POST.get('F_op')
       Ib_op=request.POST.get('Ib_op')
       
       
       #Copying of the units
       F1_op=F_op
       Ib1_op=Ib_op

       F,F_c=convert2("volt",F_op,F)
       Ib,Ib_c=convert2("res",Ib_op,Ib)

       Ia=F/Ib
       Ia1=Ia
       #Power 
       p=F*Ia
       
       if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
       else:
        Ia=round(Ia,5)
       
       if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
       else:
         Ib=round(Ib,5) 

       if not  ((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
         base1,power1=Roundoff(p)
         p=f"{base1} X 10"+add_tags('sup',power1)
       else:
         p=round(p,5) 
       
       if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
       else:
         F=round(F,5) 
       
       

       context={
         'F':F,
         'Ia':Ia,
         'Ib':Ib,
         'F1':F1,
         'Ia1':Ia1,
         'Ib1':Ib1,
         'F_op':F_op,
         'Ib_op':Ib_op,
         'F1_op':F1_op,
         'Ib1_op':Ib1_op,
         'p':p,
         'given_data':given_data,
         'id':1,
         'F_c':F_c,
         'Ib_c':Ib_c
       }

       return render(request,'ohmslawcalculator.html',context)

     elif given_data=="form3" and F and Ia:
       
       #Copy of the values
       Ia1=Ia
       F1=F

       #Units
       F_op=request.POST.get('F_op')
       Ia_op=request.POST.get('Ia_op')

       #Copying of the units
       F1_op=F_op
       Ia1_op=Ia_op
       
       F,F_c=convert2("volt",F_op,F)
       Ia,Ia_c=convert2("curr",Ia_op,Ia)

       Ib=F/Ia
       Ib1=Ib
       #Power 
       p=F*Ia

       if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
       else:
        Ia=round(Ia,5)
       
       if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
       else:
         Ib=round(Ib,5) 

       if not  ((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000 )):
         base1,power1=Roundoff(p)
         p=f"{base1} X 10"+add_tags('sup',power1)
       else:
         p=round(p,5) 
       
       if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
       else:
         F=round(F,5)  
      
       

       context={
         'F':F,
         'Ia':Ia,
         'Ib':Ib,
         'F1':F1,
         'Ia1':Ia1,
         'Ib1':Ib1,
         'F_op':F_op,
         'Ia_op':Ia_op,
         'F1_op':F1_op,
         'Ia1_op':Ia1_op,
         'p':p,
         'given_data':given_data,
         'id':1,
         'F_c':F_c,
         'Ia_c':Ia_c
       }

       return render(request,'ohmslawcalculator.html',context)
   
     else:
      return render(request,'ohmslawcalculator.html',{'given_data':given_data})  

  else:  
   return render(request,'ohmslawcalculator.html',{'given_data':'form1'})





def accelerationofparticleinelectricfield(request):
   if request.method=='POST':
      given_data=request.POST.get('given_data')

      if request.POST.get('Ia')!=None and  request.POST.get('Ia')!="":
        inp=str(request.POST.get('Ia'))
        if inp.isdigit():
          Ia=int(request.POST.get('Ia'))
        else:
         Ia=float(request.POST.get('Ia'))

      else:
        Ia=None


      if request.POST.get('Ib')!=None and request.POST.get('Ib')!="":
        inp=str(request.POST.get('Ib'))
        if inp.isdigit():
          Ib=int(request.POST.get('Ib'))
        else:
          Ib=float(request.POST.get('Ib'))

      else:
        Ib=None


      if request.POST.get('F')!=None and request.POST.get('F')!="":
        inp=str(request.POST.get('F'))
        if inp.isdigit():
          F=int(request.POST.get('F'))
        else:
         F=float(request.POST.get('F'))
      else:
        F=None


      if request.POST.get('d')!=None and request.POST.get('d')!="":
        inp=str(request.POST.get('d'))
        if inp.isdigit():
          d=int(request.POST.get('d'))
        else:
          d=float(request.POST.get('d'))

      else:
        d=None

      if given_data=='form1' and Ia and Ib and d:
        #Copying the variables
        Ia1=Ia
        Ib1=Ib
        d1=d

        #Fetching the units  
        Ia_op=request.POST.get('Ia_op')
        Ib_op=request.POST.get('Ib_op')
        d_op=request.POST.get('d_op')

        #Conversion of units
        Ia,Ia_c=convert2("mass",Ia_op,Ia)
        Ib,Ib_c=convert2("force",Ib_op,Ib)
        d,d_c=convert2("charge",d_op,d)
        ###
        Ia=Ia/1000

        #Calculation
        F=Ib*d/Ia

        if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and round(Ia,3)<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
        else:
         Ia=round(Ia,5)
       
        if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and round(Ib,3)<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
        else:
          Ib=round(Ib,5) 

        if not  ((d>=1 and d<=10000) or (round(d,3)!=0 and round(d,3)!=0.001 and round(d,3)<=10000)):
         base1,power1=Roundoff(d)
         d=f"{base1} X 10"+add_tags('sup',power1)
        else:
         d=round(d,5) 
       
        if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and round(F,3)<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
        else:
         F=round(F,5)  
      

        #Passing the variables
        context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'd':d,
          'Ia1':Ia1,
          'Ib1':Ib1,
          'd1':d1,
          'Ia_op':Ia_op,
          'Ib_op':Ib_op,
          'd_op':d_op,
          'given_data':given_data,
          'id':1,
          'Ia_c':Ia_c,
          'Ib_c':Ib_c,
          'd_c':d_c,
          
        }

        #Rendering the template
        return render(request,'accelerationofparticleinelectricfield.html',context)
      
      
      elif given_data=='form2' and F and Ib and d:
        #Copying the variables
        F1=F
        Ib1=Ib
        d1=d

        #Fetching the units  
        F_op=request.POST.get('F_op')
        Ib_op=request.POST.get('Ib_op')
        d_op=request.POST.get('d_op')

        #Conversion of units
        
        Ib,Ib_c=convert2("force",Ib_op,Ib)
        d,d_c=convert2("charge",d_op,d)
        

        #Calculation
        Ia=Ib*d/F
        if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
          base1,power1=Roundoff(Ia)
          Ia=f"{base1} X 10 "+add_tags('sup',power1)
        else:
          Ia=round(Ia,5)
        
        if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
          base1,power1=Roundoff(Ib)
          Ib=f"{base1} X 10"+add_tags('sup',power1)
        else:
          Ib=round(Ib,5) 

        if not  ((d>=1 and d<=10000) or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
          base1,power1=Roundoff(d)
          d=f"{base1} X 10"+add_tags('sup',power1)
        else:
          d=round(d,5) 
        
        if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
          base1,power1=Roundoff(F)
          F=f"{base1} X 10"+add_tags('sup',power1)
        else:
          F=round(F,5)  
        


        #Passing the variables
        context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'd':d,
          'F1':F1,
          'Ib1':Ib1,
          'd1':d1,
          'F_op':F_op,
          'Ib_op':Ib_op,
          'd_op':d_op,
          'given_data':given_data,
          'id':1,
          'Ib_c':Ib_c,
          'd_c':d_c,
        }
        #Rendering the template
        return render(request,'accelerationofparticleinelectricfield.html',context)
      
      elif given_data=='form3' and F and Ia and d:
        #Copying the variables
        F1=F
        Ia1=Ia
        d1=d

        #Fetching the units  
        F_op=request.POST.get('F_op')
        Ia_op=request.POST.get('Ia_op')
        d_op=request.POST.get('d_op')

        #Conversion of units
        Ia,Ia_c=convert2("mass",Ia_op,Ia)
        d,d_c=convert2("charge",d_op,d)
        ###

        Ia=Ia/1000


        #Calculation
        Ib=Ia*F/d

        if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
          base1,power1=Roundoff(Ia)
          Ia=f"{base1} X 10 "+add_tags('sup',power1)
        else:
          Ia=round(Ia,5)
        
        if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
          base1,power1=Roundoff(Ib)
          Ib=f"{base1} X 10"+add_tags('sup',power1)
        else:
          Ib=round(Ib,5) 

        if not  ((d>=1 and d<=10000) or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
          base1,power1=Roundoff(d)
          d=f"{base1} X 10"+add_tags('sup',power1)
        else:
          d=round(d,5) 
        
        if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
          base1,power1=Roundoff(F)
          F=f"{base1} X 10"+add_tags('sup',power1)
        else:
          F=round(F,5)  
        


        #Passing the variables
        context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'd':d,
          'F1':F1,
          'Ia1':Ia1,
          'd1':d1,
          'F_op':F_op,
          'Ia_op':Ia_op,
          'd_op':d_op,
          'given_data':given_data,
          'id':1,
          'Ia_c':Ia_c,
          'd_c':d_c,
        }
        #Rendering the template
        return render(request,'accelerationofparticleinelectricfield.html',context)
      
      elif given_data=='form4' and F and Ia and Ib:
        #Copying the variables
        F1=F
        Ia1=Ia
        Ib1=Ib

        #Fetching the units  
        F_op=request.POST.get('F_op')
        Ia_op=request.POST.get('Ia_op')
        Ib_op=request.POST.get('Ib_op')

        #Conversion of units
        Ia,Ia_c=convert2("mass",Ia_op,Ia)
        Ib,Ib_c=convert2("force",Ib_op,Ib)
        
        ###
        Ia=Ia/1000

        #Calculation
        d=Ia*F/Ib
        
        if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
          base1,power1=Roundoff(Ia)
          Ia=f"{base1} X 10 "+add_tags('sup',power1)
        else:
          Ia=round(Ia,5)
        
        if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
          base1,power1=Roundoff(Ib)
          Ib=f"{base1} X 10"+add_tags('sup',power1)
        else:
          Ib=round(Ib,5) 

        if not  ((d>=1 and d<=10000) or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
          base1,power1=Roundoff(d)
          d=f"{base1} X 10"+add_tags('sup',power1)
        else:
          d=round(d,5) 
        
        if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)): 
          base1,power1=Roundoff(F)
          F=f"{base1} X 10"+add_tags('sup',power1)
        else:
          F=round(F,5)  
        


        #Passing the variables
        context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'd':d,
          'F1':F1,
          'Ia1':Ia1,
          'Ib1':Ib1,
          'F_op':F_op,
          'Ia_op':Ia_op,
          'Ib_op':Ib_op,
          'given_data':given_data,
          'id':1,
          'Ia_c':Ia_c,
          'Ib_c':Ib_c,
        }

        #Rendering the template
        return render(request,'accelerationofparticleinelectricfield.html',context)



      else:
        return render(request,'accelerationofparticleinelectricfield.html',{'given_data':given_data})

   else: 
    return render(request,'accelerationofparticleinelectricfield.html',{'given_data':'form1'})




def weightotherplanets(request):
  if request.method=='POST':
     
     given_data=request.POST.get('given_data')
     
     val={"Earth":1,"Mercury":0.38,"Venus":0.91,"Mars":0.38,"Jupiter":2.34,"Saturn":1.06,"Uranus":0.92,"Neptun":1.19,"Pluto":0.06,"Moon":0.167}
     
     names=["Earth","Mercury","Venus","Mars","Jupiter","Saturn","Uranus","Neptun","Pluto","Moon"]
     values=[1,0.38,0.91,0.38,2.34,1.06,0.92,1.19,0.06,0.167]
     

     form=False
     if 'f1' in request.POST:
       form=True

     if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
              inp=str(request.POST.get('Ia'))
              if inp.isdigit():
                  Ia=int(request.POST.get('Ia'))
              else:
                  Ia=float(request.POST.get('Ia'))
     else:
       Ia=None


     if given_data=="form1" and form:
       
       name="Earth"       
        
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       
       Ia=round(Ia/1000,6)

       ans=[]
       for i in val:
         j=round(val[i]*Ia,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)
     


     elif given_data=="form2" and form:
       name="Mercury" 
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)  
     


     elif given_data=="form3" and form:
       name="Venus"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)   
     


     elif given_data=="form4" and form:
       name="Mars"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)  
     


     elif given_data=="form5" and form:
       name="Jupiter"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)  
     


     elif given_data=="form6" and form:
       name="Saturn"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)  
     


     elif given_data=="form7" and form:
       name="Uranus"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,
         'Ia_c':Ia_c          
       }
       return render(request,'weightotherplanets.html',context)  
     


     elif given_data=="form8" and form:
       name="Neptun"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,    
         'Ia_c':Ia_c      
       }
       return render(request,'weightotherplanets.html',context)  
      


     elif given_data=="form9" and form:
       name="Pluto"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
         
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,   
         'Ia_c':Ia_c       
       }
       return render(request,'weightotherplanets.html',context) 
     


     elif given_data=="form10" and form:
       name="Moon"
       Ia1=Ia
       Ia_op=request.POST.get('Ia_op')
       Ia,Ia_c=convert2("mass",Ia_op,Ia)
       Ia=round(Ia/1000,6)

       Iw=round(Ia/val[name],6)

       ans=[]
       for i in val:
         j=round(val[i]*Iw,6)
         ans.append(j)  

       list=zip(names,values,ans)
       sellername=[1,2,3,4]  
       context={
         'name':name,
         'given_data':given_data,
         'Ia':Ia,
         'Ia1':Ia1,
         'Ia_op':Ia_op,
         'list':list,
         'fact':val[name],
         'Iw':Iw,
         'id':1,          
         'Ia_c':Ia_c
       }
       return render(request,'weightotherplanets.html',context)  

     else:
        id=int(given_data[4:])
        Name=names[id-1]  
        return render(request,'weightotherplanets.html',{'given_data':given_data,'Ia1':12,'name':Name})  
      
  else:
    return render(request,'weightotherplanets.html',{'name':'Earth','Ia1':12})





#FUNCTION FOR THE MOMENTUM WITH TIME CALCULATOR
def momentumwithtimecalculator(request):
  """Here Ib is for the change in time
     Here F is for the change in momentum
     Here Ia is for the Force
  """
  if request.method=='POST':
  
    given_data=request.POST.get('given_data')
   
    #Obtaining the Ia
    if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
              inp=str(request.POST.get('Ia'))
              if inp.isdigit():
                  Ia=int(request.POST.get('Ia'))
              else:
                  Ia=float(request.POST.get('Ia'))
    else:
       Ia=None
    
    #Obtaining the Ib
    if request.POST.get('Ib')!=None and request.POST.get('Ib')!='' :     
              inp=str(request.POST.get('Ib'))
              if inp.isdigit():
                  Ib=int(request.POST.get('Ib'))
              else:
                  Ib=float(request.POST.get('Ib'))
    else:
       Ib=None

   #Obtaining the F 
    if request.POST.get('F')!=None and request.POST.get('F')!='' :     
              inp=str(request.POST.get('F'))
              if inp.isdigit():
                  F=int(request.POST.get('F'))
              else:
                  F=float(request.POST.get('F'))
    else:
       F=None

    form=False
  
    if "f1" in request.POST:
      form=True

    if given_data=='form1' and form:  
      #Copying of variables
      Ia1=Ia
      Ib1=Ib
      
      #Units
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')

      #Conversion of units
      Ia,Ia_c=convert2("force",Ia_op,Ia)
      Ib,Ib_c=convert2("time",Ib_op,Ib)
      

      #Calculation
      F=Ia*Ib
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
          base1,power1=Roundoff(Ia)
          Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
      
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
        base1,power1=Roundoff(Ib)
        Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
        Ib=round(Ib,5) 
      
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
        base1,power1=Roundoff(F)
        F=f"{base1} X 10"+add_tags('sup',power1)
      else:
        F=round(F,5)  
      
      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'Ia1':Ia1,
          'Ib1':Ib1,
          'Ia_op':Ia_op,
          'Ib_op':Ib_op,
          'id':1,
          'given_data':given_data,
          'Ia_c':Ia_c,
          'Ib_c':Ib_c,  
      }
      return render(request,'momentumwithtimecalculator.html',context)

    elif given_data=='form2' and form:  
      #Copying of variables
      F1=F
      Ib1=Ib
      
      #Units
      F_op=request.POST.get('F_op')
      Ib_op=request.POST.get('Ib_op')
      
      #Conversion of units
      
      #for the momentum
      F_c=""
      if F_op[0]!='k':
        F=F/1000
        F_c="/1000"
      
      Ib,Ib_c=convert2("time",Ib_op,Ib)
  
      #Calculation
      Ia=F/Ib

      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ib<=10000)):
        base1,power1=Roundoff(Ia)
        Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
      
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
        base1,power1=Roundoff(Ib)
        Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
        Ib=round(Ib,5) 

      
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
        base1,power1=Roundoff(F)
        F=f"{base1} X 10"+add_tags('sup',power1)
      else:
        F=round(F,5)  
    
      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'F1':F1,
          'Ib1':Ib1,
          'F_op':F_op,
          'Ib_op':Ib_op,
          'id':1,
          'given_data':given_data,
          'Ib_c':Ib_c,
          'F_c':F_c
      }
      return render(request,'momentumwithtimecalculator.html',context)

    elif given_data=='form3' and form:  
      #Copying of variables
      Ia1=Ia
      F1=F
      
      #Units
      Ia_op=request.POST.get('Ia_op')
      F_op=request.POST.get('F_op')
      
      #Conversion of units
      F_c=""
      if F_op[0]!='k':
        F=F/1000
        F_c="/1000"
      Ia,Ia_c=convert2("force",Ia_op,Ia)
      
      #Calculation
      Ib=F/Ia
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
        base1,power1=Roundoff(Ia)
        Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
       Ia=round(Ia,5)
      
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
        base1,power1=Roundoff(Ib)
        Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
        Ib=round(Ib,5) 

      
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
        base1,power1=Roundoff(F)
        F=f"{base1} X 10"+add_tags('sup',power1)
      else:
        F=round(F,5)  

      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'Ia1':Ia1,
          'F1':F1,
          'Ia_op':Ia_op,
          'F_op':F_op,
          'id':1,
          'given_data':given_data,
          'Ia_c':Ia_c,
          'F_c':F_c
      }
      return render(request,'momentumwithtimecalculator.html',context)  
      
    else:
       return render(request,'momentumwithtimecalculator.html',{'given_data':given_data})

  else:
        return render(request,'momentumwithtimecalculator.html',{'given_data':'form1'})  

  




#FUNCTION FOR THE SPECIFIC HEAT CAPACITY CALCULATOR
def specificheatcalculator(request):
  """
  Here Ia is for the change in temperature
  mass is for the mass
  F is for the energy
  mat_op is for the material
  c is for the specific heat capacity
  """
  if request.method=="POST":
    given_data=request.POST.get('given_data')
    #Obtaining the Ia
    if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
              inp=str(request.POST.get('Ia'))
              if inp.isdigit():
                  Ia=int(request.POST.get('Ia'))
              else:
                  Ia=float(request.POST.get('Ia'))
    else:
       Ia=None
    
   #Obtaining the F 
    if request.POST.get('F')!=None and request.POST.get('F')!='' :     
              inp=str(request.POST.get('F'))
              if inp.isdigit():
                  F=int(request.POST.get('F'))
              else:
                  F=float(request.POST.get('F'))
    else:
       F=None

    form=False

   #Obtaining the mass 
    if request.POST.get('mass')!=None and request.POST.get('mass')!='' :     
              inp=str(request.POST.get('mass'))
              if inp.isdigit():
                  mass=int(request.POST.get('mass'))
              else:
                  mass=float(request.POST.get('mass'))
    else:
       mass=None

    #OBTAINING THE MATERIAL
    mat_op=request.POST.get("mat_op")
  
    form=False
    if "f1" in request.POST:
      form=True
    
     
     #FORM 1
    if given_data=='form1' and form:  
      #Copying of variables
      Ia1=Ia
      mass1=mass
      
      #Specific heat capacity of material
      c=specificHeat[mat_op]

      #Units
      mass_op=request.POST.get('mass_op')
      Ia_op=request.POST.get('Ia_op')

      #Conversion of units
      mass,mass_c=convert2("mass",mass_op,mass)
      Ia_c=""
      if Ia_op=="°F":
        Ia=0.55*Ia
        Ia_c="*0.55"


      mass=mass/1000
      #Calculation
      F=c*mass*Ia

      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((mass>=1 and mass<=10000) or (round(mass,3)!=0 and round(mass,3)!=0.001 and mass<=10000)):
         base1,power1=Roundoff(mass)
         mass=f"{base1} X 10"+add_tags('sup',power1)
      else:
         mass=round(mass,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)       

      context={
          'F':F,
          'Ia':Ia,
          'mass':mass,
          'Ia1':Ia1,
          'mass1':mass1,
          'Ia_op':Ia_op,
          'mass_op':mass_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          'id':1,
          'mass_c':mass_c,
          'Ia_c':Ia_c
      }
      return render(request,'specificheatcalculator.html',context)


    #FORM 2
    elif given_data=='form2' and form:  
      #Copying of variables
      F1=F
      mass1=mass

      
      #Units
      F_op=request.POST.get('F_op')
      mass_op=request.POST.get('mass_op')

      
      if mass==0:
        context={
         'F1':F1,
         'F':F,
         'mass':mass,
         'mass1':mass1,
         'F_op':F_op,
         'mass_op':mass_op,
         'given_data':given_data,
          'message':"Enter Valid data"
        }
        return render(request,'specificheatcalculator.html',context)

      #Specific heat capacity of material
      c=specificHeat[mat_op]

      #Conversion of units
      F,F_c=convert2("energy",F_op,F)
      mass,mass_c=convert2("mass",mass_op,mass)
      mass=mass/1000
      #Calculation
      Ia=F/(c*mass)
      
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((mass>=1 and mass<=10000) or (round(mass,3)!=0 and round(mass,3)!=0.001 and mass<=10000)):
         base1,power1=Roundoff(mass)
         mass=f"{base1} X 10"+add_tags('sup',power1)
      else:
         mass=round(mass,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)  
      
 
      context={
          'F':F,
          'Ia':Ia,
          'mass':mass,
          'F1':F1,
          'mass1':mass1,
          'F_op':F_op,
          'mass_op':mass_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          'F_c':F_c,
          'mass_c':mass_c
      }
      return render(request,'specificheatcalculator.html',context)


    elif given_data=='form3' and form:  
      #Copying of variables
      Ia1=Ia
      F1=F
     
      #Specific heat capacity of material
      c=specificHeat[mat_op]

      #Units
      Ia_op=request.POST.get('Ia_op')
      F_op=request.POST.get('F_op')
           

      #Conversion of units
      F,F_c=convert2("energy",F_op,F)
      Ia_c=""
      if Ia=="°F":
        Ia=0.55*Ia
        Ia_c="*0.55"

      #Calculation
      mass=F/(c*Ia)
      
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((mass>=1 and mass<=10000) or (round(mass,3)!=0 and round(mass,3)!=0.001 and mass<=10000)):
         base1,power1=Roundoff(mass)
         mass=f"{base1} X 10"+add_tags('sup',power1)
      else:
         mass=round(mass,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)  
      


      context={
          'F':F,
          'Ia':Ia,
          'mass':mass,
          'Ia1':Ia1,
          'F1':F1,
          'F_op':F_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          'F_c':F_c,
          'Ia_c':Ia_c
      }
      return render(request,'specificheatcalculator.html',context)    
    
    else:
        return render(request,'specificheatcalculator.html',{'given_data':given_data}) 
  
  else:
    return render(request,'specificheatcalculator.html',{'given_data':'form1'})
  
  



#FUNCTION FOR THE HALF LIFE CALCULATOR
def halflifecalculator(request):
 """
  Here Ia is for the remainig quantity 
  decay is for the decay constant
  F is for the initial quantity
  mat is for the total time
  
  """
 if request.method=="POST":
    given_data=request.POST.get('given_data')
    #Obtaining the Ia
    if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
              inp=str(request.POST.get('Ia'))
              if inp.isdigit():
                  Ia=int(request.POST.get('Ia'))
              else:
                  Ia=float(request.POST.get('Ia'))
    else:
       Ia=None
    
   #Obtaining the F 
    if request.POST.get('F')!=None and request.POST.get('F')!='' :     
              inp=str(request.POST.get('F'))
              if inp.isdigit():
                  F=int(request.POST.get('F'))
              else:
                  F=float(request.POST.get('F'))
    else:
       F=None

    form=False

   #Obtaining the decay 
    if request.POST.get('decay')!=None and request.POST.get('decay')!='' :     
              inp=str(request.POST.get('decay'))
              if inp.isdigit():
                  decay=int(request.POST.get('decay'))
              else:
                  decay=float(request.POST.get('decay'))
    else:
       decay=None

    #OBTAINING THE MATERIAL
    if request.POST.get('mat')!=None and request.POST.get('mat')!='' :     
              inp=str(request.POST.get('mat'))
              if inp.isdigit():
                  mat=int(request.POST.get('mat'))
              else:
                  mat=float(request.POST.get('mat'))
    else:
       mat=None


  
    form=False
    if "f1" in request.POST:
      form=True
    
     
     #FORM 1
    if given_data=='form1' and form:  
      #Copying of variables
      Ia1=Ia
      decay1=decay
      mat1=mat

      
      if decay==0:
          message="Decay Consant cannot be 0"
          context={
           'Ia':Ia, 
           'mat':mat,
           'Ia1':Ia1,
           'mat1':mat1,
           'decay':decay,
           'decay1':decay1,
           'decay_op':request.POST.get('decay_op'),
           'given_data':given_data,
           'message':message
          }
          return render(request,'halflifecalculator.html',context)
      

      
      #Units
      decay_op=request.POST.get('decay_op')
      mat_op=request.POST.get('mat_op')

      #Conversion of units
      decay,decay_c=convert2("frequency",decay_op,decay)
      mat,mat_c=convert2("time",mat_op,mat)
      
      
      half=0.693/decay
      
      #Calculation
      #N(t) = N(0) * 0.5(t/T)
      if 0.5**(mat/half)!=0:
        F=Ia/(0.5**(mat/half))
      else:
        F= float('inf')  

     #CALCULATING THE HALF LIFE
      half=0.693/decay
      
      if not((half>=1 and half<=10000) or (round(half,3)!=0 and round(half,3)!=0.001 and half<=10000)):
              base1,power1=Roundoff(half)
              half=f"{base1} X 10 "+add_tags('sup',power1)
            
      else:
              half=round(half,4)
         
  
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
            if Ia!=0:
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10 "+add_tags('sup',power1)
            else:
              Ia='0'  
      else:
              Ia=round(Ia,4)
         
      if not((decay>=1 and decay<=10000) or (round(decay,3)!=0 and round(decay,3)!=0.001 and decay<=10000)):
              base1,power1=Roundoff(decay)
              decay=f"{base1} X 10 "+add_tags('sup',power1)
            
      else:
              decay=round(decay,4)
         
  
      if not((mat>=1 and mat<=10000) or (round(mat,3)!=0 and round(mat,3)!=0.001 and mat<=10000)):
              base1,power1=Roundoff(mat)
              mat=f"{base1} X 10 "+add_tags('sup',power1)
           
      else:
              mat=round(mat,4)
         
     
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
             if F!= float('inf'): 
              base1,power1=Roundoff(F)
              F=f"{base1} X 10 "+add_tags('sup',power1)

      else:
              F=round(F,4)
         
          
              
      
      context={
          'F':F,
          'Ia':Ia,
          'decay':decay,
          'Ia1':Ia1,
          'mat':mat,
          'mat1':mat1,
          'decay1':decay1,
          'half':half,
          'decay_op':decay_op,
          'mat_op':mat_op,
          'id':1,
          'given_data':given_data,
          'id':1,
          'decay_c':decay_c,
          'mat_c':mat_c
      }
      return render(request,'halflifecalculator.html',context)


    #FORM 2
    elif given_data=='form2' and form:  
      #Copying of variables
      F1=F
      decay1=decay
      mat1=mat
      
      if decay==0:
          message="Decay Consant cannot be 0"
          context={
           'F':F, 
           'mat':mat,
           'F1':F1,
           'mat1':mat1,
           'decay':decay,
           'decay1':decay1,
           'decay_op':request.POST.get('decay_op'),
           'given_data':given_data,
           'message':message
          }
          return render(request,'halflifecalculator.html',context)
      
      
      #Units
      mat_op=request.POST.get('mat_op')
      decay_op=request.POST.get('decay_op')

      #Conversion of units
      decay,decay_c=convert2("frequency",decay_op,decay)
      mat,mat_c=convert2("time",mat_op,mat)
      
      #CALCULATING THE HALF LIFE
      half=0.693/decay

      #Calculation
      #N(t) = N(0) * 0.5(t/T)
      Ia=F*0.5**(mat/half)

      if not((half>=1 and half<=10000) or (round(half,3)!=0 and round(half,3)!=0.001 and half<=10000)):
              base1,power1=Roundoff(half)
              half=f"{base1} X 10 "+add_tags('sup',power1) 
      else:
              half=round(half,4)
         
  
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
            if Ia!=0:
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10 "+add_tags('sup',power1)
            else:
              Ia='0'  
      else:
              Ia=round(Ia,4)
         
      if not((decay>=1 and decay<=10000) or (round(decay,3)!=0 and round(decay,3)!=0.001 and decay<=10000)):
              base1,power1=Roundoff(decay)
              decay=f"{base1} X 10 "+add_tags('sup',power1)
            
      else:
              decay=round(decay,4)
         
  
      if not((mat>=1 and mat<=10000) or (round(mat,3)!=0 and round(mat,3)!=0.001 and mat<=10000)):
              base1,power1=Roundoff(mat)
              mat=f"{base1} X 10 "+add_tags('sup',power1)
           
      else:
              mat=round(mat,4)
         
     
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10 "+add_tags('sup',power1)
            
      else:
              F=round(F,4)
         
          
      
 
      context={
          'F':F,
          'Ia':Ia,
          'decay':decay,
          'F1':F1,
          'mat1':mat1,
          'mat':mat,
          'decay1':decay1,
          'decay_op':decay_op,
          'mat_op':mat_op,
          'half':half,
          'id':1,
          'given_data':given_data,
          'decay_c':decay_c,
          'mat_c':mat_c
      }
      return render(request,'halflifecalculator.html',context)


    elif given_data=='form3' and form:  
      #Copying of variables
      Ia1=Ia
      F1=F
      decay1=decay
      
      if Ia>F or decay==0 :
          message="Remaining Quantity cannot be greater than Initial Quantity and decay constant cannot be zero"
          context={
           'F':F, 
           'Ia':Ia,
           'F1':F1,
           'Ia1':Ia1,
           'decay':decay,
           'decay1':decay1,
           'decay_op':request.POST.get('decay_op'),
           'given_data':given_data,
           'message':message
          }
          return render(request,'halflifecalculator.html',context)
      
      #Units
      decay_op=request.POST.get('decay_op')
     
      #Conversion of units
      decay,decay_c=convert2("frequency",decay_op,decay)
     
      half=0.693/decay  
      #Calculation
      #N(t) = N(0) * 0.5(t/T)
      k=math.log(Ia/F,0.5)
      mat=k*half

      if not((half>=1 and half<=10000) or (round(half,3)!=0 and round(half,3)!=0.001 and half<=10000)):
              base1,power1=Roundoff(half)
              half=f"{base1} X 10 "+add_tags('sup',power1)
             
      else:
              half=round(half,4)
         
  
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
            if Ia!=0:
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10 "+add_tags('sup',power1)
            else:
              Ia='0'  
      else:
              Ia=round(Ia,4)
         
      if not((decay>=1 and decay<=10000) or (round(decay,3)!=0 and round(decay,3)!=0.001 and decay<=10000)):
              base1,power1=Roundoff(decay)
              decay=f"{base1} X 10 "+add_tags('sup',power1)
             
      else:
              decay=round(decay,4)
         
  
      if not((mat>=1 and mat<=10000) or (round(mat,3)!=0 and round(mat,3)!=0.001 and mat<=10000)):
              base1,power1=Roundoff(mat)
              mat=f"{base1} X 10 "+add_tags('sup',power1)
             
      else:
              mat=round(mat,4)
         
     
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10 "+add_tags('sup',power1)
             
      else:
              F=round(F,4)
                       
    
      context={
          'F':F,
          'Ia':Ia,
          'decay':decay,
          'decay1':decay1,
          'decay_op':decay_op,
          'Ia1':Ia1,
          'F1':F1,
          'mat':mat,
          'half':half,
          'id':1,
          'given_data':given_data,
          'decay_c':decay_c
      }
      return render(request,'halflifecalculator.html',context)    
    
    else:
        return render(request,'halflifecalculator.html',{'given_data':given_data}) 
  
 else:
    return render(request,'halflifecalculator.html',{'given_data':'form1'})
  
  


#FUNCTION FOR THE WET BULB CALCULATOR
def wetbulbcalculator(request):
    if request.method=='POST':
      
      """Here rh is for the relative humidity
         Here Tw is for the temperature
      """
      #FETCHING THE VARIABLE rh     
      if request.POST.get('rh')!=None and request.POST.get('rh')!='' :     
              inp=str(request.POST.get('rh'))
              if inp.isdigit():
                  rh=int(request.POST.get('rh'))
              else:
                  rh=float(request.POST.get('rh'))
      else:
        rh=None

      #FETCHING THE VARIABLE T
      if request.POST.get('T')!=None and request.POST.get('T')!='' :     
              inp=str(request.POST.get('T'))
              if inp.isdigit():
                  T=int(request.POST.get('T'))
              else:
                  T=float(request.POST.get('T'))
      else:
        T=None
      
      #UNITS 
      T_op=request.POST.get('T_op')
      rh_op=request.POST.get('rh_op')

      #COPYING OF VARIABLES 
      T1=T
      rh1=rh

      #CONVERSION OF UNITS
      T,T_c=convert2("temp",T_op,T)
      
      ans1=False
      ans2=False

      if T_op=="°C" and not (T>=-20 and T<=50):
        ans1=True 
      # elif T_op=="°F" and not (T>=-4 and T<=122):
      #   ans1=True   
      # elif T_op=="K" and not (T>=-253.15 and T<=323.15):
      #   ans1=True   

      rh_c=""
      if rh_op =='‰':
        rh=rh*0.1  
        rh_c="*0.1"
       
      elif rh_op=='‱':
         rh=rh*0.01
         rh_c="*0.01"

      if not (rh>=5 and rh<=99):   
        ans2=True

      message1="This calculator is only accurate for temperatures between -20 °C to 50 °C, 253.15 k to 323.15 k , -4 °F to 122 °F"

      message2="This calculator is only accurate for relative humidities between 5% to 99%, 50‰ to 990‰,,500‱ to 9900‱"     

      if ans1 or ans2:
        context={
          'given_data':'form1',
          'rh':rh,
          'T':T,
          'rh1':rh1,
          'T1':T1,
          'T_op':T_op,
          'rh_op':rh_op,
           'message1':message1,
           'message2':message2,
        } 
        return render(request,'wetbulbcalculator.html',context)


      #CALCULATION
      Tw = T * math.atan(0.151977 * ((rh + 8.313659)**(1/2))) + math.atan(T + rh) - math.atan(rh - 1.676331) + 0.00391838 *((rh)**(3/2)) * math.atan(0.023101*rh) - 4.686035    
      
      if not  ((Tw>=1 and Tw<=10000) or (round(Tw,3)!=0 and round(Tw,3)!=0.001)):
         base1,power1=Roundoff(Tw)
         Tw=f"{base1} X 10"+add_tags('sup',power1)
      else:
         Tw=round(Tw,5) 
  
      
      context={
        'given_data':'form1',
        'T':T,
        'rh':rh,
        'T1':T1,
        'rh1':rh1,
        'T_op':T_op,
        'rh_op':rh_op,
        'Tw':Tw,
        'id':1,
        'rh_c':rh_c,
        'T_c':T_c
      }
      return render(request,'wetbulbcalculator.html',context)          

    else:  
      return render(request,'wetbulbcalculator.html',{'given_data':'form1','T1':6,'rh1':5})







def arrowspeedcalculator(request):
  if request.method=='POST':
    given_data=request.POST.get('given_data')
    
    """ Here Ib for the arrow speed(ft/s)
        Here Ia for the IBO rating(ft/s)
        Here F for the draw length(inches)
        Here p for the draw weight(pounds lb)
        Here q for the arrow weight(grains gr)
        Here r for the additional weight (grains gr)
    """
    #Obtaining the Ia
    if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
              inp=str(request.POST.get('Ia'))
              if inp.isdigit():
                  Ia=int(request.POST.get('Ia'))
              else:
                  Ia=float(request.POST.get('Ia'))
    else:
       Ia=None
    
    #Obtaining the Ib
    if request.POST.get('Ib')!=None and request.POST.get('Ib')!='' :     
              inp=str(request.POST.get('Ib'))
              if inp.isdigit():
                  Ib=int(request.POST.get('Ib'))
              else:
                  Ib=float(request.POST.get('Ib'))
    else:
       Ib=None

   #Obtaining the F 
    if request.POST.get('F')!=None and request.POST.get('F')!='' :     
              inp=str(request.POST.get('F'))
              if inp.isdigit():
                  F=int(request.POST.get('F'))
              else:
                  F=float(request.POST.get('F'))
    else:
       F=None

    #Obtaining the p
    if request.POST.get('p')!=None and request.POST.get('p')!='' :     
              inp=str(request.POST.get('p'))
              if inp.isdigit():
                  p=int(request.POST.get('p'))
              else:
                  p=float(request.POST.get('p'))
    else:
       p=None

    #Obtaining the q
    if request.POST.get('q')!=None and request.POST.get('q')!='' :     
              inp=str(request.POST.get('q'))
              if inp.isdigit():
                  q=int(request.POST.get('q'))
              else:
                  q=float(request.POST.get('q'))
    else:
       q=None

    #Obtaining the r
    if request.POST.get('r')!=None and request.POST.get('r')!='' :     
              inp=str(request.POST.get('r'))
              if inp.isdigit():
                  r=int(request.POST.get('r'))
              else:
                  r=float(request.POST.get('r'))
    else:
       r=None
       
    #FOR CHECKING THE FORM
    form=False
    if "f1" in request.POST:
      form=True   
  
    if given_data == 'form1' and form:
      
      #FETCHING THE UNITS
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')
      F_op=request.POST.get('F_op')
      p_op=request.POST.get('p_op')
      q_op=request.POST.get('q_op')
      r_op=request.POST.get('r_op')

      #COPYING OF THE VARIABLES
      Ia1=Ia
      p1=p
      F1=F
      q1=q
      r1=r

      #Conversion of units here
      Ia_c=""
      if Ia_op != 'ft/s':
        Ia,Ia_c=convert2("vel",Ia_op,Ia)
        Ia=round(Ia*3.28,2)#CONVERTING INTO ft/s
        Ia_c+=" *3.28"
      
      p_c=""
      if p_op != 'lb':
        p,p_c=convert2("mass",p_op,p)
        p=p*0.453#convert into pounds
        p=p/1000
        p_c+=" *0.453"
      
      F_c=""
      if F_op != 'in':
        F,F_c=convert2("len",F_op,F)
        F=F*39.37
        F_c+="*39.37"
      
      q_c=""
      if q_op != 'gr' :
        q,q_c=convert2("mass",q_op,q)
        q=q*15432
        q=q/1000
        q_c+=" *15432"
      
      r_c=""
      if r_op != 'gr' :
        r,r_c=convert2("mass",r_op,r)
        r=r*15432  
        r=r/1000     
        r_c+=" *15432"

      #Calculation
      Ib=Ia+(F-30)*10-r/3+min(0,-(q-5*p/3))
     
      if not((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000) or (Ib<=-1 and Ib>=-10000)):
             if Ib!=0: 
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        Ib=round(Ib,3)    

     
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000) or (Ia<=-1 and Ia>=-10000)):
             if Ia!=0: 
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        Ia=round(Ia,3)    
 

     
      if not((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000) or (p<=-1 and p>=-10000)):
             if p!=0: 
              base1,power1=Roundoff(p)
              p=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        p=round(p,3)    

             
      
      
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000) or (F<=-1 and F>=-10000)):
             if F!=0: 
              base1,power1=Roundoff(F)
              F=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        F=round(F,3)    
   


      if not((q>=1 and q<=10000) or (round(q,3)!=0 and round(q,3)!=0.001 and q<=10000) or (q<=-1 and q>=-10000)):
             if q!=0: 
              base1,power1=Roundoff(q)
              q=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        q=round(q,3)    
    
      

      if not((r>=1 and r<=10000) or (round(r,3)!=0 and round(r,3)!=0.001 and r<=10000) or (r<=-1 and r>=-10000)):
             if r!=0: 
              base1,power1=Roundoff(r)
              r=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        r=round(r,3)    
            
         

      context={
         'given_data':given_data,
         'id':1,
         'Ia':Ia,
         'Ib':Ib,
         'F':F,
         'r':r,
         'p':p,
         'q':q,
         'Ia1':Ia1,
         'F1':F1,
         'r1':r1,
         'p1':p1,
         'q1':q1,
         'Ia_op':Ia_op,
         'F_op':F_op,
         'p_op':p_op,
         'r_op':r_op,
         'q_op':q_op,
         'Ia_c':Ia_c,
         #'Ib_c':Ib_c,
         'F_c':F_c,
         'p_c':p_c,
         'r_c':r_c,
         'q_c':q_c,

      }
      return render(request,'arrowspeedcalculator.html',context)

    if given_data == 'form2' and form:
      
      #FETCHING THE UNITS
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')
      F_op=request.POST.get('F_op')
      p_op=request.POST.get('p_op')
      q_op=request.POST.get('q_op')
      r_op=request.POST.get('r_op')

      #COPYING OF THE VARIABLES
      Ib1=Ib
      p1=p
      F1=F
      q1=q
      r1=r

      #Conversion of units here
      Ib_c=""
      if Ib_op != 'ft/s':
        Ib,Ib_c=convert2("vel",Ib_op,Ib)
        Ib=round(Ib*3.28,2)#CONVERTING INTO ft/s
        Ib_c+=" *3.28"
       
      p_c=""
      if p_op != 'lb':
        p,p_c=convert2("mass",p_op,p)
        p=p*0.453#convert into pounds
        p=p/1000
        p_c+=" *0.453"
      
      F_c=""
      if F_op != 'in':
        F,F_c=convert2("len",F_op,F)
        F=F*39.37
        F_c+="*39.37"
      
      q_c=""
      if q_op != 'gr' :
        q,q_c=convert2("mass",q_op,q)
        q=q*15432
        q=q/1000
        q_c+=" *15432"
      
      r_c=""
      if r_op != 'gr' :
        r,r_c=convert2("mass",r_op,r)
        r=r*15432 
        r=r/1000     
        r_c+=" *15432"
      #Calculation
      Ia=Ib-(F-30)*10-r/3+min(0,-(q-5*p/3))
        
      if not((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000) or (Ib<=-1 and Ib>=-10000)):
             if Ib!=0: 
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        Ib=round(Ib,3)    

     
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000) or (Ia<=-1 and Ia>=-10000)):
             if Ia!=0: 
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
         Ia=round(Ia,3)    
 

     
      if not((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000) or (p<=-1 and p>=-10000)):
             if p!=0: 
              base1,power1=Roundoff(p)
              p=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        p=round(p,3)    

             
      
      
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000) or (F<=-1 and F>=-10000)):
             if F!=0: 
              base1,power1=Roundoff(F)
              F=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        F=round(F,3)    
   


      if not((q>=1 and q<=10000) or (round(q,3)!=0 and round(q,3)!=0.001 and q<=10000) or (q<=-1 and q>=-10000)):
             if q!=0: 
              base1,power1=Roundoff(q)
              q=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        q=round(q,3)    
    
      

      if not((r>=1 and r<=10000) or (round(r,3)!=0 and round(r,3)!=0.001 and r<=10000) or (r<=-1 and r>=-10000)):
             if r!=0: 
              base1,power1=Roundoff(r)
              r=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        r=round(r,3)    
            
         
     

      context={
         'given_data':given_data,
         'id':1,
         'Ia':Ia,
         'Ib':Ib,
         'F':F,
         'r':r,
         'p':p,
         'q':q,
         'Ib1':Ib1,
         'F1':F1,
         'r1':r1,
         'p1':p1,
         'q1':q1,
         'Ia_op':Ia_op,
         'F_op':F_op,
         'p_op':p_op,
         'r_op':r_op,
         'q_op':q_op,
         'Ib_op':Ib_op,
         'Ib_c':Ib_c,
         'F_c':F_c,
         'p_c':p_c,
         'r_c':r_c,
         'q_c':q_c,

      }
      return render(request,'arrowspeedcalculator.html',context)

    if given_data == 'form3' and form:
      
      #FETCHING THE UNITS
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')
      F_op=request.POST.get('F_op')
      p_op=request.POST.get('p_op')
      q_op=request.POST.get('q_op')
      r_op=request.POST.get('r_op')

      #COPYING OF THE VARIABLES
      Ib1=Ib
      p1=p
      Ia1=Ia
      q1=q
      r1=r

      #Conversion of units here
      Ib_c=""
      if Ib_op != 'ft/s':
        Ib,Ib_c=convert2("vel",Ib_op,Ib)
        Ib=round(Ib*3.28,2)#CONVERTING INTO ft/s
        Ib_c+=" *3.28"
        
      Ia_c=""
      if Ia_op != 'ft/s':
        Ia,Ia_c=convert2("vel",Ia_op,Ia)
        Ia=round(Ia*3.28,2)#CONVERTING INTO ft/s
        Ia_c+=" *3.28"
      
      p_c=""
      if p_op != 'lb':
        p,p_c=convert2("mass",p_op,p)
        p=p*0.453#convert into pounds
        p=p/1000
        p_c+=" *0.453"
      
      
      q_c=""
      if q_op != 'gr' :
        q,q_c=convert2("mass",q_op,q)
        q=q*15432
        q=q/1000
        q_c+=" *15432"
      
      r_c=""
      if r_op != 'gr' :
        r,r_c=convert2("mass",r_op,r)
        r=r*15432  
        r=r/1000     
        r_c+="*15432"
      #Calculation
      F=(Ib-Ia+r/3-min(0,- (q-5*p)/3 ) )/10+30

      if not((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000) or (Ib<=-1 and Ib>=-10000)):
              if Ib!=0: 
                base1,power1=Roundoff(Ib)
                Ib=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
          Ib=round(Ib,3)    

      
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000) or (Ia<=-1 and Ia>=-10000)):
              if Ia!=0: 
                base1,power1=Roundoff(Ia)
                Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
          Ia=round(Ia,3)    
  

      
      if not((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000) or (p<=-1 and p>=-10000)):
              if p!=0: 
                base1,power1=Roundoff(p)
                p=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
          p=round(p,3)    

              
        
        
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000) or (F<=-1 and F>=-10000)):
              if F!=0: 
                base1,power1=Roundoff(F)
                F=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
          F=round(F,3)    
    


      if not((q>=1 and q<=10000) or (round(q,3)!=0 and round(q,3)!=0.001 and q<=10000) or (q<=-1 and q>=-10000)):
             if q!=0: 
              base1,power1=Roundoff(q)
              q=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        q=round(q,3)    
    
      

      if not((r>=1 and r<=10000) or (round(r,3)!=0 and round(r,3)!=0.001 and r<=10000) or (r<=-1 and r>=-10000)):
             if r!=0: 
              base1,power1=Roundoff(r)
              r=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        r=round(r,3)    
            
      
      context={
         'given_data':given_data,
         'id':1,
         'Ia':Ia,
         'Ib':Ib,
         'F':F,
         'r':r,
         'p':p,
         'q':q,
         'Ib1':Ib1,
         'Ia1':Ia1,
         'r1':r1,
         'p1':p1,
         'q1':q1,
         'Ia_op':Ia_op,
         'F_op':F_op,
         'p_op':p_op,
         'r_op':r_op,
         'q_op':q_op,
         'Ib_op':Ib_op, 
         'Ia_c':Ia_c,
         'Ib_c':Ib_c,
         'p_c':p_c,
         'r_c':r_c,
         'q_c':q_c,

      }
      return render(request,'arrowspeedcalculator.html',context)
    
    
    if given_data == 'form6' and form:
      
      #FETCHING THE UNITS
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')
      F_op=request.POST.get('F_op')
      p_op=request.POST.get('p_op')
      q_op=request.POST.get('q_op')
      r_op=request.POST.get('r_op')

      #COPYING OF THE VARIABLES
      Ib1=Ib
      F1=F
      Ia1=Ia
      p1=p
      q1=q

      #Conversion of units here
      Ib_c=""
      if Ib_op != 'ft/s':
        Ib,Ib_c=convert2("vel",Ib_op,Ib)
        Ib=round(Ib*3.28,2)#CONVERTING INTO ft/s
        Ib_c+=" *3.28"
        
      Ia_c=""
      if Ia_op != 'ft/s':
        Ia,Ia_c=convert2("vel",Ia_op,Ia)
        Ia=round(Ia*3.28,2)#CONVERTING INTO ft/s
        Ia_c+=" *3.28"
      
      p_c=""
      if p_op != 'lb':
        p,p_c=convert2("mass",p_op,p)
        p=p*0.453#convert into pounds
        p=p/1000
        p_c+=" *0.453"
      
      F_c=""
      if F_op != 'in':
        F,F_c=convert2("len",F_op,F)
        F=F*39.37
        F_c+="*39.37"
      
      q_c=""
      if q_op != 'gr' :
        q,q_c=convert2("mass",q_op,q)
        q=q*15432
        q=q/1000
        q_c+=" *15432"
      
      
      #Ia=Ib-(F-30)*10-r/3+min(0,-(q-5*p/3))
      r=(Ib+(F-30)*10-Ia+min(0,-(q-5*p)/3))*3
      
      
      
      if not((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000) or (Ib<=-1 and Ib>=-10000)):
             if Ib!=0: 
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        Ib=round(Ib,3)    

     
      if not((Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000) or (Ia<=-1 and Ia>=-10000)):
             if Ia!=0: 
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        Ia=round(Ia,3)    
 

     
      if not((p>=1 and p<=10000) or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000) or (p<=-1 and p>=-10000)):
             if p!=0: 
              base1,power1=Roundoff(p)
              p=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        p=round(p,3)    

             
      
      
      if not((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000) or (F<=-1 and F>=-10000)):
             if F!=0: 
              base1,power1=Roundoff(F)
              F=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        F=round(F,3)    
   


      if not((q>=1 and q<=10000) or (round(q,3)!=0 and round(q,3)!=0.001 and q<=10000) or (q<=-1 and q>=-10000)):
             if q!=0: 
              base1,power1=Roundoff(q)
              q=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        q=round(q,3)    
    
      

      if not((r>=1 and r<=10000) or (round(r,3)!=0 and round(r,3)!=0.001 and r<=10000) or (r<=-1 and r>=-10000)):
             if r!=0: 
              base1,power1=Roundoff(r)
              r=f"{base1} X 10 "+add_tags('sup',power1)
      else:  
        r=round(r,3)    
            


      context={
         'given_data':given_data,
         'id':1,
         'Ia':Ia,
         'Ib':Ib,
         'F':F,
         'r':r,
         'p':p,
         'q':q,
         'Ib1':Ib1,
         'Ia1':Ia1,
         'q1':q1,
         'F1':F1,
         'p1':p1,
         'Ia_op':Ia_op,
         'F_op':F_op,
         'p_op':p_op,
         'r_op':r_op,
         'q_op':q_op,
         'Ib_op':Ib_op,
        'Ia_c':Ia_c,
         'Ib_c':Ib_c,
         'F_c':F_c,
         'p_c':p_c,
         'q_c':q_c,


      }
      return render(request,'arrowspeedcalculator.html',context)
      

    else:
     return render(request,'arrowspeedcalculator.html',{'given_data':given_data,'F1':12,'Ia1':9,'Ib1':9,'p1':6,'q1':5,'r1':11,'id1':2})
    
  else:
    return render(request,'arrowspeedcalculator.html',{'given_data':'form1','F1':12,'Ia1':9,'Ib1':9,'p1':6,'q1':5,'r1':11,'id1':2})




def frictionlosscalculator(request):
  """Here Ib is for the pipe length
     Here Ia is for the pipe inside diameter
     Here F is for the friction head loss
     Here mat_op is for the pipe material
     Here flow is for the flow rate of fluid
     Here c is for the Specific heat capacity of material
  """
  if request.method=="POST":
    given_data=request.POST.get('given_data')
    #Obtaining the Ia
    if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
              inp=str(request.POST.get('Ia'))
              if inp.isdigit():
                  Ia=int(request.POST.get('Ia'))
              else:
                  Ia=float(request.POST.get('Ia'))
    else:
       Ia=None
    
    #Obtaining the Ib
    if request.POST.get('Ib')!=None and request.POST.get('Ib')!='' :     
              inp=str(request.POST.get('Ib'))
              if inp.isdigit():
                  Ib=int(request.POST.get('Ib'))
              else:
                  Ib=float(request.POST.get('Ib'))
    else:
       Ib=None

   #Obtaining the F 
    if request.POST.get('F')!=None and request.POST.get('F')!='' :     
              inp=str(request.POST.get('F'))
              if inp.isdigit():
                  F=int(request.POST.get('F'))
              else:
                  F=float(request.POST.get('F'))
    else:
       F=None

    form=False

   #Obtaining the flow 
    if request.POST.get('flow')!=None and request.POST.get('flow')!='' :     
              inp=str(request.POST.get('flow'))
              if inp.isdigit():
                  flow=int(request.POST.get('flow'))
              else:
                  flow=float(request.POST.get('flow'))
    else:
       flow=None

    #OBTAINING THE MATERIAL
    mat_op=request.POST.get("mat_op")
  
    form=False
    if "f1" in request.POST:
      form=True
    
     
     #FORM 1
    if given_data=='form1' and form:  
      #Copying of variables
      Ia1=Ia
      Ib1=Ib
      flow1=flow
      
      #Specific heat capacity of material
      c=materialValueCalculator(mat_op)

      #Units
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')
      flow_op=request.POST.get('flow_op')

      #Conversion of units
      #F,F_c=convert2("len",F_op,F)
      Ia,Ia_c=convert2("len",Ia_op,Ia)
      Ib,Ib_c=convert2("len",Ib_op,Ib)
      flow,flow_c=convert2("flow",flow_op,flow)
      
      #Calculation
      v1=flow**1.852
      v2=int(c)**1.852
      v3=Ia**4.87

      
      F=10.67*Ib*v1/(v2*v3)

      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
         Ib=round(Ib,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)  
      
      if not  ((flow>=1 and flow<=10000) or (round(flow,3)!=0 and round(flow,3)!=0.001 and flow<=10000)):
         base1,power1=Roundoff(flow)
         flow=f"{base1} X 10"+add_tags('sup',power1)
      else:
         flow=round(flow,5)

      A=""
      B=""
      for i in range(0,len(flow_op)):
        if flow_op[i]=="/":      
           break
        A+= flow_op[i]
      
      for j in range(i,len(flow_op)):
        B+= flow_op[j]
      

      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'flow':flow,
          'Ia1':Ia1,
          'Ib1':Ib1,
          'flow1':flow1,
          'Ia_op':Ia_op,
          'Ib_op':Ib_op,
          'flow_op':flow_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          #'F_c':F_c,
          'Ia_c':Ia_c,
          'Ib_c':Ib_c,
          'flow_c':flow_c,
          'A':A,
          'B':B
      }
      return render(request,'frictionlosscalculator.html',context)


    #FORM 2
    elif given_data=='form2' and form:  
      #Copying of variables
      F1=F
      Ib1=Ib
      flow1=flow
      
      #Specific heat capacity of material
      c=materialValueCalculator(mat_op)

      #Units
      F_op=request.POST.get('F_op')
      Ib_op=request.POST.get('Ib_op')
      flow_op=request.POST.get('flow_op')

      #Conversion of units
      F,F_c=convert2("len",F_op,F)
      Ib,Ib_c=convert2("len",Ib_op,Ib)
      flow,flow_c=convert2("flow",flow_op,flow)
     
      #Calculation
      v1=flow**1.857
      v2=int(c)**1.857
      v3=10.67*Ib*v1/(v2*F)
      Ia=v3**(1/4.87)
      
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
         Ib=round(Ib,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)  
      
      if not  ((flow>=1 and flow<=10000) or (round(flow,3)!=0 and round(flow,3)!=0.001 and flow<=10000)):
         base1,power1=Roundoff(flow)
         flow=f"{base1} X 10"+add_tags('sup',power1)
      else:
         flow=round(flow,5)
      
      A=""
      B=""
      for i in range(0,len(flow_op)):
        if flow_op[i]=="/":      
           break
        A+= flow_op[i]
      
      for j in range(i,len(flow_op)):
        B+= flow_op[j]
                     

      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'flow':flow,
          'F1':F1,
          'Ib1':Ib1,
          'flow1':flow1,
          'F_op':F_op,
          'Ib_op':Ib_op,
          'flow_op':flow_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          'F_c':F_c,
          'Ib_c':Ib_c,
          'flow_c':flow_c,
          'A':A,
          'B':B
      }
      return render(request,'frictionlosscalculator.html',context)


    elif given_data=='form3' and form:  
      #Copying of variables
      Ia1=Ia
      F1=F
      flow1=flow
      
      #Specific heat capacity of material
      c=materialValueCalculator(mat_op)

      #Units
      Ia_op=request.POST.get('Ia_op')
      F_op=request.POST.get('F_op')
      flow_op=request.POST.get('flow_op')


      #Conversion of units
      F,F_c=convert2("len",F_op,F)
      Ia,Ia_c=convert2("len",Ia_op,Ia)
      flow,flow_c=convert2("flow",flow_op,flow)
     
      #Calculation
      v1=flow**1.857
      v2=int(c)**1.857
      v3=Ia**4.87
      
      #F=10.67*Ib*v1/(v2*v3)
      Ib=F*v2*v3/(10.67*v1)

      
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
         Ib=round(Ib,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)  
      
      if not  ((flow>=1 and flow<=10000) or (round(flow,3)!=0 and round(flow,3)!=0.001 and flow<=10000)):
         base1,power1=Roundoff(flow)
         flow=f"{base1} X 10"+add_tags('sup',power1)
      else:
         flow=round(flow,5)   

      A=""
      B=""
      for i in range(0,len(flow_op)):
        if flow_op[i]=="/":      
           break
        A+= flow_op[i]
      
      for j in range(i,len(flow_op)):
        B+= flow_op[j]
       


      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'flow':flow,
          'Ia1':Ia1,
          'F1':F1,
          'flow1':flow1,
          'Ia_op':Ia_op,
          'F_op':F_op,
          'flow_op':flow_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          'F_c':F_c,
          'Ia_c':Ia_c,
          'flow_c':flow_c,
          'A':A,
          'B':B
      }
      return render(request,'frictionlosscalculator.html',context)

    elif given_data=='form4' and form:  
      #Copying of variables
      Ia1=Ia
      Ib1=Ib
      F1=F
      
      #Specific heat capacity of material
      c=materialValueCalculator(mat_op)

      #Units
      Ia_op=request.POST.get('Ia_op')
      Ib_op=request.POST.get('Ib_op')
      F_op=request.POST.get('F_op')

      #Conversion of units
      F,F_c=convert2("len",F_op,F)
      Ia,Ia_c=convert2("len",Ia_op,Ia)
      Ib,Ib_c=convert2("len",Ib_op,Ib)
      
      #Calculation
      
      #v1=flow**1.8
      v2=int(c)**1.852
      v3=Ia**4.87
      #F=10.67*Ib*v1/(v2*v3)
      v1=F*v2*v3/(10.67*Ib)
      flow=v1**(1/1.852)
      
      
      if not ( (Ia>=1 and Ia<=10000) or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
         base1,power1=Roundoff(Ia)
         Ia=f"{base1} X 10 "+add_tags('sup',power1)
      else:
        Ia=round(Ia,5)
       
      if not  ((Ib>=1 and Ib<=10000) or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
         base1,power1=Roundoff(Ib)
         Ib=f"{base1} X 10"+add_tags('sup',power1)
      else:
         Ib=round(Ib,5) 
       
      if not  ((F>=1 and F<=10000) or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
         base1,power1=Roundoff(F)
         F=f"{base1} X 10"+add_tags('sup',power1)
      else:
         F=round(F,5)  
      
      if not  ((flow>=1 and flow<=10000) or (round(flow,3)!=0 and round(flow,3)!=0.001 and flow<=10000)):
         base1,power1=Roundoff(flow)
         flow=f"{base1} X 10"+add_tags('sup',power1)
      else:
         flow=round(flow,5)   


      
      context={
          'F':F,
          'Ia':Ia,
          'Ib':Ib,
          'flow':flow,
          'Ia1':Ia1,
          'Ib1':Ib1,
          'F1':F1,
          'Ia_op':Ia_op,
          'Ib_op':Ib_op,
          'F_op':F_op,
          'mat_op':mat_op,
          'c':c,
          'id':1,
          'given_data':given_data,
          'F_c':F_c,
          'Ia_c':Ia_c,
          'Ib_c':Ib_c,
          
      }
      return render(request,'frictionlosscalculator.html',context)
        
    
    
    else:
        return render(request,'frictionlosscalculator.html',{'given_data':given_data}) 
  
  else:
    return render(request,'frictionlosscalculator.html',{'given_data':'form1'})
  





#CODE FOR THE VOLATGE DIVIDER CALCULATOR

def voltagedividercalculator(request):
  if request.method=='POST':
      given_data=request.POST.get('given_data')
      given_option=request.POST.get('given_option')
      
      #VALUE FOR THE RESISTANCE 1
      if request.POST.get('Ia')!=None and request.POST.get('Ia')!='' :     
        inp=str(request.POST.get('Ia'))
        if inp.isdigit():
           Ia=int(request.POST.get('Ia'))
        else:
           Ia=float(request.POST.get('Ia'))
      else:
         Ia=None

      #VALUE FOR THE RESISTANCE 2
      if request.POST.get('Ib')!=None and request.POST.get('Ib')!='':
        inp=str(request.POST.get('Ib'))
        if inp.isdigit():
            Ib=int(request.POST.get('Ib'))
        else:
            Ib=float(request.POST.get('Ib'))
      else:
        Ib=None

      #VALUE FOR THE OUTPUT VOLTAGE
      if request.POST.get('F')!=None and request.POST.get('F')!='':
        inp=str(request.POST.get('F'))
        if inp.isdigit():
           F=int(request.POST.get('F'))
        else:
           F=float(request.POST.get('F'))
      else:
        F=None
      
      #VALUE FOR THE INPUT VOLTAGE 
      if request.POST.get('d')!=None and request.POST.get('d')!='':
        inp=str(request.POST.get('d'))
        if inp.isdigit():
            d=int(request.POST.get('d'))
        else:
             d=float(request.POST.get('d'))
      else:
        d=None

      form=False
      if "f1" in request.POST:
        form=True  

      if given_option=='RR':
          unit=str(request.POST.get('Ia_op'))
          ch=unit[len(unit)-1]
          
          if given_data=='form1'  and form:
            #Copying the variables
            Ia1=Ia
            Ib1=Ib
            d1=d 

            #Fetching the units  
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')
            

            #Conversion of units
            Ia,Ia_c=convert2("res",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            
            #Calculation
            F=Ib*d/(Ia+Ib)
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)


            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'd1':d1,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ia_c':Ia_c,
              'Ib_c':Ib_c,
              'd_c':d_c,
             }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form4'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            Ib1=Ib

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')

            #Conversion of units

            Ia,Ia_c=convert2("res",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            F,F_c=convert2("volt",F_op,F)

            #Calculation
            d=F*(Ia+Ib)/Ib

            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
 

            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ia_c':Ia_c,
              'Ib_c':Ib_c,
              'F_c':F_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form3'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            d1=d

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ia,Ia_c=convert2("res",Ia_op,Ia)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F)
            #Calculation
            Ib=F*Ia/(d-F)
           
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)


            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ia_c':Ia_c,
              'F_c':F_c,
              'd_c':d_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form2' and form:
            #Copying the variables
            F1=F
            Ib1=Ib
            d1=d
            
            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F)
            

            #Calculation
            Ia=Ib*d/F -Ib
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)


            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ib1':Ib1,
              'd1':d1,
              'F_op':F_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ib_c':Ib_c,
              'F_c':F_c,
              'd_c':d_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)
                          
          else:
            if given_data==None:
              given_data='form1'  
            return render(request,'voltagedividercalculator.html',{'given_data':given_data,'given_option':given_option})
      

      elif given_option=='CC':
          unit=str(request.POST.get('Ia_op'))
          ch=unit[len(unit)-1]
          
          if given_data=='form1'  and form:
            #Copying the variables
            Ia1=Ia
            Ib1=Ib
            d1=d 

            #Fetching the units  
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            Ib,Ib_c=convert2("cap",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            #F=convert2("volt",F_op,F) 
            #Calculation
            F=d*Ia/(Ia+Ib)
           
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
      
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'd1':d1,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1, 
              'Ia_c':Ia_c,
              'Ib_c':Ib_c,
              'd_c':d_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form4'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            Ib1=Ib

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')

            #Conversion of units
            
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            Ib,Ib_c=convert2("cap",Ib_op,Ib)
            F,F_c=convert2("volt",F_op,F) 

            #Calculation
            d=F*(Ia+Ib)/Ia
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
      
            
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ia_c':Ia_c,
              'Ib_c':Ib_c,
              'F_c':F_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form3'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            d1=d

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F) 
          
            #Calculation
            Ib=Ia*d/F -Ia
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
      
            
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ia_c':Ia_c,
              'F_c':F_c,
              'd_c':d_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form2' and form:
            #Copying the variables
            F1=F
            Ib1=Ib
            d1=d
            
            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ib,Ib_c=convert2("cap",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F) 

            #Calculation
            Ia=F*Ib/(d-F)

            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
      
            
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ib1':Ib1,
              'd1':d1,
              'F_op':F_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ib_c':Ib_c,
              'F_c':F_c,
              'd_c':d_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)
                          
          else:
            if given_data==None:
              given_data='form1'  
            return render(request,'voltagedividercalculator.html',{'given_data':given_data,'given_option':given_option})
      
      
      
      elif given_option=='LL':
          unit=str(request.POST.get('Ia_op'))
          ch=unit[len(unit)-1]
          
          if given_data=='form1' and form:
            #Copying the variables
            Ia1=Ia
            Ib1=Ib
            d1=d 

            #Fetching the units  
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ia,Ia_c=convert2("ind",Ia_op,Ia)
            Ib,Ib_c=convert2("ind",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            #F,F_c=convert2("volt",F_op,F)
          
            #Calculation
            F=Ib*d/(Ia+Ib)

            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
            
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'd1':d1,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'Ia_c':Ia_c,
              'd_c':d_c,
              'Ib_c':Ib_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form4'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            Ib1=Ib

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')

            #Conversion of units
            Ia,Ia_c=convert2("ind",Ia_op,Ia)
            Ib,Ib_c=convert2("ind",Ib_op,Ib)
            #d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F)
          

            #Calculation
            d=F*(Ia+Ib)/Ib
            
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,              
              'Ia_c':Ia_c,
              'F_c':F_c,
              'Ib_c':Ib_c,
            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form3'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            d1=d

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ia,Ia_c=convert2("ind",Ia_op,Ia)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F)
          
            #Calculation
            Ib=F*Ia/(d-F)
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,              
              'Ia_c':Ia_c,
              'F_c':F_c,
              'd_c':d_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form2' and form:
            #Copying the variables
            F1=F
            Ib1=Ib
            d1=d
            
            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')

            #Conversion of units
            Ib,Ib_c=convert2("ind",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F)
          

            #Calculation
            Ia=Ib*d/F -Ib
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)
           
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ib1':Ib1,
              'd1':d1,
              'F_op':F_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'id':1,
              'F_c':F_c,
              'd_c':d_c,
              'Ib_c':Ib_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)
                          
          else:
            if given_data==None:
              given_data='form1'  
            return render(request,'voltagedividercalculator.html',{'given_data':given_data,'given_option':given_option})


        
      elif given_option=='RC':
          unit=str(request.POST.get('p_op'))
          if given_data!="form5":
           ch=unit[len(unit)-1]
          else:
            ch='z' 
        
          if request.POST.get('p')!=None and request.POST.get('p')!='' :     
              inp=str(request.POST.get('p'))
              if inp.isdigit():
                  p=int(request.POST.get('p'))
              else:
                  p=float(request.POST.get('p'))
          else:
               p=None

          
          if given_data=='form1'  and form:
            #Copying the variables
            Ia1=Ia
            Ib1=Ib
            d1=d 
            p1=p

            #Fetching the units  
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')
            p_op=request.POST.get('p_op')

            #Conversion of units
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            p,p_c=convert2("freq",p_op,p)
            
          
            #Calculation
            val=( (2*math.pi*Ia*Ib*p)**2 +1 )**0.5
            F=d/val
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           

            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'd1':d1,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p1':p1,
              'p_op':p_op,
              'id':1,              
              'Ia_c':Ia_c,
              'd_c':d_c,
              'Ib_c':Ib_c,
              'p_c':p_c
            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form4'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            Ib1=Ib
            p1=p

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            p_op=request.POST.get('p_op')

            #Conversion of units
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            p,p_c=convert2("freq",p_op,p)
            F,F_c=convert2("volt",F_op,F)
          
            #Calculation
            val=((2*math.pi*Ia*Ib*p)**2+1)**0.5
            d=F*val
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'given_data':given_data,
              'given_option':given_option,
               'p':p,
               'p_op':p_op,
               'p1':p1,
               'id':1,    
              'Ia_c':Ia_c,
              'F_c':F_c,
              'Ib_c':Ib_c,
              'p_c':p_c

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form3' and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            d1=d
            p1=p

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            d_op=request.POST.get('d_op')
            p_op=request.POST.get('p_op')

            #Conversion of units
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            d,d_c=convert2("volt",d_op,d)
            p,p_c=convert2("freq",p_op,p)
            F,F_c=convert2("volt",F_op,F)

            if F>=d:
               context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p1':p1,
              'p_op':p_op,
              'message':"Output voltage cannot be greater than or equal to input volatge"
               }
               return render(request,'voltagedividercalculator.html',context)

               
            #Calculation
            Ib=(d*d/(F*F)-1)**0.5/(2*math.pi*Ia*p)
            
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p_op':p_op,
              'p1':p1,
              'id':1,  
              'Ia_c':Ia_c,
              'F_c':F_c,
              'd_c':d_c,
              'p_c':p_c

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form2' and form:
            #Copying the variables
            F1=F
            Ib1=Ib
            d1=d
            p1=p
            
            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')
            p_op=request.POST.get('p_op')

            #Conversion of units
            
           
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            p,p_c=convert2("freq",p_op,p)
            F,F_c=convert2("volt",F_op,F)
            
            if F>=d:
               context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ib1':Ib1,
              'd1':d1,
              'F_op':F_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p1':p1,
              'p_op':p_op,
              'message':"Output voltage cannot be greater than or equal to input volatge"
               }
               return render(request,'voltagedividercalculator.html',context)


            #Calculation
            val=(abs( (d/F)**2 -1))**0.5
            Ia=val/(2*math.pi*p*Ib)
          
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           
            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ib1':Ib1,
              'd1':d1,
              'F_op':F_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
               'p_op':p_op,
               'p1':p1,
               'id':1,
              'F_c':F_c,
              'd_c':d_c,
              'Ib_c':Ib_c,
              'p_c':p_c

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

          
            
          elif given_data=='form5' and form:
            #Copying the variables
            F1=F
            Ib1=Ib
            d1=d
            Ia1=Ia
            
            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')
            Ia_op=request.POST.get('Ia_op')

            #Conversion of units
            Ia,Ia_c=convert2("cap",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            F,F_c=convert2("volt",F_op,F)

            
            if F>=d:
               context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'Ib1':Ib1,
              'Ib_op':Ib_op,
              'message':"Output voltage cannot be greater than or equal to input volatge"
               }
               return render(request,'voltagedividercalculator.html',context)

          
            #Calculation
            val=((d/F)**2-1)**0.5
            p=val/(math.pi*2*Ia*Ib)
            
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           

            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ib1':Ib1,
              'd1':d1,
              'Ia1':Ia1,
              'Ia_op':Ia_op,
              'F_op':F_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
               'id':1, 
              'Ia_c':Ia_c,
              'F_c':F_c,
              'd_c':d_c,
              'Ib_c':Ib_c,

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)
                          

          else:
            if given_data==None:
              given_data='form1'  
            return render(request,'voltagedividercalculator.html',{'given_data':given_data,'given_option':given_option})


      elif given_option=='RL':
          unit=str(request.POST.get('p_op'))
          if given_data!="form5":
           ch=unit[len(unit)-1]
          else:
            ch='z' 
        
          if request.POST.get('p')!=None and request.POST.get('p')!='' :     
              inp=str(request.POST.get('p'))
              if inp.isdigit():
                  p=int(request.POST.get('p'))
              else:
                  p=float(request.POST.get('p'))
          else:
               p=None

          
          if given_data=='form1' and form:
            #Copying the variables
            Ia1=Ia
            Ib1=Ib
            d1=d 
            p1=p

            #Fetching the units  
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            d_op=request.POST.get('d_op')
            p_op=request.POST.get('p_op')


            #Conversion of units
            Ia,Ia_c=convert2("ind",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            d,d_c=convert2("volt",d_op,d)
            p,p_c=convert2("freq",p_op,p)
          
          
            #Calculation
            val=2*math.pi*Ia*p
            F=val*d/(Ib*Ib+val*val)**0.5
            
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           


            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'd1':d1,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p1':p1,
              'p_op':p_op,
              'id':1,
              'Ia_c':Ia_c,
              'Ib_c':Ib_c,
              'd_c':d_c,
              'p_c':p_c

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form4'  and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            Ib1=Ib
            p1=p

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            Ib_op=request.POST.get('Ib_op')
            p_op=request.POST.get('p_op')

            #Conversion of units
            Ia,Ia_c=convert2("ind",Ia_op,Ia)
            Ib,Ib_c=convert2("res",Ib_op,Ib)
            p,p_c=convert2("freq",p_op,p)
            F,F_c=convert2("volt",F_op,F)
          
            #Calculation
            val=2*math.pi*Ia*p
            #F=val*d/(Ib*Ib+val*val)**0.5
            d=(Ib*Ib+val*val)**0.5*F/val
            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           

            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'Ib1':Ib1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'Ib_op':Ib_op,
              'given_data':given_data,
              'given_option':given_option,
               'p':p,
               'p_op':p_op,
               'p1':p1,
               'id':1,
              'Ia_c':Ia_c,
              'Ib_c':Ib_c,
              'F_c':F_c,
              'p_c':p_c

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

            
          elif given_data=='form3' and form:
            #Copying the variables
            F1=F
            Ia1=Ia
            d1=d
            p1=p

            #Fetching the units  
            F_op=request.POST.get('F_op')
            Ia_op=request.POST.get('Ia_op')
            d_op=request.POST.get('d_op')
            p_op=request.POST.get('p_op')

            #Conversion of units
            Ia,Ia_c=convert2("ind",Ia_op,Ia)
            d,d_c=convert2("volt",d_op,d)
            p,p_c=convert2("freq",p_op,p)
            F,F_c=convert2("volt",F_op,F)
          
            #Calculation
            val=2*math.pi*Ia*p
            #F=val*d/(Ib*Ib+val*val)**0.5

            Ib=( (val*d/F)**2-val*val)**0.5
            if isinstance(Ib, complex):
             context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p_op':p_op,
              'p1':p1,
              'message':"Enter valid data"
            }
             return render(request,'voltagedividercalculator.html',context)

            
            if not  (Ia>=1 and Ia<=10000 or (round(Ia,3)!=0 and round(Ia,3)!=0.001 and Ia<=10000)):
              base1,power1=Roundoff(Ia)
              Ia=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ia=round(Ia,4)
          
            if not  (Ib>=1 and Ib<=10000 or (round(Ib,3)!=0 and round(Ib,3)!=0.001 and Ib<=10000)):
              base1,power1=Roundoff(Ib)
              Ib=f"{base1} X 10"+add_tags('sup',power1)
            else:
              Ib=round(Ib,4)


           
            if not  (d>=1 and d<=10000 or (round(d,3)!=0 and round(d,3)!=0.001 and d<=10000)):
              base1,power1=Roundoff(d)
              d=f"{base1} X 10"+add_tags('sup',power1)
            else:
              d=round(d,4)
        
           
            if not  (F>=1 and F<=10000 or (round(F,3)!=0 and round(F,3)!=0.001 and F<=10000)):
              base1,power1=Roundoff(F)
              F=f"{base1} X 10"+add_tags('sup',power1)
            else:
              F=round(F,4)

            
            if not  (p>=1 and p<=10000 or (round(p,3)!=0 and round(p,3)!=0.001 and p<=10000)):
              base1,power1=Roundoff(p)
              p=f"{base1} X 10"+add_tags('sup',power1)
            else:
              p=round(p,4)  
           

            #Passing the variables
            context={
              'F':F,
              'Ia':Ia,
              'Ib':Ib,
              'd':d,
              'F1':F1,
              'Ia1':Ia1,
              'd1':d1,
              'F_op':F_op,
              'Ia_op':Ia_op,
              'd_op':d_op,
              'given_data':given_data,
              'given_option':given_option,
              'p':p,
              'p_op':p_op,
              'p1':p1,
              'id':1,
              'Ia_c':Ia_c,
              'F_c':F_c,
              'd_c':d_c,
              'p_c':p_c

            }

            #Rendering the template
            return render(request,'voltagedividercalculator.html',context)

          else:
            if given_data==None:
              given_data='form1'  
            return render(request,'voltagedividercalculator.html',{'given_data':given_data,'given_option':given_option})  

      
  else:
   return render(request,'voltagedividercalculator.html',{'given_data':'form1','given_option':'RR'})




#CODE FOR THE FREQEUNCY CALCULATOR


def frequencycalcultor(request):
  
  if request.method=='POST':
     
     #FOR GETTING THE FORM
     given_data=request.POST.get('given_data')
     
     #FOR GETTING THE wave velocity
     if request.POST.get('waveVel')!=None and request.POST.get('waveVel')!='' :
              waveVel_op=request.POST.get('waveVel_op')     
              inp=str(request.POST.get('waveVel'))
              if inp.isdigit():
                  waveVel=int(request.POST.get('waveVel'))
              else:
                  waveVel=float(request.POST.get('waveVel'))
              waveVel1=waveVel    
     else:
       waveVel=None
     
     #FOR GETTING THE time
     if request.POST.get('time')!=None and request.POST.get('time')!='' :
              time_op=request.POST.get('time_op')     
              inp=str(request.POST.get('time'))
              if inp.isdigit():
                  time=int(request.POST.get('time'))
              else:
                  time=float(request.POST.get('time'))
              time1=time    
     else:
       time=None

     #FOR GETTING THE WAVELENGTH
     if request.POST.get('wave')!=None and request.POST.get('wave')!='' :
              wave_op=request.POST.get('wave_op')     
              inp=str(request.POST.get('wave'))
              if inp.isdigit():
                  wave=int(request.POST.get('wave'))
              else:
                  wave=float(request.POST.get('wave'))
              wave1=wave    
     else:
       wave=None

     #TO CHECK WHETHER THE FORM IS SUBMITTED OR NOT
     form= False
     if "f1" in request.POST:
       form=True


     if given_data=='form1' and form:    
       
       #Conversion
       time,time_c=convert2('time',time_op,time)
       wave,wave_c=convert2('len',wave_op,wave)
       
       #Calculation
       waveVel=wave/time
       freq=1/time

       if not( (wave>=1 and wave<=10000) or (round(wave,3)!=0 and round(wave,3)!=0.001 and wave<=10000)):
              base1,power1=Roundoff(wave)
              wave=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              wave=round(wave,4)
       
       if not( (time>=1 and time<=10000) or (round(time,3)!=0 and round(time,3)!=0.001 and time<=10000)):
              base1,power1=Roundoff(time)
              time=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              time=round(time,4)

       if not( (waveVel>=1 and waveVel<=10000) or (round(waveVel,3)!=0 and round(waveVel,3)!=0.001 and waveVel<=10000)):
              base1,power1=Roundoff(waveVel)
              waveVel=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              waveVel=round(waveVel,4)
       
       if not( (freq>=1 and freq<=10000) or (round(freq,3)!=0 and round(freq,3)!=0.001 and freq<=10000)):
              base1,power1=Roundoff(freq)
              freq=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              freq=round(freq,4)

       context={
          'waveVel':waveVel,
          'freq':freq,
          'time':time,
          'wave':wave,
          'time1':time1,
          'wave1':wave1,
          'wave_op':wave_op,
          'time_op':time_op,
          'id':1,
          'given_data':given_data,
          'time_c':time_c,
          'wave_c':wave_c,
          }       
       return render(request,'frequencycalcultor.html',context)
     
     
     if given_data=='form2' and form:    
       
       #Conversion
       waveVel,waveVel_c=convert2('vel',waveVel_op,waveVel)
       time,time_c=convert2('time',time_op,time)
       
       #Calculation
       wave=waveVel*time
       freq=1/time

       if not( (wave>=1 and wave<=10000) or (round(wave,3)!=0 and round(wave,3)!=0.001 and wave<=10000)):
              base1,power1=Roundoff(wave)
              wave=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              wave=round(wave,4)
       
       if not( (time>=1 and time<=10000) or (round(time,3)!=0 and round(time,3)!=0.001 and time<=10000)):
              base1,power1=Roundoff(time)
              time=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              time=round(time,4)

       if not( (waveVel>=1 and waveVel<=10000) or (round(waveVel,3)!=0 and round(waveVel,3)!=0.001 and waveVel<=10000)):
              base1,power1=Roundoff(waveVel)
              waveVel=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              waveVel=round(waveVel,4)
       
       if not( (freq>=1 and freq<=10000) or (round(freq,3)!=0 and round(freq,3)!=0.001 and freq<=10000)):
              base1,power1=Roundoff(freq)
              freq=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              freq=round(freq,4)

       context={
          'wave':wave,
          'freq':freq,
          'time':time,
          'waveVel':waveVel,
          'time1':time1,
          'waveVel1':waveVel1,
          'waveVel_op':waveVel_op,
          'time_op':time_op,
          'id':1,
          'given_data':given_data,
          'time_c':time_c,
          'waveVel_c':waveVel_c
       }       
       return render(request,'frequencycalcultor.html',context)


     if given_data=='form3' and form:    
       
       #Conversion
       waveVel,waveVel_c=convert2('vel',waveVel_op,waveVel)
       wave,wave_c=convert2('len',wave_op,wave)
       
       
       #Calculation
       time=wave/waveVel
       freq=1/time

       if not( (wave>=1 and wave<=10000) or (round(wave,3)!=0 and round(wave,3)!=0.001 and wave<=10000)):
              base1,power1=Roundoff(wave)
              wave=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              wave=round(wave,4)
       
       if not( (time>=1 and time<=10000) or (round(time,3)!=0 and round(time,3)!=0.001 and time<=10000)):
              base1,power1=Roundoff(time)
              time=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              time=round(time,4)

       if not( (waveVel>=1 and waveVel<=10000) or (round(waveVel,3)!=0 and round(waveVel,3)!=0.001 and waveVel<=10000)):
              base1,power1=Roundoff(waveVel)
              waveVel=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              waveVel=round(waveVel,4)
       
       if not( (freq>=1 and freq<=10000) or (round(freq,3)!=0 and round(freq,3)!=0.001 and freq<=10000)):
              base1,power1=Roundoff(freq)
              freq=f"{base1} X 10 "+add_tags('sup',power1)
       else:
              freq=round(freq,4)


       context={
          'wave':wave,
          'freq':freq,
          'time':time,
          'waveVel':waveVel,
          'wave1':wave1,
          'waveVel1':waveVel1,
          'waveVel_op':waveVel_op,
          'wave_op':wave_op,
          'id':1,
          'given_data':given_data,
          'wave_c':wave_c,
          'waveVel_c':waveVel_c
       }       
       return render(request,'frequencycalcultor.html',context)
 

     else:
        return render(request,'frequencycalcultor.html',{'given_data':given_data})   
  else:
    return render(request,'frequencycalcultor.html',{'given_data':'form1'})




