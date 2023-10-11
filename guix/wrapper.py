__author__ = "Quentin Guilloteau"
__copyright__ = "Copyright 2023, Quentin Guilloteau"
__license__ = "MIT"

from snakemake.shell import shell

manifest = snakemake.input.get("manifest", "")
channels = snakemake.input.get("channels", "")
is_container = snakemake.params.get("container", "")
container = "--container" if is_container else ""

shell_command = snakemake.params.get("shell", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

assert shell_command is not None, "`params.shell` is required"
assert manifest is not None, "`input.manifest` is required"
assert channels is not None, "`input.channels` is required"

if type(shell_command) == bytes:
    shell_command = shell_command.decode("utf-8").format(wildcards=snakemake.wildcards,\
            output=snakemake.output,\
            input=snakemake.input)
shell(
    "guix time-machine -C {channels} -- shell {container} -m {manifest} -- {shell_command} {log}"
)
