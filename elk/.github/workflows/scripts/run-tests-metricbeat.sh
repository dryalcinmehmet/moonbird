#!/usr/bin/env bash

set -eu
set -o pipefail


source "$(dirname ${BASH_SOURCE[0]})/lib/testing.sh"


cid_es="$(container_id elasticsearch)"
cid_mb="$(container_id metricbeat)"

ip_es="$(service_ip elasticsearch)"
ip_mb="$(service_ip metricbeat)"

log 'Waiting for readiness of Elasticsearch'
poll_ready "$cid_es" "http://${ip_es}:9200/" -u 'elastic:testpasswd'

log 'Waiting for readiness of Metricbeat'
poll_ready "$cid_mb" "http://${ip_mb}:5066/?pretty"

# We expect to find one monitoring entry for the 'elasticsearch' Compose
# service using the following query:
#
#   agent.type:"metricbeat"
#   AND event.module:"docker"
#   AND event.dataset:"docker.container"
#   AND container.name:"elk_elasticsearch_1"
#
log 'Searching a document generated by Metricbeat'

declare response
declare -i count

# retry for max 60s (30*2s)
for _ in $(seq 1 30); do
	response="$(curl "http://${ip_es}:9200/metricbeat-*/_search?q=agent.type:%22metricbeat%22%20AND%20event.module:%22docker%22%20AND%20event.dataset:%22docker.container%22%20AND%20container.name:%22elk_elasticsearch_1%22&pretty" -s -u elastic:testpasswd)"

	set +u  # prevent "unbound variable" if assigned value is not an integer
	count="$(jq -rn --argjson data "${response}" '$data.hits.total.value')"
	set -u

	if (( count > 0 )); then
		break
	fi

	echo -n 'x' >&2
	sleep 2
done
echo -e '\n' >&2

echo "$response"
if (( count != 1 )); then
	echo "Expected 1 document, got ${count}"
	exit 1
fi
