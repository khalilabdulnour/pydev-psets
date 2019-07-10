"""
Spotify Playlists - Sorting
"""

playlist_titles = ['Tiny Dancer', 'At Last', 'Fortunate Son', 
'Hey Jude', 'Isn\'t She Lovely', 'Just the Way You Are', 'I\'m Yours',
'Vienna', 'Roxanne', 'Dancing in the Moonlight']

# Alphabetize these songs and print the result.

print(sorted(playlist_titles))
"""['At Last', 'Dancing in the Moonlight', 'Fortunate Son', 'Hey Jude', "I'm Yours", "Isn't She Lovely", 'Just the Way You Are', 'Roxanne', 'Tiny Dancer', 'Vienna']"""


# Now do the reverse.

print(sorted(playlist_titles, reverse=True))
"""['Vienna', 'Tiny Dancer', 'Roxanne', 'Just the Way You Are', "Isn't She Lovely", "I'm Yours", 'Hey Jude', 'Fortunate Son', 'Dancing in the Moonlight', 'At Last']"""
