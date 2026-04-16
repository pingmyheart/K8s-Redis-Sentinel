FROM redis:8.2.5
RUN apt-get update && \
    apt-get install -y curl jq