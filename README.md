# Gaia Sky website

This repository contains the Gaia Sky website. It is a static webisite generated using [Hugo](https://gohugo.io), a static website generator.

## Deployment

Deploy the site with:

```bash
just deploy
```

This target cleans the output directory, generates the site with hugo, copies the output to the `gaiasky-pages` project, and commits it. The site is deployed directly in a repository in GitHub, and is hosted in GitHub Pages.

## Development server

Start the server with:

```bash
just serve
```

This starts the server in the background. Stop it with:

```bash
just stop
```

That's all you need. If you want more details, keep reading.

The default `baseURL` points to the deployed environment. To test the site locally, you need to use an environment variable:

```bash
export HUGO_BASEURL="http://localhost:1313/"
```

You can also just set the variable when running the server.

```bash
HUGO_BASEURL="http://localhost:1313/" hugo server
```

## Dataset page generation

Additionally, the datasets page is automatically generated as a dependency. You can generate it directly with:

```bash
just datasets
```
