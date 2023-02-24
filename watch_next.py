# Import Python library spaCy
import spacy


# The description of the movie which was watched
movie_des = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, " \
            "the Illuminati trick Hulk into a shuttle and " \
            "launch him into space to a planet where the Hulk can live in peace." \
            "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."


# Create the function to return which movies a user would watch next
# if they have watched particular movie with a particular description (parameter of the function)
def next_movie_to_watch(watched_movie_des):

    # Set local variables
    dict_movies = {}
    movie_to_watch = []

    # Specifying the English model to use
    nlp = spacy.load('en_core_web_md')

    # Open the file for reading
    movies_file = open("movies.txt", "r")
    contents = movies_file.readlines()
    movies_file.close()

    # Use model for the description of the movie which was watched
    model_sentence = nlp(watched_movie_des)

    # The loop to iterate through the list of movies
    for line in range(0, len(contents)):

        # Split the list of movies to separate name and description of the movie
        movie_content = contents[line].split(":")

        # Find the similarity between the description of initial movie which was watched and the list of movies
        similarity = nlp(movie_content[1]).similarity(model_sentence)

        # Create the list with the values of similarity for each movie in the list
        movie_to_watch.append(similarity)

        # Create the dictionary with keys - name of the movie in the list, values - similarity
        dict_movies[movie_content[0]] = similarity

    # Find the maximum value among similarities
    sim_movie_to_watch = max(movie_to_watch)

    # The loop to iterate through the dictionary
    for key, value in dict_movies.items():

        # Check to find the value which is equal to maximum value of similarity then print out the key for this value
        if value == sim_movie_to_watch:
            return f"Your next movie to watch is: {key}"


# Call the function and print out the resul
print(next_movie_to_watch(movie_des))
