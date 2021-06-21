{
  "variables": {
    "dlldir%": "<(module_root_dir)/build/Release"
  },
  "targets": [
    {
      "target_name": "lzma_native",
      "sources": [
        "src/util.cpp",
        "src/liblzma-functions.cpp",
        "src/filter-array.cpp",
        "src/lzma-stream.cpp",
        "src/module.cpp",
        "src/mt-options.cpp",
        "src/index-parser.cpp"
      ],
      'include_dirs': ["<!@(node -p \"require('node-addon-api').include\")"],
      'dependencies': ["<!(node -p \"require('node-addon-api').gyp\")"],
      'cflags!': [ '-fno-exceptions', "<!@(pkg-config --cflags liblzma)" ],
      'link_settings': {
        'libraries': [ "<!@(pkg-config --libs-only-l liblzma)" ]
      },
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      }
    }
  ]
}
