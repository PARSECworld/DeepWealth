import numpy as np


def load_npz(path, verbose=True):
    '''Loads .npz file into a dict.

    Args
    - path: str, path to .npz file

    Returns
    - result: dict
    '''
    result = {}
    with np.load(path) as npz:
        for key, value in npz.items():
            result[key] = value
            if verbose:
                print('{k}: dtype={d}, shape={s}'.format(k=key, d=value.dtype, s=value.shape))
    return result


def colordisplay(df, columns=None, cmap='coolwarm'):
    '''Displays a pandas DataFrame with background color.

    This function should only be called inside a Jupyter Notebook.

    Args
    - df: pd.DataFrame
    - columns: str or list of str, column(s) to color
    - cmap: str, name of matplotlib colormap
    '''
    display(df.style.background_gradient(cmap=cmap, subset=columns))