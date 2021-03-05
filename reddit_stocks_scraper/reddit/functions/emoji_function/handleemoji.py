from emoji import emojize
import emojis


def get_all_emojis():
	emotes_tuple = emojis.db.get_emoji_aliases().values()
	emotes = list(emotes_tuple)
	return emotes


