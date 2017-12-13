import textwrap
import yapf

from yapf.yapflib import yapf_api
from flask import Flask, render_template, request

app = Flask(__name__)

SOURCE_CODE = textwrap.dedent("""
    x = {  'a':37,'b':42,

    'c':927}

    y = 'hello ''world'
    z = 'hello '+'world'
    a = 'hello {}'.format('world')
    class foo  (     object  ):
      def f    (self   ):
        return       37*-2
      def g(self, x,y=42):
          return y
    def f  (   a ) :
      return      37-a[42-x :  y**3]

    """)


@app.route('/', methods=['POST', 'GET'])
def index():
    source = SOURCE_CODE
    style_config = 'pep8'

    if request.method == 'POST':
        source = request.form['source']
        style_config = request.form['style_config']

    try:
        formatted, _ = yapf_api.FormatCode(source, style_config=style_config)
        error = None
    except Exception as error:
        formatted = ''

    data = {
        'source': source,
        'formatted': formatted,
        'style_config': style_config,
        'error': error,
        'yapf_version': yapf.__version__
    }

    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
