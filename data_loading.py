import warnings
import pandas as pd


class DataPlausibilityError(ValueError):
    pass


def load_data(file_path: str, object_path: str, attribute: str) -> pd.DataFrame:
    """
    Reads a hd5 file containing water distribution data

    # TODO add docstring
    :param file_path:
    :param object_path:
    :param attribute:
    :return:
    """
    try:
        df: pd.DataFrame = pd.read_hdf(file_path, key="/".join([object_path, attribute]))
    except KeyError:
        warnings.warn(f"The attribute {attribute!r} for object path {object_path!r} does not exist.")
    else:
        return df


def check_plausibility(df: pd.DataFrame, center_node: str):
    """
    # TODO
    :param df:
    :param center_node:
    :return:
    """
    if not (df.loc[14400:, center_node] == 0.0).all():
        raise DataPlausibilityError(
            f"The dataframe contains non 0 m**3/s requirements for center_node {center_node!r}.")
