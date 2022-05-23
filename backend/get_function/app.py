import json
import boto3

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
dbTableName = 'visitorCounterTable'
table = dynamodb.Table(dbTableName)

def lambda_handler(event, context):
    # 1 Update item in table and return value
    dbResponse = table.update_item(
        Key={
            'id': 'total'
        },
        UpdateExpression='SET visitor_count = visitor_count + :value',
        ExpressionAttributeValues={
            ':value':1
        },
        ReturnValues="UPDATED_NEW"
    )

    visitorCount = int(dbResponse["Attributes"]["visitor_count"])
    print('visitorCount obtained from table = ' + str(visitorCount))
    
     # 2. Construct the body of the response object
    transactionResponse = {}
    transactionResponse['visitorCount'] = visitorCount
    transactionResponse['message'] = 'Successful GET'
    
    # 3. Construct HTTP response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        },
        "body": json.dumps(transactionResponse)
    }

    # 4. Return api response object
    return apiResponse