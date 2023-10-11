# Nix/Guix Snakemake Wrapper

Snakemake wrapper to simplify the use of Nix and Guix

## Nix

The Nix wrapper requires:

- `params.flake` to know which shell to use

- `params.shell` for the command to execute

```
rule test:
    input:
        "flake.nix",
        "flake.lock",
        script="run.py"
    output:
        "test_{i}"
    params:
        flake = ".#pyshell",
        shell = lambda wildcards, input, output: f"python3 {input.script} {wildcards.i} > {output}"
    wrapper:
        "https://github.com/Nix4Science/snakemake-wrapper/raw/0.1.0/nix"
```

To simplify the transition from a classical `Snakefile` to a `Snakefile` using this wrapper, we extend the `params.shell` to do the evaluation inside the wrapper. 
If you define the string of `params.shell` as `bytes`, the wrapper will evaluate the string itself.
So the following is exactly the same as above:

```
# ...
    params:
        shell = b"python3 {input.script} {wildcards.i} > {output}"
# ...
```

## Guix


The Guix wrapper requires:

- `input.manifest` for the manifest of the environment

- `input.channels` for the description of the channels to use

- `params.shell` for the command to execute

Optional parameters:

- `params.container` to run the shell with the `--container` option

```
rule test_guix:
    input:
        channels="channels.scm",
        manifest="manifest.scm",
        script="run.py"
    output:
        "test_{i}"
    params:
        container=True,
        shell = b"python3 {input.script} {wildcards.i} > {output}"
    wrapper:
        "https://github.com/Nix4Science/snakemake-wrapper/raw/0.1.0/guix"
```

To simplify the transition from a classical `Snakefile` to a `Snakefile` using this wrapper, we extend the `params.shell` to do the evaluation inside the wrapper. 
If you define the string of `params.shell` as `bytes`, the wrapper will evaluate the string itself.
So the following is exactly the same as above:

```
# ...
    params:
        shell = b"python3 {input.script} {wildcards.i} > {output}"
# ...
```

