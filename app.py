import textwrap
import yapf

from yapf.yapflib import yapf_api
from flask import Flask, render_template, request


app = Flask(__name__)

SOURCE_CODE = textwrap.dedent(
    """
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

    """
)


@app.route('/', methods=['POST', 'GET'])
def index():
    source = SOURCE_CODE

    if request.method == 'POST':
        source = request.form['source']

    try:
        formatted = yapf_api.FormatCode(source)
        error = None
    except Exception as error:
        formatted = ''

    data = {
        'source': source,
        'formatted': formatted,
        'error': error,
        'yapf_version': yapf.__version__
    }

    return render_template('index.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
