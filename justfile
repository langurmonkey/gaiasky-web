DEPLOY_TARGET := "~/Projects/gaiasky-pages/"

# Serve the hugo site locally in http://localhost:1313
serve:
    HUGO_BASEURL="http://localhost:1313/" nohup hugo server 2>&1 1>/dev/null &

# Stop the local server
stop:
    pkill hugo || true

# Cleans the generated site
clean:
    rm -rf public/*

# Generates all the releases in /downloads/releases
releases:
    (cd script && pipenv run python gen-releases.py)

# Generates the datasets.md file
datasets:
    (cd script && pipenv run python gen-datasets.py)
    mv script/datasets.md content/resources/datasets/index.md

# Generate the icon font
iconfont:
    (cd script && npx svgtofont --config svgtofont.config.js --output ./font --sources ./icons)
    cp script/font/gaiasky-icons.css script/font/gaiasky-icons.eot script/font/gaiasky-icons.svg script/font/gaiasky-icons.ttf script/font/gaiasky-icons.woff script/font/gaiasky-icons.woff2 static/webfonts/

# icons:
#     (cd script && node gen-icon-json.js)
#     mv script/custom-icons.json static/icons/

# Generates the site with hugo
hugo:
    hugo

alias publish := deploy
# Deploys the site to github pages (project gaiasky-pages)
deploy: stop clean hugo
    git -C {{DEPLOY_TARGET}} pull
    rsync -avh --delete --exclude={'.git','.gitignore','.gitmodules'} public/ {{DEPLOY_TARGET}}
    git -C {{DEPLOY_TARGET}} add .
    git -C {{DEPLOY_TARGET}} commit -m "feat: deploy website."
    git -C {{DEPLOY_TARGET}} push

deploy-ari: clean hugo
    rsync -avh --delete public/ tsagrista@andromeda:/gaiasky/web/
    
