
serve:
    HUGO_BASEURL="http://localhost:1313/" hugo server

clean:
    rm -rf public/*

hugo:
    hugo

deploy: clean hugo
    rsync -avh --delete public/ tsagrista@andromeda:/gaiasky/web/
    
