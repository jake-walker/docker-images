# Docker Images

These are some custom images that are regularly built for AMD64 and ARM64 architectures.

<!-- generate start -->
| Name | Description |
| --- | --- |
| `ghcr.io/jake-walker/beeper_bridge-manager` | This is an exact build of Beeper's [bridge-manager](https://github.com/beeper/bridge-manager) but with an ARM64 build. |
<!-- generate end -->

_Images are also available on Docker Hub at `jakewalker/<image name>`._

## Builds

Images are built weekly and after a push to the main branch.

Each image has the following tags:
- `latest` - this is always the latest built image
- `main` - this is always the latest built image
- `sha-XXXXXXX` - this is based on the git commit hash, this may get overwritten by newer versions so is not suitable for pinning a version
- `XXXXXXXX` - this is a date in the format `YYYYMMDD` for the weekly builds. This will not get overwritten so is suitable for version pinning
