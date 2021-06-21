import json
import requests

class Solution:


	def run(film, character):
		#
		# Write your code below; return type and arguments should be according to the problem's requirements
		#
		
		characterRequest = requests.get('https://challenges.hackajob.co/swapi/api/people/?search=' + character)
		loadedCharacter = json.loads(characterRequest.text)
		filmRequest = requests.get('https://challenges.hackajob.co/swapi/api/films/?search=' + film)
		loadedFilm = json.loads(filmRequest.text)
		filmList = ''
		characterList = ''

		first = True
		for starredIn in loadedCharacter['results'][0]['films']:
			if first:
				first=False;
			else:
				filmList = filmList + ','

			data = requests.get(starredIn)
			parsed_data = json.loads(data.text)
			filmList = filmList + parsed_data['title'];
		
		first = True

		try:
			for characterL in loadedFilm['results'][0]['characters']:
				if first:
					first = False;
				else:
					characterList = characterList + ','
				data = requests.get(characterL)
				parsed_data = json.loads(data.text)
				characterList = characterList + parsed_data['name']
		except:
			characterList = 'None'
	
		sortedCharacterList = ((sorted(characterList.split(','))))
		sortedFilmList = ((sorted(filmList.split(','))))
		filmsAndCharacters = film + ': ' + ', '.join(sortedCharacterList) + '; ' + character + ': ' +', '.join(sortedFilmList)

		print(filmsAndCharacters)
		
		return filmsAndCharacters

	run("A New Hope","Raymus Antilles")
