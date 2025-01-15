import json

import matplotlib.pyplot as plt

with open("facedetails.json5", "r") as file:
    data = json.load(file)


for element in data["FaceDetails"]:
    if element["AgeRange"]:
        min_age = element["AgeRange"]["Low"]
        max_age = element["AgeRange"]["High"]
        print(f"La edad minima estimada es: {min_age} y maxima {max_age}")

    if element["Eyeglasses"]["Value"] == True:
        eyeglasses_conf = element["Eyeglasses"]["Confidence"]
        print(
            f'Si lleva gafas con una confianza del {"{:.2f}".format(eyeglasses_conf)} %'
        )

    if element["Sunglasses"]["Value"] == True:
        sunglasses_conf = element["Sunglasses"]["Confidence"]
        print(
            f'Las gafas que lleva son de sol con un acierto del {"{:.2f}".format(sunglasses_conf)} %'
        )
    if element["Gender"]:
        gender = element["Gender"]["Value"]
        gender_conf = element["Gender"]["Confidence"]
        print(
            f'Su genero es {gender} con un porcentaje de acierto del {"{:.2f}".format(gender_conf)} %'
        )

    emotion_min = element["Emotions"][0]["Type"]
    emotion_min_conf = element["Emotions"][0]["Confidence"]
    emotion_max = element["Emotions"][0]["Type"]
    emotion_max_conf = element["Emotions"][0]["Confidence"]

    for emotion in element["Emotions"]:
        if emotion["Confidence"] < emotion_min_conf:
            emotion_min = emotion["Type"]
            emotion_min_conf = emotion["Confidence"]
        elif emotion["Confidence"] > emotion_max_conf:
            emotion_max = emotion["Type"]
            emotion_max_conf = emotion["Confidence"]

    print(
        f"La emocion con nivel mas bajo es: {emotion_min} con un {"{:.2f}".format(emotion_min_conf)} %"
    )
    print(
        f"La emocion con nivel mas alto es: {emotion_max} con un {"{:.2f}".format(emotion_max_conf)} %"
    )

    emotions_array = []
    emotions_array_conf = []

    for emotion in element["Emotions"]:
        emotions_array.append(emotion["Type"])
        emotions_array_conf.append(emotion["Confidence"])

    x = emotions_array
    y = emotions_array_conf

    plt.bar(x, y)
    plt.ylim(0, 100)
    plt.show()

    landmark_array_label = []
    landmarks_array_x = []
    landmarks_array_y = []

    for mark in element["Landmarks"]:
        landmark_name = mark["Type"]
        landmark_x = mark["X"]
        landmark_y = mark["Y"]
        landmark_array_label.append(landmark_name)
        landmarks_array_x.append(landmark_x)
        landmarks_array_y.append(landmark_y)

    for i, label in enumerate(landmark_array_label):
        plt.text(landmarks_array_x[i], landmarks_array_y[i], label, fontsize=8, ha='right', va='bottom')
        
    plt.title("Landmarks")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(landmarks_array_x, landmarks_array_y)
    plt.show()


