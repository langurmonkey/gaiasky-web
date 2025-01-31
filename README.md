# Gaia Sky website

This repository contains the Gaia Sky website. It is a static webisite generated using [Hugo](https://gohugo.io), a static website generator.


## Development server

Start the server with:

```bash
just serve
```
If you want more details, keep reading.

The default `baseURL` points to the deployed environment. To test the site locally, you need to use an environment variable:

```bash
export HUGO_BASEURL="http://localhost:1313/"
```

You can also just set the variable when running the server.

```bash
HUGO_BASEURL="http://localhost:1313/" hugo server
```
