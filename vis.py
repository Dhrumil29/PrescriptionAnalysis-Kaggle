import numpy
import json
import csv
import collections
import operator
import codecs
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
# import matplotlib.axes.Axes as axis
import numpy as np
import matplotlib.pyplot as plt
#
# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]


def generate_visualization():
    experience_data=collections.defaultdict(dict)
    pkmn_type_colors = ['#78C850',  # Grass
                        '#F08030',  # Fire
                        '#6890F0',  # Water
                        '#A8B820',  # Bug
                        '#A8A878',  # Normal
                        '#A040A0',  # Poison
                        '#F8D030',  # Electric
                        '#E0C068',  # Ground
                        '#EE99AC',  # Fairy
                        '#C03028',  # Fighting
                        '#F85888',  # Psychic
                        '#B8A038',  # Rock
                        '#705898',  # Ghost
                        '#98D8D8',  # Ice
                        '#7038F8',  # Dragon,
                        '#1A1D1E',
                        '#4B4A4C'
                        ]
    with open("abc.jsonl") as f:
        for line in f:
            j_content = json.loads(line)
            speciality=j_content.get('provider_variables').get('specialty')
            if speciality.find("General Practice"):
                years_of_practicing = j_content.get('provider_variables').get('years_of_practicing')
                # experience_data['years_of_practicing']=years_of_practicing
                if years_of_practicing not in experience_data.keys():
                    experience_data[years_of_practicing]=1
                else:
                    experience_data[years_of_practicing]+=1
    x=list(experience_data.keys())
    print(x)
    print(type(x))
    y_pos= x.__len__()
    print(y_pos)
    y=[]
    for p in x:
        y.append(int(experience_data[p]))
    print(y)
    # plt.bar(y_pos, y, align='center', alpha=0.5)
    # plt.xticks(y_pos, x)
    # plt.ylabel('Usage')
    # plt.title('Programming language usage')
    #
    # plt.show()
    x=['General Practice','Neurology','Medical','']
    ax=sns.barplot(x=x,y=y,orient="v",saturation=0.8)
    ax.set(xlabel='Experience in years', ylabel='Number of General Practice Doctors')
    # ax.savefig("output.png")
    sns.plt.savefig("output5.png")
    sns.plt.show()
    # sns.save
    # vis_data=pd.DataFrame(list(experience_data.items()), columns=['year','value'])
    # sns.countplot(x=vis_data['year'],data=vis_data, palette=pkmn_type_colors)
    # sns.jointplot(x='year', y='value', data=experience_data)
    # Rotate x-labels
    # plt.xticks(rotation=-45)

    return
# read_medicine_median_from_csv()
generate_visualization()