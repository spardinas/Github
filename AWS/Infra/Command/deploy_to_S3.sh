#!/bin/bash

# Configuration
BUCKET="arn-bucket-s3"
DISTRIBUTION_ID="DISTRIBUTION_ID"
BUILD_DIR="./dist"

echo "Starting deployment to S3..."

# sync files to S3 bucket
aws s3 sync $BUILD_DIR s3://$BUCKET 

echo "Files synced to S3 bucket: $BUCKET"

# Invalidate CloudFront
aws cloudfront create-invalidation \
  --distribution-id $DISTRIBUTION_ID \
  --paths "/*"

echo "CloudFront invalidation created."
echo "Deployment completed successfully!"