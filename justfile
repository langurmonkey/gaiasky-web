DEPLOY_TARGET := "~/Projects/gaiasky-pages/"

serve:
    HUGO_BASEURL="http://localhost:1313/" hugo server

# Cleans the generated site
clean:
    rm -rf public/*

# Generates the datasets.md file
datasets:
    (cd script && pipenv run python gen-datasets.py)
    mv script/datasets.md content/datasets/index.md

# Generates the site with hugo
hugo:
    hugo

# Deploys the site to github pages (project gaiasky-pages)
deploy: clean hugo
    git -C {{DEPLOY_TARGET}} pull
    rsync -avh --delete --exclude={'.git','.gitignore','.gitmodules'} public/ {{DEPLOY_TARGET}}
    git -C {{DEPLOY_TARGET}} add .
    git -C {{DEPLOY_TARGET}} commit -m "feat: deploy website."
    git -C {{DEPLOY_TARGET}} push

deploy-ari: clean hugo
    rsync -avh --delete public/ tsagrista@andromeda:/gaiasky/web/
    
