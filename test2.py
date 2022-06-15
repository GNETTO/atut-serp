import re

# re.search("^The.*Spain$", txt)

def test_func(liste):
    final_links_ordered = []
    for i in range(len(liste)):
        #base_path = re.search("^https.*/$", liste[i])
        base_path = liste[i].split("/")
        print(base_path)
        final_links_ordered.append(base_path)



l = ['https://fr.wikipedia.org/wiki/Michael_Jackson',
     'https://www.nostalgie.fr/artistes/michael-jacks',
     'https://apprendre-le-home-studio.fr/composer-une-musique-michael-jackson/'
     ]
test_func(l)
# base_path = (liste[i][:liste[i].find('/')])