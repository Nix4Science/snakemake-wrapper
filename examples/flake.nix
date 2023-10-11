{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/23.05";
    nuix.url = "github:GuilloteauQ/nix-overlay-guix";
  };

  outputs = { self, nixpkgs, nuix }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; overlays = [ nuix.overlays.default ]; };
    in
    {

      devShells.${system} = {
        default = pkgs.mkShell {
          shellHook = ''
            sudo ${pkgs.guix}/bin/guix-daemon > .guix-daemon.log 2>&1 &
            GD_PID=$!
            trap "sudo kill $GD_PID" SIGINT
          '';
          packages = with pkgs; [
            snakemake
            guix
          ];
        };
        pyshell = pkgs.mkShell {
          packages = with pkgs; [
            python3
          ];
        };
      };

    };
}
