#!/usr/bin/env bash

set -eu
# set -x

cd $(dirname $(realpath $0))

NAMESPACE=${1:-test-intercept}

kubectl create namespace "${NAMESPACE}"

manifests=(
    bo/manifests/configmap.yaml
    bo/manifests/deployment.yaml
    bo/manifests/service.yaml
    fe/manifests/deployment.yaml
    fe/manifests/service.yaml
)

for manifest in "${manifests[@]}"; do
    kubectl create -n "${NAMESPACE}" -f "${manifest}"
done
