import spacy

nlp = spacy.load('en_core_web_md')

titles = []
descrips = []

def read_file():
    with open('movies.txt', 'r') as f:
        for line in f:
            line = line.strip()
            line = line.split(':')
            titles.append(line[0])
            descrips.append(line[1])


def find_new_movie(last_movie):
    loop = 0
    sims = []
    last_movie = nlp(last_movie)
    for movie in descrips:
        similarity = nlp(movie).similarity(last_movie)
        sims.append(float(similarity))
    sorted_sims = sorted(sims)
    highest_sim = sorted_sims[-1]
    for sim in sims:
        loop += 1
        if sim == highest_sim:
            return titles[loop-1]


read_file()

last_movie = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

print(find_new_movie(last_movie))
