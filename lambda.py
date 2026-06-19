import json
import boto3
from datetime import datetime

polly = boto3.client('polly')
s3 = boto3.client('s3')
sns = boto3.client('sns')

BUCKET = "voice-reminder-storage"
TOPIC_ARN = "arn:aws:sns:ap-south-1:287871537034:VoiceReminderTopic"

def lambda_handler(event, context):

    message = event.get("message", "Hello from AWS")

    response = polly.synthesize_speech(
        Text=message,
        OutputFormat='mp3',
        VoiceId='Aditi'
    )

    filename = f"reminder-{int(datetime.now().timestamp())}.mp3"

    print("Bucket:", BUCKET)
    print("Filename:", filename)

    s3.put_object(
        Bucket=BUCKET,
        Key=filename,
        Body=response['AudioStream'].read(),
        ContentType='audio/mpeg'
    )

    print("S3 upload completed")

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="Voice Reminder Created",
        Message=f"Your reminder audio has been stored in S3: {filename}"
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Reminder created successfully",
            "file": filename
        })
    }
