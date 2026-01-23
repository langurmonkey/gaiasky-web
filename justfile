DEPLOY_TARGET := "~/Projects/gaiasky-pages/"

# Serve the hugo site locally in http://localhost:1313
serve: pagefind
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

# Generate a font from all icons in /assets/icons
iconfont:
    (cd script && npx svgtofont --config svgtofont.config.js --output ./generated --sources ../assets/icons)
    cp script/generated/gaiasky-icons.css script/generated/gaiasky-icons.eot script/generated/gaiasky-icons.svg script/generated/gaiasky-icons.ttf script/generated/gaiasky-icons.woff script/generated/gaiasky-icons.woff2 static/webfonts/

# Runs hugo. To generate the site use target 'generate'.
hugo:
    hugo

# Generation alias.
alias generate := pagefind
# Generate the site with the pagefind post-hook.
pagefind: hugo
    npx pagefind --site "public/"

# Publishes the site to GitHub pages.
alias publish := deploy
# Deploys the site to GitHub pages.
deploy: stop clean pagefind
    git -C {{DEPLOY_TARGET}} pull
    rsync -avh --delete --exclude={'.git','.gitignore','.gitmodules'} public/ {{DEPLOY_TARGET}}
    git -C {{DEPLOY_TARGET}} add .
    git -C {{DEPLOY_TARGET}} commit -m "feat: deploy website."
    git -C {{DEPLOY_TARGET}} push

# Deploys the site to the ARI server.
deploy-ari: clean hugo
    rsync -avh --delete public/ tsagrista@andromeda:/gaiasky/web/
    
