# Voice Reminder Scheduler using AWS Lambda, Polly, S3, EventBridge & SNS

## Project Overview

This project demonstrates a serverless AWS solution that converts user-entered text into speech, stores the generated audio file in Amazon S3, and sends email notifications using Amazon SNS.

## Architecture

API Gateway → Lambda → Polly → S3 → SNS

### Workflow

1. User submits a reminder message through API Gateway.
2. AWS Lambda receives the request.
3. Amazon Polly converts the text into MP3 audio.
4. The MP3 file is stored in Amazon S3.
5. Amazon SNS sends a confirmation email.
6. EventBridge can be used to schedule future reminder notifications.

## AWS Services Used

* AWS Lambda
* Amazon API Gateway
* Amazon Polly
* Amazon S3
* Amazon SNS
* Amazon EventBridge
* IAM

## Project Structure

```text
voice-reminder-scheduler/
├── lambda_function.py
├── requirements.txt
├── screenshots/
└── README.md
```

## Sample Input

```json
{
  "message": "Remember to complete AWS certification"
}
```

## Expected Output

* MP3 file generated successfully
* Audio stored in S3 bucket
* SNS email notification sent
* Reminder scheduled through EventBridge

## Learning Outcomes

* Serverless architecture design
* AWS Lambda development
* Text-to-Speech using Amazon Polly
* S3 object storage
* SNS email notifications
* Event-driven automation with EventBridge

## Author

Dinesh Ghule
AWS | DevOps | Cloud Enthusiast
