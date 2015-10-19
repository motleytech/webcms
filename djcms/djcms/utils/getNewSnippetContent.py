import string
from random import choice
import json

charPool = string.letters + string.digits

jsTemplate = """
<script type="text/javascript"
 src="//cdnjs.cloudflare.com/ajax/libs/require.js/2.1.20/require.min.js">
</script>

<script type="text/javascript">
    require(["{}"], function (main) {{
        main.initialize("{}");
    }});
</script>
"""

htmlTemplate = """
<h2>Placeholder here</h2>

<div id="{}">
</div>
"""

def getRandomId(N=20):
    id_postfix = ''.join(choice(charPool) for ignore in xrange(N))
    return "id_{}".format(id_postfix)


def main():
    divId = getRandomId()
    scriptFile = "/static/viz/js/demo/main.js"

    javascript = jsTemplate.format(scriptFile, divId)
    html = htmlTemplate.format(divId)

    data = {
        "javascript": javascript,
        "html": html,
    }

    print json.dumps(data, indent=4)

if __name__ == "__main__":
    main()

