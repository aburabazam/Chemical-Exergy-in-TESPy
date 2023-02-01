import plotly.graph_objects as go
from plotly.offline import plot

links = {'source': [0, 1, 1, 1, 14, 14, 14, 3, 3, 4, 4, 4, 5, 5, 7, 7, 7, 9, 9, 9, 10, 10, 10, 11, 11, 11],
         'target': [1, 5, 5, 3, 3, 16, 9, 18, 4, 18, 5, 10, 18, 7, 14, 18, 4, 18, 11, 17, 18, 9, 11, 18, 10, 14],
         'value': [85195128.52053699, 84610563.2928355, 624155.518258245, -39590.290538220426, 29695495.427327663, 42753646.46216907,
                   61619.41918133848, 2101222.023175236, 27554683.11361421, 2557498.70672952, 41238174.873131804,
                   22123939.23688353, 25417458.062753588, 101055435.62145343, 59695495.42732767, 2995010.4909951165,
                   38364929.70313065, 1915952.0600772942, 2247562.915332827, 2853754.7228096835, 4591419.821871854,
                   6955650.2790384665, 15973398.851422915, 9166.16995562613, 5396529.715449708, 12815265.88135041],
         'color': ['rgba(228.0, 26.0, 28.0, 0.75)', 'rgba(9, 48, 5, 0.8)', 'rgba(235, 115, 9, 0.8)', 'rgba(153.0, 153.0, 153.0, 0.75)',
                   'rgba(228.0, 26.0, 28.0, 0.75)', 'rgba(228.0, 26.0, 28.0, 0.75)', 'rgba(255.0, 255.0, 51.0, 0.75)',
                   'rgba(55.0, 126.0, 184.0, 0.75)', 'rgba(235, 115, 9, 0.8)', 'rgba(55.0, 126.0, 184.0, 0.75)',
                   'rgba(153.0, 153.0, 153.0, 0.75)', 'rgba(153.0, 153.0, 153.0, 0.75)', 'rgba(55.0, 126.0, 184.0, 0.75)',
                   'rgba(153.0, 153.0, 153.0, 0.75)', 'rgba(228.0, 26.0, 28.0, 0.75)', 'rgba(55.0, 126.0, 184.0, 0.75)',
                   'rgba(153.0, 153.0, 153.0, 0.75)', 'rgba(55.0, 126.0, 184.0, 0.75)', 'rgba(255.0, 255.0, 51.0, 0.75)',
                   'rgba(77.0, 175.0, 74.0, 0.75)', 'rgba(55.0, 126.0, 184.0, 0.75)', 'rgba(153.0, 153.0, 153.0, 0.75)',
                   'rgba(255.0, 255.0, 51.0, 0.75)', 'rgba(55.0, 126.0, 184.0, 0.75)', 'rgba(255.0, 255.0, 51.0, 0.75)',
                   'rgba(228.0, 26.0, 28.0, 0.75)']}

nodes = ['E_F', 'Fuel_Bus', 'methane', 'compressor', 'air preheater', 'combustion chamber', 'ambient air',
         'gas turbine', 'chimney', 'economizer', 'evaporator', 'drum', 'feed water', 'live steam', 'Product_Bus',
         'Loss_Bus', 'E_P', 'E_L', 'E_D']

fig = go.Figure(go.Sankey(
     arrangement="snap",
     node={
         "label": nodes,
         'pad': 11,
         'color': 'orange'},
     link=links))
plot(fig, filename='CGAM_sankey_example.html')