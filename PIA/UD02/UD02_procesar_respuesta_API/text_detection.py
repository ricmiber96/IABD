import json

import pandas as pd

with open(
    "C:/Users/ESP/Desktop/PIA/U02/Practicas/procesar_respuesta_API/textdetections.json5",
    "r",
) as file:
    data = json.load(file)

elements_dic = []
elements_df = pd.DataFrame({})

for line in data["TextDetections"]:
    if "ParentId" in line:
        element = {
            "DetectedText": line["DetectedText"],
            "Confidence": line["Confidence"],
            "Type": line["Type"],
            "ParentId": line["ParentId"],
            "Top": line["Geometry"]["BoundingBox"]["Top"],
        }
        elements_dic.append(element)

elements_df = pd.DataFrame(elements_dic)
elements_df_grouped = (
    elements_df.groupby("ParentId")
    .agg(
        {
            "DetectedText": " ".join,
            "Confidence": "mean",
            "Type": "first",
            "Top": "mean",
        }
    )
    .reset_index()
)

elements_df_sorted = elements_df_grouped.sort_values(by=["Top"])
text_array = elements_df_sorted["DetectedText"].tolist()
text_output = " ".join(text_array)

for index, row in elements_df_sorted.iterrows():
    print(
        f"Linea {index+1}: {row['DetectedText']} (Confianza: {round(row['Confidence'],2)}%)"
    )

print(f"Texto completo detectado: {text_output}")
