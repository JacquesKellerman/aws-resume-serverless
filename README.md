<<<<<<< HEAD
# aws-resume-serverless

This repository holds the frontend code for my personal website HeyItsChris.com.

  The template used can be found here.

CI/CD
Detailed in the .github/workflows/main.yml is the GitHub Actions workflow that syncronizes this repository's contents with the S3 bucket where the website is served from. On a push to the master branch, it uses the access keys stored with GitHub Secrets to authenticate against the AWS infrastructure and simply pushes the files to S3.
=======
![S3-CI](https://github.com/JacquesKellerman/aws-resume-serverless/workflows/CI/badge.svg)

This repository holds the frontend code for my personal website [JacquesKellerman.me](https://jacqueskellerman.me).

The template used is available to download [here](https://www.styleshout.com/free-templates/ceevee/).

## CI/CD
Detailed in the `.github/workflows/main.yml` is the GitHub Actions workflow that syncronizes this repository's contents with the AWS S3 bucket where the static website is hosted. 

When there is a push to the master branch, GitHub Actions uses the access keys stored with GitHub Secrets to authenticate against the AWS infrastructure and then simply pushes the updated files to S3.
>>>>>>> 992672edfedb314043557eaa5d960b1c49e0661b
