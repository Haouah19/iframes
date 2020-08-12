from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return """ <!DOCTYPE html>
<html>
<head>
<title>Bob on coursera</title>
<meta charset="utf-8" />

</head>
<body>
    <iframe
    id="myIframe"
    style="width:100%;height:100%;position:fixed;overflow: auto;"
    frameBorder="0"
    src="https://www.coursera.org/"></iframe>

    <iframe
    id="bob"
    scolling="no"
    style="width:100%; height:100%; position: fixed; bottom: 0; z-index: 1; "
    frameBorder="0"
    src="https://bobtva.theaiinstitute.ai:5000/?exercice=149&user=37486"></iframe>


    <!-- Activation -->
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script type="text/javascript" src="static/iframeResizer.min.js"></script>

    <script type="text/javascript">
        iFrameResize({
            log: true, // Enable console logging
            enablePublicMethods: true, // Enable methods within iframe hosted page
            enableInPageLinks: true,
            /*
            onResized: function(messageData) {
            // Callback fn when resize is received
            $('p#callback').html(
                '<b>Frame ID:</b> ' +
                messageData.iframe.id +
                ' <b>Height:</b> ' +
                messageData.height +
                ' <b>Width:</b> ' +
                messageData.width +
                ' <b>Event type:</b> ' +
                messageData.type
            )
            },
            */
            onMessage: function(messageData) {
            // Callback fn when message is received
            $('p#callback').html(
                '<b>Frame ID:</b> ' +
                messageData.iframe.id +
                ' <b>Message:</b> ' +
                messageData.message
            )
            alert(messageData.message + ' (' + messageData.iframe.id + ')')
            },
            onClosed: function(id) {
            // Callback fn when iFrame is closed
            $('p#callback').html(
                '<b>IFrame (</b>' + id + '<b>) removed from page.</b>'
            )
            }
        })
    </script>
</body>
</html>"""

if __name__ == "__main__":
	app.run(port=8000, threaded=True)
