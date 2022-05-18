# aws-resume-serverless

The frontend code for my personal website [JacquesKellerman.me](https://jacqueskellerman.me).

The template used is available to download [here](https://www.styleshout.com/free-templates/ceevee/).

## CI/CD
Detailed in the `.github/workflows/main.yml` is the GitHub Actions workflow that syncronizes this repository's contents with the AWS S3 bucket where the static website is hosted. 

When there is a push to the master branch, GitHub Actions uses the access keys stored with GitHub Secrets to authenticate against the AWS infrastructure and then simply pushes the updated files to S3.
