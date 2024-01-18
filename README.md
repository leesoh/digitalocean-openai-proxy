# DigitalOcean OpenAI Proxy

A simple OpenAI API proxy hosted in the DigitalOcean App platform. Accompanying blog post can be found [here](https://blog.smallsec.ca/openai-proxy). If you'd like to build on this, fork the repository and update the repository name in `.do/app.yaml`.

## Client

The `client/` directory contains the CLI tools used to call the APIs.

To install:

```sh
cd client/extwis
pipx install .
```

## Server

The `server/` directory contains everything required to deploy the APIs to DigitalOcean Apps Platform.

To deploy with [doctl](https://docs.digitalocean.com/reference/doctl/reference/apps/create/):

```sh
doctl doctl apps create --spec .do/app.yaml
```
