"""
.. module:: __main__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Specialization validator.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import os

from generate_js import Generator as JavascriptGenerator
from generate_json import Generator as JSONGenerator
from generate_mm import Generator as MindmapGenerator
from utils_factory import get_specialization
from utils_loader import get_modules


# Path to directory in which specializations reside.
_DIR = os.path.dirname(os.path.dirname(__file__))

# Name of associated project.
_PROJECT = __file__.split('/')[-3].split('-specializations-')[0]

# Name of associated specialization.
_TYPEOF = __file__.split('/')[-3].split('-specializations-')[-1]

# Map of generator types to generator.
_GENERATORS = {
    'js': JavascriptGenerator,
    'json': JSONGenerator,
    'mm': MindmapGenerator,
}

# Set specialization modules.
specialization = get_specialization(get_modules(_DIR, _TYPEOF))

logging_output = []
for generator_type, generator_cls in _GENERATORS.iteritems():
    # Run generator
    generator = generator_cls(_PROJECT, specialization)
    generator.run()

    # Set output file name.
    fname = "_{}.{}".format(_PROJECT, generator_type)
    if fname.endswith('.py'):
        fname = fname.replace("-", "_")

    # Set output file path.
    fpath = os.path.join(_DIR, fname)

    # Write generated output to file system.
    with open(fpath, 'w') as fstream:
        fstream.write(generator.get_output())

    logging_output.append((fname.split('.')[-1], fpath))


# Inform user.
for encoding, fpath in sorted(logging_output):
    print "ES-DOC :: generated {} file written to --> {}".format(encoding, fpath)
