
# System Design Document

## Architecture
Frontend → API Gateway → AWS Lambda → S3 → RDS → Forecasting Engine → Amazon Bedrock

## AI Workflow
1. Sales data uploaded
2. Data stored in S3/RDS
3. Forecasting engine predicts demand
4. Bedrock generates business insights
5. Dashboard updates with recommendations
