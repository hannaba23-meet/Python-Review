

def create_youtube_video(title,descreption):
	vid1={"t":"title","d":"descreption","likes":0,"dislikes":0,"comments":{}}
	return vid1
def like(vid1):
	if "likes" in vid1:
		likes += 1
	return vid1

def dislike(vid1):
	if "dislikes" in vid1:
		dislikes += 1
	return vid1
def add_comment(vid1,username,comment_text):
	comments[username] = comment_text
	return comments
