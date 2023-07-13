#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import glob
import json


# In[2]:


client=boto3.client('s3')


# In[3]:


client.create_bucket(Bucket='sathyalady')


# In[4]:


def upload_files(file_name,bucket,object_name=None,args=None):
    if object_name is None:
        object_name=file_name
    
    response = client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print(response)


# In[5]:


args={'StorageClass':'STANDARD_IA','ServerSideEncryption':'AES256'}
upload_files(r'C:\Users\kowsh\OneDrive\Pictures\Saved Pictures\ho.png','sathyalady','SunnyK',args=args)


# In[6]:


bucket_name='sathyalady'
s3=boto3.resource('s3')
versioning=s3.BucketVersioning(bucket_name)
response=versioning.enable()
print(response)

#we can suspend the versioning by versioning.suspend() command#


# In[7]:


bucket_name='sathyalady'
tagging=s3.BucketTagging(bucket_name)
Set_Tag=tagging.put(Tagging={'TagSet':[{'Key':'sathyalady','Value':''}]})


# In[8]:


response = client.put_bucket_encryption(
     Bucket="sathyalady",
ServerSideEncryptionConfiguration={
            "Rules": [ {"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}   ]
        }
    )
print(response)

#response =client.delete_bucket_encryption(Bucket="sathyalady") we can delete the encryption#


# In[10]:


bucket_name='sathyalady'
bucket_policy={
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject", "s3:GetObjectVersion"],
            "Resource": [ "arn:aws:s3:::sathyalady/*"]
        }
    ]
}

bucket_policy=json.dumps(bucket_policy)
client.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)
#client.delete_bucket_policy(Bucket='sathyalady') we can delete the bucket policy#
#block public access should be disable for bucket policy#


# In[11]:


files=glob.glob(r'C:\Users\kowsh\OneDrive\Pictures\Predator/*')
files


# In[12]:


for file in files:
    upload_files(file,'sathyalady')
    print('uploaded',file)


# In[13]:


def delete_object_from_bucket():
    bucket_name="sathyalady"

response=client.delete_object(Bucket=bucket_name,Key='SunnyK')
print(response)


# In[14]:


response=client.list_buckets()
print(response)


# In[ ]:




