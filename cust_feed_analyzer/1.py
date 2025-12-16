import pandas as pd
import numpy as np
rate=int(input("entera number between 1 and 5 that you want to rate us:"))
feedback=input("please provide your feedback about our service:")
feedbacked=feedback.lower().split()
if rate>=1 and rate<=5:
    print("thank you for your rating")
else:
    print("invalid rating")
import pandas as pd

data = {
    "word": [
        "good", "great", "excellent", "amazing", "awesome", "fast", "smooth", "easy",
        "bad", "terrible", "poor", "slow", "buggy", "crash", "confusing", "laggy",
        "love", "like", "satisfied", "happy", "useful", "helpful",
        "hate", "dislike", "annoying", "frustrating", "worst", "broken",
        "okay", "fine", "average", "normal", "acceptable",
        "delay", "issue", "problem", "error", "fail",
        "improve", "update", "feature", "request", "add"
    ],
    "sentiment_point": [
        0.6, 0.8, 0.9, 0.85, 0.8, 0.5, 0.6, 0.4,
        -0.6, -0.9, -0.7, -0.6, -0.8, -0.9, -0.7, -0.6,
        0.8, 0.5, 0.6, 0.7, 0.5, 0.6,
        -0.8, -0.6, -0.7, -0.8, -0.9, -0.85,
        0.0, 0.1, 0.0, 0.0, 0.2,
        -0.5, -0.4, -0.6, -0.7, -0.8,
        0.3, 0.2, 0.1, 0.0, 0.1
    ]
}

df = pd.DataFrame(data)
total = 0
points = 0
count=0
while len(feedbacked) >0:
    for word in feedbacked:
        if word in df["word"].values:
            points+=df.loc[df["word"]==word,"sentiment_point"].values[0]
            count+=1
            feedbacked.pop()
        else:    
            feedbacked.pop()
total=points/count
total_score=total+rate
percentage=(total_score/10)*100
print(f"percentage score: {percentage}%")
if total_score>=3:
    print("overall sentiment: positive")
elif total_score==2:
    print("overall sentiment: neutral")
else:
    print("overall sentiment: negative")




