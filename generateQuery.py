import json

userList = ['adagar']





def transformer(user):
	return {
		"match_phrase": {
			"user_display_name": user
		}
	}

print json.dumps(map(transformer, userList))
