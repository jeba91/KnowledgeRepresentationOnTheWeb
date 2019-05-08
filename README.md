# Knowledge Representation on the Web
## Linking sentiment words of reviews with movie rating scores for a movie search engine.

The .sparql files are used with TARQL to parse the .csv or .tsv files into turtle files,
the convert.sh contains a runnable bash script to convert all files to useable turtle files.

The python scripts are for cleaning up used datasets or conversion to useable .csv or .tsv files.

## Libraries

NLTK(Used to parse text, clean, tokenize and retrieve sentiments words).
https://www.nltk.org/ \n
https://www.nltk.org/_modules/nltk/sentiment/vader.html \n

TARQL(Used to parse .tsv and .csv into turtle files).
http://tarql.github.io/examples/ \n


## Data

Kaggle competition where IMDB ratings and comments from users are saved into a database.
The database consists of 25.000 negative and 25.000 positive comments and ratings, the comments are parsed with a VADER sentiment analysis used from the NLTK library. Together with the rating they are linked to the IMDB URI.
https://www.kaggle.com/iarunava/imdb-movie-reviews-dataset

IMDB datasets where the ratings and descriptions of movies including genre and year are extracted and linked to their URI's.
https://www.imdb.com/interfaces/

Movie ontology plus the DBpedia ontology for description purposes.
https://github.com/ontop/ontop/wiki/Example_MovieOntology

A movie rating from tweets database, updated on a daily base. The ratings are parsed together with the IMDB URI's for linking.
https://github.com/sidooms/MovieTweetings

The online database of the final RDF statements with saved queries.
https://krr.triply.cc/jeba91/Jeroen-krw/sparql/jeroen-sparql
