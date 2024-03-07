# mirrord Demo

## Installation

```bash
# install mirrord
# `mirrord` binary will be downloaded to `~/.local/bin`
./install_mirrord.sh
```

```bash
# deploy demo app bo and fe in current kube culster (namespace `test-intercept`)
./deploy.sh
```

## intercept target deployment

```bash
cd bo
source .env/bin/activate
WHOAMI=LOCAL mirrord exec --steal --target deployment/test-intercept-bo python main.py
WHOAMI=LOCAL mirrord exec --steal -f config/read_remote.json --target deployment/test-intercept-bo python main.py
```

## Features

- traffic mirroring:incoming TCP traffic is duplicated to container and local process but local traffic outgoing is dropped
- traffic stealing: local process handles all traffic
- [configuration file](https://mirrord.dev/docs/reference/configuration/#root-complete)

## Limitation

- for target deployment, the first pod is taken.
  impersonating all pods is supported only with premium version.

## mirrord for Teams

- Concurrent work on the same pod
- Targeting whole deployments
- RBAC
- Support
- 40$/month: [pricing](https://mirrord.dev/pricing/)

## Alternatives

- [Ambassador/telepresence](https://www.getambassador.io/docs/telepresence/latest/quick-start?os=gnu-linux)
