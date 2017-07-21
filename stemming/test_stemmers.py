#from stemmer_package.stemming import porter, porter2, paicehusk, lovins
from stemmers import porter, porter2, paicehusk, lovins
from testing_functions import getstems, stemmer_accuracy

porter_stemmer = porter.stem
porter2_stemmer = porter2.stem
paicehusk_stemmer = paicehusk.stem
lovins_stemmer = lovins.stem



inflected_words = ['buses', 'misses', 'wishes', 'watches', 'foxes', 'potatos',
					'does', 'parties', 'studies', 'tried', 'happier',
					'easiest', 'carrying', 'buys', 'played', 'dying', 'lying',
					'riding', 'loving', 'writing', 'providing', 'hitting', 'stopped',
					'wetter', 'fattest', 'beginning', 'preferred', 'happening', 'visited'] # 'cries',


original_stems = ['bus', 'miss', 'wish', 'watch', 'fox', 'potato', 'do', 'party',
					'study', 'studies',  'try', 'happy', 'easy', 'carry',
					'buy', 'play', 'die', 'lie', 'ride', 'love', 'write', 'provide',
					'hit', 'stop', 'stopped', 'wet', 'fat', 'begin', 'prefer'] #'cry',



#derived_stems = getstems(inflected_words, porter2_stemmer)



#matched_stems = [i for i in derived_stems for j in original_stems if i==j]

print("Stemmer's accuracy:")

print("Porter's stemmer: ", stemmer_accuracy(inflected_words, original_stems, porter_stemmer))
print("Porter2's stemmer: ", stemmer_accuracy(inflected_words, original_stems, porter2_stemmer))
#print("Paicehusk's stemmer: ", stemmer_accuracy(inflected_words, original_stems, paicehusk_stemmer))
print("Lovin's stemmer: ", stemmer_accuracy(inflected_words, original_stems, lovins_stemmer))
