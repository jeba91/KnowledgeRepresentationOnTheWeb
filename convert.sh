sh tarql/target/appassembler/bin/tarql mapping_kaggle.sparql csv_file/neg_test.csv  > turtle_files/neg_test.ttl
sh tarql/target/appassembler/bin/tarql mapping_kaggle.sparql csv_file/neg_train.csv > turtle_files/neg_train.ttl
sh tarql/target/appassembler/bin/tarql mapping_kaggle.sparql csv_file/pos_test.csv  > turtle_files/pos_test.ttl
sh tarql/target/appassembler/bin/tarql mapping_kaggle.sparql csv_file/pos_train.csv > turtle_files/pos_train.ttl
sh tarql/target/appassembler/bin/tarql mapping_tweetratings.sparql csv_file/tweets_ratings.csv > turtle_files/tweets_ratings.ttl
sh tarql/target/appassembler/bin/tarql mapping_imdbnames.sparql csv_file/parsed_imdbnames.csv > turtle_files/imdb_names.ttl
sh tarql/target/appassembler/bin/tarql mapping_imdbgenre.sparql csv_file/parsed_imdbgenres1.csv > turtle_files/imdb_genres1.ttl
sh tarql/target/appassembler/bin/tarql mapping_imdbgenre.sparql csv_file/parsed_imdbgenres2.csv > turtle_files/imdb_genres2.ttl
sh tarql/target/appassembler/bin/tarql mapping_imdbgenre.sparql csv_file/parsed_imdbgenres3.csv > turtle_files/imdb_genres3.ttl
sh tarql/target/appassembler/bin/tarql --tab mapping_imdbrating.sparql IMDB/title.ratings.tsv > turtle_files/imdb_ratings.ttl
