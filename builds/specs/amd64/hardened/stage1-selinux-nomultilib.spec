subarch: amd64
target: stage1
version_stamp: hardened-selinux+nomultilib-latest
rel_type: hardened
profile: hardened/linux/amd64/no-multilib/selinux
snapshot: latest
source_subpath: hardened/stage3-amd64-hardened-selinux+nomultilib-latest
update_seed: yes
update_seed_command: --update --deep @world
portage_confdir: @REPO_DIR@/releases/weekly/portage/stages
