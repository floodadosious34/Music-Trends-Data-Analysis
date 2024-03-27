spotify_tracks_data_query = (''' 
SELECT s.*,
       g.*,
       t.genres,
       t.popularity
    
FROM artists t
INNER JOIN spotify2023_tracks s ON t.name = s."artist(s)_name"
INNER JOIN the_grammy_awards g on t.name = g.artist;

''')
