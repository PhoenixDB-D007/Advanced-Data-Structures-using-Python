Text = input("Enter the Text:\n")
Pattern = input("Enter The Pattern:")
Text_Length = len(Text)
Pattern_Length = len(Pattern)
if Pattern_Length > Text_Length:
	print("No Match Found")
else:
	Found = False
	for i in range(0,Text_Length):
		j = 0
		while j < Pattern_Length and Text[i] == Pattern[j] :
			i=i+1
			j=j+1
		if j == Pattern_Length:
			Found = True
			print("Matching Found At " + str(i-Pattern_Length+1))
	if not Found:		
		print("No Matching Found")
