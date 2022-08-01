# 1. There is string s = "Python Bootcamp".
# Write the code that hashes string.

s = "Python Bootcamp"
hashed_s = hash(s)
print(hashed_s)

# 2. You are working on a project
# for TikTok. The future project will be a web-site of all public GIF images.
# You need to write a function that converts TikTok video to GIF.
# The input parameter is url address of TikTok video, i.e."TikTok example".
# The output parameter is path to GIF image, i.e."/home/user/TikTok-example-1.gif".

def videoToGIF(url):
    return f"/home/user/{url.replace(' ', '-')}-1.gif"

some_video = "TikTok example"
print(videoToGIF(some_video))
