import os
import json
import boto3

route53 = boto3.client('route53')
# Environment variables for AWS Lambda function
# Must set those variables as environment variables in the Lambda function configuration
ZONE_ID = os.environ['HOSTED_ZONE_ID']
RECORD = os.environ['RECORD_NAME']

def lambda_handler(event, context):
    ip = event.get('ip')
    if not ip:
        return {'status': 'error', 'message': 'No IP provided'} # Ensure the event contains an 'ip' key
    # Validate the IP and update the DNS record
    response = route53.change_resource_record_sets(
        HostedZoneId=ZONE_ID,
        ChangeBatch={
            'Changes': [{
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': RECORD,
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [{'Value': ip}]
                }
            }]
        }
    )
    return {'status': 'success', 'changeInfo': response['ChangeInfo']}
