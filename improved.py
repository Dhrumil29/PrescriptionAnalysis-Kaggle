import numpy
import json
import csv
import collections
import operator
import codecs
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from textwrap import wrap

import matplotlib.pyplot as plt; plt.rcdefaults()
cool_colors = ['#78C850',  # Grass
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
region=[]
list_of_specialities=[]
medicines_array = []
spec_patient_analysis = collections.defaultdict(dict)
one_medicine = collections.defaultdict(dict)
freq_data=collections.defaultdict(dict)
analyzed_data=collections.defaultdict(dict)
medicine_array=collections.defaultdict(dict)
speciality_region_data=collections.defaultdict(dict)
speciality_settlement_type_data=collections.defaultdict(dict)
speciality_gender_data=collections.defaultdict(dict)
medicine_median=collections.defaultdict(dict)
medicine_region_data=collections.defaultdict(dict)
output_data = collections.defaultdict(dict)
def generate_medicine_region_data(region,medicine):
    if region in medicine_region_data[medicine].keys():
        medicine_region_data[medicine][region]+=1
    else:
        medicine_region_data[medicine][region]=1
    return
def create_speciality_data(region,settlement_type,gender,speciality):
    if region in speciality_region_data[speciality].keys():
        speciality_region_data[speciality][region]+=1
    else:
        speciality_region_data[speciality][region]=1
    if settlement_type in speciality_settlement_type_data[speciality].keys():
        speciality_settlement_type_data[speciality][settlement_type] += 1
    else:
        speciality_settlement_type_data[speciality][settlement_type] = 1
    if gender in speciality_gender_data[speciality].keys():
        speciality_gender_data[speciality][gender]+=1
    else:
        speciality_gender_data[speciality][gender]=1
    return
def write_gender_data_as_csv(speciality_gender_data):
    with open('speciality_gender_data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["speciality","Male","Female"])
        for key, value in speciality_gender_data.items():
            if 'M' in speciality_gender_data[key].keys():
                male = speciality_gender_data[key]["M"]
            else:
                male=0
            if 'F' in speciality_gender_data[key].keys():
                female = speciality_gender_data[key]["F"]
            else:
                female=0
            key=key.encode("utf-8")
            writer.writerow([key,male,female])
    return
def write_medicine_region_data_as_csv(medicine_region_data):
    with open('medicine_region_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["speciality", "South", "Midwest", "West", "Northeast"])
        for key, value in medicine_region_data.items():
            if 'South' in medicine_region_data[key].keys():
                south = medicine_region_data[key]["South"]
            else:
                south = 0
            if 'Midwest' in medicine_region_data[key].keys():
                Midwest = medicine_region_data[key]["Midwest"]
            else:
                Midwest = 0
            if 'West' in medicine_region_data[key].keys():
                West = medicine_region_data[key]["West"]
            else:
                West = 0
            if 'Northeast' in medicine_region_data[key].keys():
                Northeast = medicine_region_data[key]["Northeast"]
            else:
                 Northeast = 0
            key = key.encode("utf-8")
            # print(key, south, Midwest, West, Northeast)
            writer.writerow([key, south, Midwest, West, Northeast])
    return
def write_region_data_as_csv(speciality_region_data):
    with open('speciality_region_data.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(["speciality","South", "Midwest", "West", "Northeast"])
        for key, value in speciality_region_data.items():
            if 'South' in speciality_region_data[key].keys():
                south = speciality_region_data[key]["South"]
            else:
                south = 0
            if 'Midwest' in speciality_region_data[key].keys():
                Midwest = speciality_region_data[key]["Midwest"]
            else:
                Midwest = 0
            if 'West' in speciality_region_data[key].keys():
                West = speciality_region_data[key]["West"]
            else:
                West = 0
            if 'Northeast' in speciality_region_data[key].keys():
                Northeast = speciality_region_data[key]["Northeast"]
            else:
                Northeast = 0
            key = key.encode("utf-8")
            print(key,south,Midwest,West,Northeast)
            writer.writerow([key,south,Midwest,West,Northeast])
    return
def write_settlement_data_as_csv(speciality_settlement_type_data):
    with open('speciality_settlement_type_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["speciality", "Urban","Non-Urban"])
        for key, value in speciality_settlement_type_data.items():
            if 'non-urban' in speciality_settlement_type_data[key].keys():
                nonUrban=speciality_settlement_type_data[key]["non-urban"]
            else:
                nonUrban = 0
            if 'urban' in speciality_settlement_type_data[key].keys():
                urban = speciality_settlement_type_data[key]['urban']
            else:
                urban = 0
            key=key.encode("utf-8")
            print(key,nonUrban,urban)
            writer.writerow([key,nonUrban,urban])
    return
def write_medicine_median_as_csv(medicine_median):
    with open("medicine_median.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(["medicine","median"])
        for key,value in medicine_median.items():
            writer.writerow([key,value])
    return
def write_medicine_speciality_probability_as_csv(analyzed_data):
    with open("medicine_speciality_probability.csv",'w') as f:
        writer = csv.writer(f)
        arr=[]
        arr.append("medicine")
        arr.append(list_of_specialities)
        writer.writerow(arr)
        arr=[]
        for key,value in analyzed_data.items():
            arr=[]
            arr.append(key)
            for i in list_of_specialities:
                if i in analyzed_data[medicines].keys():
                    arr.append(analyzed_data[medicines][i])
                else:
                    arr.append(0)
            writer.writerow(arr)
    print("Lakhai Gayu")
    return

def generate_medicine_median(medicine,value):
    if medicine in medicine_array.keys():
        medicine_array[medicine].append(value)
        array=medicine_array[medicine]
        median=numpy.median(array)
    else:
        arr=[]
        arr.append(value)
        medicine_array[medicine]=arr
        median=value
        # print(medicine_median)
    medicine_median[medicine] = median

    # if speciality in value_data[medicine].keys():
    #     value_data[medicine][speciality].append(value)
    #     medicine_array=value_data[medicine][speciality]
    #     medicine_speciality_median = numpy.median(medicine_array)
    # else:
    #     arr=[]
    #     arr.append(value)
    #     value_data[medicine][speciality] = arr
    #     medicine_speciality_median=arr[0]
    # change_median(medicine,speciality,medicine_speciality_median)
    return
def insert_into_analysis(medicine,speciality,years_of_practicing,value,region):
    frequencies = "frequencies"
    _region_ = "region"
    _mean_ = "mean"
    _experience_ = "experience"
    total = "total"

    if _region_ not in analyzed_data[medicine].keys():
        analyzed_data[medicine][_region_]=collections.defaultdict(dict)
        analyzed_data[medicine][_region_][region]=1
    else:
        if region in analyzed_data[medicine][_region_].keys():
            analyzed_data[medicine][_region_][region] += 1
        else:
            analyzed_data[medicine][_region_][region] = 1
    if frequencies not in analyzed_data[medicine].keys():
        analyzed_data[medicine][frequencies]=collections.defaultdict(dict)
        analyzed_data[medicine][frequencies][speciality] = 1
        analyzed_data[medicine][frequencies][total]=1
    else:
        analyzed_data[medicine][frequencies][total]+=1
        if speciality in analyzed_data[medicine][frequencies].keys():
            analyzed_data[medicine][frequencies][speciality]+=1
        else:
            analyzed_data[medicine][frequencies][speciality]=1

    if _mean_ not in analyzed_data[medicine].keys():
        analyzed_data[medicine][_mean_] = collections.defaultdict(dict)
        analyzed_data[medicine][_mean_][speciality] = value
    else:
        if speciality in analyzed_data[medicine][_mean_].keys():
            p = analyzed_data[medicine][_mean_][speciality]* (analyzed_data[medicine][frequencies][speciality]-1)
            p = p + value
            p = p / analyzed_data[medicine][frequencies][speciality]
            analyzed_data[medicine][_mean_][speciality]= p
        else:
            analyzed_data[medicine][_mean_][speciality] = value

    if _experience_ not in analyzed_data[medicine].keys():
        analyzed_data[medicine][_experience_] = collections.defaultdict(dict)
        analyzed_data[medicine][_experience_][speciality] = years_of_practicing
        analyzed_data[medicine][_experience_][_mean_]=years_of_practicing
    else:
        analyzed_data[medicine][_experience_][_mean_]= analyzed_data[medicine][_experience_][_mean_]*(analyzed_data[medicine][frequencies][total]-1)
        analyzed_data[medicine][_experience_][_mean_]=analyzed_data[medicine][_experience_][_mean_]+ years_of_practicing
        analyzed_data[medicine][_experience_][_mean_] = analyzed_data[medicine][_experience_][_mean_]/analyzed_data[medicine][frequencies][total]
        if speciality in analyzed_data[medicine][_experience_].keys():
            temp = analyzed_data[medicine][_experience_][speciality] * (analyzed_data[medicine][frequencies][speciality] - 1)
            temp = temp + years_of_practicing
            temp = temp / analyzed_data[medicine][frequencies][speciality]
            analyzed_data[medicine][_experience_][speciality] = temp
        else:
            analyzed_data[medicine][_experience_][speciality] = years_of_practicing

    return
def read_spec_patient_from_csv(speciality,region):
    print(speciality)
    print(region)
    with open('spec.csv') as f:
        reader=csv.DictReader(f,delimiter=',')
        for line in reader:
            # print(line["Specialty"])
            if speciality in line["Specialty"]:
                patients="Patients in "+region
                doctors="Doctors in "+region
                ratio ="Actual P/D ratio in "+region
                recommended_ratio="recommended P/D value"
                print("Patients in "+region+":  "+line[patients])
                print("Doctors in "+region+":   "+line[doctors])
                print("Actual P/D ratio in"+region+":    "+line[ratio])
                print("Recommended P/D value:    "+line[recommended_ratio])
                print(line[ratio])
                print(line[recommended_ratio])
                if int(line[recommended_ratio]) > int(line[ratio]):
                    print("There are sufficient doctors")
                else:
                    print()
                    print()
                    print("There has to be more doctors as patients are more")
                    print("Possible solutions:")
                    print("1:Transfer doctors from one region to another")
                    print("2:Improve Medical Infrastructure of that region")
                    print("3:Promote similar courses in medical colleges")
                    print()
                    print()
                    print()
                break
def read_medicine_median_from_csv():
    with open('medicine_median.csv') as f:
        reader=csv.DictReader(f, delimiter=',')
        for line in reader:
            medicine_median[line["medicine"]] = line["median"]
    # print(medicine_median)
    return
def generate_probability(analyzed_data):

    for key,value in analyzed_data.items():
        total = 0
        for ky,val in value.items():
            total = total + val
        for ky,val in value.items():
            analyzed_data[key][ky]=analyzed_data[key][ky]/total
    return
def generate_visualize_output(one_medicine, x, output_data):
    sss=x
    print(one_medicine)
    print(type(x),x)
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    if sss ==1:
        output_data = one_medicine
    else:
        odk = output_data.keys()
        odv = output_data.values()
        p=[]
        odk = ['\n'.join(wrap(l, 20)) for l in odk]
        order = collections.OrderedDict(sorted(output_data.items(), key=lambda t: t[1], reverse=True)[:6])
        print(order)
        order = collections.OrderedDict(sorted(order.items(), key=lambda t: t[0]))
        for x in order:
            p.append(float(output_data[x]))
        prob_show = ['\n'.join(wrap(l, 20)) for l in order]
        prescription = ""
        i = 0
        for medicine in medicines_array:
            if i < len(medicines_array) - 1:
                if prescription == "":
                    prescription += medicines_array[i]
                else:
                    prescription += "," + medicines_array[i]
            i = i + 1
        ax2.barh(np.arange(len(order)), p, align='center', color=cool_colors)
        ax2.set_yticks(np.arange(len(order)))
        ax2.set_yticklabels(prob_show)
        ax2.set_title(prescription)

        for p in output_data.keys():
                if p in one_medicine.keys():
                    temp = float(output_data[p]) * (sss-1)
                    temp += one_medicine[p]
                    temp = temp/sss
                    output_data[p] = temp
                else:
                    temp = float(output_data[p]) * (sss - 1)
                    temp = temp / sss
                    output_data[p] = temp
        for p in one_medicine.keys():
            if p not in output_data.keys():
                output_data[p] = one_medicine[p]/sss
    odk = output_data.keys()
    odv = output_data.values()
    odk = ['\n'.join(wrap(l, 20)) for l in odk]
    # odk = ['\n'.join(wrap(l, 20)) for l in odk]
    order = collections.OrderedDict(sorted(output_data.items(), key=lambda t: t[1], reverse=True)[:6])
    print(order)
    order = collections.OrderedDict(sorted(order.items(), key=lambda t: t[0]))
    p=[]
    for x in order:
        p.append(float(output_data[x]))
    prob_spec = ['\n'.join(wrap(l, 20)) for l in order]
    ax1.barh(np.arange(len(order)), p, align='center', color=cool_colors)
    # ax1.barh(np.arange(len(odk)), odv, align='center', color=cool_colors)
    ax1.set_yticks(np.arange(len(order)))
    ax1.set_yticklabels(prob_spec)

    prescription=""
    i=0
    for medicine in medicines_array:
        if prescription=="":
           prescription+=medicines_array[i]
        else:
            prescription +=","+medicines_array[i]
        i=i+1
    print(prescription)
    ax1.set_title(prescription)
    predicted_field = max(output_data.items(), key=operator.itemgetter(1))[0]
    probability=max(output_data.items(), key=operator.itemgetter(1))[1]
    print(predicted_field)
    print(probability)
    sns.plt.savefig("output101.png")
    sns.plt.show()
    return output_data
def suggest_doctors(spec):
    print(spec)
    with open("abc.jsonl") as f:
        x=0
        for line in f:
            # print(x)

                j_content = json.loads(line)
                speciality = j_content.get('provider_variables').get('specialty')
                region = j_content.get('provider_variables').get('region')
                settlement_type = j_content.get('provider_variables').get('settlement_type')
                years_of_practicing = j_content.get('provider_variables').get('years_practicing')
                gender=j_content.get('provider_variables').get('gender')
                # print(speciality)
                # print(spec)
                npi= j_content.get('npi')
                # print(npi)
                if speciality == spec:
                    x = x + 1
                    print("npi: ",npi,"  region:  ",region," settlement_type: ",settlement_type," experience: ",years_of_practicing,"gender: ",gender)
                if x > 10:
                    break

def generate_graphs(medicine,x,output_data):
    medicines_array.append(medicine)
    temp =x
    # medicine_array.append(medicine)
    # print(analyzed_data)
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    freq_data = analyzed_data[medicine]["frequencies"]
    total_freq = analyzed_data[medicine]["frequencies"]["total"]
    every_speciality = freq_data.keys()
    max_freq = max(freq_data.items(), key=operator.itemgetter(1))[1]
    mean = analyzed_data[medicine]["mean"]
    max_mean = max(mean.items(), key=operator.itemgetter(1))[1]
    max_difference = max_mean - float(medicine_median[medicine])
    # print( type(analyzed_data[medicine]["mean"][every_speciality[0]]))
    print(type(medicine_median[medicine]))
    print(every_speciality)
    total = 0
    one_medicine={}
    for x in every_speciality:
        if "total" not in x:
            if max_freq > 5 :
                freq_weight = 1+ (max_freq/int(analyzed_data[medicine]["frequencies"][x]))
            else:
                freq_weight = 1
            mean_weight = (float(analyzed_data[medicine]["mean"][x]) - float(medicine_median[medicine]))/max_difference
            # print(mean_weight)
            if mean_weight < 0:
                mean_weight = 1 / (1+abs(mean_weight))
            else:
                mean_weight = 1 + mean_weight

            experience_weight = (float(analyzed_data[medicine]["experience"][x]) - float(analyzed_data[medicine]["experience"]["mean"]))/analyzed_data[medicine]["experience"]["mean"]
            # print(experience_weight)
            if experience_weight <= 0:
                experience_weight = 1 / (1+abs(experience_weight))
            else:
                experience_weight = 1 + experience_weight
            # print(x,freq_weight,mean_weight,experience_weight)
            one_medicine[x] = freq_weight*mean_weight*experience_weight*500
            total += one_medicine[x]
    for x in one_medicine.keys():
        one_medicine[x] = one_medicine[x]/total
    print(one_medicine)
    order = collections.OrderedDict(sorted(one_medicine.items(), key=lambda t: t[1], reverse=True)[:6])
    # print(order)
    order = collections.OrderedDict(sorted(order.items(), key=lambda t: t[0]))
    probability_spec = list(order.keys())
    probability_value = list(order.values())
    print(probability_value)
    # order = collections.OrderedDict(sorted(freq_data.items(), key=lambda t: t[1],reverse=True)[:6])
    # # print(order)
    # order=collections.OrderedDict(sorted(order.items(), key=lambda t: t[0]))
    # # print(order)
    # print(freq_data)

    freq_graph_spec_list = probability_spec
    # index1 = freq_graph_spec_list.index('total')
    freq_graph_value_list = np.zeros(len(freq_graph_spec_list))
    # freq_graph_spec_list.remove('total')
    # del freq_graph_value_list[index1]
    i=0
    length = len(freq_graph_value_list)
    for spec in freq_graph_spec_list:
        freq_graph_value_list[i]=int(freq_data[spec])
        i = i+1
    print(freq_graph_spec_list)
    print(freq_graph_value_list)
    freq_graph_spec = [ '\n'.join(wrap(l, 20)) for l in freq_graph_spec_list ]
    ax1.barh(np.arange(length), freq_graph_value_list, align='center',color=cool_colors)
    ax1.set_yticks(np.arange(length))
    ax1.set_yticklabels(freq_graph_spec)
    ax1.set_title("Frequency")
    ax1.legend()
    # ax1.yticks(length, freq_graph_spec_list)

    # ax1.xlabel('Usage')
    # ax1.barh(freq_graph_value_list, freq_graph_spec_list, color='red')
    # sns.barplot(x=freq_graph_spec_list, y=freq_graph_value_list,orient="v", saturation=0.8,ax=ax1)

    # ax1.set(xlabel='Experience in years', ylabel='Number of General Practice Doctors')
    # ax.savefig("output.png")

    # Plot
    # ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
    #         autopct='%1.1f%%', shadow=True, startangle=140)
    #
    # plt.axis('equal')
    # plt.show()
    region_data = analyzed_data[medicine]["region"]
    region_order = collections.OrderedDict(sorted(region_data.items(), key=lambda t: t[1], reverse=True)[:5])
    print(region_order)
    order = collections.OrderedDict(sorted(order.items(), key=lambda t: t[0]))
    print(region_order)
    # print(freq_data)
    # 
    # region_graph_spec_list = list(region_order.keys())
    # region_graph_value_list = list(region_order.values())
    # i = 0
    # length = len(region_graph_value_list)
    # while i < 5 & i < length:
    #     region_graph_value_list[i] = int(region_graph_value_list[i])
    #     i = i + 1
    # print(region_graph_spec_list)
    # print(region_graph_value_list)
    # ax2.pie(region_graph_value_list, labels=region_graph_spec_list,autopct='%1.1f%%')
    # ax2.axis('equal')
    # ax2.set_title("Region Wise Distribution")
    # ax2.set(xlabel='Experience in years', ylabel='Number of General Practice Doctors')
    # ax.savefig("output.png")
    # sns.plt.subplot(212,ax)



    # print(freq_data)

    # mean_graph_spec_list = list(order.keys())
    # mean_graph_value_list = list(order.values())
    mean_graph_value_list=[]
    mean_graph_spec_list = freq_graph_spec_list
    for x in mean_graph_spec_list:
        mean_graph_value_list.append(analyzed_data[medicine]["mean"][x])
    i = 0
    length = len(mean_graph_value_list)
    while i < 5 & i < length:
        mean_graph_value_list[i] = int(mean_graph_value_list[i])
        i = i + 1
    print(mean_graph_spec_list)
    print(mean_graph_value_list)
    median_medicine = float(medicine_median[medicine])
    # sns.barplot(x=mean_graph_spec_list, y=mean_graph_value_list, orient="v", saturation=0.8, ax=ax2)
    ax2.barh(np.arange(length), mean_graph_value_list, color=cool_colors,align='center')
    ax2.set_yticks(np.arange(length))
    ax2.set_yticklabels(freq_graph_spec)
    ax2.set_title("Mean of value(prescribed in one year)")
    # ax2.yticks(length,mean_graph_spec_list)
    # ax2.axline(y=median_medicine)

    experience = analyzed_data[medicine]["experience"]
    # print(analyzed_data)
    order = collections.OrderedDict(sorted(experience.items(), key=lambda t: t[1], reverse=True)[:5])
    print(order)
    order = collections.OrderedDict(sorted(experience.items(), key=lambda t: t[0]))
    print(order)
    # print(freq_data)

    experience_graph_spec_list = freq_graph_spec_list
    experience_graph_value_list = []
    i = 0
    length = len(experience_graph_value_list)
    for x in experience_graph_spec_list:
        experience_graph_value_list.append(analyzed_data[medicine]["experience"][x])
    i = 0
    length = len(experience_graph_value_list)
    while i < 5 & i < length:
        experience_graph_value_list[i] = int(experience_graph_value_list[i])
        i = i + 1
    print(experience_graph_spec_list)
    print(experience_graph_value_list)
    # sns.barplot(x=experience_graph_spec_list, y=experience_graph_value_list, orient="v", saturation=0.8, ax=ax3)
    ax3.barh(np.arange(length),experience_graph_value_list,color=cool_colors,align='center')
    ax3.set_yticks(np.arange(length))
    ax3.set_yticklabels(freq_graph_spec)
    ax3.set_title("Mean of Experience")
    # ax3.yticks(length,experience_graph_spec_list)

    probability_spec_show = ['\n'.join(wrap(l, 20)) for l in probability_spec]
    ax4.barh(np.arange(len(probability_spec)), probability_value, align='center', color=cool_colors)
    ax4.set_yticks(np.arange(len(probability_spec)))
    ax4.set_yticklabels(probability_spec_show)
    ax4.set_title("Calculated probability just for " + medicine)
    ax4.legend()
    sns.plt.savefig("output10.png")
    sns.plt.show()

    ss=generate_visualize_output(one_medicine,temp,output_data)
    # generate_output(medicine,x)
    return ss

read_medicine_median_from_csv()

with open("ok.jsonl") as f:
    # x=0
    for line in f:
        # print(line)
        # print(x)
        # x=x+1
        j_content = json.loads(line)
        speciality = j_content.get('provider_variables').get('specialty')
        if speciality not in list_of_specialities:
            list_of_specialities.append(speciality)
        region = j_content.get('provider_variables').get('region')
        settlement_type = j_content.get('provider_variables').get('settlement_type')
        years_of_practicing = j_content.get('provider_variables').get('years_practicing')
        # create_speciality_data(region,settlement_type,years_of_practicing,speciality)
        #print(speciality)
        medicines = j_content.get('cms_prescription_counts')
        #print(medicines)
        # for key,value in medicines.items():
        #     if key not in list_of_medicines:
        #         list_of_medicines.append(key)
        # print(medicines,speciality,years_of_practicing)
        for key, value in medicines.items():
                # if key not in list_of_medicines:
                insert_into_analysis(key,speciality,years_of_practicing,value,region)
                # generate_medicine_median(key,value)
                # generate_medicine_region_data(region,key)

# print(analyzed_data)
# generate_probability(analyzed_data)
# read_spec_patient_from_csv("'Acute Care'","Northeast")
# print(analyzed_data)
# print(medicine_median)
# print(value_data)
# print(speciality_region_data)
# print(speciality_gender_data)
# print(speciality_settlement_type_data)
# write_medicine_median_as_csv(medicine_median)
# write_gender_data_as_csv(speciality_gender_data)
# write_region_data_as_csv(speciality_region_data)
# write_settlement_data_as_csv(speciality_settlement_type_data)
# write_medicine_region_data_as_csv(medicine_region_data)
# write_medicine_speciality_probability_as_csv(analyzed_data)
# read_medicine_median_from_csv()
# print(freq_data)
# print(value_data)
x=0
choice=0
while(choice!="4"):
    print("1. Predict speciality from prescription")
    print("2.Suggest Doctors")
    print("3.Show Statistics")
    print("4.Exit")
    choice = input("What do you want to do?")
    ss={}
    if choice =="2":
        spec=input("Enter speciality")
        suggest_doctors(spec)
    if choice == "1":
        x = 1
        ss=generate_graphs(input("Enter Medicine:"),x,output_data=None)
        # generate_output(input("Enter Medicine:"),x)
        add_more=input("Do you want to add more?")
        while(add_more!="N"):
            x=x+1
            generate_graphs(input("Enter Medicine:"), x,ss)
            add_more = input("Do you want to add more?")
        if output_data.__len__()>0:
            predicted_field="'"+max(ss.items(), key=operator.itemgetter(1))[0]+"'"
            print(predicted_field)
        else:
            print("You have not entered valid medicine")
        # print("1.Suggest Doctors")
        print("2.Show statistics")
        print("3.exit")
        ai=input("Enter input:")
        if(ai=="2"):
            print("1.South")
            print("2.Midwest")
            print("3.West")
            print("4.Northeast")
            region_input=input("Enter Region from above to show statistics and recommendation")
            if region_input == "1":
                region_input = "South"
            elif region_input == "2":
                region_input = "Midwest"
            elif region_input == "3":
                region_input = "West"
            else:
                region_input = "Northeast"
            if predicted_field.__len__()>1:
                read_spec_patient_from_csv(predicted_field,region_input)
            else:
                print("Invalid medicine entered")
        else:
            choice=4
    elif choice =="3":
            specialty=input("Enter Specialty:")
            print("1.South")
            print("2.Midwest")
            print("3.West")
            print("4.Northeast")
            region_input = input("Enter Region from above to show statistics and recommendation")
            if region_input == "1":
                region_input="South"
            elif region_input=="2":
                region_input="Midwest"
            elif region_input=="3":
                region_input="West"
            else:
                region_input="Northeast"
            read_spec_patient_from_csv(specialty,region_input)
# while(input("Do you want to predict more?")!="N"):
#     x =x +1
#     generate_output(input("Enter Medicine:"), x)
# print(output_data)

# generate_output(output_data)
            # else:
            #     if speciality in key.items():
            #         key[speciality]+=value
            #     else:
            #         key[speciality]=value
        #print(spec.dumps())
        #print(spec.values())

        # if spec not in region:
        #     region.append(spec)
        #     print("changed")
        # print(region.__len__())
        # print(region)
##to read region
# with open("roam_prescription_based_prediction.jsonl") as f:
#     for line in f:
#         j_content = json.loads(line)
#         spec=j_content.get('provider_variables').get('region')
#         if spec not in region:
#             region.append(spec)
#             print("changed")
#     print(region.__len__())
#     print(region)
