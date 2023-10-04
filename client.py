from pyclarify import APIClient
from pyclarify import DataFrame
from datetime import datetime

client = APIClient(credentials=open("maqtt.json"))

t1 = datetime.now()
t2 = t1 + datetime.timedelta(hours=1)
df = DataFrame(
    times=[t1, t2],
    series={
        "a": [1.0, 1.2],
        "b": [2.0, None],
    },
)

client.insert(df)