import copy


# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if not title or not genre or not rating:
        return None

    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    '''This function removes a specified movie from user's
    watchlist and adds it to their list of watched movies'''

    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    total = 0

    for movie_dict in user_data["watched"]:
        movie_rating = movie_dict.get("rating", 0.0)
        total += movie_rating

    average = total/len(user_data["watched"])

    return average

    # looping the watched_list
    # get rating value
    # compare values
    # count number
    # calculate average


def get_most_watched_genre(user_data):
    user_genres = {}
    most_watched = None

    # Creates dictionary from list of movies watched
    # with genres as keys and their occurences as values
    for movie in user_data["watched"]:
        if movie["genre"] not in user_genres:
            user_genres[movie["genre"]] = 1
        else:
            user_genres[movie["genre"]] += 1

    if user_genres:
        most_watched = max(user_genres, key=user_genres.get)

    return most_watched


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    # Creates deep copy to avoid changing original list
    unique_watched = copy.deepcopy(user_data["watched"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in unique_watched:
                unique_watched.remove(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie not in user_data["watched"] and
                    movie not in unique_watched):
                unique_watched.append(movie)

    return unique_watched


# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    friends_recs = get_friends_unique_watched(user_data)
    final_recs = []

    for movie in friends_recs:
        if movie["host"] in user_data["subscriptions"]:
            final_recs.append(movie)

    return final_recs


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    friends_recs = get_friends_unique_watched(user_data)
    user_fav_genre = get_most_watched_genre(user_data)
    final_recs = []

    for movie in friends_recs:
        if movie["genre"] is user_fav_genre:
            final_recs.append(movie)

    return final_recs


def get_rec_from_favorites(user_data):
    user_recs = get_unique_watched(user_data)
    final_recs = []

    for movie in user_recs:
        if movie in user_data["favorites"]:
            final_recs.append(movie)

    return final_recs