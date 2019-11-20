def find_by_name(collection, album_name):
    for item in collection:
        if item['album'] == album_name:
            return item
    return None



def find_by_rank(collection, album_rank):
    for item in collection:
        if item['number'] == album_rank:
            return item
    return None



def find_by_year(collection, year):
    albums = []
    for item in collection:
        if item['year'] == year:
            albums.append(item['album'])
    return albums



def find_by_years(collection, start_year, end_year):
    albums_year = []
    for item in collection:
        if int(item['year']) >= int(start_year) and int(item['year']) <= int(end_year):
            albums_year.append(item['album'])
    return albums_year



def find_by_ranks(collection, start_rank, end_rank):
    album_ranks = []
    for item in collection:
        if int(item['number']) >= int(start_rank) and int(item['number']) <= int(end_rank):
            album_ranks.append(item['album'])
    return album_ranks



def all_titles(collection):
    titles = []
    for item in collection:
        titles.append(item['album'])
    return titles

    # albums = list(map(lambda item: item['album'], collection))
    # albums = [item['album'] for item in collection]



def all_artists(collection):
    artists = []
    for item in collection:
        artists.append(item['artist'])
    return artists



def most_albums(collection):
    album_counts = {}
    for artist in all_artists(collection):
        if artist in album_counts:
            album_counts[artist] += 1
        else:
            album_counts[artist] = 1
    max_albums = (sorted(album_counts.items(), key=lambda x: x[1], reverse=True))
    y = max_albums[0][1]
    z = 0
    max_albums_list = []
    while y == max_albums[z][1]:
        max_albums_list.append(max_albums[z][0])
        z += 1
    return max_albums_list



def popular_word(collection):
    word_counts = {}
    for title in all_titles(collection):
        for word in title.split():
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    max_word = (sorted(word_counts.items(), key=lambda x: x[1], reverse=True))
    y = max_word[0][1]
    z = 0
    max_words_list = []
    while y == max_word[z][1]:
        max_words_list.append(max_word[z][0])
        z += 1
    return max_words_list



def string_to_list(lines):
    item_list = []
    for item in lines:
        item_list.append(item.split('\t'))
    for term in item_list:
        term[-1] = term[-1].replace('\n','')
    return item_list



def list_to_dict(lines):
    catalog = []
    for row in string_to_list(lines):
        item_dict = {}
        item_dict['rank'] = row[0]
        item_dict['name'] = row[1]
        item_dict['artist'] = row[2]
        item_dict['year'] = row[3]
        catalog.append(item_dict)
    return catalog