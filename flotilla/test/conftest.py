"""
This file will be auto-imported for every testing session, so you can use
these objects and functions across test files.
"""
import os
import subprocess

import matplotlib as mpl


# Tell matplotlib to not make any window popups
mpl.use('Agg')

import numpy as np
import pytest
import pandas as pd


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
# DATA_BASE_URL = 'https://raw.githubusercontent.com/YeoLab/shalek2013/master'
DATA_BASE_URL = 'http://sauron.ucsd.edu/flotilla_projects/shalek2013'

class ExampleData(object):
    __slots__ = ('metadata', 'expression', 'splicing', 'data')

    def __init__(self, metadata, expression, splicing):
        self.metadata = metadata
        self.expression = expression
        self.splicing = splicing
        self.data = (metadata, expression, splicing)


@pytest.fixture(scope='module')
def data_dir():
    return '{}/example_data'.format(CURRENT_DIR.rstrip('/'))

@pytest.fixture(scope='module')
def example_data():
    expression = pd.read_csv('{}/expression.csv'.format(DATA_BASE_URL),
                             index_col=0)
    splicing = pd.read_csv('{}/splicing.csv'.format(DATA_BASE_URL),
                           index_col=0, header=[0, 1])
    metadata = pd.read_csv('{}/metadata.csv'.format(DATA_BASE_URL),
                           index_col=0)
    return ExampleData(metadata, expression, splicing)


@pytest.fixture(scope='module')
def example_study(example_data):
    from flotilla.data_model import Study

    return Study(sample_metadata=example_data.metadata,
                 expression_data=example_data.expression,
                 splicing_data=example_data.splicing)


@pytest.fixture(scope='module')
def example_datapackage_path():
    return os.path.join(DATA_BASE_URL, 'datapackage.json')


@pytest.fixture(scope='module')
def example_datapackage(example_datapackage_path):
    from flotilla.datapackage import data_package_url_to_dict

    return data_package_url_to_dict(example_datapackage_path)


@pytest.fixture(scope='module')
def expression(example_data):
    from flotilla.data_model import ExpressionData

    return ExpressionData(example_data.expression)


@pytest.fixture(scope='module')
def study(example_datapackage_path):
    import flotilla

    return flotilla.embark(example_datapackage_path)


@pytest.fixture(scope='module')
def genelist_path(data_dir):
    return '{}/example_gene_list.txt'.format(data_dir)


@pytest.fixture(scope='module')
def genelist_dropbox_link():
    return 'https://www.dropbox.com/s/652y6hb8zonxe4c/example_gene_list.txt' \
           '?dl=0'


@pytest.fixture(params=['local', 'dropbox'])
def genelist_link(request, genelist_path, genelist_dropbox_link):
    if request.param == 'local':
        return genelist_path
    elif request.param == 'dropbox':
        return genelist_dropbox_link


@pytest.fixture(params=[None, 'gene_category: LPS Response',
                        'link',
                        'path'], scope='module')
def feature_subset(request, genelist_dropbox_link, genelist_path):
    from flotilla.util import link_to_list

    name_to_location = {'link': genelist_dropbox_link,
                        'path': genelist_path}

    if request.param is None:
        return request.param
    elif request.param in ('link', 'path'):

        try:
            return link_to_list(name_to_location[request.param])
        except subprocess.CalledProcessError:
            # Downloading the dropbox link failed, aka not connected to the
            # internet, so just test "None" again
            return None
    else:
        # Otherwise, this is a name of a subset
        return request.param

@pytest.fixture(scope='module')
def x_norm():
    """Normally distributed numpy array"""
    n_samples = 50
    n_features = 1000
    x = np.random.randn(n_samples * n_features)
    x = x.reshape(n_samples, n_features)
    return x


@pytest.fixture(scope='module')
def df_norm(x_norm):
    """Normally distributed pandas dataframe"""
    nrow, ncol = x_norm.shape
    index = ['sample_{0:02d}'.format(i) for i in range(nrow)]
    columns = ['feature_{0:04d}'.format(i) for i in range(ncol)]
    df = pd.DataFrame(x_norm, index=index, columns=columns)
    return df