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

## Dataset generation

Additionally, the datasets page is automatically generated as a dependency. You can generate it directly with:

```bash
just datasets
```

## Releases generation

Similarly to datasets, we auto-generate the releases pages with a script. This script crawls our repository HTML listing and generates a page for each old Gaia Sky release. Run it with:

```bash
just releases
```

## Icon generation

We generate our own icon font from the SVG icons in `/assets/icons`. You can get more icons at [Iconify](https://icon-sets.iconify.design). There is a `just` target that runs the whole thing and puts the output in the required directory. You first need to install `svgtofont` (see below).

```bash
just iconfont
```

If you need to add new icons, just put them in `/assets/icons` and re-run the target.

### Details

To generate the font, first install `svgtofont` in the `/script` directory.

```bash
cd script
npm install --save-dev svgtofont
```

And then run:

```bash
npx svgtofont --config svgtofont.config.js --output ./font --sources .icons
```

Now the font is available in `/script/font`.

