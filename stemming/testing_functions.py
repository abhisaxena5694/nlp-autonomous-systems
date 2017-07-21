def getstems(inflect_list, algorithm):
	stemmed = []
	for i in inflect_list:
		stemmed.append(algorithm(i))
	return stemmed
	


'''
def stemmer_accuracy(matched, original):
	#print(len(matched) / len(original))
	return 100 * len(matched) / len(original)
'''

def stemmer_accuracy(inflected, original, algorithm):
	derived_stems = getstems(inflected, algorithm)
	matched = [i for i in derived_stems for j in original if i==j]
	#print(len(matched) / len(original))
	return 100 * len(matched) / len(original)
