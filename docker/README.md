Quick Docker run examples (as per the lab document):

# Create docker network
docker network create --driver bridge lab

# Prometheus
docker run -d -p 9090:9090 --name prometheus -h prometheus --net lab -v $(pwd)/prometheus/:/etc/prometheus/ docker.io/prom/prometheus:v3.2.1

# Grafana
docker run -d -p 3000:3000 --name grafana -h grafana --net lab docker.io/grafana/grafana:11.6.0

# Node exporter (host network)
docker run -d --name node-exporter --net host --pid host -v /:/host:ro,rslave docker.io/prom/node-exporter:v1.9.1 --path.rootfs=/host

# cAdvisor
docker run -d --name cadvisor -h cadvisor --net lab -v /:/rootfs:ro -v /var/run:/var/run:ro -v /sys:/sys:ro -v /var/lib/docker/:/var/lib/docker:ro -v /dev/disk/:/dev/disk:ro gcr.io/cadvisor/cadvisor:v0.52.1

# cpu-exporter build & run
cd docker/cpu-exporter
docker build -t cpu-exporter .
docker run -d --net lab --pid host --name cpu-exporter -h cpu-exporter -e LC_ALL=C cpu-exporter
