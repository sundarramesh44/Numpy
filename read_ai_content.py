#function definition to read all files
#major difference with the above program is that we are including all key words in list
#and we are comparing those key words with the (input)question and we are returning the output files
#based on the keywords which we have filtered out.
def Electromagnetism():
  with open('Electromagnetism.txt','r') as r1:
    output1 = r1.read()
    print(output1)
    return output1

def AC_DC_Current():
  with open('AC_DC_Current.txt','r') as r2:
    output2 = r2.read()
    print(output2)
    return output2

def Apps_Electro():
  with open('Applications_Electromagnetism.txt','r') as r3:
    output3 = r3.read()
    print(output3)
    return output3

def Electric_Charge():
  with open('Electric_charge.txt','r') as r4:
    output4 = r4.read()
    print(output4)
    return output4

def Electric_field():
  with open('Electric_field.txt','r') as r5:
    output5 = r5.read()
    print(output5)
    return output5

def Electromagnetic_Spectrum():
  with open('Electromagnetic_Spectrum.txt','r') as r6:
    output6 = r6.read()
    print(output6)
    return output6

def Electromagnetic_induction():
  with open('Electromagnetic_induction.txt','r') as r7:
    output7 = r7.read()
    print(output7)
    return output7

def Magnetic_field():
  with open('Magnetic_field.txt','r') as r8:
    output8 = r8.read()
    print(output8)
    return output8

def Maxwells_Equations():
  with open('Maxwells_Equations.txt','r') as r9:
    output9 = r9.read()
    print(output9)
    return output9

def Relationship_Electric_Magnetic_Fields():
  with open('Relationship_Electric_Magnetic_Fields.txt','r') as r10:
    output10 = r10.read()
    print(output10)
    return output10
for i in range(10):
  input1 = input('How can I help you ---')
  input_lower = input1.lower()
  input_split = input_lower.split()

  key_words = ['electromagnetism','ac','dc','current','applications','electromagnetic','electric','fields','charge','field','spectrum','induction','magnetic','maxwell','equations','relationship',"maxwell's"]

  filter_words_before = [word for word in input_split if word.lower() in key_words]
  filter_words = ' '.join(filter_words_before)
  #print(filter_words)
  if filter_words == 'electromagnetism' or filter_words == 'electro_magnetism?*' or filter_words == 'electro magnetism?*' :
    Electromagnetism()
  elif filter_words == 'ac dc current' or filter_words == 'ac_dc_current' or filter_words == 'ac_dc current' or filter_words == 'ac dc_current' or filter_words == 'dc ac current' or filter_words == 'dc_ac_current' or filter_words == 'dc_ac current' or filter_words == 'dc ac_current':
    AC_DC_Current()
  elif filter_words == 'applications electromagnetism' or filter_words == 'apps electromagnetism' or filter_words == 'electromagnetism applications' or filter_words == 'electromagnetism apps' :
    Apps_Electro()
  elif filter_words == 'electric charge' or filter_words == 'electric_charge' or filter_words == 'charge electric' or filter_words == 'charge_electric':
    Electric_Charge()
  elif filter_words == 'electric field' or filter_words == 'electric_field' or filter_words == 'field_electric' or filter_words == 'field electric' :
    Electric_field()
  elif filter_words == 'electromagnetic spectrum' or filter_words == 'electromagnetic_spectrum' or filter_words == 'spectrum electromagnetic' or filter_words == 'spectrum_electromagnetic':
    Electromagnetic_Spectrum()
  elif filter_words == 'electromagnetic induction' or filter_words == 'electromagnetic_induction' or filter_words == 'induction electromagnetic'  or filter_words == 'induction_electromagnetic' :
    Electromagnetic_induction()
  elif filter_words == 'magnetic field'  or filter_words == 'magnetic_field' or filter_words == 'magnetic_electric' or filter_words == 'magnetic electric' :
    Magnetic_field()
  elif filter_words == "maxwell's equations" or filter_words == "maxwells equations" or filter_words == "maxwell equations" or filter_words == "maxwell's_equations?*" or filter_words == "maxwells_equations" or filter_words == "maxwell_equations" or filter_words == "maxwell's_equation" or filter_words == "maxwells_equation" or filter_words == "maxwell_equation" :
    Maxwells_Equations()
  elif filter_words == 'relationship electric magnetic fields' or filter_words == 'relationship electric_magnetic fields' or filter_words == 'relationship_electric_magnetic_fields'  or filter_words == 'electric_magnetic fields' or filter_words == 'electric magnetic fields' or filter_words == 'electric magnetic' or filter_words == 'electric_magnetic':
    Relationship_Electric_Magnetic_Fields()
  else:
    i1 = 'electromagnetism'
    i2 = 'ac dc current'
    i3 = 'applications electromagnetism'
    i4 = 'electric charge'
    i5 = 'electric field'
    i6 = 'electromagnetic spectrum'
    i7 = 'electromagnetic induction'
    i8 = 'magnetic field'
    i9 = "maxwell's equations"
    i10 = 'relationship electric magnetic fields'

    input_text = filter_words

    y1 = fuzz.WRatio(input_text, i1)
    #print(i1,y1)
    y2 = fuzz.WRatio(input_text, i2)
    #print(i2,y2)
    y3 = fuzz.WRatio(input_text, i3)
    #print(i3,y3)
    y4 = fuzz.WRatio(input_text, i4)
    #print(i4,y4)
    y5 = fuzz.WRatio(input_text, i5)
    #print(i5,y5)
    y6 = fuzz.WRatio(input_text, i6)
    #print(i6,y6)
    y7 = fuzz.WRatio(input_text, i7)
    #print(i7,y7)
    y8 = fuzz.WRatio(input_text, i8)
    #print(i8,y8)
    y9 = fuzz.WRatio(input_text, i9)
    #print(i9,y9)
    y10 = fuzz.WRatio(input_text, i10)
    #print(i10,y10)

    print('')
    print(f'File content for {input1} below')

    if y1 > 80 and y1 > y6 and y1 > y7 and y1 > y3:
      Electromagnetism()
    elif y2 > 80:
      AC_DC_Current()
    elif y3 > 80 and y3 > y1 and y3 > y6 and y3 > y7:
      Apps_Electro()
    elif y4 > 80 and y4 > y5:
      Electric_Charge()
    elif y5 > 80 and y5 > y10:
      Electric_field()
    elif y6 > 80 and y6 > y7:
      Electromagnetic_Spectrum()
    elif y7 > 80:
      Electromagnetic_induction()
    elif y8 > 80 and y8 > y10:
      Magnetic_field()
    elif y9 > 80:
      Maxwells_Equations()
    elif y10 > 80:
      Relationship_Electric_Magnetic_Fields()
    else:
      print('Please enter the valid input')