# -*- coding: utf-8 -*-
"""DM_preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CDQuBY1M0BgtVzIYZ-xvPT3LHasRUKon
"""

import pandas as pd
df=pd.read_csv("/content/original_data/merged_data_1.csv")
df

dataset=pd.read_csv('/content/merged_data_1.csv')

dataset

dataset=dataset.rename(columns={dataset.columns[0] : 'District' })

dataset

region=[]
district=[]

n=dataset.shape[0]
for i in range(n):

    name=dataset.iloc[i]['District']

    if(name.find('Rural')!=-1):

        name=name.replace('- Rural', '')
        name=name.replace('-Rural', '')

        name=name.strip()
        district.append(name)
        region.append('Rural')

    elif(name.find('Urban')!=-1):
        name=name.replace('- Urban', '')
        name=name.replace('-Urban', '')
        name=name.strip()
        district.append(name)
        region.append('Urban')

    elif(name.find('Total')!=-1):
        name=name.replace('- Total', '')
        name=name.replace('-Total', '')
        name=name.strip()
        district.append(name)
        region.append('Total')

print(len(region))
print(len(district))
print(dataset.shape[0])

dataset['Region']=region
dataset['District']=district
dataset

"""DATA PREPROCESSING: Feature Construction : Zone"""

zone={ 'Southern Zone' : ['AP', 'TN' , 'KL', 'KA', 'TG'] , 'Western Zone' : ['GA', 'MH', 'GJ'] , 'Eastern Zone' : ['OR','WB', 'BR', 'JH', 'SK'] , 'North Eastern Zone' : ['AR','NL','MN','MZ','ML','AS','TR'], 'Central Zone' : ['MP' , 'CT' , 'UP' , 'UT'], 'Northern Zone' : ['RJ', 'DL' , 'PB' , 'HR' , 'HP' , 'JK']}

zone_list=[]
n=dataset.shape[0]
for i in range(n):
    name=dataset.iloc[i]['State']
    for z in zone:
        if name in zone[z]:
            zone_list.append(z)
print(len(zone_list))
print(n)

dataset['Zone']=zone_list
dataset

dataset.to_csv('/content/feature_constructed_data_2.csv', index=False)

dataset=pd.read_csv('/content/feature_constructed_data_2.csv')
dataset

dataset.isna().sum().sum()

"""Data Cleaning : Removing rows with 'Households Surveyed' == 0"""

dataset=dataset[dataset['Households surveyed'] != 0.00]


dataset

new_columns_names={'District' : 'District' ,
'Households surveyed' :'Households surveyed' ,
'Women age 15-49 years interviewed' : 'Women age 15-49 years interviewed',
'Men age 15-49 years interviewed' : 'Men age 15-49 years interviewed' ,
'1. Population (female) age 6+ years who ever attended school (%)' : 'pop_f_school' ,
'2. Population below age 15 years (%)' : 'pop_below_15' ,
'3. Sex ratio of the total population (females per 1000 males)' : 'sex_ratio_total' ,
'4. Sex ratio at birth for children born in the last five years (females per 1000 males)' : 'sex_ratio_children' ,
'5. Children under age 5 years whose birth was registered (%)' : 'child_birth_reg' ,
'6. Households with electricity (%)' : 'hh_elec' ,
'7. Households with an improved drinking-water source1 (%)' : 'hh_water' ,
'8. Households using improved sanitation facility2 (%)' : 'hh_san' ,
'9. Households using clean fuel for cooking3 (%)' : 'hh_fuel' ,
'10. Households using iodized salt (%)' : 'hh_iodine' ,
'11. Households with any usual member covered by a health scheme or health insurance (%)' : 'hh_health_scheme' ,
'12. Women who are literate (%)' : 'f_lit' ,
'13. Men who are literate (%)' : 'm_lit' ,
'14. Women with 10 or more years of schooling (%)' : 'f_edu' ,
'15. Women age 20-24 years married before age 18 years (%)' : 'f_marriage' ,
'16. Men age 25-29 years married before age 21 years (%)' : 'm_marriage' ,
'17. Women age 15-19 years who were already mothers or pregnant at the time of the survey (%)' : 'f_mother_pregnant' ,
'18. Any method (%)' : 'contra_any' ,
'19. Any modern method (%)' : 'contra_modern' ,
'20. Female sterilization (%)' : 'contra_f_ster' ,
'21. Male sterilization (%)' : 'contra_m_ster' ,
'22. IUD/PPIUD (%)' : 'contra_iud' ,
'23. Pill (%)' : 'contra_pill' ,
'24. Condom (%)' : 'contra_condom' ,
'25. Total unmet need (%)' : 'contra_unmet_total' ,
'26. Unmet need for spacing (%)' : 'contra_unmet_spacing' ,
'27. Health worker ever talked to female non-users about family planning5 (%)' : 'fp_non_users' ,
'28. Current users ever told about side effects of current method (%)' : 'fp_side_effects' ,
'29. Mothers who had antenatal check-up in the first trimester (%)' : 'mc_ante_first_tri' ,
'30. Mothers who had at least 4 antenatal care visits (%)' : 'mc_ante_4_vis' ,
'31. Mothers whose last birth was protected against neonatal tetanus6 (%)' : 'mc_neo_tetanus' ,
'32. Mothers who consumed iron folic acid for 100 days or more when they were pregnant (%)' : 'mc_folic_acid' ,
'33. Mothers who had full antenatal care7 (%)' : 'mc_ante_full_care' ,
'34. Registered pregnancies for which the mother received Mother and Child Protection (MCP) card (%)' : 'mc_MCP' ,
'35. Mothers who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)' : 'mc_post_care' ,
'36. Mothers who received financial assistance under Janani Suraksha Yojana (JSY) for births delivered in an institution (%)' : 'mc_JSY' ,
'37. Average out of pocket expenditure per delivery in public health facility (Rs.)' : 'mc_expenditure' ,
'38. Children born at home who were taken to a health facility for check-up within 24 hours of birth (%)' : 'mc_home_child' ,
'39. Children who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)' : 'mc_child_care' ,
'40. Institutional births (%)' : 'insti_births' ,
'41. Institutional births in public facility (%)' : 'insti_births_public' ,
'42. Home delivery conducted by skilled health personnel (out of total deliveries) (%)' : 'home_delivery' ,
'43. Births assisted by a doctor/nurse/LHV/ANM/other health personnel (%)' : 'doc_delivery' ,
'44. Births delivered by caesarean section (%)' : 'cs_delivery' ,
'45. Births in a private health facility delivered by caesarean section (%)' : 'private_cs_delivery' ,
'46. Births in a public health facility delivered by caesarean section (%)' : 'public_cs_delivery' ,
'47. Children age 12-23 months fully immunized (BCG measles and 3 doses each of polio/DPT) (%)' : 'imm_full' ,
'48. Children age 12-23 months who have received BCG (%)' : 'imm_BCG' ,
'49. Children age 12-23 months who have received 3 doses of polio vaccine (%)' : 'imm_polio' ,
'50. Children age 12-23 months who have received 3 doses of DPT vaccine (%)' : 'imm_DPT' ,
'51. Children age 12-23 months who have received measles vaccine (%)' : 'imm_measles' ,
'52. Children age 12-23 months who have received 3 doses of Hepatitis B vaccine (%)' : 'imm_hep' ,
'53. Children age 9-59 months who received a vitamin A dose in last 6 months (%)' : 'imm_vit_A' ,
'54. Children age 12-23 months who received most of the vaccinations in public health facility (%)' : 'imm_public' ,
'55. Children age 12-23 months who received most of the vaccinations in private health facility (%)' : 'imm_private' ,
'56. Prevalence of diarrhoea (reported) in the last 2 weeks preceding the survey (%)' : 'cdis_diar_reported' ,
'57. Children with diarrhoea in the last 2 weeks who received oral rehydration salts (ORS) (%)' : 'cdis_diar_ORS' ,
'58. Children with diarrhoea in the last 2 weeks who received zinc (%)' : 'cdis_diar_zinc' ,
'59. Children with diarrhoea in the last 2 weeks taken to a health facility (%)' : 'cdis_diar_health_facility' ,
'60. Prevalence of symptoms of acute respiratory infection (ARI) in the last 2 weeks preceding the survey (%)' : 'cdis_ARI' ,
'61. Children with fever or symptoms of ARI in the last 2 weeks preceding the survey taken to a health facility (%)' : 'cdis_ARI_health_facility' ,
'62. Children under age 3 years breastfed within one hour of birth8 (%)' : 'cnut_breastfed_one_hour' ,
'63. Children under age 6 months exclusively breastfed9 (%)' : 'cnut_breastfed_ex' ,
'64. Children age 6-8 months receiving solid or semi-solid food and breastmilk9 (%)' : 'cnut_food' ,
'65. Breastfeeding children age 6-23 months receiving an adequate diet9 10 (%)' : 'cnut_breastfeeding_diet' ,
'66. Non-breastfeeding children age 6-23 months receiving an adequate diet9 10 (%)' : 'cnut_non_breastfeeding_diet' ,
'67. Total children age 6-23 months receiving an adequate diet9 10 (%)' : 'cnut_non_total_diet' ,
'68. Children under 5 years who are stunted11 (%)' : 'cnut_stunted' ,
'69. Children under 5 years who are wasted11 (%)' : 'cnut_wasted' ,
'70. Children under 5 years who are severely wasted12 (%)' : 'cnut_sev_wasted' ,
'71. Children under 5 years who are underweight11 (%)' : 'cnut_uweight' ,
'72. Women whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2) (%)' : 'f_low_BMI' ,
'73. Men whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2) (%)' : 'm_low_BMI' ,
'74. Women who are overweight or obese (BMI >=25.0 kg/m2) (%)' : 'f_high_BMI' ,
'75. Men who are overweight or obese (BMI >=25.0 kg/m2) (%)' : 'm_high_BMI' ,
'76. Children age 6-59 months who are anaemic (<11.0 g/dl) (%)' : 'anaemia_children' ,
'77. Non-pregnant women age 15-49 years who are anaemic (<12.0 g/dl) (%)' : 'anaemia_f_non_preg' ,
'78. Pregnant women age 15-49 years who are anaemic (<11.0 g/dl) (%)' : 'anaemia_f_preg' ,
'79. All women age 15-49 years who are anaemic (%)' : 'anaemia_f_all' ,
'80. Men age 15-49 years who are anaemic (<13.0 g/dl) (%)' : 'anaemia_m' ,
'81. Blood sugar level - high (>140 mg/dl) (%)' : 'BSL_high_f' ,
'82. Blood sugar level - very high (>160 mg/dl) (%)' : 'BSL_v_high_f' ,
'83. Blood sugar level - high (>140 mg/dl) (%)' : 'BSL_high_m' ,
'84. Blood sugar level - very high (>160 mg/dl) (%)' : 'BSL_v_high_m' ,
'85. Slightly above normal (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)' : 'hypertension_f_high_1' ,
'86. Moderately high (Systolic 160-179 mm of Hg and/or Diastolic 100-109 mm of Hg) (%)' : 'hypertension_f_high_2' ,
'87. Very high (Systolic ?180 mm of Hg and/or Diastolic ?110 mm of Hg) (%)' : 'hypertension_f_high_3' ,
'88. Slightly above normal (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)' : 'hypertension_m_high_1' ,
'89. Moderately high (Systolic 160-179 mm of Hg and/or Diastolic 100-109 mm of Hg) (%)' : 'hypertension_m_high_2' ,
'90. Very high (Systolic ?180 mm of Hg and/or Diastolic ?110 mm of Hg) (%)' : 'hypertension_m_high_3' ,
'91. Cervix (%)' : 'cervix' ,
'92. Breast (%)' : 'breast' ,
'93. Oral cavity (%)' : 'oral_cavity' ,
'State' : 'State' ,
'Region' : 'Region' ,
'Zone' : 'Zone' }

new_columns_names_inv = {v: k for k, v in new_columns_names.items()}
new_columns_names_inv

attribute_categories={'population' : [] , 'literacy' : [] , 'marriage': [] , 'family_planning' : [] , 'maternity_care' : [] , 'delivery_care': [], 'child_immunisation' : [] , 'childhood_diseases' : [] , 'child_nutrition':[], 'adult_nutrition':[], 'anaemia': [], 'blood_sugar_level' : [], 'hypertension': [] , 'women_examination' : []    }

for i in range(len(dataset.columns)):
                if(i<=14):
                   attribute_categories['population'].append(dataset.columns[i])
                elif(i<=17):
                    attribute_categories['literacy'].append(dataset.columns[i])
                elif(i<=20):
                    attribute_categories['marriage'].append(dataset.columns[i])
                elif(i<=31):
                    attribute_categories['family_planning'].append(dataset.columns[i])
                elif(i<=42):
                    attribute_categories['maternity_care'].append(dataset.columns[i])
                elif(i<=49):
                    attribute_categories['delivery_care'].append(dataset.columns[i])
                elif(i<=58):
                    attribute_categories['child_immunisation'].append(dataset.columns[i])
                elif(i<=64):
                    attribute_categories['childhood_diseases'].append(dataset.columns[i])
                elif(i<=74):
                    attribute_categories['child_nutrition'].append(dataset.columns[i])
                elif(i<=78):
                    attribute_categories['adult_nutrition'].append(dataset.columns[i])
                elif(i<=83):
                    attribute_categories['anaemia'].append(dataset.columns[i])
                elif(i<=87):
                    attribute_categories['blood_sugar_level'].append(dataset.columns[i])
                elif(i<=90):
                  attribute_categories['hypertension'].append(dataset.columns[i])
                elif(i<=93):
                    attribute_categories['hypertension'].append(dataset.columns[i])
                elif(i<=96):
                    attribute_categories['women_examination'].append(dataset.columns[i])
                else:
                    attribute_categories['population'].append(dataset.columns[i])

attribute_categories

"""
Data Cleaning : Removing attributes with many missing (NA) values"""

pd.set_option('display.max_rows', 500)
num_of_na=list(dataset.isna().sum())
columns_to_drop=[]
for i in range(len(num_of_na)):
    if num_of_na[i] >= 0.3*dataset.shape[0]:


        columns_to_drop.append(dataset.columns[i])

print(columns_to_drop)
dataset2=dataset.drop(columns_to_drop,axis=1)
print(dataset2.shape[1])
print(dataset.shape[1])

"""Data Cleaning: Removing rows with missing values for at least one category of attributes"""

n = dataset2.shape[0]
to_delete=[]
for i in range(n):
   count=[0 for i in range(14)]
   for column in dataset2.columns:
        #print(dataset.iloc[i][column])
        if(pd.isnull(dataset2.iloc[i][column])):

           for x in range(len(list(attribute_categories.keys()))):
               key= list(attribute_categories.keys())[x]
               if column in attribute_categories[key]:
                    count[x]+=1
   #print(count)
   for y in range(len(count)):
        key=list(attribute_categories.keys())[y]
#         print(count[y])
#         print(len(attribute_categories[key]))
#         print("....")
        if(count[y]>=0.5*len(attribute_categories[key])):
            #print("YESSS")
            to_delete.append(i)
            break

print(to_delete)

print(len(to_delete))

dataset3=dataset2.drop(dataset2.index[to_delete],axis=0)

print(dataset3.shape[0])
dataset2.shape[0]

"""Data Cleaning: Replacing remaining NA values with mean"""

dataset3.isna().sum().sum()

for col in dataset3.columns:
    if(dataset3[col].isna().any()):
        dataset3[col].fillna(dataset3[col].mean(), inplace=True)

dataset3.isna().sum().sum()

dataset3.to_csv('/content/data_missing_values_removed_3.csv')

dataset3.shape

"""Splitting data based on 'Region' attribute"""

dataset3_total=dataset3[dataset3['Region']=='Total']
dataset3_total.to_csv('/content/data_total_4.csv')

dataset3_rural_urban=dataset3[dataset3['Region']!='Total']
dataset3_rural_urban.to_csv('/content/data_rural_urban_4.csv')

"""DATA PREPROCESSING : Feature Subset Selection
( Based on domain knowledge and correlation between different attributes)

Attribute Subset Selection (Irrelevant Features)
"""

dataset3=dataset3.drop(['2. Population below age 15 years (%)', '5. Children under age 5 years whose birth was registered (%)', '6. Households with electricity (%)',
      '10. Households using iodized salt (%)',
       '11. Households with any usual member covered by a health scheme or health insurance (%)', '17. Women age 15-19 years who were already mothers or pregnant at the time of the survey (%)',
                        '41. Institutional births in public facility (%)', '44. Births delivered by caesarean section (%)',
       '45. Births in a private health facility delivered by caesarean section (%)',
       '46. Births in a public health facility delivered by caesarean section (%)', '54. Children age 12-23 months who received most of the vaccinations in public health facility (%)',
       '55. Children age 12-23 months who received most of the vaccinations in private health facility (%)','81. Blood sugar level - high (>140 mg/dl) (%)',
       '82. Blood sugar level - very high (>160 mg/dl) (%)',
       '83. Blood sugar level - high (>140 mg/dl) (%)',
       '84. Blood sugar level - very high (>160 mg/dl) (%)',
       '85. Slightly above normal (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)',
       '86. Moderately high (Systolic 160-179 mm of Hg and/or Diastolic 100-109 mm of Hg) (%)',
       '87. Very high (Systolic ?180 mm of Hg and/or Diastolic ?110 mm of Hg) (%)',
       '88. Slightly above normal (Systolic 140-159 mm of Hg and/or Diastolic 90-99 mm of Hg) (%)',
       '89. Moderately high (Systolic 160-179 mm of Hg and/or Diastolic 100-109 mm of Hg) (%)',
       '90. Very high (Systolic ?180 mm of Hg and/or Diastolic ?110 mm of Hg) (%)',  '80. Men age 15-49 years who are anaemic (<13.0 g/dl) (%)',
       '73. Men whose Body Mass Index (BMI) is below normal (BMI <18.5 kg/m2) (%)',
       '74. Women who are overweight or obese (BMI >=25.0 kg/m2) (%)',
       '75. Men who are overweight or obese (BMI >=25.0 kg/m2) (%)',  '56. Prevalence of diarrhoea (reported) in the last 2 weeks preceding the survey (%)',
       '60. Prevalence of symptoms of acute respiratory infection (ARI) in the last 2 weeks preceding the survey (%)',
       '34. Registered pregnancies for which the mother received Mother and Child Protection (MCP) card (%)',
       '36. Mothers who received financial assistance under Janani Suraksha Yojana (JSY) for births delivered in an institution (%)',
       '37. Average out of pocket expenditure per delivery in public health facility (Rs.)'], axis=1)

dataset3=dataset3.drop(['25. Total unmet need (%)', '26. Unmet need for spacing (%)',
       '27. Health worker ever talked to female non-users about family planning5 (%)',
       '28. Current users ever told about side effects of current method (%)'], axis=1)

dataset3=dataset3.drop(['39. Children who received postnatal care from a doctor/nurse/LHV/ANM/midwife/other health personnel within 2 days of delivery (%)'],axis=1)

dataset3=dataset3.drop(['31. Mothers whose last birth was protected against neonatal tetanus6 (%)'],axis=1)

dataset3.shape

"""Correlation Matrix"""

pd.set_option('display.max_columns', 100)
x=dataset3.corr()
x.to_csv('/content/corr_matrix_5.csv')
x

dataset3=dataset3.drop(['43. Births assisted by a doctor/nurse/LHV/ANM/other health personnel (%)', '48. Children age 12-23 months who have received BCG (%)',
  '49. Children age 12-23 months who have received 3 doses of polio vaccine (%)',
  '50. Children age 12-23 months who have received 3 doses of DPT vaccine (%)',
  '51. Children age 12-23 months who have received measles vaccine (%)',
  '52. Children age 12-23 months who have received 3 doses of Hepatitis B vaccine (%)', '69. Children under 5 years who are wasted11 (%)',
  '70. Children under 5 years who are severely wasted12 (%)',
  '71. Children under 5 years who are underweight11 (%)',  '77. Non-pregnant women age 15-49 years who are anaemic (<12.0 g/dl) (%)',
    '18. Any method (%)',
   '20. Female sterilization (%)',
   '21. Male sterilization (%)',
   '22. IUD/PPIUD (%)',
   '23. Pill (%)',
   '24. Condom (%)'], axis = 1)

dataset3.shape

# Dropping highly correlated attributes in the category 'maternity_care'
# The threshold for correlation is set to be 0.7

for col in dataset3.columns:
    if col in attribute_categories['maternity_care']:
        if col !='30. Mothers who had at least 4 antenatal care visits (%)' and col !='32. Mothers who consumed iron folic acid for 100 days or more when they were pregnant (%)' :
            print(col)
            print(dataset3[col].corr(dataset3['30. Mothers who had at least 4 antenatal care visits (%)']))
            dataset3=dataset3.drop(col,axis=1)
dataset3.shape

dataset3

dataset3.columns

len(dataset3.columns)

dataset3.to_csv('/content/data_attributes_removed_5_5.csv')

"""DATA PREPROCESSING: Z-Score Normalisation/Standardisation"""

to_ignore = ['District', 'Households surveyed', 'Women age 15-49 years interviewed',
       'Men age 15-49 years interviewed', 'State', 'Region', 'Zone']
for col in dataset3.columns:
    if col not in to_ignore:
        dataset3[col]=(dataset3[col] - dataset3[col].mean())/dataset3[col].std()

dataset3

len(dataset3.columns)

dataset3.to_csv('/content/normalised_data_6.csv')

"""DATA PREPROCESSING: Unsupervised Discretisation : Equal Interval Binning"""

dataset4=dataset3.copy()
to_ignore = ['District', 'Households surveyed', 'Women age 15-49 years interviewed',
       'Men age 15-49 years interviewed', 'State', 'Region', 'Zone']
for col in dataset4.columns:
    if col not in to_ignore:
        dataset4[col]=pd.cut(dataset4[col],3,labels=['low', 'medium', 'high'])

dataset4

dataset4.to_csv('/content/equal_interval_discretised_data_7.csv')

"""DATA PREPROCESSING: Unsupervised Discretisation : Equal Frequency Binning"""

dataset5=dataset3.copy()
to_ignore = ['District', 'Households surveyed', 'Women age 15-49 years interviewed',
       'Men age 15-49 years interviewed', 'State', 'Region', 'Zone']
for col in dataset5.columns:
    if col not in to_ignore:
        dataset5[col]=pd.qcut(dataset5[col],3,labels=['low', 'medium', 'high'])

dataset5

dataset5.to_csv('/content/equal_frequency_discretised_data_7.csv')

"""Splitting the normalised data further, based on 'Region' attribute"""

dataset3_total=dataset3[dataset3['Region']=='Total']
dataset3_total.to_csv('/content/normalised_data_total_8.csv')

dataset3_rural_urban=dataset3[dataset3['Region']!='Total']
dataset3_rural_urban.to_csv('/content/normalised_data_rural_urban_8.csv')