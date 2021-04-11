def main():
	textFile = open("input.txt", "r", encoding="utf8")
	text = textFile.read().replace('\n', '')
	textFile.close()
	
	print("File loaded successfully...")
	
	numCharInQuotes = 0
	totalChar = 0
	
	countingQuotes = False
	for char in text:
		if(char == '\"' or char == "“" or char == "”"): #different kinds of quotes...
			countingQuotes = not countingQuotes
			#print("quote")
			continue
		if(countingQuotes):
			numCharInQuotes+=1
		#print(char)
		totalChar += 1 #Do this rather than len() because we aren't counting quotes as characters!
		
	ratio = numCharInQuotes/totalChar
		
	print("_"*50)
	print("Analysis complete!\n")
	print("Number of characters in quotes:    ",numCharInQuotes)
	print("Total characters:                  ", totalChar)
	print("Ratio (characters in quotes/total):", ratio, " (",(ratio*100),"%)")
	print("_"*50)
main()