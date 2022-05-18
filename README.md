# aws-resume-serverless

This repository holds the frontend code for my personal website HeyItsChris.com.

  The template used can be found here.

CI/CD
Detailed in the .github/workflows/main.yml is the GitHub Actions workflow that syncronizes this repository's contents with the S3 bucket where the website is served from. On a push to the master branch, it uses the access keys stored with GitHub Secrets to authenticate against the AWS infrastructure and simply pushes the files to S3.