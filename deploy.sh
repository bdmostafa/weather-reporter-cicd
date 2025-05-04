#!/bin/bash
echo "Deploying to S3..."
aws s3 cp report.html s3://weather-reporter-cicd/ --acl public-read
