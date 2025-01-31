
serve:
    HUGO_BASEURL="http://localhost:1313/" hugo server

hugo:
    hugo

deploy: hugo
    rsync -avh --delete public/ tsagrista@andromeda:/gaiasky/web/
    
