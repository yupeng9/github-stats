## setup environment
```
cd github-stats
virtualenv -p python env
source env/bin/activate
pip install -r requirements.txt
```

Create a file `input` in the working directory with the following format: GithubID, Repos(owner/repo). For example:
```
yupeng9	apache/pinot,pinot-contrib/pinot-docs
```
