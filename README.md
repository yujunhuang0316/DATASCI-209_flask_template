# DATASCI 209 flask template

This repo provides a basic flask app for DATASCI 209 students and instructors. You can run this flask app locally for development/debugging, or deploy it to Digital Ocean's [App Platform](https://www.digitalocean.com/products/app-platform).

## Getting Started

1. Install Python 3.x on your computer.
2. [Create a copy](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) of this repo.
3. Clone your copy of this repo to your computer.
4. Create a [Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/) to run your flask app (Optional).

## Local Development

**Install dependencies**

On a Mac, open a terminal and run the following command to install the necessary Python libraries.  See the [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) if you need more information, or if you run Python on Windows.

```
pip3 install -r requirements.txt
```

**Run your app locally**

In the folder where you cloned a copy of this repo, run the following command.  The --debug option will cause flask to automatically load any code changes you make.

```
flask --app app.py --debug run
```

**Point your browser to http://127.0.0.1:5000**

## Digital Ocean

Digital Ocean provides a public cloud platform that you can use to host your flask app.  See [How To Deploy a Flask App Using Gunicorn to App Platform](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-app-using-gunicorn-to-app-platform) for an overview of how their flask app hosting works.

This repo already has the necessary configuration files to build and launch a flask app on Digital Ocean's App Platform (gunicorn_config.py and requirements.txt), so the only things you should need to do are:

1. Create a [Digital Ocean](https://www.digitalocean.com) account.
2. Follow the instructions in [Step 5 - Deploying to Digital Ocean with App Platform](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-app-using-gunicorn-to-app-platform#step-5-mdash-deploying-to-digitalocean-with-app-platform).

Please note the following:

1. Digital Ocean does not offer free App Platform hosting.  The smallest App Platform VM costs $5 per month as of October 2024.
2. Automatically deploying your code changes to App Platform requires installing the Digital Ocean GitHub app.  It's easier to set up this app in your personal GitHub workspace than in a GitHub organization owned by someone else.  For this reason, we recommend that you keep your flask app repo in your personal GitHub workspace.
