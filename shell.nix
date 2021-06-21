with (import <nixpkgs> {}); stdenv.mkDerivation {
  name = "lzma-native";

  nativeBuildInputs = [
    pkg-config
    lzma
  ];
}
