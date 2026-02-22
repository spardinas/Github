# Configuration
$Bucket = "arn:aws:s3:::BUCKET_NAME"
$DistributionId = "DISTRIBUTION_ID"
$BuildDir = "./dist"

Write-Host "Starting deployment to S3..."

# Sync files to S3 bucket
aws s3 sync $BuildDir "s3://$Bucket" 

Write-Host "Files synced to S3 bucket: $Bucket"

# Invalidate CloudFront
aws cloudfront create-invalidation `
  --distribution-id $DistributionId `
  --paths "/*"

Write-Host "CloudFront invalidation created."
Write-Host "Deployment to S3 completed successfully!" 