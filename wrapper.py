__author__ = "Quentin Guilloteau"
__copyright__ = "Copyright 2023, Quentin Guilloteau"
__license__ = "MIT"

from snakemake.shell import shell

flake = snakemake.params.get("flake", "")
shell_command = snakemake.params.get("shell", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True)

assert shell_command is not None, "`params.shell` is required"

if type(shell_command) == bytes:
    shell_command = shell_command.decode("utf-8").format(wildcards=snakemake.wildcards,\
            output=snakemake.output,\
            input=snakemake.input)
shell(
    "nix develop {flake} --command {shell_command} {log}"
)
