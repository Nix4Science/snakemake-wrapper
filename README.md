# Nix Snakemake Wrapper

Snakemake wrapper to simplify the use of Nix

## Example

The wrapper requires:

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
        "https://github.com/Nix4Science/nix-snakemake-wrapper/raw/0.0.1"
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

