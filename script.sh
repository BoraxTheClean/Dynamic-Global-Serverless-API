#!/bin/bash
mkdir dist
cp src/* dist/

aws cloudformation package --template-file template.yaml --output-template processed.template.yaml --s3-bucket "owen-lambda-bucket" --s3-prefix list-instances
aws cloudformation deploy --template-file processed.template.yaml --stack-name header-api --capabilities CAPABILITY_IAM CAPABILITY_AUTO_EXPAND --region us-east-1

rm processed.template.yaml
rm -rf dist/
