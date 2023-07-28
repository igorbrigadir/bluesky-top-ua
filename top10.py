import requests
import pandas as pd

data = requests.get("https://s3.jazco.io/exported_graph_minified.json").json()

ua_community_id = int(
    [
        key
        for key, value in data["attributes"]["clusters"].items()
        if "label" in value and value["label"] == "Ukrainian Cluster"
    ][0]
)

ua_df = pd.DataFrame(
    [
        d["attributes"]
        for d in data["nodes"]
        if d["attributes"]["community"] == ua_community_id
    ]
).sort_values(by="size", ascending=False)

ua_df.head(10)[["label", "size"]].to_csv("top10.csv", index=False)
ua_df.head(100)[["label", "size"]].to_csv("top100.csv", index=False)
