DEPLOY_TARGET := "~/Projects/gaiasky-pages/"

serve:
    HUGO_BASEURL="http://localhost:1313/" hugo server

clean:
    rm -rf public/*

hugo:
    hugo

deploy: clean hugo
    git -C {{DEPLOY_TARGET}} pull
    rsync -avh --delete --exclude={'.git','.gitignore','.gitmodules'} public/ {{DEPLOY_TARGET}}
    git -C {{DEPLOY_TARGET}} add .
    git -C {{DEPLOY_TARGET}} commit -m "feat: deploy website."
    git -C {{DEPLOY_TARGET}} push

deploy-ari: clean hugo
    rsync -avh --delete public/ tsagrista@andromeda:/gaiasky/web/
    
