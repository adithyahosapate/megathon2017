
import pandas as pd
import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username = 'ad1455f0-5ac2-449c-90e5-99cffb8a701f',
  password = '62kvrHeqYsZc',
  version = '2017-05-26'
)
workspace_id='9d795050-7e84-4536-8f78-3080cba723df'

# Replace with the context obtained from the initial request

context = {}

df=pd.read_csv("database.csv")

print(df)


while True:
	text=input()

	response = conversation.message(
  	workspace_id = workspace_id,
  	message_input = {'text':text },
  	context = context
	)

	print( "Mark: "+response["output"]["text"][0]+"\n")
	