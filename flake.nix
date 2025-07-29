{
  description = "A Nix flake for the Reality Draw project, providing development environment and dependencies.";
    inputs = {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
      flake-utils.url = "github:numtide/flake-utils";
    };
    outputs = { self, nixpkgs, flake-utils}:
      flake-utils.lib.eachDefaultSystem (system: let
        pkgs = import nixpkgs { inherit system; };
      in {
      }
           
}