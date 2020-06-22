import instaloader
import pandas as pd
import numpy as np

L = instaloader.Instaloader(download_pictures=False,
                            download_video_thumbnails=False,
                            download_videos=False,
                            download_geotags=True,
                            download_comments=False,
                            save_metadata=False)

def get_it(nameOfExercise):
    # Get instance
    numbers_of_loop = 1000
    while numbers_of_loop > 0:
        for post in L.get_hashtag_posts(nameOfExercise):
            # post is an instance of instaloader.Post
            L.download_post(post, target='#'+nameOfExercise)
            numbers_of_loop-=1
            # print(numbers_of_loop)
            if numbers_of_loop ==0:
                break
        print("loop ended for " + nameOfExercise)

df = pd.read_csv("./word2vec_wrangling.csv")
kinds_of_exercise = df["exercise_name"].to_list()
print(len(kinds_of_exercise))

for item in kinds_of_exercise:
    get_it(item)
