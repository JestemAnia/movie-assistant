from filmweb.filmweb import Filmweb
fw = Filmweb()
items = fw.search('Jak działa jamniczek')
item = items[0] # grab first result
info = item.get_info() # fetch more info
print('Title: {} ({}) Rate: {} ({} votes) Description: {}'.format(item.name, item.year, item.rate, item.votes, info['description_short']))