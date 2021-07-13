import numpy as np
import plotly.express as px
import plotly.io as pio
import pandas as pd

pio.kaleido.scope.default_width = 700 * 2
pio.kaleido.scope.default_height = 500 * 2

df = pd.read_csv("./speedup.csv")
df["best"] = df["best"] * 1e-9

fig = px.bar(
    df,
    title="Best Execution Times Per Parallelism Model",
    x="model",
    y="best",
    labels={"model": "Parallelism Platform Model", "best": "Best Execution Time (seconds)"},
    # range_x=[1, 20],
    # range_y=[0, 50],
    # facet_row_spacing=0.1
)
fig.update_layout(font_size=22)
# fig.update_xaxes(tickvals=np.arange(1, 21, 1))
fig.write_image("./benchmark.png")