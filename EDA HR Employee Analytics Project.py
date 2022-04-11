#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[46]:


df=pd.read_excel('HR_Employee_data.xlsx')
df.head()


# In[47]:


df.info()


# # 1.Find out the last evaluation and satisfaction level?

# In[48]:


df["last_evaluation"].describe()


# In[49]:


df["satisfaction_level"].describe()


# In[50]:


sns.lmplot(x="last_evaluation",y="satisfaction_level",height=7,aspect=3,data=df)

Observation:
    1. I found count,mean,max,min values of satisfaction level and last evaluation
    2. And also i used seaborn regression plot
# 
# # 2 .How many employees are left in salary wise?

# In[51]:


df[df["left"]==1]["salary"].value_counts()


# In[52]:


df[['left','salary']].groupby(['left','salary']).size().reset_index().rename(columns={0:'total'})

Observation:
    1. Here i found employees left and active  from company in salarywise count and total 
# # 3.Dept wise distribution of projects?

# In[54]:


for i in df["Department"].unique():
    print("The sector is :" ,i)
    print("The total number of projects :",len(df[df["Department"]==i]))
    print("The total number distributed  projects ")
    print(df[df["Department"]==i]["number_project"].value_counts())


# In[55]:


sns.boxplot('Department','number_project',data=df)

Observation:
    1.I found total number of projects in department wise and they distributed list of projects
# In[ ]:





# # 4.Average monthly hrs spent by people with low salaries?

# In[18]:


lowsalary=df[df["salary"]=="low"]["average_montly_hours"].mean()


# In[19]:


lowsalary


# # 5.Average monthly hrs spent by people withMedium salary?

# In[20]:


medium=df[df["salary"]=="medium"]["average_montly_hours"].mean()


# In[21]:


medium


# # 6.Average monthly hrs spent by people withHigh salary? 

# In[22]:


high=df[df["salary"]=="high"]["average_montly_hours"].mean()


# In[23]:


high

Observation:
    1 . in past 4,5,6 questions i found Average monthly hrs spent by people with low ,medium,high in salariwise
# # 7.Out of total data what was the no. of accidents happened?

# In[16]:


total=len(df["Work_accident"])
total


# In[17]:


accidents =sum(df["Work_accident"])
accidents


# In[63]:


plt.figure(figsize=(8,8))
values=df["Work_accident"].value_counts()
label=("Not happened any accident ","Happened Accident")
#explode=[0,0.5]
plt.pie(values,labels=label,autopct='%0.0f%%',shadow=True,counterclock=False)
plt.title("Accidents count",bbox={'facecolor':'0.8','pad':10})
plt.show()

Observation:
    1. 86% is not happened any accident in past years 
    2. 14% happened accidents
# # 8.Time spend in the company with respect to promotions employees list?

# In[18]:


df[df["promotion_last_5years"]==1]["time_spend_company"].value_counts()
df.groupby(['promotion_last_5years','time_spend_company']).size().reset_index().rename(columns={0:'Total Employees'})


# In[31]:


sns.boxplot(x="promotion_last_5years",y="time_spend_company",data=df)


# In[32]:


Observation:
    1. In this got promotion list maximum 10 yrs worked 16 employees .
    2. In this meximum employees are got promotion in 3 years spend in that company total is 134 employees


# # 9.Satisfaction level as per the salary?

# In[33]:


for i in df.salary.unique():
    print("The Satisfactory level for :",i)
    print (df[df["salary"]==i]["satisfaction_level"].sum())

Observation:
    1. Low salary getting employees satisfaction level is high its maximum
    2. High salary getting employees satisfaction level is low its minimum
    3. Medium salary getting employees satisfaction level is Average 
# # 10.Dept wise satisfaction level?

# In[34]:


for i in df.Department.unique():
    print("The Satisfactory level for :",i)
    print (df[df["Department"]==i]["satisfaction_level"].sum())

Observation :
    1. Sales department satisfaction level is High then, Technical,Support,IT,Product management,Marketing,RandD,Accounting and HR departments
    2. Management department is very low satisfaction level
# # 11.Which dept got max promotion  ?

# In[35]:


for i in df.Department.unique():
    print(" Dept wise promotion:",i)
    print(df[df["Department"]==i]["promotion_last_5years"].max())

Observation:
    1. Maximum got promotion departments are sales,accounting ,hr,technical,support,management,IT,marketing,Rand
# # 12.Spending dept wise maximum monthly hrs ?

# In[36]:


for i in df.Department.unique():
    print ("The maximum monthly hour  :",i)
    print(df[df["Department"]==i]["average_montly_hours"].max())

Observation:
    1. Maximum  monthly 310 hrs spending departments are Marketing,product_mng, support, technica,hr,accounting,sales
    2. than 308 hrs spending departments are RandD and IT
    3. Minimum monthly 307 hrs spending departments are management 

# # 13.Salary wise differing employees?

# In[40]:


salaries=df.groupby(['salary']).size().reset_index().rename(columns={0:"salary levels"})


# In[41]:


salaries.head()


# In[42]:


sns.barplot(x='salary',y='salary levels',data=salaries)

Observation:
    1. In employees salary 3 differents are there like , low ,medium and high
    2. Maximum of employees got low range salary than medium salary range
    3. minimum of employees only getting high salary range 
# # 14.Promotion details in last 5yrs ?

# In[43]:


values=df["promotion_last_5years"].value_counts()
plt.figure(figsize=(8,8))
label=("No Promotion","Got Promotion")
explode=[0,0.7,]
plt.pie(values,labels=label,autopct='%.0f%%',explode=explode,shadow=True,counterclock=False)
plt.title("Promotion plot",bbox={'facecolor':'0.8','pad':10})
plt.show()

Observation:
    1. In last 5 years 98% of the employees are not get any promotion
    2. In last 5 years 2% of the employees only got promotion
# # 15	 Time spend in company in years wise?  

# In[44]:


plt.figure(figsize=(8,8))
values=df["time_spend_company"].value_counts()
label=("3years","2years","4years","5years","6years","7years","8years","10years")
#explode=[0,0.5]
plt.pie(values,labels=label,autopct='%0.0f%%',shadow=True,counterclock=False)
plt.title("Time Spend in Company",bbox={'facecolor':'0.8','pad':10})
plt.show()

Observation:
    1. 3years working employees are time spend company in maximum  they are highest its 43%
    2. 2 years working employees are spending 22%
    3. 4 years working employees are spending 17%
    4. 7years,8years,10years working employees are spending 1%
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




