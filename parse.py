import re
import pandas as pd

# Paste your entire evaluation output here as a raw multiline string
raw_output = """
[
                   all       3798       4444      0.466       0.43      0.379      0.237
      rice leaf roller       3798         39       0.37      0.769       0.61       0.42
 rice leaf caterpillar       3798         26     0.0549     0.0385     0.0928     0.0545
     paddy stem maggot       3798          5          1          0     0.0476     0.0277
    asiatic rice borer       3798         34      0.188      0.471      0.216      0.139
     yellow rice borer       3798         16      0.311      0.562      0.444      0.272
       rice gall midge       3798         19      0.369       0.77      0.711      0.302
          Rice Stemfly       3798          6          1          0       0.13     0.0889
    brown plant hopper       3798         22      0.279      0.353      0.225      0.109
white backed plant hopper       3798         16      0.299      0.625      0.359      0.234
small brown plant hopper       3798         12      0.117      0.167      0.112       0.05
     rice water weevil       3798         30      0.311        0.9      0.463      0.322
       rice leafhopper       3798         23      0.256      0.348      0.341      0.231
 grain spreader thrips       3798          4          1          0      0.191      0.119
       rice shell pest       3798          7          1          0     0.0701     0.0388
                  grub       3798        118      0.706      0.975      0.879      0.517
          mole cricket       3798        176      0.904      0.955      0.979      0.547
              wireworm       3798        109      0.579      0.826      0.735      0.491
   white margined moth       3798         13      0.193     0.0769      0.191      0.152
         black cutworm       3798         67      0.326      0.701      0.407      0.304
         large cutworm       3798         40      0.165        0.3      0.172      0.137
        yellow cutworm       3798         43      0.181      0.395      0.171      0.133
            red spider       3798         37      0.368      0.703      0.487      0.363
            corn borer       3798         90      0.401      0.778       0.61       0.41
             army worm       3798         41      0.234      0.366      0.196      0.128
                aphids       3798        282      0.422      0.816      0.568      0.313
   Potosiabre vitarsis       3798         47      0.727      0.872      0.863      0.639
           peach borer       3798         50      0.643        0.7      0.741      0.513
   english grain aphid       3798         60      0.211        0.2      0.169      0.087
             green bug       3798         12          1          0      0.038     0.0201
  bird cherry-oataphid       3798         28          0          0     0.0341     0.0193
   wheat blossom midge       3798          6          0          0      0.159     0.0659
      penthaleus major       3798         14      0.596      0.528      0.585        0.3
longlegged spider mite       3798         15      0.374      0.133      0.248      0.122
    wheat phloeothrips       3798         22      0.308      0.636      0.445      0.285
          wheat sawfly       3798         29      0.369      0.138      0.285      0.162
 cerodonta denticornis       3798          5          1          0      0.107      0.067
              beet fly       3798          7          1          0      0.378      0.249
           flea beetle       3798         74      0.608      0.838      0.808      0.442
     cabbage army worm       3798         56      0.187      0.304      0.198      0.135
        beet army worm       3798         83      0.351       0.47      0.413        0.3
       Beet spot flies       3798         14      0.343      0.225      0.471      0.312
           meadow moth       3798         20      0.337        0.4        0.4      0.275
           beet weevil       3798         31      0.238      0.613      0.341        0.2
sericaorient alismots chulsky       3798         18      0.356      0.667      0.619      0.468
        alfalfa weevil       3798         19      0.111      0.211      0.136     0.0838
          flax budworm       3798         85      0.184      0.118       0.16      0.114
     alfalfa plant bug       3798         46      0.225      0.217      0.175     0.0889
   tarnished plant bug       3798         71      0.388      0.648      0.561      0.331
           Locustoidea       3798        109      0.395      0.587      0.475      0.273
          lytta polita       3798         51      0.255      0.137       0.22      0.109
 legume blister beetle       3798         96      0.519      0.771      0.632      0.302
        blister beetle       3798        198      0.587      0.783      0.742      0.394
therioaphis maculata Buckton       3798          3          0          0          0          0
     odontothrips loti       3798         13       0.23      0.692      0.395      0.157
                Thrips       3798          9      0.269      0.572      0.319      0.216
  alfalfa seed chalcid       3798          4          1          0     0.0804     0.0404
        Pieris canidia       3798         11      0.193      0.273      0.191     0.0913
      Apolygus lucorum       3798          7          1          0      0.137     0.0404
           Limacodidae       3798         47          0          0     0.0734     0.0282
   oides decempunctata       3798         35      0.616      0.943      0.893      0.426
Pseudococcus comstocki Kuwana       3798         13      0.222      0.692      0.297      0.177
    parathrene regalis       3798          6      0.315      0.167      0.299      0.166
           Ampelophaga       3798         56      0.811      0.946      0.939      0.761
    Lycorma delicatula       3798         68       0.94      0.985      0.992       0.69
           Xylotrechus       3798         31       0.64      0.861      0.725      0.521
     Cicadella viridis       3798         41      0.526      0.854      0.782      0.488
               Miridae       3798        254      0.583      0.772      0.741      0.421
Trialeurodes vaporariorum       3798         23      0.297      0.609      0.332      0.262
 Erythroneura apicalis       3798          2          1          0          0          0
        Papilio xuthus       3798         22      0.328      0.909      0.512      0.285
Panonchus citri McGregor       3798         14      0.435      0.115      0.283       0.16
Icerya purchasi Maskell       3798         59      0.405       0.78      0.649      0.341
    Unaspis yanonensis       3798        102      0.144      0.931      0.647       0.24
    Ceroplastes rubens       3798         85      0.281      0.694      0.558      0.236
 Chrysomphalus aonidum       3798         39      0.102      0.231      0.113     0.0513
  Nipaecoccus vastalor       3798         12     0.0746      0.167      0.125     0.0696
Aleurocanthus spiniferus       3798         27      0.188      0.778      0.412      0.199
Tetradacus c Bactrocera minax       3798         13      0.192      0.385      0.317      0.236
Dacus dorsalis(Hendel)       3798         26      0.431      0.654      0.569      0.428
  Bactrocera tsuneonis       3798          6     0.0488     0.0733      0.105     0.0473
       Prodenia litura       3798         85      0.409       0.66      0.475      0.292
         Adristyrannus       3798         27      0.708       0.63      0.735      0.535
Phyllocnistis citrella Stainton       3798          5          1          0      0.107      0.093
  Toxoptera citricidus       3798          5          1          0     0.0133    0.00663
    Toxoptera aurantii       3798          4          1          0     0.0715     0.0344
Aphis citricola Vander Goot       3798          1          1          0          0          0
Scirtothrips dorsalis Hood       3798         15      0.105      0.133      0.122     0.0802
          Dasineura sp       3798          5          1          0     0.0368     0.0235
Lawana imitata Melichar       3798         29      0.415      0.828       0.75      0.545
Salurnis marginella Guerr       3798         37       0.53      0.757      0.717      0.547
Deporaus marginatus Pascoe       3798         13      0.423     0.0769      0.297       0.18
  Chlumetia transversa       3798         12          1          0     0.0595     0.0435
Mango flat beak leafhopper       3798          3          1          0    0.00622    0.00485
Rhytidodera bowrinii white       3798         29      0.414      0.621      0.509      0.398
 Sternochetus frigidus       3798         12      0.299      0.417      0.253      0.177
          Cicadellidae       3798        593      0.849      0.956      0.957       0.72]
"""

# Regular expression to extract: class name + precision + recall + mAP50 + mAP50-95
pattern = re.compile(
    r"^\s*(.+?)\s+\d+\s+\d+\s+([\d.]+|0)\s+([\d.]+|0)\s+([\d.]+|0)\s+([\d.]+|0)\s*$", re.MULTILINE
)

results = []
for match in pattern.finditer(raw_output):
    cls, precision, recall, map50, map5095 = match.groups()
    precision = float(precision)
    recall = float(recall)
    f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) != 0 else 0
    results.append({
        "Class": cls.strip(),
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1_score,
        "mAP50": float(map50),
        "mAP50-95": float(map5095)
    })

# Create a DataFrame
df = pd.DataFrame(results)

# Sort by F1-Score or mAP50-95 if you prefer
df_sorted = df.sort_values(by="F1-Score", ascending=False)

# Save to CSV
df_sorted.to_csv("classwise_accuracy_report.csv", index=False)

# Show top 10 performing classes
print(df_sorted.head(10))
