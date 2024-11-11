ARG CADDY_VERSION=latest

FROM caddy:${CADDY_VERSION}-builder AS builder

RUN xcaddy build \
        --with github.com/mholt/caddy-webdav \
        --with github.com/caddyserver/replace-response \
        --with github.com/caddy-dns/cloudflare

FROM caddy:${CADDY_VERSION}-alpine

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
