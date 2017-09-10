import numpy
import json
import csv
import collections
import operator
import codecs
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
region=[]
list_of_specialities=[]
spec_patient_analysis = collections.defaultdict(dict)
analyzed_data=collections.defaultdict(dict)
medicine_array=collections.defaultdict(dict)
speciality_region_data=collections.defaultdict(dict)
speciality_settlement_type_data=collections.defaultdict(dict)
speciality_gender_data=collections.defaultdict(dict)
medicine_median=collections.defaultdict(dict)
medicine_region_data=collections.defaultdict(dict)
output_data=collections.defaultdict(dict)
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
def insert_into_analysis(medicine,speciality,years_of_practicing,value):
    if value > float(medicine_median[medicine]):
        median_factor=1+(value-float(medicine_median[medicine]))/value
    else:
        median_factor=1
    if years_of_practicing > 5:
        years_of_practicing = numpy.floor((years_of_practicing - 5)/5)
        exp_factor = 1 + years_of_practicing/10
    else:
        exp_factor = 1
    analyzed_value = value * median_factor * exp_factor

    if speciality in analyzed_data[medicine].keys():
        analyzed_data[medicine][speciality]+=analyzed_value
    else:
        analyzed_data[medicine][speciality]=analyzed_value
    # print(analyzed_data)
    #print(freq_data[medicine])
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
def generate_visualize_probability(x):

    for key,value in analyzed_data.items():
        total = 0
        for ky,val in value.items():
            total = total + val
        for ky,val in value.items():
            analyzed_data[key][ky]=analyzed_data[key][ky]/total
    return
def generate_output(medicine,x):
    print(output_data)
    print(analyzed_data[medicine])
    for key,value in analyzed_data[medicine].items():

        if key in output_data.keys():
            output_data[key]=output_data[key]+value
            # print(type(output_data[key]))
            # print(output_data[key])
        else:
            output_data[key]=value
    for key,value in output_data.items():
        output_data[key]=output_data[key]/x
    print(output_data)
    print("Predicted field & probability")
    predicted_field = "Please Enter Valid Medicine"
    probability="Do you want to try again?"
    if output_data.__len__()>0:
        # print("Below is ------------------------------")
        # print(sorted(output_data.iteritems(), key=lambda x: -x[1])[:5])
        predicted_field = max(output_data.items(), key=operator.itemgetter(1))[0]
        probability=max(output_data.items(), key=operator.itemgetter(1))[1]
    print(predicted_field)
    print(probability)
    return
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

read_medicine_median_from_csv()

with open("ok.jsonl") as f:
    # x=0
    for line in f:
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
        for key, value in medicines.items():
                # if key not in list_of_medicines:
                insert_into_analysis(key,speciality,years_of_practicing,value)
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
    if choice =="2":
        spec=input("Enter speciality")
        suggest_doctors(spec)
    if choice == "1":
        x = 1
        generate_output(input("Enter Medicine:"),x)
        add_more=input("Do you want to add more?")
        while(add_more!="N"):
            x=x+1
            generate_output(input("Enter Medicine:"), x)
            add_more = input("Do you want to add more?")
        if output_data.__len__()>0:
            predicted_field="'"+max(output_data.items(), key=operator.itemgetter(1))[0]+"'"
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
