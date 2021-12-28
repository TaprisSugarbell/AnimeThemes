# import os
# import subprocess
# import cloudscraper
from AnimeThemes.moe import AnimeThemes

# c = cloudscraper.create_scraper()
at = AnimeThemes()
_anime = {'id': 847, 'name': 'Gamers!', 'slug': 'gamers', 'year': 2017, 'season': 'Summer',
          'synopsis': 'Centering on the gaming lives of various high school students who play video games, '
                      'including: Keita Amano, a lonely young man who loves video games; Karen Tendou, the beaut'
                      'iful president of the video game club; Chiaki Hoshinomori, who constantly fights with Keita; '
                      'and Tasuku Uehara, who puts on a facade of being satisfied with his life in the real world, but'
                      ' he in truth loves video games.\n<br><br>\n(Source: Anime News Network)',
          'created_at': '2021-03-27T00:43:46.788527Z',
          'updated_at': '2021-03-28T02:11:32.266936Z',
          'deleted_at': None}
# animethemes = at.search("Gamers!")["search"]["anime"][0]["animethemes"]
animetheme = {'id': 7512, 'type': 'OP', 'sequence': None, 'group': None, 'slug': 'OP',
              'created_at': '2021-03-27T03:40:33.149971Z', 'updated_at': '2021-03-27T03:40:33.197500Z',
              'deleted_at': None, 'animethemeentries': [{'id': 8793, 'version': None, 'episodes': '2-5, 7-12',
                                                         'nsfw': False, 'spoiler': False, 'notes': '',
                                                         'created_at': '2021-03-27T03:40:33.222074Z',
                                                         'updated_at': '2021-03-27T03:40:33.222074Z',
                                                         'deleted_at': None,
                                                         'videos': [
                                                             {'id': 8352,
                                                              'basename': 'Gamers-OP1-NCBD1080.webm',
                                                              'filename': 'Gamers-OP1-NCBD1080',
                                                              'path': '2017/Summer/Gamers-OP1-NCBD1080.webm',
                                                              'size': 39551499, 'mimetype': 'video/webm',
                                                              'resolution': 1080, 'nc': True, 'subbed': False,
                                                              'lyrics': False, 'uncen': False, 'source': 'BD',
                                                              'overlap': 'None', 'created_at':
                                                                  '2021-03-27T00:29:24.885780Z',
                                                              'updated_at': '2021-03-27T00:29:24.885780Z',
                                                              'deleted_at': None, 'tags': 'NCBD1080',
                                                              'link':
                                                                  'https://staging.animethemes.moe/video/'
                                                                  'Gamers-OP1-NCBD1080.webm'},
                                                             {'id': 8353, 'basename': 'Gamers-OP1.webm',
                                                              'filename': 'Gamers-OP1', 'path':
                                                                  '2017/Summer/Gamers-OP1.webm',
                                                              'size': 27828034, 'mimetype': 'video/webm',
                                                              'resolution': 720, 'nc': False, 'subbed': False,
                                                              'lyrics': False, 'uncen': False, 'source': None,
                                                              'overlap': 'None', 'created_at':
                                                                  '2021-03-27T00:29:24.908009Z',
                                                              'updated_at': '2021-03-27T00:40:42.502095Z',
                                                              'deleted_at': None, 'tags': '', 'link':
                                                                  'https://staging.animethemes.moe/video/'
                                                                  'Gamers-OP1.webm'
                                                              }]}]}

# animes = at.search("Bakemonogatari")["search"]["anime"]
# print(animes)
# animethemes = animes[0]["animethemes"]
# for theme in animethemes:
#     print(theme)

# for i in animetheme["animethemeentries"]:
#     for j in i["videos"]:
#         print(j)
#         print(j["basename"])
# print(at.search_anime("Gamers!")["anime"][0])
# print(at.video("Gamers-OP1-NCBD1080.webm"))

# print(at.search_anime("Bakemonogatari"))
# animes = at.search_anime("Bakemonogatari")["anime"]
# for anime in animes:
#     print(anime)

print(at.search_anime(anime_id=218))

# print(at.anime("bakemonogatari"))
# anime = at.anime("bakemonogatari")["anime"]
# print(anime)
# animethemes = anime["animethemes"]
# vid = animethemes[-1]
# vid = animethemes
# print(vid)
# print("\n\n")
# for i in vid:
#     print(i)
#     for j in i["animethemeentries"]:
#         print(j)
#         for h in j["videos"]:
#             print(h)
#             print("link:", h["link"].replace("staging.", ""))
#             print("\n\n")

# for theme in animethemes:
#     print(theme)

# r = c.get("https://animethemes.moe/video/Gamers-OP1-NCBD1080.webm")
# with open("Gamers-OP1-NCBD1080.webm", "wb") as wf:
#     for chunk in r.iter_content():
#         if chunk:
#             wf.write(chunk)


