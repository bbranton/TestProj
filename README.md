# TestProj

A Software Factory: a team of AI personas, and the products it builds.
[FACTORY.md](/FACTORY.md) says what the factory is for and how we'll show
it works.

Starting a new project like this one? See
[Set up a new project like this one](/SETUP-NEW-PROJECT.md).

## Site layout

The GitHub Pages site is assembled by `.github/workflows/pages.yml`:

- `/` is the landing page in `site/index.html`, with a link to each project.
- `/qml-hello/` is the QML WebAssembly app, copied from `qml-hello-wasm/site/`.
- `/canvas-portal/` is a "coming soon" placeholder in `site/canvas-portal/`.

To add a project, give it a folder under `site/` (or a copy step in the
workflow for built output) and add a card to `site/index.html`.

## QML hello world for WebAssembly

`qml-hello-wasm/` holds a Qt 6.8 Quick app with a "Hello, World!" label and a
button that counts clicks, built to WebAssembly. `qml-hello-wasm/site/` holds
the built files and the `index.html` page that runs them; the
`Deploy TestProj site to GitHub Pages` workflow publishes that folder at
`/qml-hello/`.

To rebuild, use Qt 6.8 for WebAssembly (single-threaded) with Emscripten
3.1.56:

```sh
source /path/to/emsdk/emsdk_env.sh
/path/to/qt-wasm/bin/qt-cmake -S qml-hello-wasm -B build -G Ninja -DCMAKE_BUILD_TYPE=MinSizeRel
cmake --build build
cp build/hello.js build/hello.wasm build/qtloader.js qml-hello-wasm/site/
```
