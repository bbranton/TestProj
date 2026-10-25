import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: root
    visible: true
    width: 640
    height: 480
    title: "Hello QML"

    property int clicks: 0

    Column {
        anchors.centerIn: parent
        spacing: 20

        Label {
            anchors.horizontalCenter: parent.horizontalCenter
            text: root.clicks === 0 ? "Hello, World!"
                                    : "Hello, World! (clicked " + root.clicks + "×)"
            font.pixelSize: 32
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            text: "Click me"
            onClicked: root.clicks++
        }
    }
}
