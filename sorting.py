sorting value different types
sorted_term = sorted(j.keys(), key = lambda x : (j[x]['wiki_score'], isinstance(x, str)),reverse=True)
