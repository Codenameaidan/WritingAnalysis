def main():
	text_file = open("input.txt", "r", encoding="utf8")
	text = text_file.read().replace('\n', '')
	text_file.close()
	
	print("File loaded successfully...")
	
	num_char_in_quotes = 0
	total_char = 0
	
	counting_quotes = False
	for char in text:
		if(char == '\"' or char == "“" or char == "”"): #different kinds of quotes (especially if copy-pasted from word doc...)
			counting_quotes = not counting_quotes #Start or stop counting quotes
			continue
		if(counting_quotes):
			num_char_in_quotes+=1
		total_char += 1 #Do this rather than len() because we aren't counting quotes as characters!
	ratio = num_char_in_quotes/total_char
		
	

	print("_"*50)
	print("Analysis complete!\n")
	#print("Number of characters in quotes:    ",num_char_in_quotes)
	#print("Total characters:                  ", total_char)
	#print("Ratio (characters in quotes/total):", round(ratio,2), " (",(round(ratio,2)*100),"%)")
	print("Percent of characters enclosed in quotes: ",(round(ratio,2)*100),"%")
	print("_"*50)
main()