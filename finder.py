print('இந்த நூலை மெய்ப்பு செய்த அனைத்து விக்கிமூல பங்களிப்பாளர்களுக்கும் நன்றி!\n') 
fh  =open ("Tamil_Proverbs.txt", "r")
word=input ("சொல்லை உள்ளீடு செய்யவும்:        ")
s = " "
count = 1
 
L=fh.readlines ()

for i in L:
	L2=i.split()
	if word in L2:
		print (i)
