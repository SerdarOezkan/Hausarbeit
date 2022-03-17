from collections import namedtuple

import pandas as pd

five_node_tuple = namedtuple("Five_Node_Selection",
                             ["rescue_node", "junction_node_1", "junction_node_2", "junction_node_3",
                              "junction_node_4"])


def calc_fulfillment_of_demand(df_demand: pd.DataFrame, df_req_demand: pd.DataFrame) -> pd.DataFrame:
    """
    # TODO
    :param df_demand:
    :param df_req_demand:
    :return:
    """
    # bring both dfs into same shape
    df_demand_rel = df_demand.loc[:, df_req_demand.columns]
    df_fullfillment_of_demand = df_demand_rel / df_req_demand

    # drop na columns
    df_fullfillment_of_demand = df_fullfillment_of_demand.loc[:, ~df_fullfillment_of_demand.isnull().any(axis=0)]

    return df_fullfillment_of_demand


def calc_mean_and_std_of_fullfillment(df_fullfillment: pd.DataFrame) -> pd.DataFrame:
    # Add mean and std of fulfillment
    df_fullfillment_orig = df_fullfillment.copy()
    df_fullfillment["mean"] = df_fullfillment_orig.mean(axis=1)
    df_fullfillment["std"] = df_fullfillment_orig.std(axis=1)

    return df_fullfillment


def calc_average_pressure(df_pressure: pd.DataFrame, nodes: five_node_tuple) -> pd.DataFrame:
    """

    :param df_pressure:
    :param nodes:
    :return:
    """
    df_rel_pressure = df_pressure.loc[:, list(nodes)]

    return pd.concat([df_rel_pressure[["J511", "J411"]].mean(axis=1).rename("mean_pressure"),
                      df_rel_pressure[["J511", "J411"]].std(axis=1).rename("std_pressure")], axis=1)
