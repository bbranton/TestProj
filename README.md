# TestProj
a project to test github features

## QML hello world for WebAssembly

`qml-hello-wasm/` holds a Qt 6.8 Quick app with a "Hello, World!" label and a
button that counts clicks, built to WebAssembly. `qml-hello-wasm/site/` holds
the built files and the `index.html` page that runs them; the
`Deploy QML hello world to GitHub Pages` workflow publishes that folder.

To rebuild, use Qt 6.8 for WebAssembly (single-threaded) with Emscripten
3.1.56:

```sh
source /path/to/emsdk/emsdk_env.sh
/path/to/qt-wasm/bin/qt-cmake -S qml-hello-wasm -B build -G Ninja -DCMAKE_BUILD_TYPE=MinSizeRel
cmake --build build
cp build/hello.js build/hello.wasm build/qtloader.js qml-hello-wasm/site/
```
